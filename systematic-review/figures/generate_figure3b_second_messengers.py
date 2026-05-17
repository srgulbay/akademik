"""
Figure 3B: Second-messenger integration with the QS decision point in
Acinetobacter baumannii.

Renders the three-pool nucleotide-second-messenger network
(c-di-GMP, (p)ppGpp, 3',5'-cAMP) converging on the AbaR-AHL QS decision
point, and the downstream phenotypic outputs.

Outputs:
- figure3b_second_messengers.png (300 DPI, 10x7 in)
- figure3b_second_messengers.svg
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
from matplotlib.lines import Line2D

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------------
# Color palette
# -----------------------------------------------------------------------------
COL_CDG    = "#2ca02c"   # c-di-GMP   = green
COL_PPGPP  = "#d62728"   # (p)ppGpp   = red
COL_CAMP   = "#1f77b4"   # cAMP       = blue
COL_QS     = "#f1c40f"   # QS decision = amber/yellow
COL_OUT    = "#bdbdbd"   # outputs    = gray
COL_TEXT   = "#222222"

# -----------------------------------------------------------------------------
# Figure
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.axis("off")

ax.text(5.0, 6.78,
        "Figure 3B.  Second-messenger integration with the QS decision point",
        ha="center", va="center", fontsize=12, fontweight="bold")

# -----------------------------------------------------------------------------
# Central QS decision point (AbaR-AHL complex)
# -----------------------------------------------------------------------------
qs_x, qs_y, qs_w, qs_h = 4.05, 3.05, 1.9, 1.0
ax.add_patch(FancyBboxPatch((qs_x, qs_y), qs_w, qs_h,
                            boxstyle="round,pad=0.04,rounding_size=0.12",
                            facecolor=COL_QS, edgecolor="black",
                            lw=1.8, zorder=5))
ax.text(qs_x + qs_w/2, qs_y + qs_h/2 + 0.18,
        "QS decision point",
        ha="center", va="center", fontsize=10, fontweight="bold",
        color=COL_TEXT, zorder=6)
ax.text(qs_x + qs_w/2, qs_y + qs_h/2 - 0.15,
        "(AbaR-AHL complex)",
        ha="center", va="center", fontsize=8, style="italic",
        color="#5a4a00", zorder=6)

# -----------------------------------------------------------------------------
# LEFT pool: c-di-GMP (green)
# -----------------------------------------------------------------------------
cdg_x, cdg_y = 1.55, 3.55
ax.add_patch(FancyBboxPatch((cdg_x-0.95, cdg_y-0.85), 1.9, 1.7,
                            boxstyle="round,pad=0.03,rounding_size=0.1",
                            facecolor="#eafbe7", edgecolor=COL_CDG,
                            lw=1.6, zorder=3))
ax.text(cdg_x, cdg_y + 0.65, "c-di-GMP pool",
        ha="center", fontsize=9.5, fontweight="bold", color=COL_CDG)

# GGDEF DGCs (3 small circles)
for i, lab in enumerate(["A1S_1695", "A1S_2506", "A1S_3692"]):
    cx = cdg_x - 0.55 + i*0.55
    cy = cdg_y + 0.20
    ax.add_patch(Circle((cx, cy), 0.18, facecolor=COL_CDG,
                        edgecolor="black", lw=0.8, zorder=5))
    ax.text(cx, cy - 0.32, lab, ha="center", fontsize=5.5, color="#1a4a1a")
ax.text(cdg_x, cdg_y + 0.42, "GGDEF (DGC)", ha="center",
        fontsize=6.5, style="italic", color="#1a4a1a")

# Diamond = c-di-GMP molecule
diamond = mpatches.RegularPolygon((cdg_x, cdg_y - 0.30), numVertices=4,
                                  radius=0.18, orientation=0,
                                  facecolor=COL_CDG, edgecolor="black",
                                  lw=1.0, zorder=5)
ax.add_patch(diamond)
ax.text(cdg_x, cdg_y - 0.30, "c-di-GMP", ha="center", va="center",
        fontsize=5.5, fontweight="bold", color="white", zorder=6)

# EAL (degrades) - small box
ax.add_patch(Rectangle((cdg_x - 0.85, cdg_y - 0.70), 0.55, 0.20,
                       facecolor="#a8d8a3", edgecolor="black",
                       lw=0.7, zorder=5))
ax.text(cdg_x - 0.575, cdg_y - 0.60, "EAL A1S_1254",
        ha="center", va="center", fontsize=5.5, color="black", zorder=6)
# Arrow EAL -> degrade diamond
arr_eal = FancyArrowPatch((cdg_x - 0.30, cdg_y - 0.60),
                          (cdg_x - 0.18, cdg_y - 0.32),
                          arrowstyle="-|>", mutation_scale=8,
                          color=COL_PPGPP, lw=0.9, zorder=4)
ax.add_patch(arr_eal)

# Effector EF-P
ax.add_patch(Rectangle((cdg_x + 0.10, cdg_y - 0.70), 0.65, 0.20,
                       facecolor="#a8d8a3", edgecolor="black",
                       lw=0.7, zorder=5))
ax.text(cdg_x + 0.425, cdg_y - 0.60, "EF-P A1S_2419",
        ha="center", va="center", fontsize=5.5, color="black", zorder=6)

# Biofilm output text (small)
ax.text(cdg_x, cdg_y - 0.92, "-> biofilm",
        ha="center", fontsize=6, style="italic", color="#1a4a1a")

# Arrow from c-di-GMP pool -> QS
arr_cdg = FancyArrowPatch((cdg_x + 0.95, cdg_y),
                          (qs_x - 0.02, qs_y + qs_h*0.5),
                          arrowstyle="-|>", mutation_scale=14,
                          color=COL_CDG, lw=2.0, zorder=4)
ax.add_patch(arr_cdg)

# -----------------------------------------------------------------------------
# TOP pool: (p)ppGpp (red)
# -----------------------------------------------------------------------------
ppg_x, ppg_y = 5.0, 5.65
ax.add_patch(FancyBboxPatch((ppg_x-1.3, ppg_y-0.55), 2.6, 1.1,
                            boxstyle="round,pad=0.03,rounding_size=0.1",
                            facecolor="#fde7e7", edgecolor=COL_PPGPP,
                            lw=1.6, zorder=3))
ax.text(ppg_x, ppg_y + 0.35, "(p)ppGpp pool",
        ha="center", fontsize=9.5, fontweight="bold", color=COL_PPGPP)

# RelA_Ab box
ax.add_patch(Rectangle((ppg_x - 1.15, ppg_y - 0.05), 0.95, 0.28,
                       facecolor=COL_PPGPP, edgecolor="black",
                       lw=0.8, alpha=0.85, zorder=5))
ax.text(ppg_x - 0.675, ppg_y + 0.09, "RelA_Ab",
        ha="center", va="center", fontsize=6.5, fontweight="bold",
        color="white", zorder=6)
ax.text(ppg_x - 0.675, ppg_y - 0.22, "ABUW_3302",
        ha="center", va="center", fontsize=5.5, color="#660000")

# Arrow RelA -> (p)ppGpp circle
arr_rela = FancyArrowPatch((ppg_x - 0.18, ppg_y + 0.09),
                           (ppg_x + 0.10, ppg_y + 0.09),
                           arrowstyle="-|>", mutation_scale=9,
                           color="black", lw=1.0, zorder=4)
ax.add_patch(arr_rela)

ax.add_patch(Circle((ppg_x + 0.35, ppg_y + 0.09), 0.18,
                    facecolor=COL_PPGPP, edgecolor="black",
                    lw=0.9, zorder=5))
ax.text(ppg_x + 0.35, ppg_y + 0.09, "ppGpp",
        ha="center", va="center", fontsize=5.5, fontweight="bold",
        color="white", zorder=6)

# (p)ppGpp -| ABUW_1132 -> abaIR (annotation)
ax.text(ppg_x + 0.95, ppg_y + 0.10,
        "represses\nABUW_1132",
        ha="left", va="center", fontsize=5.8,
        style="italic", color="#660000")
ax.text(ppg_x, ppg_y - 0.32,
        "stringent response on QS",
        ha="center", fontsize=6.2, style="italic", color="#660000")

# Arrow from (p)ppGpp pool -> QS (with T-bar = repression)
arr_ppg = FancyArrowPatch((ppg_x, ppg_y - 0.55),
                          (qs_x + qs_w/2, qs_y + qs_h + 0.02),
                          arrowstyle="-", color=COL_PPGPP,
                          lw=2.0, zorder=4)
ax.add_patch(arr_ppg)
# T-bar at bottom (repression)
tx = qs_x + qs_w/2
ax.plot([tx - 0.16, tx + 0.16], [qs_y + qs_h + 0.02]*2,
        color=COL_PPGPP, lw=2.2, zorder=5)

# -----------------------------------------------------------------------------
# RIGHT pool: 3',5'-cAMP (blue)
# -----------------------------------------------------------------------------
cmp_x, cmp_y = 8.45, 3.55
ax.add_patch(FancyBboxPatch((cmp_x-0.95, cmp_y-0.85), 1.9, 1.7,
                            boxstyle="round,pad=0.03,rounding_size=0.1",
                            facecolor="#e6f0fb", edgecolor=COL_CAMP,
                            lw=1.6, zorder=3))
ax.text(cmp_x, cmp_y + 0.65, "3',5'-cAMP pool",
        ha="center", fontsize=9.5, fontweight="bold", color=COL_CAMP)

# CavA (adenylate cyclase)
ax.add_patch(Rectangle((cmp_x - 0.85, cmp_y + 0.10), 0.75, 0.28,
                       facecolor=COL_CAMP, edgecolor="black",
                       lw=0.8, alpha=0.85, zorder=5))
ax.text(cmp_x - 0.475, cmp_y + 0.24, "CavA",
        ha="center", va="center", fontsize=6.5, fontweight="bold",
        color="white", zorder=6)
ax.text(cmp_x - 0.475, cmp_y - 0.05, "adenylate\ncyclase",
        ha="center", va="top", fontsize=5.5, color="#1a3a66")

# cAMP circle
ax.add_patch(Circle((cmp_x + 0.30, cmp_y + 0.24), 0.18,
                    facecolor=COL_CAMP, edgecolor="black",
                    lw=0.9, zorder=5))
ax.text(cmp_x + 0.30, cmp_y + 0.24, "cAMP",
        ha="center", va="center", fontsize=5.5, fontweight="bold",
        color="white", zorder=6)

# VfrAb receptor
ax.add_patch(Rectangle((cmp_x - 0.50, cmp_y - 0.55), 0.95, 0.26,
                       facecolor="#9ec3e3", edgecolor="black",
                       lw=0.7, zorder=5))
ax.text(cmp_x - 0.025, cmp_y - 0.42, "VfrAb (receptor)",
        ha="center", va="center", fontsize=6, color="black", zorder=6)
# Annotation
ax.text(cmp_x, cmp_y - 0.78,
        "+ activates DGCs\n- represses abaI",
        ha="center", fontsize=5.7, style="italic", color="#1a3a66")

# Arrow cAMP pool -> QS
arr_camp = FancyArrowPatch((cmp_x - 0.95, cmp_y),
                           (qs_x + qs_w + 0.02, qs_y + qs_h*0.5),
                           arrowstyle="-|>", mutation_scale=14,
                           color=COL_CAMP, lw=2.0, zorder=4)
ax.add_patch(arr_camp)

# Cross-talk arrow: cAMP -> c-di-GMP (top of arc, slight)
arr_cross1 = FancyArrowPatch((cmp_x - 0.7, cmp_y + 0.55),
                             (cdg_x + 0.7, cdg_y + 0.55),
                             arrowstyle="-|>", mutation_scale=8,
                             color="#888888", lw=0.8, linestyle=":",
                             zorder=2,
                             connectionstyle="arc3,rad=-0.45")
ax.add_patch(arr_cross1)
ax.text(5.0, 4.95, "cAMP activates DGCs",
        ha="center", fontsize=5.8, style="italic", color="#666")

# -----------------------------------------------------------------------------
# Output boxes (bottom)
# -----------------------------------------------------------------------------
outputs = [
    ("Biofilm", "csu, bap,\npgaABCD"),
    ("Motility", "twitching,\nsurface"),
    ("Virulence", "OmpA, OMVs,\nacinetobactin"),
    ("Efflux / resistance", "adeABC, adeFGH,\nadeIJK"),
]
out_y = 1.55
out_w, out_h = 1.85, 0.85
start = 0.55
for i, (title, body) in enumerate(outputs):
    bx = start + i * (out_w + 0.20)
    ax.add_patch(FancyBboxPatch((bx, out_y - out_h), out_w, out_h,
                                boxstyle="round,pad=0.03,rounding_size=0.08",
                                facecolor=COL_OUT, edgecolor="black",
                                lw=1.0, zorder=4))
    ax.text(bx + out_w/2, out_y - 0.22, title, ha="center", va="center",
            fontsize=8.5, fontweight="bold", color="#222", zorder=6)
    ax.text(bx + out_w/2, out_y - 0.55, body, ha="center", va="center",
            fontsize=6.8, fontstyle="italic", color="#333", zorder=6)

# Fan-out arrows from QS to each output
for i in range(len(outputs)):
    bx = start + i * (out_w + 0.20) + out_w/2
    arr = FancyArrowPatch((qs_x + qs_w/2, qs_y - 0.02),
                          (bx, out_y + 0.02),
                          arrowstyle="-|>", mutation_scale=11,
                          color="#444444", lw=1.1, zorder=3,
                          connectionstyle="arc3,rad=0.0")
    ax.add_patch(arr)

# -----------------------------------------------------------------------------
# Input sensing box (bottom-right)
# -----------------------------------------------------------------------------
ib_x, ib_y, ib_w, ib_h = 6.5, 0.18, 3.4, 0.45
ax.add_patch(FancyBboxPatch((ib_x, ib_y), ib_w, ib_h,
                            boxstyle="round,pad=0.02,rounding_size=0.05",
                            facecolor="#fffbe6", edgecolor="#b8860b",
                            lw=1.0, zorder=4))
ax.text(ib_x + ib_w/2, ib_y + ib_h - 0.10,
        "Inputs sensed",
        ha="center", va="top", fontsize=7.5, fontweight="bold",
        color="#7a5a00", zorder=6)
ax.text(ib_x + ib_w/2, ib_y + 0.12,
        "cell density - nutrient state - host cues - carbon source",
        ha="center", va="bottom", fontsize=6.5, style="italic",
        color="#5a4400", zorder=6)

# -----------------------------------------------------------------------------
# Legend (top-left corner)
# -----------------------------------------------------------------------------
leg_handles = [
    mpatches.Patch(color=COL_CDG,   label="c-di-GMP"),
    mpatches.Patch(color=COL_PPGPP, label="(p)ppGpp"),
    mpatches.Patch(color=COL_CAMP,  label="3',5'-cAMP"),
    mpatches.Patch(color=COL_QS,    label="QS decision (AbaR-AHL)"),
    mpatches.Patch(color=COL_OUT,   label="phenotypic outputs"),
    Line2D([0], [0], color="black", lw=1.4, marker=">", markersize=6,
           label="activation"),
    Line2D([0], [0], color=COL_PPGPP, lw=2.0, marker="_",
           markersize=10, label="repression (T-bar)"),
    Line2D([0], [0], color="#666666", lw=0.9, linestyle=":",
           label="cross-talk"),
]
leg = ax.legend(handles=leg_handles, loc="lower left",
                bbox_to_anchor=(0.005, 0.005),
                fontsize=6.0, frameon=True, framealpha=0.95,
                title="Legend", title_fontsize=6.8, ncol=4,
                handlelength=1.4, columnspacing=1.0,
                handletextpad=0.5)
leg.get_frame().set_edgecolor("#888888")

# -----------------------------------------------------------------------------
# Save outputs
# -----------------------------------------------------------------------------
png_path = os.path.join(OUT_DIR, "figure3b_second_messengers.png")
svg_path = os.path.join(OUT_DIR, "figure3b_second_messengers.svg")
plt.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(svg_path, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Wrote: {png_path}")
print(f"Wrote: {svg_path}")
