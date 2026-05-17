"""Shared IJAA-style configuration for all figures.

Import as: from _style import apply_style, PALETTE, panel_label
"""
from __future__ import annotations

import matplotlib as mpl


PALETTE = {
    "blue":   "#2E5C8A",
    "red":    "#D62828",
    "teal":   "#52796F",
    "amber":  "#E89C2A",
    "purple": "#7B2CBF",
    "gray":   "#6c757d",
    "lightgray": "#bfbfbf",
}

# Lighter stage tints (10-15% saturation) for PRISMA backgrounds
STAGE_TINTS = {
    "Identification": "#e8eef7",   # blue tint
    "Screening":      "#e6efec",   # teal tint
    "Eligibility":    "#fbf1de",   # amber tint
    "Included":       "#e4f2e6",   # green tint
}
STAGE_BORDERS = {
    "Identification": "#2E5C8A",
    "Screening":      "#52796F",
    "Eligibility":    "#E89C2A",
    "Included":       "#3a8a4d",
}


def apply_style() -> None:
    """Apply the unified IJAA-style rcParams used across all figures."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Liberation Sans", "Arial", "DejaVu Sans"],
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.labelsize": 9,
        "axes.labelweight": "normal",
        "axes.linewidth": 0.8,
        "axes.edgecolor": "#333333",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "xtick.major.width": 0.7,
        "ytick.major.width": 0.7,
        "legend.fontsize": 8,
        "legend.frameon": False,
        "figure.titlesize": 11,
        "figure.titleweight": "bold",
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.15,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
    })


def panel_label(ax, letter: str, x: float = 0.02, y: float = 0.98) -> None:
    """Add a bold 12pt panel label (A, B, C...) at top-left of an axes."""
    ax.text(
        x, y, letter,
        transform=ax.transAxes,
        fontsize=12, fontweight="bold",
        va="top", ha="left",
    )
