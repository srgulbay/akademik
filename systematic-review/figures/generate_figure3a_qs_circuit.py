"""
Figure 3A: AbaI/AbaR/AbaM quorum-sensing circuit in Acinetobacter baumannii.

Renders a publication-quality schematic showing:
- A bacterial cell (top half) with intracellular QS machinery
- Extracellular space (bottom half) with AHL diffusion and QQ enzymes
- Numbered cycle steps (1 -> 6)

Outputs:
- figure3a_qs_circuit.png (300 DPI, 10x7 in)
- figure3a_qs_circuit.svg
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Ellipse
from matplotlib.lines import Line2D

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------------
# Color palette (consistent with figure legend)
# -----------------------------------------------------------------------------
COL_AHL    = "#1f77b4"   # blue
COL_ABAI   = "#2ca02c"   # green (synthase)
COL_ABAR   = "#ff7f0e"   # orange (receptor)
COL_ABAM   = "#d62728"   # red (brake)
COL_QQ     = "#7b3294"   # purple (quorum-quenching)
COL_DNA    = "#000000"   # black (genome)
COL_TARGET = "#dddddd"   # light gray (target gene boxes)
COL_LYSR   = "#8c564b"   # brown for ABUW_1132 (LysR)
COL_PPGPP  = "#b15928"   # ppGpp accent

CELL_TOP_COLOR    = "#fff8e7"   # cell interior (pale cream)
CELL_BOTTOM_COLOR = "#eaf3fb"   # extracellular (pale blue)
MEMBRANE_COLOR    = "#4d4d4d"

# -----------------------------------------------------------------------------
# Figure / axes
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.axis("off")

# Title
ax.text(5.0, 6.75, "Figure 3A.  AbaI / AbaR / AbaM quorum-sensing circuit in $\\it{A.\\ baumannii}$",
        ha="center", va="center", fontsize=12, fontweight="bold")

# -----------------------------------------------------------------------------
# Cell envelope (top half = intracellular, bottom half = extracellular)
# -----------------------------------------------------------------------------
cell_top    = FancyBboxPatch((0.4, 3.2), 9.2, 3.0,
                             boxstyle="round,pad=0.02,rounding_size=0.18",
                             linewidth=1.8, edgecolor=MEMBRANE_COLOR,
                             facecolor=CELL_TOP_COLOR, zorder=1)
extracell   = FancyBboxPatch((0.4, 0.5), 9.2, 2.55,
                             boxstyle="round,pad=0.02,rounding_size=0.18",
                             linewidth=1.0, edgecolor="#9ec3e3",
                             facecolor=CELL_BOTTOM_COLOR, zorder=1)
ax.add_patch(extracell)
ax.add_patch(cell_top)

# Membrane line (top of extracellular = bottom of cell)
ax.plot([0.4, 9.6], [3.18, 3.18], color=MEMBRANE_COLOR, lw=2.5, zorder=2)
# Decorative phospholipid heads
for x in [i*0.25 + 0.55 for i in range(int((9.05)/0.25))]:
    ax.add_patch(Circle((x, 3.18), 0.045, facecolor="#9ecae1",
                        edgecolor=MEMBRANE_COLOR, lw=0.4, zorder=3))

# Labels for compartments
ax.text(0.55, 6.05, "Bacterial cell (cytoplasm)", fontsize=9, style="italic",
        color="#555555", ha="left")
ax.text(0.55, 2.85, "Extracellular space", fontsize=9, style="italic",
        color="#3a6a91", ha="left")

# -----------------------------------------------------------------------------
# AbaI (synthase) - green circle, left side
# -----------------------------------------------------------------------------
abaI_xy = (1.7, 5.3)
ax.add_patch(Circle(abaI_xy, 0.35, facecolor=COL_ABAI, edgecolor="black",
                    lw=1.2, zorder=5))
ax.text(abaI_xy[0], abaI_xy[1], "AbaI", ha="center", va="center",
        fontsize=9, fontweight="bold", color="white", zorder=6)
ax.text(abaI_xy[0], abaI_xy[1]-0.55, "synthase", ha="center",
        fontsize=7, style="italic", color="#2a5d2a")

# Substrates feeding AbaI
ax.text(0.55, 6.0, "SAM\n+\n3-OH-C12-ACP", ha="left", va="top",
        fontsize=6.5, color="#444")
arr_sub = FancyArrowPatch((1.05, 5.55), (1.4, 5.35),
                          arrowstyle="-|>", mutation_scale=10,
                          color="black", lw=1.0, zorder=4)
ax.add_patch(arr_sub)

# -----------------------------------------------------------------------------
# AbaR (receptor) - orange rectangle with two domains, center
# -----------------------------------------------------------------------------
abaR_x, abaR_y, abaR_w, abaR_h = 4.0, 4.7, 1.8, 0.7
ax.add_patch(FancyBboxPatch((abaR_x, abaR_y), abaR_w, abaR_h,
                            boxstyle="round,pad=0.02,rounding_size=0.05",
                            facecolor=COL_ABAR, edgecolor="black",
                            lw=1.2, zorder=5))
# Domain split (vertical line in middle of receptor)
ax.plot([abaR_x + abaR_w/2]*2, [abaR_y+0.05, abaR_y+abaR_h-0.05],
        color="black", lw=0.8, zorder=6)
ax.text(abaR_x + abaR_w*0.25, abaR_y + abaR_h/2, "AHL-bind\n(N-term)",
        ha="center", va="center", fontsize=6.5, color="black", zorder=6)
ax.text(abaR_x + abaR_w*0.75, abaR_y + abaR_h/2, "HTH-DNA\n(C-term)",
        ha="center", va="center", fontsize=6.5, color="black", zorder=6)
ax.text(abaR_x + abaR_w/2, abaR_y - 0.22, "AbaR (receptor / LuxR-type)",
        ha="center", va="top", fontsize=8, fontweight="bold", color="#a35400")

# -----------------------------------------------------------------------------
# AbaM (brake) - red cap on top of AbaR
# -----------------------------------------------------------------------------
abaM_x = abaR_x + abaR_w/2
abaM_y = abaR_y + abaR_h + 0.18
ax.add_patch(Ellipse((abaM_x, abaM_y), width=0.85, height=0.32,
                     facecolor=COL_ABAM, edgecolor="black",
                     lw=1.0, zorder=6))
ax.text(abaM_x, abaM_y, "AbaM (brake)", ha="center", va="center",
        fontsize=7, fontweight="bold", color="white", zorder=7)
# T-bar inhibition from AbaM to AbaR
inh_line = Line2D([abaM_x, abaM_x], [abaM_y-0.18, abaR_y + abaR_h + 0.02],
                  color=COL_ABAM, lw=1.6, zorder=6)
ax.add_line(inh_line)
ax.plot([abaM_x-0.13, abaM_x+0.13], [abaR_y + abaR_h + 0.02]*2,
        color=COL_ABAM, lw=2.0, zorder=6)

# -----------------------------------------------------------------------------
# ABUW_1132 (LysR regulator) - upper-left -> activates abaI transcription
# -----------------------------------------------------------------------------
lysr_xy = (2.7, 6.05)
ax.add_patch(FancyBboxPatch((lysr_xy[0]-0.45, lysr_xy[1]-0.18), 0.9, 0.36,
                            boxstyle="round,pad=0.02,rounding_size=0.05",
                            facecolor=COL_LYSR, edgecolor="black",
                            lw=1.0, zorder=5))
ax.text(lysr_xy[0], lysr_xy[1], "ABUW_1132", ha="center", va="center",
        fontsize=7, fontweight="bold", color="white", zorder=6)
ax.text(lysr_xy[0], lysr_xy[1]-0.32, "LysR-type", ha="center", va="top",
        fontsize=6, style="italic", color="#4d2e23")

# -----------------------------------------------------------------------------
# RelA -> (p)ppGpp side icon
# -----------------------------------------------------------------------------
rela_x, rela_y = 8.55, 5.85
ax.add_patch(FancyBboxPatch((rela_x-0.45, rela_y-0.18), 0.9, 0.36,
                            boxstyle="round,pad=0.02,rounding_size=0.05",
                            facecolor="#bbbbbb", edgecolor="black",
                            lw=1.0, zorder=5))
ax.text(rela_x, rela_y, "RelA", ha="center", va="center",
        fontsize=8, fontweight="bold", color="black", zorder=6)
# arrow to ppGpp
arr_rela = FancyArrowPatch((rela_x, rela_y-0.22), (rela_x, rela_y-0.55),
                           arrowstyle="-|>", mutation_scale=10,
                           color="black", lw=1.2, zorder=4)
ax.add_patch(arr_rela)
ax.add_patch(Circle((rela_x, rela_y-0.78), 0.18, facecolor=COL_PPGPP,
                    edgecolor="black", lw=1.0, zorder=5))
ax.text(rela_x, rela_y-0.78, "(p)ppGpp", ha="center", va="center",
        fontsize=6.5, fontweight="bold", color="white", zorder=6)
ax.text(rela_x, rela_y-1.05, "nutritional /\nstringent sensing",
        ha="center", va="top", fontsize=6, style="italic", color="#555")

# -----------------------------------------------------------------------------
# Genome line at bottom of cell with lux-box, abaI, target gene regulons
# -----------------------------------------------------------------------------
genome_y = 3.55
ax.plot([0.7, 9.3], [genome_y, genome_y], color=COL_DNA, lw=2.0, zorder=3)
# helical hatch marks (DNA)
for x in [0.7 + 0.18*i for i in range(int((9.3-0.7)/0.18))]:
    ax.plot([x, x+0.09], [genome_y-0.05, genome_y+0.05],
            color=COL_DNA, lw=0.5, zorder=3)

# lux-box (purple-ish small box)
ax.add_patch(Rectangle((1.05, genome_y-0.12), 0.55, 0.24,
                       facecolor="#ffe599", edgecolor="black", lw=0.8, zorder=4))
ax.text(1.32, genome_y, "lux-box", ha="center", va="center",
        fontsize=6.5, fontweight="bold", color="black", zorder=5)

# abaI gene
ax.add_patch(Rectangle((1.65, genome_y-0.14), 0.55, 0.28,
                       facecolor=COL_ABAI, edgecolor="black",
                       lw=0.8, alpha=0.85, zorder=4))
ax.text(1.92, genome_y, "abaI", ha="center", va="center",
        fontsize=7, fontstyle="italic", fontweight="bold",
        color="white", zorder=5)

# Target gene regulon boxes
targets = ["csu", "bap", "pgaABCD", "adeFGH", "ompA"]
start_x = 3.3
gap = 1.15
for i, g in enumerate(targets):
    bx = start_x + i*gap
    ax.add_patch(Rectangle((bx, genome_y-0.16), 0.9, 0.32,
                           facecolor=COL_TARGET, edgecolor="black",
                           lw=0.7, zorder=4))
    ax.text(bx + 0.45, genome_y, g, ha="center", va="center",
            fontsize=7, fontstyle="italic", fontweight="bold",
            color="black", zorder=5)

ax.text(5.0, genome_y - 0.45, "target gene regulons (biofilm, motility, virulence, efflux)",
        ha="center", fontsize=7, style="italic", color="#444")

# Arrow: AbaR (with AHL) -> transcription at lux-box / abaI
arr_tx = FancyArrowPatch((abaR_x + 0.6, abaR_y), (1.4, genome_y + 0.18),
                         arrowstyle="-|>", mutation_scale=12,
                         color="black", lw=1.3, zorder=4,
                         connectionstyle="arc3,rad=-0.25")
ax.add_patch(arr_tx)
ax.text(2.55, 4.15, "binds lux-box", fontsize=6.5,
        style="italic", color="#333")

# Arrow: AbaR -> target regulons (downstream activation)
arr_tx2 = FancyArrowPatch((abaR_x + abaR_w - 0.2, abaR_y),
                          (6.5, genome_y + 0.18),
                          arrowstyle="-|>", mutation_scale=12,
                          color="black", lw=1.3, zorder=4,
                          connectionstyle="arc3,rad=0.2")
ax.add_patch(arr_tx2)

# Arrow: ABUW_1132 -> abaI (activation of transcription)
arr_lysr = FancyArrowPatch((lysr_xy[0], lysr_xy[1]-0.2),
                           (1.92, genome_y + 0.16),
                           arrowstyle="-|>", mutation_scale=11,
                           color="black", lw=1.2, zorder=4,
                           connectionstyle="arc3,rad=-0.15")
ax.add_patch(arr_lysr)
ax.text(2.55, 5.45, "activates", fontsize=6.5, style="italic", color="#333")

# AbaI -> produces AHL (arrow to extracellular AHL pool)
arr_synth = FancyArrowPatch((abaI_xy[0]+0.05, abaI_xy[1]-0.35),
                            (1.85, 2.55),
                            arrowstyle="-|>", mutation_scale=12,
                            color=COL_AHL, lw=1.4, zorder=4)
ax.add_patch(arr_synth)

# -----------------------------------------------------------------------------
# Extracellular: AHL molecules (lactone-like glyphs) + diffusion arrows
# -----------------------------------------------------------------------------
def draw_ahl(ax, x, y, scale=1.0):
    """Cartoon 3-OH-C12-HSL: lactone ring + hydroxyl side chain."""
    r = 0.13 * scale
    ax.add_patch(Circle((x, y), r, facecolor=COL_AHL, edgecolor="black",
                        lw=0.8, zorder=5))
    # side chain (zig-zag)
    pts_x = [x + r + i*0.10*scale for i in range(6)]
    pts_y = [y + (0.05 if i % 2 == 0 else -0.05)*scale for i in range(6)]
    ax.plot(pts_x, pts_y, color=COL_AHL, lw=1.3, zorder=5)
    # OH group
    ax.text(pts_x[-1] + 0.05*scale, pts_y[-1], "OH",
            fontsize=5, color=COL_AHL, va="center", zorder=5)

ahl_positions = [(1.9, 2.4), (3.4, 2.2), (4.7, 2.55),
                 (6.1, 2.15), (7.4, 2.45)]
for (x, y) in ahl_positions:
    draw_ahl(ax, x, y)

ax.text(4.7, 1.85, "3-OH-C12-HSL (AHL)", ha="center",
        fontsize=8, fontweight="bold", color=COL_AHL)

# Diffusion arrows across membrane (dashed blue, both directions)
for x in [2.4, 4.4, 6.8]:
    arr_d = FancyArrowPatch((x, 2.65), (x, 3.65),
                            arrowstyle="<|-|>", mutation_scale=10,
                            color=COL_AHL, lw=1.0,
                            linestyle="--", zorder=4)
    ax.add_patch(arr_d)

# AHL re-entry -> AbaR binding
arr_bind = FancyArrowPatch((4.4, 3.7), (abaR_x + 0.4, abaR_y + 0.1),
                           arrowstyle="-|>", mutation_scale=11,
                           color=COL_AHL, lw=1.2, linestyle="--",
                           zorder=4,
                           connectionstyle="arc3,rad=0.2")
ax.add_patch(arr_bind)
ax.text(4.55, 4.25, "AHL binds AbaR", fontsize=6.5,
        style="italic", color=COL_AHL)

# -----------------------------------------------------------------------------
# Quorum-quenching enzymes (purple) cleaving AHL
# -----------------------------------------------------------------------------
qq_y = 1.15
qq_enzymes = [("MomL", 1.6), ("AaL", 3.1), ("AidA", 4.6), ("PvdQ", 7.5)]
for name, x in qq_enzymes:
    ax.add_patch(FancyBboxPatch((x-0.32, qq_y-0.16), 0.64, 0.32,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                facecolor=COL_QQ, edgecolor="black",
                                lw=0.9, zorder=5))
    ax.text(x, qq_y, name, ha="center", va="center",
            fontsize=7, fontweight="bold", color="white", zorder=6)

ax.text(3.55, qq_y + 0.36,
        "lactonases (MomL, AaL, AidA) + acylase (PvdQ)  -- cleave AHL",
        ha="center", fontsize=7, style="italic", color="#4a235a")

# Scissor-style arrows from QQ -> nearest AHL
for ((name, x), (ax_x, ax_y)) in zip(qq_enzymes,
                                     [(1.9, 2.4), (3.4, 2.2),
                                      (4.7, 2.55), (7.4, 2.45)]):
    arr_q = FancyArrowPatch((x, qq_y + 0.18), (ax_x, ax_y - 0.18),
                            arrowstyle="-|>", mutation_scale=9,
                            color=COL_QQ, lw=1.0, zorder=4)
    ax.add_patch(arr_q)

# -----------------------------------------------------------------------------
# Numbered cycle steps (1 -> 6)
# -----------------------------------------------------------------------------
steps = [
    ("1", "Synthesis", "AbaI makes AHL\nfrom SAM + acyl-ACP"),
    ("2", "Diffusion", "AHL crosses membrane"),
    ("3", "Accumulation", "AHL builds up\nwith cell density"),
    ("4", "Binding", "AHL binds AbaR;\nAbaM brakes it"),
    ("5", "Transcription", "AbaR-AHL binds\nlux-box -> abaI +\ntarget regulons"),
    ("6", "Output", "biofilm, motility,\nvirulence, efflux"),
]
legend_x0 = 0.35
legend_y0 = 0.45
ax.text(0.55, legend_y0 - 0.05, "Quorum-sensing cycle:",
        ha="left", va="top", fontsize=8.5, fontweight="bold", color="#222")
for i, (num, title, desc) in enumerate(steps):
    cx = legend_x0 + 0.25 + i*1.58
    cy = legend_y0 - 0.32
    ax.add_patch(Circle((cx, cy), 0.13, facecolor="#333333",
                        edgecolor="black", lw=0.8, zorder=5))
    ax.text(cx, cy, num, ha="center", va="center",
            fontsize=7.5, fontweight="bold", color="white", zorder=6)
    ax.text(cx + 0.20, cy + 0.04, title, ha="left", va="center",
            fontsize=7, fontweight="bold", color="#222")
    ax.text(cx + 0.20, cy - 0.18, desc, ha="left", va="top",
            fontsize=5.6, color="#444")

# -----------------------------------------------------------------------------
# Arrow-type legend (top-right corner)
# -----------------------------------------------------------------------------
leg_handles = [
    mpatches.Patch(color=COL_ABAI, label="AbaI (synthase)"),
    mpatches.Patch(color=COL_ABAR, label="AbaR (receptor)"),
    mpatches.Patch(color=COL_ABAM, label="AbaM (brake)"),
    mpatches.Patch(color=COL_AHL,  label="AHL signal"),
    mpatches.Patch(color=COL_QQ,   label="QQ enzymes"),
    Line2D([0], [0], color="black", lw=1.4,
           marker=">", markersize=6, label="activation"),
    Line2D([0], [0], color=COL_ABAM, lw=1.6,
           marker="_", markersize=10, label="inhibition (T-bar)"),
    Line2D([0], [0], color=COL_AHL, lw=1.2, linestyle="--",
           label="diffusion"),
]
leg = ax.legend(handles=leg_handles, loc="upper right",
                bbox_to_anchor=(0.995, 0.97),
                fontsize=6.5, frameon=True, framealpha=0.9,
                title="Legend", title_fontsize=7, ncol=1)
leg.get_frame().set_edgecolor("#888888")

# -----------------------------------------------------------------------------
# Save outputs
# -----------------------------------------------------------------------------
png_path = os.path.join(OUT_DIR, "figure3a_qs_circuit.png")
svg_path = os.path.join(OUT_DIR, "figure3a_qs_circuit.svg")
plt.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(svg_path, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Wrote: {png_path}")
print(f"Wrote: {svg_path}")
