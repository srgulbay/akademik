"""
Figure 3B: Second-messenger integration with the QS decision point.

Simplified layout:
- Central rounded amber rectangle: "QS decision (AbaR + AHL)"
- Three pools as coloured circles around it:
    c-di-GMP (green)   at  9 o'clock - activation (+) arrow inward
    (p)ppGpp (red)     at 12 o'clock - repression (-) arrow inward
    3',5'-cAMP (blue)  at  3 o'clock - repression (-) arrow inward
- Enzyme producers as small annotations next to each pool
- Outputs as four small grey rounded boxes at bottom (Biofilm, Motility,
  Virulence, Efflux)
- "Inputs sensed" as a thin footer banner

Outputs:
- figure3b_second_messengers.png (600 DPI, 8x6 in)
- figure3b_second_messengers.svg
"""

import os
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE

apply_style()

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------------
# Palette (from unified palette)
# -----------------------------------------------------------------------------
COL_CDG   = "#3a8a4d"      # c-di-GMP   = green
COL_PPGPP = PALETTE["red"]
COL_CAMP  = PALETTE["blue"]
COL_QS    = PALETTE["amber"]
COL_OUT   = "#bfbfbf"

# -----------------------------------------------------------------------------
# Figure
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=600)
ax.set_xlim(0, 10)
ax.set_ylim(-0.6, 7)
ax.set_aspect("equal")
ax.axis("off")

ax.text(5.0, 6.75,
        "Second-messenger integration with the QS decision point",
        ha="center", va="center", fontsize=10, fontweight="bold")

# -----------------------------------------------------------------------------
# Central QS decision (large rounded amber rectangle)
# -----------------------------------------------------------------------------
qs_cx, qs_cy = 5.0, 3.50
qs_w, qs_h = 2.20, 1.20
ax.add_patch(FancyBboxPatch(
    (qs_cx - qs_w/2, qs_cy - qs_h/2), qs_w, qs_h,
    boxstyle="round,pad=0.04,rounding_size=0.15",
    facecolor=COL_QS, edgecolor="black", lw=1.4, zorder=5,
))
ax.text(qs_cx, qs_cy + 0.18, "QS decision",
        ha="center", va="center", fontsize=11, fontweight="bold",
        color="white", zorder=6)
ax.text(qs_cx, qs_cy - 0.18, "(AbaR + AHL)",
        ha="center", va="center", fontsize=8, style="italic",
        color="white", zorder=6)

# -----------------------------------------------------------------------------
# Three pools at 9, 12, 3 o'clock
# -----------------------------------------------------------------------------
def draw_pool(ax, x, y, color, name, sign, enzyme_text):
    """Coloured circle + label + small enzyme annotation."""
    ax.add_patch(Circle((x, y), 0.55, facecolor=color,
                        edgecolor="black", lw=1.0, zorder=5))
    ax.text(x, y, name, ha="center", va="center",
            fontsize=8, fontweight="bold", color="white", zorder=6)
    # enzyme annotation positioned away from QS centre
    ax.text(x, y - 0.85, enzyme_text, ha="center", va="top",
            fontsize=6.5, style="italic", color="#444")


# c-di-GMP pool at 9 o'clock
cdg_x, cdg_y = 1.65, 3.50
draw_pool(ax, cdg_x, cdg_y, COL_CDG, "c-di-GMP", "+",
          "GGDEF (DGC):\nA1S_1695 / 2506 / 3692")
# Activation arrow inward (+)
arr_cdg = FancyArrowPatch(
    (cdg_x + 0.55, cdg_y), (qs_cx - qs_w/2 - 0.02, qs_cy),
    arrowstyle="-|>", mutation_scale=12, color=COL_CDG,
    lw=2.0, zorder=4,
)
ax.add_patch(arr_cdg)
ax.text((cdg_x + 0.55 + qs_cx - qs_w/2) / 2, qs_cy + 0.18, "+",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color=COL_CDG, zorder=6)

# (p)ppGpp pool at 12 o'clock
ppg_x, ppg_y = 5.0, 5.50
draw_pool(ax, ppg_x, ppg_y, COL_PPGPP, "(p)ppGpp", "-",
          "RelA_Ab (ABUW_3302):\nstringent response")
# Repression arrow inward (T-bar)
arr_ppg = FancyArrowPatch(
    (ppg_x, ppg_y - 0.55), (ppg_x, qs_cy + qs_h/2 + 0.02),
    arrowstyle="-[", mutation_scale=12, color=COL_PPGPP,
    lw=2.0, zorder=4,
)
ax.add_patch(arr_ppg)
ax.text(ppg_x + 0.25, (ppg_y - 0.55 + qs_cy + qs_h/2) / 2, "−",
        ha="left", va="center", fontsize=12, fontweight="bold",
        color=COL_PPGPP, zorder=6)
ax.text(ppg_x, ppg_y + 0.95, "represses ABUW_1132",
        ha="center", va="bottom", fontsize=6.5, style="italic",
        color=COL_PPGPP)

