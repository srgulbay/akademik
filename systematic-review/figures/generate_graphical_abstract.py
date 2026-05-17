"""Generate a graphical abstract for the IJAA submission.

Layout: 3 horizontal panels with full-width top/bottom banners.
- Top banner (~10% height): Title, bold.
- Panel A (~30% width): Simplified QS circuit (AbaI -> AHL -> AbaR -> output).
- Panel B (~30% width): Bar chart of 7 intervention classes by maturity.
- Panel C (~30% width): Pictogram outcomes — Biofilm / Virulence / MIC.
- Bottom banner (~15% height): Italic take-home message.

Saves PNG (1200x900 px footprint, 600 DPI internally) and editable SVG.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (
    FancyArrowPatch, FancyBboxPatch, Rectangle, RegularPolygon, Polygon,
    Circle, PathPatch,
)
from matplotlib.path import Path as MPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE

apply_style()

OUT_DIR = Path(__file__).resolve().parent
OUT_PNG = OUT_DIR / "graphical_abstract.png"
OUT_SVG = OUT_DIR / "graphical_abstract.svg"

# Layout: 1200x900 px @ 600 dpi  ->  2 x 1.5 inches at 600dpi
# Use 12x9 inch canvas at 100 dpi displayable (the 600 dpi raster will be sharp)
FIG_W, FIG_H = 12.0, 9.0
fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=600)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.set_aspect("equal")
ax.axis("off")

# Background white
ax.add_patch(Rectangle((0, 0), FIG_W, FIG_H, facecolor="white", zorder=0))

# ---------------------------------------------------------------------------
# Banner constants
# ---------------------------------------------------------------------------
TOP_BANNER_H = 0.10 * FIG_H        # 0.9 in
BOTTOM_BANNER_H = 0.13 * FIG_H     # ~1.17 in
PANEL_H = FIG_H - TOP_BANNER_H - BOTTOM_BANNER_H
PANEL_Y0 = BOTTOM_BANNER_H

# ---------------------------------------------------------------------------
# Top banner
# ---------------------------------------------------------------------------
ax.add_patch(Rectangle(
    (0, FIG_H - TOP_BANNER_H), FIG_W, TOP_BANNER_H,
    facecolor=PALETTE["blue"], edgecolor="none", zorder=1,
))
ax.text(
    FIG_W / 2, FIG_H - TOP_BANNER_H / 2,
    "Quorum sensing as a therapeutic target in Acinetobacter baumannii:\n"
    "22 years of evidence",
    ha="center", va="center",
    fontsize=18, fontweight="bold", color="white", zorder=2,
)

# ---------------------------------------------------------------------------
# Bottom banner
# ---------------------------------------------------------------------------
ax.add_patch(Rectangle(
    (0, 0), FIG_W, BOTTOM_BANNER_H,
    facecolor="#f4f1e8", edgecolor=PALETTE["amber"], linewidth=2, zorder=1,
))
ax.text(
    FIG_W / 2, BOTTOM_BANNER_H / 2 + 0.20,
    "Adjunctive QSI–antibiotic combinations and phage cocktails",
    ha="center", va="center",
    fontsize=13, fontstyle="italic", color="#3a3a3a", zorder=2,
)
ax.text(
    FIG_W / 2, BOTTOM_BANNER_H / 2 - 0.30,
    "are the nearest-term clinical strategies",
    ha="center", va="center",
    fontsize=13, fontstyle="italic", color="#3a3a3a", zorder=2,
)

# Compute panel x-extents
PANEL_W = FIG_W / 3.0

# ---------------------------------------------------------------------------
# Panel A — simplified QS circuit
# ---------------------------------------------------------------------------
PA_X0 = 0.0
PA_X1 = PANEL_W

ax.text(
    PA_X0 + PANEL_W / 2, FIG_H - TOP_BANNER_H - 0.45,
    "A   QS circuit",
    ha="center", va="top",
    fontsize=13, fontweight="bold", color=PALETTE["blue"],
)

# Vertical centre of panel area
pa_cy = PANEL_Y0 + PANEL_H / 2 - 0.30

# AbaI green pentagon
abaI_x = PA_X0 + 0.65
abaI_y = pa_cy
ax.add_patch(RegularPolygon(
    (abaI_x, abaI_y), numVertices=5, radius=0.45,
    orientation=0, facecolor="#3a8a4d", edgecolor="black", lw=1.2, zorder=4,
))
ax.text(abaI_x, abaI_y, "AbaI", ha="center", va="center",
        fontsize=11, fontweight="bold", color="white", zorder=5)
ax.text(abaI_x, abaI_y - 0.85, "synthase",
        ha="center", va="center", fontsize=9, fontstyle="italic", color="#234d2c")

# AHL molecule (lactone ring + tail)
ahl_x = PA_X0 + 1.85
ahl_y = pa_cy
ring_r = 0.22
ax.add_patch(RegularPolygon(
    (ahl_x, ahl_y), numVertices=5, radius=ring_r,
    orientation=np.pi / 2, facecolor=PALETTE["blue"],
    edgecolor="black", lw=0.9, zorder=4,
))
ax.text(ahl_x, ahl_y, "O", ha="center", va="center",
        fontsize=8, fontweight="bold", color="white", zorder=5)
# C12 zigzag tail to the right
verts = [(ahl_x + ring_r + 0.03, ahl_y)]
step = 0.14
amp = 0.07
for i in range(1, 7):
    verts.append((ahl_x + ring_r + 0.03 + i * step, ahl_y + (amp if i % 2 else -amp)))
codes = [MPath.MOVETO] + [MPath.LINETO] * 6
ax.add_patch(PathPatch(MPath(verts, codes), edgecolor=PALETTE["blue"],
                       lw=1.5, fill=False, zorder=4))
ax.text(ahl_x, ahl_y - 0.85, "AHL signal",
        ha="center", va="center", fontsize=9, fontstyle="italic", color=PALETTE["blue"])

# Arrow AbaI -> AHL
ax.add_patch(FancyArrowPatch(
    (abaI_x + 0.50, abaI_y), (ahl_x - ring_r - 0.04, ahl_y),
    arrowstyle="-|>", mutation_scale=15, color="black", lw=1.4, zorder=3,
))

# AbaR two-domain rectangle
abaR_w, abaR_h = 1.05, 0.55
abaR_x = PA_X0 + 2.75
abaR_y = pa_cy - abaR_h / 2
ax.add_patch(Rectangle(
    (abaR_x, abaR_y), abaR_w / 2, abaR_h,
    facecolor=PALETTE["amber"], edgecolor="black", lw=1.2, zorder=4,
))
ax.add_patch(Rectangle(
    (abaR_x + abaR_w / 2, abaR_y), abaR_w / 2, abaR_h,
    facecolor="#f1b966", edgecolor="black", lw=1.2, zorder=4,
))
ax.plot([abaR_x + abaR_w / 2] * 2,
        [abaR_y + 0.04, abaR_y + abaR_h - 0.04],
        color="black", lw=0.7, zorder=5)
ax.text(abaR_x + abaR_w / 2, abaR_y + abaR_h / 2,
        "AbaR", ha="center", va="center",
        fontsize=11, fontweight="bold", color="black", zorder=5)
ax.text(abaR_x + abaR_w / 2, abaR_y - 0.35, "receptor",
        ha="center", va="center", fontsize=9, fontstyle="italic", color="#a35400")

# Arrow AHL -> AbaR (zigzag end approx ahl_x + 6*step + ring_r + 0.03)
ahl_tail_end = ahl_x + ring_r + 0.03 + 6 * step
ax.add_patch(FancyArrowPatch(
    (ahl_tail_end + 0.05, ahl_y), (abaR_x - 0.04, abaR_y + abaR_h / 2),
    arrowstyle="-|>", mutation_scale=15, color="black", lw=1.4, zorder=3,
))

# Output gene cluster (three small grey boxes representing target operon)
out_x0 = PA_X0 + 0.50
out_y = pa_cy - 1.60
out_w = PANEL_W - 1.0
ax.add_patch(FancyBboxPatch(
    (out_x0, out_y - 0.30), out_w, 0.65,
    boxstyle="round,pad=0.02,rounding_size=0.06",
    facecolor="#eaeaea", edgecolor="#666", lw=1.0, zorder=3,
))
ax.text(out_x0 + out_w / 2, out_y + 0.13,
        "Target gene cluster", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#222", zorder=4)
ax.text(out_x0 + out_w / 2, out_y - 0.15,
        "biofilm · motility · virulence · efflux",
        ha="center", va="center", fontsize=8.5, fontstyle="italic", color="#444",
        zorder=4)

# Arrow AbaR -> output cluster
ax.add_patch(FancyArrowPatch(
    (abaR_x + abaR_w / 2, abaR_y - 0.05),
    (out_x0 + out_w / 2, out_y + 0.40),
    arrowstyle="-|>", mutation_scale=15, color="black", lw=1.4, zorder=3,
))

# ---------------------------------------------------------------------------
# Panel B — intervention classes bar chart
# ---------------------------------------------------------------------------
PB_X0 = PANEL_W
PB_X1 = 2 * PANEL_W

ax.text(
    PB_X0 + PANEL_W / 2, FIG_H - TOP_BANNER_H - 0.45,
    "B   Intervention classes (n=340)",
    ha="center", va="top",
    fontsize=13, fontweight="bold", color=PALETTE["blue"],
)

# Data: 7 intervention classes (sorted by total descending)
# total counts and maturity (animal+clinical) split
interventions = [
    ("phage",              50, 15),  # 15 of 50 are animal/clinical
    ("natural product",    30, 11),
    ("peptide",            19,  6),
    ("enzyme QQ",          17,  9),
    ("nanoparticle",       12,  5),
    ("synthetic cmpd",     11,  4),
    ("repurposed drug",    10,  5),
]
# Order by total desc
interventions.sort(key=lambda x: x[1], reverse=True)

# Place a sub-axes for this panel chart
pb_ax_left   = (PB_X0 + 1.10) / FIG_W
pb_ax_bottom = (PANEL_Y0 + 0.50) / FIG_H
pb_ax_width  = (PANEL_W - 1.30) / FIG_W
pb_ax_height = (PANEL_H - 1.30) / FIG_H
ax_b = fig.add_axes([pb_ax_left, pb_ax_bottom, pb_ax_width, pb_ax_height])

names  = [t[0] for t in interventions]
totals = np.array([t[1] for t in interventions], dtype=float)
maturs = np.array([t[2] for t in interventions], dtype=float)
prelim = totals - maturs

ypos = np.arange(len(interventions))
ax_b.barh(ypos, prelim, color="#cfe2f3", edgecolor="white",
          linewidth=0.7, height=0.62, label="in vitro / in silico")
ax_b.barh(ypos, maturs, left=prelim, color=PALETTE["red"],
          edgecolor="white", linewidth=0.7, height=0.62,
          label="animal / clinical")
for i, t in enumerate(totals):
    ax_b.text(t + 1.2, i, f"{int(t)}", va="center",
              ha="left", fontsize=10, fontweight="bold", color="#222")
ax_b.set_yticks(ypos)
ax_b.set_yticklabels(names, fontsize=10)
ax_b.invert_yaxis()
ax_b.set_xlim(0, totals.max() * 1.20)
ax_b.set_xlabel("Papers", fontsize=10)
ax_b.tick_params(axis="x", labelsize=9)
ax_b.spines["top"].set_visible(False)
ax_b.spines["right"].set_visible(False)
ax_b.legend(loc="lower right", frameon=False, fontsize=9)

# ---------------------------------------------------------------------------
# Panel C — pictogram outcomes
# ---------------------------------------------------------------------------
PC_X0 = 2 * PANEL_W
PC_X1 = 3 * PANEL_W

ax.text(
    PC_X0 + PANEL_W / 2, FIG_H - TOP_BANNER_H - 0.45,
    "C   Key effect sizes",
    ha="center", va="top",
    fontsize=13, fontweight="bold", color=PALETTE["blue"],
)

# Three icon-text rows
row_centers = [pa_cy + 1.0, pa_cy - 0.05, pa_cy - 1.15]
icon_x = PC_X0 + 0.95

outcomes = [
    ("Biofilm",   "50–80% ↓",   "sub-MIC QSI",            PALETTE["teal"]),
    ("Virulence", "30–70% ↓",   "gene/factor reduction",  PALETTE["purple"]),
    ("MIC",       "2–8× ↓",     "adjunct synergy",        PALETTE["red"]),
]

def draw_biofilm_icon(ax, cx, cy, color):
    """Three stacked stylised cells representing a biofilm."""
    for i, (dx, dy, r) in enumerate([(-0.22, -0.10, 0.18),
                                      (0.05, 0.08, 0.20),
                                      (0.25, -0.10, 0.17)]):
        ax.add_patch(Circle((cx + dx, cy + dy), r,
                            facecolor=color, edgecolor="black",
                            lw=0.8, alpha=0.85, zorder=4))

def draw_virulence_icon(ax, cx, cy, color):
    """A bacterium-cell with two short flagella."""
    ax.add_patch(mpatches.Ellipse((cx, cy), width=0.55, height=0.30,
                                  facecolor=color, edgecolor="black",
                                  lw=0.9, zorder=4))
    # flagella
    ax.add_patch(FancyArrowPatch(
        (cx + 0.28, cy + 0.04), (cx + 0.55, cy + 0.18),
        arrowstyle="-", color="black", lw=1.0, zorder=4,
        connectionstyle="arc3,rad=0.3",
    ))
    ax.add_patch(FancyArrowPatch(
        (cx + 0.28, cy - 0.04), (cx + 0.55, cy - 0.18),
        arrowstyle="-", color="black", lw=1.0, zorder=4,
        connectionstyle="arc3,rad=-0.3",
    ))

def draw_mic_icon(ax, cx, cy, color):
    """A small antibiotic-tablet icon: rectangle with cross."""
    w, h = 0.50, 0.32
    ax.add_patch(FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=color, edgecolor="black", lw=0.9, zorder=4,
    ))
    # split line
    ax.plot([cx, cx], [cy - h / 2 + 0.04, cy + h / 2 - 0.04],
            color="black", lw=0.7, zorder=5)

icon_drawers = [draw_biofilm_icon, draw_virulence_icon, draw_mic_icon]

for (label, magnitude, mech, color), cy_row, icon_fn in zip(
        outcomes, row_centers, icon_drawers):
    icon_fn(ax, icon_x, cy_row, color)
    # Label
    ax.text(icon_x + 0.70, cy_row + 0.22, label,
            ha="left", va="center", fontsize=14, fontweight="bold",
            color=color, zorder=5)
    # Magnitude (largest text)
    ax.text(icon_x + 0.70, cy_row - 0.05, magnitude,
            ha="left", va="center", fontsize=16, fontweight="bold",
            color="#222", zorder=5)
    # Mechanism subtitle
    ax.text(icon_x + 0.70, cy_row - 0.32, mech,
            ha="left", va="center", fontsize=9, fontstyle="italic",
            color="#555", zorder=5)

# ---------------------------------------------------------------------------
# Panel dividers (thin grey lines)
# ---------------------------------------------------------------------------
for x in (PANEL_W, 2 * PANEL_W):
    ax.plot([x, x],
            [PANEL_Y0 + 0.20, FIG_H - TOP_BANNER_H - 0.15],
            color="#cccccc", lw=0.7, zorder=2)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
fig.savefig(OUT_PNG, dpi=600, facecolor="white")
fig.savefig(OUT_SVG, facecolor="white")
plt.close(fig)

print(f"Wrote: {OUT_PNG}  ({os.path.getsize(OUT_PNG):,} bytes)")
print(f"Wrote: {OUT_SVG}  ({os.path.getsize(OUT_SVG):,} bytes)")
