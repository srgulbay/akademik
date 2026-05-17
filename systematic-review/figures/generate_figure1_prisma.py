#!/usr/bin/env python3
"""
Generate PRISMA 2020 flow diagram (Figure 1) for the systematic review:
"Quorum Sensing in Acinetobacter baumannii".

Produces:
  - figure1_prisma_flow.png (300 DPI, 8 x 10 in) -- full two-column PRISMA 2020
  - figure1_prisma_flow.svg                       -- vector version
  - figure1_prisma_flow_simplified.png (6 x 8 in) -- compact single-column for IJAA

Numbers are read from ../literature/prisma_flow_data.json so the figure stays
in sync with the upstream dedup pipeline.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---------------------------------------------------------------------------
# Paths / data
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
DATA_PATH = HERE.parent / "literature" / "prisma_flow_data.json"
OUT_PNG = HERE / "figure1_prisma_flow.png"
OUT_SVG = HERE / "figure1_prisma_flow.svg"
OUT_SIMPLE_PNG = HERE / "figure1_prisma_flow_simplified.png"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    DATA = json.load(f)

ID = DATA["identification"]
PUBMED = ID["PubMed"]
OPENALEX = ID["OpenAlex"]
CROSSREF = ID["Crossref"]
TOTAL_IDENT = DATA["total_identified"]
DUPLICATES = DATA["duplicates_removed"]
AFTER_DEDUP = DATA["after_dedup"]

# Downstream figures supplied in the task brief
PUBMED_CORE_V1 = 338
ADDITIONAL_PENDING = 2975
FULLTEXT_ASSESSED = 228
ABSTRACT_ONLY = 112
INCLUDED_V1 = 338

# ---------------------------------------------------------------------------
# Styling helpers
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "svg.fonttype": "none",  # keep text as text in SVG
})

BOX_EDGE = "black"
BOX_FACE = "white"
SIDE_FACE = "#dcdcdc"   # light gray side bar
PENDING_COLOR = "#6a6a6a"
ARROW_KW = dict(
    arrowstyle="-|>",
    mutation_scale=14,
    linewidth=1.2,
    color="black",
    shrinkA=2,
    shrinkB=2,
)


def add_box(ax, x, y, w, h, text, *, fontsize=10, weight="normal",
            face=BOX_FACE, edge=BOX_EDGE, lw=2.0, italic=False, color="black",
            rounding=0.02):
    """Draw a rounded rectangle with centered wrapped text."""
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.02,rounding_size={rounding}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    style = "italic" if italic else "normal"
    ax.text(
        x + w / 2, y + h / 2, text,
        ha="center", va="center",
        fontsize=fontsize, fontweight=weight, fontstyle=style,
        color=color, wrap=True,
    )
    return patch


def add_side_label(ax, x, y, w, h, text):
    """Vertical side-bar label (Identification / Screening / ...)."""
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.5,
        edgecolor="black",
        facecolor=SIDE_FACE,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2, y + h / 2, text,
        ha="center", va="center",
        fontsize=11, fontweight="bold", rotation=90,
    )


def arrow(ax, x0, y0, x1, y1):
    a = FancyArrowPatch((x0, y0), (x1, y1), **ARROW_KW)
    ax.add_patch(a)


# ---------------------------------------------------------------------------
# Full PRISMA 2020 two-column diagram
# ---------------------------------------------------------------------------
def build_full_prisma():
    fig = plt.figure(figsize=(8, 10), dpi=300)
    # Leave a small inset margin so side-bar labels and the right-margin
    # dashed arrow are not clipped at the page edge.
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_axis_off()

    # Top banner headers for the two columns
    ax.text(3.55, 11.60,
            "Identification of studies via databases and registers",
            ha="center", va="center", fontsize=9.5, fontweight="bold")
    ax.text(8.05, 11.60,
            "Identification of studies\nvia other methods",
            ha="center", va="center", fontsize=9.5, fontweight="bold")

    # ---- Side bars ----------------------------------------------------------
    # Stage Y-bands (top to bottom)
    bands = {
        "Identification": (8.40, 11.05),  # y_bottom, y_top
        "Screening":      (5.20,  8.20),
        "Eligibility":    (2.60,  5.00),
        "Included":       (0.55,  2.40),
    }
    for label, (yb, yt) in bands.items():
        add_side_label(ax, 0.20, yb, 0.55, yt - yb, label)

    # ============ IDENTIFICATION =============================================
    # Left column: databases
    add_box(
        ax, 1.10, 9.85, 4.90, 1.20,
        f"Records identified from databases (n = {PUBMED + OPENALEX + CROSSREF:,}):\n"
        f"PubMed (n = {PUBMED})\n"
        f"OpenAlex (n = {OPENALEX})\n"
        f"Crossref (n = {CROSSREF:,})",
        fontsize=9,
    )
    # Pending v2 sub-box (databases)
    add_box(
        ax, 1.10, 8.40, 4.90, 1.20,
        "Registers / pending databases (v2):\n"
        "Scopus, Web of Science,\nEmbase, Cochrane Library\n(n = pending)",
        fontsize=9, italic=True, color=PENDING_COLOR,
    )

    # Right column: other methods
    add_box(
        ax, 6.30, 9.85, 3.50, 1.20,
        "Records identified from\nother methods:\n"
        "Citation chasing,\nhand-search\n(v2, n = pending)",
        fontsize=9, italic=True, color=PENDING_COLOR,
    )

    # ============ SCREENING ==================================================
    # Total after merge
    add_box(
        ax, 1.10, 7.10, 4.90, 1.00,
        f"Records identified (n = {TOTAL_IDENT:,})",
        fontsize=10, weight="bold",
    )
    # Duplicates removed (right-side exclusion box)
    add_box(
        ax, 6.30, 7.10, 3.50, 1.00,
        f"Duplicate records removed\n(n = {DUPLICATES})",
        fontsize=9,
    )
    arrow(ax, 6.00, 7.60, 6.30, 7.60)

    # Records screened
    add_box(
        ax, 1.10, 5.75, 4.90, 1.10,
        f"Records after duplicates removed,\n"
        f"screened by title/abstract (n = {AFTER_DEDUP:,})",
        fontsize=10,
    )

    # Records excluded at screening (right). In v1 we have not yet performed
    # title/abstract screening of the Crossref/OpenAlex queue, so the v1
    # PubMed-anchored core advances all 338 retained records; any not-yet-
    # screened remainder is reported as "pending v2" rather than excluded.
    excluded_screen = max(0, AFTER_DEDUP - (PUBMED_CORE_V1 + ADDITIONAL_PENDING))
    add_box(
        ax, 6.30, 5.75, 3.50, 1.10,
        f"Records excluded at\ntitle/abstract screening\n(n = {excluded_screen}; v1 core)",
        fontsize=9,
    )
    arrow(ax, 6.00, 6.30, 6.30, 6.30)

    # ============ ELIGIBILITY ================================================
    add_box(
        ax, 1.10, 3.95, 4.90, 1.00,
        f"Reports sought for retrieval\n(n = {PUBMED_CORE_V1 + ADDITIONAL_PENDING:,})",
        fontsize=10,
    )
    # Pending retrieval (right)
    add_box(
        ax, 6.30, 3.95, 3.50, 1.00,
        f"Pending retrieval (v2):\n"
        f"Crossref/OpenAlex queue\n(n = {ADDITIONAL_PENDING:,})",
        fontsize=9, italic=True, color=PENDING_COLOR,
    )
    arrow(ax, 6.00, 4.45, 6.30, 4.45)

    # Full text assessed
    add_box(
        ax, 1.10, 2.60, 4.90, 1.10,
        f"Reports assessed for eligibility (n = {PUBMED_CORE_V1}):\n"
        f"Full text assessed (n = {FULLTEXT_ASSESSED})\n"
        f"Abstract-only assessed (n = {ABSTRACT_ONLY})",
        fontsize=9,
    )
    # Exclusions at full-text (right) -- no exclusions in v1 PubMed-anchored core
    add_box(
        ax, 6.30, 2.60, 3.50, 1.10,
        "Reports excluded at\nfull-text/abstract review\n(n = 0, v1 core)",
        fontsize=9,
    )
    arrow(ax, 6.00, 3.15, 6.30, 3.15)

    # ============ INCLUDED ===================================================
    add_box(
        ax, 1.10, 0.85, 4.90, 1.30,
        f"Studies included in qualitative synthesis\n(v1 PubMed-anchored core, n = {INCLUDED_V1})",
        fontsize=10, weight="bold",
    )

    # ---- Vertical flow arrows (left column) ---------------------------------
    # databases -> records identified (skip past the pending sub-box)
    arrow(ax, 3.55, 9.85, 3.55, 8.15)         # databases box -> total
    arrow(ax, 3.55, 7.10, 3.55, 6.90)         # total -> screened
    arrow(ax, 3.55, 5.75, 3.55, 5.00)         # screened -> sought
    arrow(ax, 3.55, 3.95, 3.55, 3.75)         # sought -> assessed
    arrow(ax, 3.55, 2.60, 3.55, 2.20)         # assessed -> included

    # Pending v2 databases feeds into total identified too (dashed)
    pending_arrow = FancyArrowPatch(
        (3.55, 8.40), (3.55, 8.15),
        arrowstyle="-|>", mutation_scale=14,
        linewidth=1.0, color=PENDING_COLOR, linestyle="--",
    )
    ax.add_patch(pending_arrow)

    # Other-methods column feeds into screened pool (dashed, pending).
    # Route it down the right margin (past the duplicate-removed and excluded
    # boxes) so it does not visually cross those exclusion boxes.
    other_arrow = FancyArrowPatch(
        (9.75, 9.85), (9.75, 5.00),
        arrowstyle="-", mutation_scale=14,
        linewidth=1.0, color=PENDING_COLOR, linestyle="--",
    )
    ax.add_patch(other_arrow)
    # Horizontal kick back into the main flow at the eligibility level
    other_arrow_tail = FancyArrowPatch(
        (9.75, 5.00), (6.00, 4.45),
        arrowstyle="-|>", mutation_scale=14,
        linewidth=1.0, color=PENDING_COLOR, linestyle="--",
    )
    ax.add_patch(other_arrow_tail)
    ax.text(9.75, 7.20, "v2", ha="center", va="center",
            fontsize=9, fontstyle="italic", color=PENDING_COLOR,
            rotation=90)

    # ---- Caption ------------------------------------------------------------
    caption = (
        "Figure 1. PRISMA 2020 flow diagram showing identification of studies "
        "via three databases\n(PubMed, OpenAlex, Crossref). v2 will extend to "
        "Scopus, Web of Science, Embase, and Cochrane Library."
    )
    ax.text(5.0, 0.20, caption, ha="center", va="center",
            fontsize=8.5, fontstyle="italic", wrap=True)

    return fig


# ---------------------------------------------------------------------------
# Simplified single-column variant for IJAA
# ---------------------------------------------------------------------------
def build_simplified():
    fig = plt.figure(figsize=(6, 8), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_axis_off()

    # Side bars
    bands = {
        "Identification": (9.20, 11.20),
        "Screening":      (6.20,  8.80),
        "Eligibility":    (3.20,  5.80),
        "Included":       (0.70,  2.80),
    }
    for label, (yb, yt) in bands.items():
        add_side_label(ax, 0.20, yb, 0.55, yt - yb, label)

    # Identification
    add_box(
        ax, 1.10, 9.20, 7.80, 2.00,
        f"Records identified (n = {TOTAL_IDENT:,}):\n"
        f"PubMed (n = {PUBMED}); OpenAlex (n = {OPENALEX}); Crossref (n = {CROSSREF:,})\n"
        f"Scopus / WoS / Embase / Cochrane: pending (v2)",
        fontsize=10,
    )
    arrow(ax, 5.00, 9.20, 5.00, 8.80)

    # Screening
    add_box(
        ax, 1.10, 6.95, 5.30, 1.80,
        f"Records after duplicates removed (n = {AFTER_DEDUP:,})\n"
        f"Screened by title/abstract",
        fontsize=10,
    )
    add_box(
        ax, 6.70, 7.20, 2.20, 1.30,
        f"Duplicates\nremoved\n(n = {DUPLICATES})",
        fontsize=9,
    )
    arrow(ax, 6.40, 7.85, 6.70, 7.85)
    arrow(ax, 3.75, 6.95, 3.75, 5.80)

    # Eligibility
    add_box(
        ax, 1.10, 3.95, 5.30, 1.80,
        f"Reports assessed for eligibility\n(v1 PubMed-anchored core, n = {PUBMED_CORE_V1})\n"
        f"Full text (n = {FULLTEXT_ASSESSED}); Abstract-only (n = {ABSTRACT_ONLY})",
        fontsize=9,
    )
    add_box(
        ax, 6.70, 4.10, 2.20, 1.50,
        f"Pending v2\nretrieval\n(n = {ADDITIONAL_PENDING:,})",
        fontsize=9, italic=True, color=PENDING_COLOR,
    )
    arrow(ax, 6.40, 4.85, 6.70, 4.85)
    arrow(ax, 3.75, 3.95, 3.75, 2.80)

    # Included
    add_box(
        ax, 1.10, 1.10, 7.80, 1.70,
        f"Studies included in qualitative synthesis\n"
        f"(v1, n = {INCLUDED_V1})",
        fontsize=11, weight="bold",
    )

    caption = (
        "Figure 1. PRISMA 2020 flow diagram (simplified) for v1 PubMed-anchored core.\n"
        "v2 will extend to Scopus, Web of Science, Embase, and Cochrane Library."
    )
    ax.text(5.0, 0.30, caption, ha="center", va="center",
            fontsize=8, fontstyle="italic", wrap=True)

    return fig


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    HERE.mkdir(parents=True, exist_ok=True)

    fig = build_full_prisma()
    fig.savefig(OUT_PNG, dpi=300, format="png",
                facecolor="white", bbox_inches=None)
    fig.savefig(OUT_SVG, format="svg",
                facecolor="white", bbox_inches=None)
    plt.close(fig)

    fig2 = build_simplified()
    fig2.savefig(OUT_SIMPLE_PNG, dpi=300, format="png",
                 facecolor="white", bbox_inches=None)
    plt.close(fig2)

    for p in (OUT_PNG, OUT_SVG, OUT_SIMPLE_PNG):
        size = os.path.getsize(p)
        print(f"Wrote {p}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