# 3',5'-cAMP pool at 3 o'clock
cmp_x, cmp_y = 8.35, 3.50
draw_pool(ax, cmp_x, cmp_y, COL_CAMP, "3',5'-cAMP", "-",
          "CavA (adenylate cyclase)\n→ VfrAb")
# Repression arrow inward (T-bar)
arr_cmp = FancyArrowPatch(
    (cmp_x - 0.55, cmp_y), (qs_cx + qs_w/2 + 0.02, qs_cy),
    arrowstyle="-[", mutation_scale=12, color=COL_CAMP,
    lw=2.0, zorder=4,
)
ax.add_patch(arr_cmp)
ax.text((cmp_x - 0.55 + qs_cx + qs_w/2) / 2, qs_cy + 0.18, "−",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color=COL_CAMP, zorder=6)
ax.text(cmp_x, cmp_y + 0.95, "represses abaI",
        ha="center", va="bottom", fontsize=6.5, style="italic",
        color=COL_CAMP)

# -----------------------------------------------------------------------------
# Output boxes (bottom row)
# -----------------------------------------------------------------------------
outputs = [
    ("Biofilm", "csu, bap,\npgaABCD"),
    ("Motility", "twitching,\nsurface"),
    ("Virulence", "OmpA, OMVs,\nacinetobactin"),
    ("Efflux", "adeABC, adeFGH,\nadeIJK"),
]
out_w, out_h = 1.80, 0.85
out_y = 1.10
start_x = (10 - (4 * out_w + 3 * 0.20)) / 2
for i, (title, body) in enumerate(outputs):
    bx = start_x + i * (out_w + 0.20)
    ax.add_patch(FancyBboxPatch(
        (bx, out_y - out_h), out_w, out_h,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        facecolor=COL_OUT, edgecolor="black", lw=0.8, zorder=4,
    ))
    ax.text(bx + out_w/2, out_y - 0.20, title,
            ha="center", va="center", fontsize=8.5, fontweight="bold",
            color="#222", zorder=6)
    ax.text(bx + out_w/2, out_y - 0.55, body,
            ha="center", va="center", fontsize=6.5, fontstyle="italic",
            color="#333", zorder=6)

# Fan-out arrows from QS to each output
for i in range(len(outputs)):
    bx = start_x + i * (out_w + 0.20) + out_w/2
    arr = FancyArrowPatch(
        (qs_cx, qs_cy - qs_h/2 - 0.02), (bx, out_y + 0.02),
        arrowstyle="-|>", mutation_scale=10, color="#444",
        lw=1.0, zorder=3,
    )
    ax.add_patch(arr)

# -----------------------------------------------------------------------------
# Inputs-sensed footer banner (thin, full width near bottom)
# -----------------------------------------------------------------------------
ib_x, ib_y, ib_w, ib_h = 0.50, -0.05, 9.0, 0.40
ax.add_patch(FancyBboxPatch(
    (ib_x, ib_y), ib_w, ib_h,
    boxstyle="round,pad=0.02,rounding_size=0.05",
    facecolor="#fef7e0", edgecolor="#b8860b", lw=0.8, zorder=4,
))
ax.text(ib_x + 0.20, ib_y + ib_h/2, "Inputs sensed:",
        ha="left", va="center", fontsize=7.5,
        fontweight="bold", color="#7a5a00", zorder=6)
ax.text(ib_x + ib_w/2 + 0.55, ib_y + ib_h/2,
        "cell density · nutrient state · host cues · carbon source",
        ha="center", va="center", fontsize=7,
        fontstyle="italic", color="#5a4400", zorder=6)

# -----------------------------------------------------------------------------
# Legend at the very bottom-left
# -----------------------------------------------------------------------------
leg_handles = [
    mpatches.Patch(color=COL_CDG,   label="c-di-GMP"),
    mpatches.Patch(color=COL_PPGPP, label="(p)ppGpp"),
    mpatches.Patch(color=COL_CAMP,  label="3',5'-cAMP"),
    mpatches.Patch(color=COL_QS,    label="QS decision"),
    mpatches.Patch(color=COL_OUT,   label="outputs"),
    Line2D([0], [0], color="black", lw=1.2, marker=">", markersize=5,
           label="activation (+)"),
    Line2D([0], [0], color=COL_PPGPP, lw=1.6, marker="_", markersize=8,
           label="repression (−)"),
]
ax.legend(handles=leg_handles, loc="lower center",
          bbox_to_anchor=(0.5, -0.10),
          fontsize=6.5, frameon=False, ncol=7,
          handlelength=1.1, columnspacing=0.8,
          handletextpad=0.35)

# -----------------------------------------------------------------------------
# Save
# -----------------------------------------------------------------------------
png_path = os.path.join(OUT_DIR, "figure3b_second_messengers.png")
svg_path = os.path.join(OUT_DIR, "figure3b_second_messengers.svg")
plt.savefig(png_path, dpi=600, facecolor="white")
plt.savefig(svg_path, facecolor="white")
plt.close(fig)

print(f"Wrote: {png_path}  ({os.path.getsize(png_path):,} bytes)")
print(f"Wrote: {svg_path}  ({os.path.getsize(svg_path):,} bytes)")
