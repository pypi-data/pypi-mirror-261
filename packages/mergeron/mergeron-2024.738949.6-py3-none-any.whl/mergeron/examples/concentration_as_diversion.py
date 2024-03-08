R"""

Demonstrates the correspondence between concentration standards and
diversion ratio standards, graphically

Here, *correspondence* is defined as the close approximation of
boundaries for sets of mergers meeting a guidelines concentration
standard to boundaries for sets of mergers meeting a
matching diversion ratio. Separate demonstrations based on
1992 Guidelines concentration standards and 2010 Guidelines concentration
standards are generated as,
1.) Plots of the boundaries write to separate PDF files
2.) Tables of boundary coordinates written to separate Excel files

Output is written in the `mergeron` sub-folder within a user's home directory,
i.e., `%USERPROFILE%\mergeron` on Windows, or `~/mergeron/` on Unix-like
systems.

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime
from math import sqrt
from pathlib import Path
from typing import Any, Literal

import matplotlib.axes as mpa
from jinja2 import FileSystemLoader
from joblib import Parallel, cpu_count, delayed  # type: ignore
from numpy import pi
from xlsxwriter import Workbook  # type: ignore

import mergeron.core.excel_helper as xlh
import mergeron.core.guidelines_boundaries as gbl
import mergeron.ext.tol_colors as ptcolor
import mergeron.gen.investigations_stats as isl
from mergeron import DATA_DIR, RECConstants, UPPAggrSelector
from mergeron.core import UPPBoundarySpec

PROG_PATH = Path(__file__)

RECAPTURE_SPEC = RECConstants.INOUT
# Map boundary forms to titles and generating-function names, with
#   additional parameters as relevant
BDRY_SPECS_DICT: Mapping[str, Mapping[str, Any]] = {
    "ΔHHI": {
        "title_str": "ΔHHI boundary",
        "sheet_name": "ΔHHI",
        "func_str": R"\Delta HHI",
        "func": gbl.delta_hhi_boundary,
    },
    "OSWAG Own-shr-wtd Div Ratio Index": {
        "title_str": "Aggregated-diversion-ratio boundary, own-share wtd. avg.",
        "sheet_name": "OSWAG, wtd avg",
        "func_str": R"(s_1 d_{12} + s_2 d_{21}) / s_M",
        "agg_method": UPPAggrSelector.OSA,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "OSWAG Own-shr-wtd Div Ratio Distance": {
        "title_str": "Aggregated-diversion-ratio boundary, own-shr. wtd. distance",
        "sheet_name": "OSWAG, distance",
        "func_str": R"\surd (s_1 d_{12}^2 / s_M + s_2 d_{21}^2 / s_M)",
        "agg_method": UPPAggrSelector.OSD,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "OSWAG Min Div Ratio": {
        "title_str": "Aggregated-diversion-ratio boundary, minimum",
        "sheet_name": "OSWAG, minimum",
        "func_str": R"\min (d_{12}, d_{21})",
        "agg_method": UPPAggrSelector.MIN,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "SAG Combined Share": {
        "title_str": "Combined Share boundary",
        "sheet_name": "SAG, combined-share",
        "func_str": R"s_M",
        "func": gbl.combined_share_boundary,
    },
    "SAG Average Div Ratio": {
        "title_str": "Aggregated-diversion-ratio boundary, simple average",
        "sheet_name": "SAG, average",
        "func_str": R"(d_{12} + d_{21}) / 2",
        "agg_method": UPPAggrSelector.AVG,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "SAG Div Ratio Distance": {
        "title_str": "Aggregated-diversion-ratio boundary, distance",
        "sheet_name": "SAG, distance",
        "func_str": R"\surd (d_{12}^2 / 2 + d_{21}^2 / 2)",
        "agg_method": UPPAggrSelector.DIS,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "CPSWAG Premerger HHI-contribution": {
        "title_str": "Premerger HHI-contribution boundary",
        "sheet_name": "CPSWAG, HHI-contrib-pre",
        "func_str": R"HHI_M^{pre}",
        "func": gbl.hhi_pre_contrib_boundary,
    },
    "CPSWAG Cross-product-shr-wtd Div Ratio Index": {
        "title_str": "Aggregated-diversion-ratio boundary, cross-product-share wtd. avg.",
        "sheet_name": "CPSWAG, wtd avg",
        "func_str": R"(s_2 d_{12} / s_M  + s_1 d_{21} / s_M)",
        "agg_method": UPPAggrSelector.CPA,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "CPSWAG Cross-product-shr-wtd Div Ratio Distance": {
        "title_str": "Aggregated-diversion-ratio boundary, cross-prod-shr. wtd. distance",
        "sheet_name": "CPSWAG, distance",
        "func_str": R"\surd (s_2 d_{12}^2 / s_M + s_1 d_{21}^2 / s_M)",
        "agg_method": UPPAggrSelector.CPD,
        "recapture_spec": RECAPTURE_SPEC,
    },
    "CPSWAG Max Div Ratio": {
        "title_str": "Aggregated-diversion-ratio boundary, maximum",
        "sheet_name": "CPSWAG, maximum",
        "func_str": R"\max (d_{12}, d_{21})",
        "agg_method": UPPAggrSelector.MAX,
        "recapture_spec": RECAPTURE_SPEC,
    },
}


def tabulate_boundary_stats(_gpubyr: gbl.HMGPubYear, /) -> None:
    """
    Parameters
    ----------
    _gpubyr
        Guidelines version (year of publication) from which concentration standards
        are drawn

    """
    _invres_rate_table_content = isl.StatsContainer()

    gso = gbl.GuidelinesThresholds(_gpubyr)
    _dhhi_val, _r_val, _g_val = (
        getattr(gso.presumption, _f) for _f in ("delta", "rec", "guppi")
    )

    _dhhi_seq = (
        (0.005, 0.01, 0.02, gso.imputed_presumption.delta, 0.08)
        if _gpubyr == 2010
        else (0.005, 0.01, 0.02, gso.imputed_presumption.delta, 0.08)
    )

    _bdry_approx_data_dict = {
        "Criterion": {
            _k: R"\({} < {}\)".format(
                BDRY_SPECS_DICT[_k]["func_str"],
                R"\safeharb{d}"
                if "Div Ratio" in _k
                else (
                    R"\surd (2 \safeharb{H})"
                    if _k.endswith("Combined Share")
                    else R"\safeharb{H}"
                ),
            )
            for _k in BDRY_SPECS_DICT
            # if not _k.endswith("Distance")
        }
    }
    _bdry_approx_data_dict |= {
        R"{ \safeharb{H} \\ \safeharb{d} }": {
            _k: R"{}" for _k in _bdry_approx_data_dict["Criterion"]
        }
    }

    _bdry_data = Parallel(n_jobs=-1)(
        delayed(_dhhi_stats)(_dhhi_val, _r_val) for _dhhi_val in _dhhi_seq
    )
    _bdry_approx_data_dict |= dict(_bdry_data)

    _data_str = ""
    _data_str = "{} \\\\ \n".format(
        " & ".join(
            _k.replace("Criterion", R"{\text{} \\ Criterion}")  # \phantom{Criterion}
            for _k in _bdry_approx_data_dict
        )
    )
    for _sk in _bdry_approx_data_dict["Criterion"]:
        _data_str += "{} \\\\ \n".format(
            " & ".join(_bdry_approx_data_dict[_k][_sk] for _k in _bdry_approx_data_dict)
        )
    print(_data_str)

    _invres_rate_table_content.data_str = _data_str

    _j2_env = isl.latex_jinja_env
    _j2_env.loader = FileSystemLoader(str(PROG_PATH.parent / "templates"))
    _j2_templ = _j2_env.get_template(
        "concentration_as_diversion_intrinsic_enforcement_rates.tex.jinja2"
    )
    PROG_PATH.parents[1].joinpath(
        f"{PROG_PATH.stem}_intrinsic_enforcement_rates_{_gpubyr}.tex"
    ).write_text(_j2_templ.render(tmpl_data=_invres_rate_table_content))


def _dhhi_stats(_dhhi_val: float, _r_val: float) -> tuple[str, dict[str, str]]:
    _dhhi_val = round(_dhhi_val, 5)

    _divr_val = gbl.gbd_from_dsf(_dhhi_val, r_bar=_r_val)
    _delta_val = gbl.critical_shrratio(_divr_val, r_bar=_r_val)
    # _s_mid = sqrt(_dhhi_val / 2)

    # _delta_val = _s_mid / (1 - _s_mid)
    # if _dhhi_val * 1e4 in (50, 100, 200):
    #     _delta_val = gbl.critical_shrratio()(_r_val * _delta_val) / _r_val
    # _divr_val = _r_val * _delta_val

    print(
        "Processing data for ΔHHI = {0:.{1}f} points;".format(
            _dhhi_val * 1e4, 1 * (_dhhi_val * 1e4 % 1 > 1e-8)
        ),
        f"diversion ratio = {_divr_val:.{1 * (_divr_val * 1e2 % 1 > 1e-8)}%};",
    )

    _bdry_stats = Parallel(n_jobs=cpu_count() // 2)(
        delayed(_bdry_stats_col)(_bdry_spec, _dhhi_val, _delta_val, _r_val)
        for _bdry_spec in BDRY_SPECS_DICT
    )

    _bounds_string = R"{{ {} \\ {} }}".format(
        Rf"{_dhhi_val * 1e4:.{1 * (_dhhi_val * 1e4 % 1 > 1e-8)}f} points",
        Rf"{_divr_val * 1e2:.{2 * (_divr_val * 1e2 % 1 > 1e-8)}f}\%",
    )
    return _bounds_string, dict(_bdry_stats)


def _bdry_stats_col(
    _bdry_spec: str, _dhhi_val: float, _delta_val: float, _r_val: float, /
) -> tuple[str, str]:
    _dhhi_prob = 2 * gbl.dh_area(_dhhi_val)
    _cs_prob = 2 * _dhhi_val
    _hhi_m_pre_prob = pi * _dhhi_val / 2

    match _bdry_spec:
        case "ΔHHI":
            return _bdry_spec, f"{_dhhi_prob:6.5f}"
        case "SAG Combined Share":
            return _bdry_spec, f"{_cs_prob:6.5f}"
        case "CPSWAG Premerger HHI-contribution":
            return _bdry_spec, f"{_hhi_m_pre_prob:6.5f}"
        case _ if "Div Ratio" in _bdry_spec:
            _within_bdry_area = gbl.shrratio_boundary(
                UPPBoundarySpec(
                    _delta_val,
                    _r_val,
                    agg_method=BDRY_SPECS_DICT[_bdry_spec]["agg_method"],
                    recapture_spec=BDRY_SPECS_DICT[_bdry_spec]["recapture_spec"],
                )
            ).area
            _within_bdry_prob = 2 * _within_bdry_area
            if _bdry_spec.startswith("CPSWAG"):
                _within_conc_bdry_prob = _hhi_m_pre_prob
            elif _bdry_spec.startswith("SAG"):
                _within_conc_bdry_prob = _cs_prob
            else:
                _within_conc_bdry_prob = _dhhi_prob

            return _bdry_spec, R"{{ {:6.5f} \\ {:.2f}\% }}".format(  # noqa: UP032
                _within_bdry_prob,
                100 * (1 - (_within_conc_bdry_prob / _within_bdry_prob)),
            )
        case _:
            raise ValueError(f'Unexpected specification, "{_bdry_spec}"?')


def plot_and_save_boundary_coords(
    _gpubyr: gbl.HMGPubYear,
    _xl_book: Workbook,
    /,
    layout: Literal["collected", "distributed"] = "collected",
) -> None:
    gso = gbl.GuidelinesThresholds(_gpubyr)

    _hmg_standards_strings_dict = {
        "distributed": ("presumption", "inferred presumption", "safeharbor"),
        "collected": ("safeharbor", "imputed_presumption", "presumption"),
    }
    _hmg_standards_strings = _hmg_standards_strings_dict.get(layout, ())
    if not _hmg_standards_strings:
        raise ValueError(
            f"Layout parameter value, {layout!r} is invalid.  "
            f'Must be one of, ("collected", "distributed"). '
        )

    # Initialize plot area
    _plt, _my_fig1, _ax1, _set_axis_def = gbl.boundary_plot()

    _divr_agg_methods = ("OSWAG", "SAG", "CPSWAG")

    for _divr_agg_method, _hmg_standards_str in zip(
        _divr_agg_methods, _hmg_standards_strings, strict=True
    ):
        _r_bar, _g_bar = (getattr(gso.presumption, _f) for _f in ("rec", "guppi"))
        _dhhi_val = getattr(gso, _hmg_standards_str).delta
        _divr_val = (
            _g_bar
            if _hmg_standards_str == "safeharbor"
            else _r_bar * sqrt(_dhhi_val / 2) / (1 - sqrt(_dhhi_val / 2))
        )

        _dhhi_val_str = "{0:.{1}f} points".format(
            _dhhi_val * 1e4, 1 * (_dhhi_val * 1e4 % 1 > 1e-8)
        )
        _divr_val_str = f"{_divr_val:.{1 * (_divr_val * 1e2 % 1 > 1e-8)}%}"

        print(
            f"Processing data for ΔHHI = {_dhhi_val_str},",
            f"diversion ratio = {_divr_val_str}:",
        )

        _bndry_data_dict: dict[
            str, Sequence[tuple[float]]
        ] = {}  #: Container for boundary coordinates data, by boundary

        for _bdry_spec_key in BDRY_SPECS_DICT:
            _bdry_spec = (_bdry_spec_key, BDRY_SPECS_DICT[_bdry_spec_key])

            if _bdry_spec_key == "ΔHHI":
                if _hmg_standards_str != _hmg_standards_strings_dict[layout][0]:
                    continue

                _dh_s1, _dh_s2 = gen_plot_boundary(
                    _bndry_data_dict, gso, _hmg_standards_str, _bdry_spec, _ax1
                )

                del _dh_s1, _dh_s2

            elif _bdry_spec_key.startswith(
                _divr_agg_method
            ):  # and not _bdry_spec_key.endswith("Distance"):
                gen_plot_boundary(
                    _bndry_data_dict, gso, _hmg_standards_str, _bdry_spec, _ax1
                )

        _fig_leg = _ax1.legend(
            loc="upper right",
            bbox_to_anchor=(0.995, 0.999),
            shadow=True,
            fancybox=False,
            frameon=False,
            fontsize=8,
        )
        _fig_leg.set_in_layout(False)

        for _bndry_name in _bndry_data_dict:
            boundary_data_to_worksheet(
                _bndry_name,
                _dhhi_val_str,
                _divr_val_str,
                _r_bar,
                _bndry_data_dict,
                _xl_book,
            )

    _fig_savepath = DATA_DIR / rf"{PROG_PATH.stem}_{_gpubyr}.pdf"
    _my_fig1.savefig(_fig_savepath)
    print()


def gen_plot_boundary(
    _bndry_data_dict: Mapping[str, Sequence[tuple[float]]],
    _gso: gbl.GuidelinesThresholds,
    _gs_str: str,
    _bdry_spec: tuple[str, Mapping[str, Any]],
    _ax1: mpa.Axes,
    /,
) -> tuple[tuple[float], tuple[float]]:
    """
    Utility function to plot boundaries given a dict of relevant parms.

    Parameters
    ----------
    _bndry_data_dict
        mapping for storing boundary coordinates for each plotted boundary
    _gso
        gbl.GuidelinesStandards instance of tuples listing
        concentration standard, default recapture-rate, GUPPI bound,
        and diversion ratio bound for "safeharbor", "weak presumption",
        and "presumption", where "weak presumption" represents an alternative
        interpretation of the enforcement margin for the Guidelines presumption
    _gs_str
        safeharbor, presumption, or overt_presumption
    _bdry_spec
        tuple of a string specifying boundary function to plot and
        a mapping detailing the  boundary function specification including
        boundary function name and keyword parameters
    _ax1
        matplotlib Axes object for plots

    Returns
    -------
        tuples of boundary coordinates - Firm 1 shares and Firm 2 shares along
        boundary for Guidelines standard
    """

    _bdry_spec_str, _bdry_spec_dict = _bdry_spec
    print(_bdry_spec_dict["title_str"])

    _pt_mdco: ptcolor.Mcset = ptcolor.tol_cset("medium-contrast")  # type: ignore
    _pt_vbco: ptcolor.Vcset = ptcolor.tol_cset("vibrant")  # type: ignore

    _plot_line_width = 1.0
    _plot_line_alpha = 0.8
    _plot_line_color = _pt_vbco.black
    _plot_line_style = {"OSWAG": "-", "SAG": "-.", "CPSWAG": "--"}.get(
        _bdry_spec_str.split(" ")[0], "-"
    )
    if _bdry_spec_str.startswith("ΔHHI"):
        _plot_line_width = 0.5
        _plot_line_alpha = 1.0
    _zrdr = 5

    if not _bdry_spec_str.startswith("ΔHHI"):
        match _bdry_spec_str:
            case _ if _bdry_spec_str.startswith(("SAG Combined", "CPSWAG Premerger")):
                _zrdr = 2
            case _ if "Distance" in _bdry_spec_str:
                _plot_line_color = _pt_vbco.blue
                _zrdr = 3
            case _ if "shr-wtd" in _bdry_spec_str or "Mean" in _bdry_spec_str:
                _plot_line_color = _pt_vbco.teal
                _zrdr = 3
            case _:
                _plot_line_color = _pt_vbco.red

    _g_val = _gso.safeharbor.guppi

    _r_bar = _gso.presumption.rec

    _dhhi_val = getattr(_gso, _gs_str).delta
    _s_mid = sqrt(_dhhi_val / 2)
    _delta_val = _g_val / _r_bar if _gs_str == "safeharbor" else _s_mid / (1 - _s_mid)

    _bdry_func = _bdry_spec_dict.get("func", gbl.shrratio_boundary)
    if "Div Ratio" in _bdry_spec_str:
        _bdry_boundary = gbl.shrratio_boundary(
            UPPBoundarySpec(
                _delta_val,
                _r_bar,
                agg_method=_bdry_spec_dict["agg_method"],
                recapture_spec=_bdry_spec_dict["recapture_spec"],
            )
        )
        _plot_label_mag, _plot_label_uom = _r_bar * _delta_val * 1e2, "%"
    elif _bdry_spec_str.endswith("Combined Share"):
        _bdry_boundary = _bdry_func(2 * _s_mid)
        _plot_label_mag, _plot_label_uom = 2 * _s_mid * 1e2, "%"
    else:
        _bdry_boundary = _bdry_func(_dhhi_val)
        _plot_label_mag, _plot_label_uom = _dhhi_val * 1e4, " points"

    _plot_label = R"${0}$ = {1:.{2}f}{3}".format(
        _bdry_spec_dict["func_str"],
        _plot_label_mag,
        1 * (_plot_label_mag % 1 > 1e-8),
        _plot_label_uom,
    )

    _bndry_data_dict |= {
        _bdry_spec_str: (
            _bdry_spec_dict["sheet_name"],
            _bdry_boundary.coordinates,
            _bdry_boundary.area,
        )
    }  # type: ignore
    _bdry_s1, _bdry_s2 = zip(*_bdry_boundary.coordinates, strict=True)

    _ax1.plot(
        _bdry_s1,
        _bdry_s2,
        label=_plot_label,
        color=_plot_line_color,
        linestyle=_plot_line_style,
        linewidth=_plot_line_width,
        alpha=_plot_line_alpha,
        zorder=_zrdr,
    )

    print("\t", _bdry_spec_str, f"{_bdry_s2[0]:.1%}")
    if _bdry_spec_str.startswith(("ΔHHI", "OSWAG Min")):
        _plot_annotator(
            _ax1,
            f"({_bdry_s1[1]:.1%}, {_bdry_s2[1]:.1%})",
            (_bdry_s1[1], _bdry_s2[1]),
            (0.005, 0),
            "left",
        )
    elif _bdry_spec_str.startswith("SAG") or _bdry_spec_str in (
        "CPSWAG Premerger HHI-contribution",
        "CPSWAG Max Div Ratio",
    ):
        _plot_annotator(
            _ax1, f"{_bdry_s2[0]:.1%}", (_bdry_s1[0], _bdry_s2[0]), (-0.005, 0), "right"
        )

    return _bdry_s1, _bdry_s2


def _plot_annotator(
    _ax: mpa.Axes,
    _a_str: str,
    _data_pt: tuple[float, float],
    _note_offset: tuple[float, float],
    _h_align: str,
    _v_align: str = "bottom",
    _font_sz: int = 3,
    _z_order: float = 5.0,
    /,
) -> None:
    _ax.annotate(
        "" if _data_pt[1] * 10 % 1 < 1e-8 else _a_str,
        xy=_data_pt,
        xytext=(_data_pt[0] + _note_offset[0], _data_pt[1] + _note_offset[1]),
        textcoords="data",
        ha=_h_align,
        va=_v_align,
        fontsize=_font_sz,
        zorder=_z_order,
    )


def boundary_data_to_worksheet(
    _bndry_name: str,
    _dhhi_val_str: str,
    _divr_val_str: str,
    _r_bar: float,
    _bndry_data_dict: Mapping[str, Sequence[tuple[Any]]],
    _xl_book: Workbook,
    /,
) -> None:
    """
    Write boundary data to worksheet in specified Excel workbook

    Parameters
    ----------
    _bndry_name
        Name of concentration or diversion boundary
    _dhhi_val_str
        ∆HHI value as a formatted string
    _divr_val_str
        Diversion ratio value as a formatted string
    _r_bar
        Specified recapture rate
    _bndry_data_dict
        Container with boundary coordinates data for various concentration and
        diversion boundaries
    _xl_book
        Specified Excel Workbook

    """
    _sheet_name, _bndry_points, _bndry_area = _bndry_data_dict[_bndry_name]

    _xl_sheet = _xl_book.add_worksheet(_sheet_name)

    _xl_sheet.write("A1", "Sound GUPPI Safeharbor")
    _xl_sheet.write("A2", "Merger Screens for Unilateral Effects")
    _xl_sheet.write("A3", f"Share Coordinates Defining {_bndry_name}")
    if "Div Ratio" in _bndry_name:
        _xl_sheet.write(
            "A4",
            "Boundary parameters: {}; {}".format(
                f"diversion ratio = {_divr_val_str}", f"recapture rate = {_r_bar:3.0%}"
            ),
        )
        _xl_sheet.write("A6", "Area Under Boundary (Simpson's Rule)")
    else:
        _xl_sheet.write("A4", f"Boundary parameters: ΔHHI = {_dhhi_val_str}")
        _xl_sheet.write("A6", "Area Under Boundary (Closed Form)")

    # Write and format the data
    _left_footer = "{}, {} on {}.\n{}".format(
        "Generated by Python module",
        ".".join(Path(__file__).parts[-3:]).rstrip(".py"),
        datetime.now().strftime("%A, %d %B %Y"),
        "© S. Murthy Kambhampaty, 2017-2023. License: CC-BY-NC-SA-4.0.",
    )
    _xl_sheet.set_footer(f"&L{_left_footer}")

    xlh.scalar_to_sheet(_xl_book, _xl_sheet, "B7", _bndry_area, xlh.CFmt.AREA_NUM)

    _results_header_row = 9
    for _cell_addr_col in range(2):
        xlh.scalar_to_sheet(
            _xl_book,
            _xl_sheet,
            _results_header_row,
            _cell_addr_col,
            f"Firm {_cell_addr_col + 1}",
            (xlh.CFmt.HDR_BORDER, xlh.CFmt.A_RIGHT),
        )
    # set column widths
    _xl_sheet.set_column(0, 1, 15)

    _results_top_row = 11
    _last_written_row, _last_written_col = xlh.matrix_to_sheet(
        _xl_book,
        _xl_sheet,
        _bndry_points,
        _results_top_row,
        cell_format=xlh.CFmt.PCT_NUM,  # type: ignore
    )

    # Draw a bottom border
    _cell_row = _last_written_row
    for _cell_col in range(_last_written_col):
        xlh.scalar_to_sheet(
            _xl_book, _xl_sheet, _cell_row, _cell_col, "", xlh.CFmt.BOT_BORDER
        )


if __name__ == "__main__":
    gpubyrs: list[gbl.HMGPubYear] = [1992, 2010, 2023]
    for gpubyr in gpubyrs[2:][:1]:
        tabulate_boundary_stats(gpubyr)

        # Initiliaze workbook for saving boundary coordinates
        with Workbook(
            DATA_DIR / rf"{PROG_PATH.stem}_{gpubyr}_BoundaryCoordinates.xlsx"
        ) as xl_book:
            # tabulate_boundary_stats(gpubyr)
            plot_and_save_boundary_coords(gpubyr, xl_book, layout="collected")  # type: ignore
            xl_book.worksheets()[0].activate()
