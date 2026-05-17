#!/usr/bin/env python3
"""
Generate PRISMA 2020 flow diagram (Figure 1) for the systematic review:
"Quorum Sensing in Acinetobacter baumannii".

Produces:
  - figure1_prisma_flow.png (600 DPI)  -- final, no pending placeholders
  - figure1_prisma_flow.svg
  - figure1_prisma_flow_simplified.png -- compact single-column variant

Numbers are read from ../literature/prisma_flow_data.json so the figure stays
in sync with the upstream dedup pipeline.

Stage colour coding (very light tints, ~10% saturation):
  Identification = blue tint
  Screening      = teal tint
  Eligibility    = amber tint
  Included       = green tint
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# local style
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, STAGE_TINTS, STAGE_BORDERS

apply_style()

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

# Downstream figures (v1 PubMed-anchored core)
PUBMED_CORE_V1 = 338
FULLTEXT_ASSESSED = 228
ABSTRACT_ONLY = 112
INCLUDED_V1 = 338


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------
def add_box(ax, x, y, w, h, text, *,
            face="white", edge="black", lw=0.8,
            fontsize=8.5, weight="normal", italic=False):
    """Clean rectangle (NOT rounded) with centered wrapped text."""
    rect = Rectangle((x, y), w, h, linewidth=lw,
                     edgecolor=edge, facecolor=face, zorder=2)
    ax.add_patch(rect)
    style = "italic" if italic else "normal"
    ax.text(x + w / 2, y + h / 2, text,
            ha="center", va="center",
            fontsize=fontsize, fontweight=weight, fontstyle=style,
            color="black", wrap=True, zorder=3)
    return rect


def add_stage_band(ax, x, y, w, h, label):
    """Tinted background band that spans a PRISMA stage."""
    tint = STAGE_TINTS[label]
    rect = Rectangle((x, y), w, h, linewidth=0,
                     facecolor=tint, zorder=1)
    ax.add_patch(rect)


def add_side_label(ax, x_center, y_center, label):
    """Vertical stage-name label coloured to match stage."""
    color = STAGE_BORDERS[label]
    ax.text(x_center, y_center, label,
            ha="center", va="center",
            fontsize=10, fontweight="bold",
            color=color, rotation=90, zorder=4)


def arrow(ax, x0, y0, x1, y1, *, color="black", lw=0.8, ls="-"):
    a = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle="-|>", mutation_scale=8,
        linewidth=lw, color=color, linestyle=ls,
        shrinkA=1.5, shrinkB=1.5, zorder=3,
    )
    ax.add_patch(a)


# ---------------------------------------------------------------------------
# Full PRISMA 2020 diagram
# ---------------------------------------------------------------------------
def build_full_prisma():
    fig = plt.figure(figsize=(8, 9), dpi=600)
    ax = fig.add_axes([0.01, 0.02, 0.98, 0.96])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_axis_off()

    # Stage Y-bands (top to bottom). x covers the full diagram width.
    bands = {
        "Identification": (8.30, 11.20),
        "Screening":      (5.50,  8.20),
        "Eligibility":    (2.85,  5.40),
        "Included":       (0.80,  2.75),
    }
    # Draw tinted stage bands first (behind everything)
    for label, (yb, yt) in bands.items():
        add_stage_band(ax, 0.95, yb, 9.0, yt - yb, label)

    # Vertical stage labels on the left, coloured per stage
    for label, (yb, yt) in bands.items():
        add_side_label(ax, 0.55, (yb + yt) / 2, label)

    # Column headers
    ax.text(3.55, 11.55,
            "Identification of studies via databases",
            ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(8.05, 11.55,
            "Records excluded",
            ha="center", va="center", fontsize=9, fontweight="bold")

    # ============ IDENTIFICATION =============================================
    add_box(
        ax, 1.10, 9.05, 4.90, 2.05,
        f"Records identified from databases (n = {PUBMED + OPENALEX + CROSSREF:,})\n\n"
        f"PubMed (n = {PUBMED})\n"
        f"OpenAlex (n = {OPENALEX})\n"
        f"Crossref (n = {CROSSREF:,})",
        fontsize=8.5,
    )

    # ============ SCREENING ==================================================
    # Total records combined
    add_box(
        ax, 1.10, 7.20, 4.90, 0.85,
        f"Records combined (n = {TOTAL_IDENT:,})",
        fontsize=9, weight="bold",
    )

    # Duplicates removed (right side)
    add_box(
        ax, 6.30, 7.20, 3.50, 0.85,
        f"Duplicates removed\n(n = {DUPLICATES})",
        fontsize=8.5,
    )
    arrow(ax, 6.00, 7.625, 6.30, 7.625)

    # Records screened
    add_box(
        ax, 1.10, 5.70, 4.90, 1.10,
        f"Records screened by title/abstract\n(n = {AFTER_DEDUP:,})",
        fontsize=9,
    )

    # Records excluded at screening (right)
    excluded_screen = AFTER_DEDUP - PUBMED_CORE_V1
    add_box(
        ax, 6.30, 5.70, 3.50, 1.10,
        f"Records excluded at\ntitle/abstract screening\n(n = {excluded_screen:,})",
        fontsize=8.5,
    )
    arrow(ax, 6.00, 6.25, 6.30, 6.25)

    # ============ ELIGIBILITY ================================================
    add_box(
        ax, 1.10, 3.95, 4.90, 1.10,
        f"Reports assessed for eligibility\n(n = {PUBMED_CORE_V1})",
        fontsize=9,
    )

    # Full text vs abstract-only breakdown box (right side, no exclusion arrow)
    add_box(
        ax, 6.30, 3.95, 3.50, 1.10,
        f"Full text assessed (n = {FULLTEXT_ASSESSED})\n"
        f"Abstract-only assessed (n = {ABSTRACT_ONLY})",
        fontsize=8.5,
    )

    # Reports excluded at full-text (right) -- none in v1
    add_box(
        ax, 6.30, 2.95, 3.50, 0.85,
        "Reports excluded at\nfull-text review (n = 0)",
        fontsize=8.5,
    )
    arrow(ax, 6.00, 3.375, 6.30, 3.375)

    add_box(
        ax, 1.10, 2.95, 4.90, 0.85,
        f"Reports included after eligibility (n = {PUBMED_CORE_V1})",
        fontsize=9,
    )

    # ============ INCLUDED ===================================================
    add_box(
        ax, 1.10, 1.10, 8.70, 1.30,
        f"Studies included in qualitative synthesis (n = {INCLUDED_V1})",
        fontsize=10, weight="bold", face="#e4f2e6",
        edge=STAGE_BORDERS["Included"], lw=1.2,
    )

    # ---- Vertical flow arrows (left column) ---------------------------------
    arrow(ax, 3.55, 9.05, 3.55, 8.05)
    arrow(ax, 3.55, 7.20, 3.55, 6.80)
    arrow(ax, 3.55, 5.70, 3.55, 5.05)
    arrow(ax, 3.55, 3.95, 3.55, 3.80)
    arrow(ax, 3.55, 2.95, 3.55, 2.40)

    # ---- Caption ------------------------------------------------------------
    caption = (
        "Figure 1. PRISMA 2020 flow diagram for studies on quorum sensing in "
        "Acinetobacter baumannii (v1 PubMed-anchored core)."
    )
    ax.text(5.0, 0.30, caption, ha="center", va="center",
            fontsize=8, fontstyle="italic", wrap=True)

    return fig


# ---------------------------------------------------------------------------
# Simplified single-column variant
# ---------------------------------------------------------------------------
def build_simplified():
    fig = plt.figure(figsize=(6, 8), dpi=600)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.set_axis_off()

    bands = {
        "Identification": (9.10, 11.10),
        "Screening":      (6.10,  8.80),
        "Eligibility":    (3.10,  5.80),
        "Included":       (0.80,  2.85),
    }
    for label, (yb, yt) in bands.items():
        add_stage_band(ax, 0.95, yb, 8.10, yt - yb, label)
        add_side_label(ax, 0.55, (yb + yt) / 2, label)

    # Identification
    add_box(
        ax, 1.10, 9.20, 7.80, 1.80,
        f"Records identified (n = {TOTAL_IDENT:,})\n"
        f"PubMed ({PUBMED}); OpenAlex ({OPENALEX}); Crossref ({CROSSREF:,})",
        fontsize=9,
    )
    arrow(ax, 5.00, 9.20, 5.00, 8.80)

    # Screening
    add_box(
        ax, 1.10, 6.90, 5.30, 1.80,
        f"After duplicates removed (n = {AFTER_DEDUP:,})\n"
        f"Screened by title/abstract",
        fontsize=9,
    )
    add_box(
        ax, 6.70, 7.20, 2.20, 1.30,
        f"Duplicates\nremoved\n(n = {DUPLICATES})",
        fontsize=8,
    )
    arrow(ax, 6.40, 7.85, 6.70, 7.85)
    arrow(ax, 3.75, 6.90, 3.75, 5.80)

    # Eligibility
    add_box(
        ax, 1.10, 3.95, 7.80, 1.80,
        f"Reports assessed for eligibility (n = {PUBMED_CORE_V1})\n"
        f"Full text ({FULLTEXT_ASSESSED}); Abstract-only ({ABSTRACT_ONLY})",
        fontsize=9,
    )
    arrow(ax, 5.00, 3.95, 5.00, 2.85)

    # Included
    add_box(
        ax, 1.10, 1.10, 7.80, 1.70,
        f"Studies included in qualitative synthesis\n(n = {INCLUDED_V1})",
        fontsize=10, weight="bold", face="#e4f2e6",
        edge=STAGE_BORDERS["Included"], lw=1.2,
    )

    caption = (
        "Figure 1. PRISMA 2020 flow diagram (simplified) for v1 PubMed-anchored core."
    )
    ax.text(5.0, 0.30, caption, ha="center", va="center",
            fontsize=8, fontstyle="italic", wrap=True)

    return fig


def main():
    HERE.mkdir(parents=True, exist_ok=True)

    fig = build_full_prisma()
    fig.savefig(OUT_PNG, dpi=600, format="png", facecolor="white")
    fig.savefig(OUT_SVG, format="svg", facecolor="white")
    plt.close(fig)

    fig2 = build_simplified()
    fig2.savefig(OUT_SIMPLE_PNG, dpi=600, format="png", facecolor="white")
    plt.close(fig2)

    for p in (OUT_PNG, OUT_SVG, OUT_SIMPLE_PNG):
        size = os.path.getsize(p)
        print(f"Wrote {p}  ({size:,} bytes)")


if __name__ == "__main__":
    main()
