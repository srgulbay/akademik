"""
Figure 3A: AbaI/AbaR/AbaM quorum-sensing circuit in Acinetobacter baumannii.

Journal-grade schematic, icon style (clean geometry, not cartoonish):
- Bacterial cell as a smooth horizontal capsule shape
- AbaI = green pentagon (synthase)
- AbaR = orange rectangle with two domains (N: AHL-bind / C: HTH-DNA)
- AbaM = small red triangle on top of AbaR (brake)
- ABUW_1132 = small purple ellipse on the side
- Lactonases / acylase = purple pacman/scissor-shaped icons
- AHL drawn with a stylised lactone ring + C12 tail using Path patches
- Numbered 1-6 cycle inset at bottom-right
- Color legend at bottom

Outputs:
- figure3a_qs_circuit.png (600 DPI, 8x6 in)
- figure3a_qs_circuit.svg
"""

import os
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import (
    FancyBboxPatch, FancyArrowPatch, Rectangle, Circle,
    RegularPolygon, Wedge, PathPatch, Polygon,
)
from matplotlib.path import Path as MPath
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE

apply_style()

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------------------
# Colours from the unified palette
# -----------------------------------------------------------------------------
COL_AHL    = PALETTE["blue"]
COL_ABAI   = "#3a8a4d"          # green pentagon
COL_ABAR   = PALETTE["amber"]
COL_ABAM   = PALETTE["red"]
COL_QQ     = PALETTE["purple"]
COL_LYSR   = "#5a3a9c"          # darker purple for ABUW_1132
COL_DNA    = "#222222"
COL_TARGET = "#e6e6e6"
COL_PPGPP  = "#a04020"

CELL_FACE = "#fdf6e7"
EXTRA_FACE = "#eef4fb"
MEMBRANE = "#444444"

# -----------------------------------------------------------------------------
# Figure
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), dpi=600)
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 7.6)
ax.set_aspect("equal")
ax.axis("off")

ax.text(5.0, 7.35,
        "Acinetobacter baumannii cell — schematic",
        ha="center", va="center", fontsize=10, fontweight="bold")
ax.text(5.0, 7.05,
        "AbaI / AbaR / AbaM quorum-sensing circuit",
        ha="center", va="center", fontsize=9, fontstyle="italic", color="#444")

# -----------------------------------------------------------------------------
# Bacterial cell as capsule (horizontal rounded rectangle)
# -----------------------------------------------------------------------------
cell = FancyBboxPatch(
    (0.5, 3.30), 9.0, 3.40,
    boxstyle="round,pad=0.02,rounding_size=0.45",
    linewidth=1.4, edgecolor=MEMBRANE,
    facecolor=CELL_FACE, zorder=1,
)
ax.add_patch(cell)

extracell = FancyBboxPatch(
    (0.5, 0.45), 9.0, 2.55,
    boxstyle="round,pad=0.02,rounding_size=0.18",
    linewidth=0.6, edgecolor="#a9c2da",
    facecolor=EXTRA_FACE, zorder=1,
)
ax.add_patch(extracell)

# Membrane line + phospholipid heads
ax.plot([0.5, 9.5], [3.28, 3.28], color=MEMBRANE, lw=1.6, zorder=2)
for x in np.arange(0.7, 9.4, 0.22):
    ax.add_patch(Circle((x, 3.28), 0.035, facecolor="#9ec3e3",
                        edgecolor=MEMBRANE, lw=0.3, zorder=3))

ax.text(0.65, 6.50, "Cytoplasm", fontsize=8, style="italic",
        color="#555", ha="left", zorder=4)
ax.text(0.65, 2.85, "Extracellular space", fontsize=8, style="italic",
        color="#3a6a91", ha="left", zorder=4)

# -----------------------------------------------------------------------------
# AbaI - green pentagon (synthases conventionally pentagons)
# -----------------------------------------------------------------------------
abaI_xy = (1.55, 5.55)
penta = RegularPolygon(abaI_xy, numVertices=5, radius=0.42,
                       orientation=0, facecolor=COL_ABAI,
                       edgecolor="black", lw=0.9, zorder=5)
ax.add_patch(penta)
ax.text(abaI_xy[0], abaI_xy[1], "AbaI", ha="center", va="center",
        fontsize=8, fontweight="bold", color="white", zorder=6)
ax.text(abaI_xy[0], abaI_xy[1] - 0.62, "synthase", ha="center",
        fontsize=6.5, style="italic", color="#234d2c")

# Substrate annotation
ax.text(0.65, 6.25, "SAM + 3-OH-C12-ACP", ha="left", va="top",
        fontsize=6.5, color="#444", zorder=4)
ax.add_patch(FancyArrowPatch(
    (1.00, 6.05), (1.35, 5.75),
    arrowstyle="-|>", mutation_scale=7, color="black", lw=0.7, zorder=4,
))

# -----------------------------------------------------------------------------
# AbaR - orange rectangle with two visually separated domains
# -----------------------------------------------------------------------------
abaR_x, abaR_y, abaR_w, abaR_h = 3.85, 4.95, 2.0, 0.75
# N-terminal domain (AHL-bind) - left half, slightly darker
ax.add_patch(Rectangle((abaR_x, abaR_y), abaR_w/2, abaR_h,
                       facecolor=COL_ABAR, edgecolor="black",
                       lw=0.9, zorder=5))
# C-terminal domain (HTH-DNA) - right half, lighter
ax.add_patch(Rectangle((abaR_x + abaR_w/2, abaR_y), abaR_w/2, abaR_h,
                       facecolor="#f1b966", edgecolor="black",
                       lw=0.9, zorder=5))
# Vertical separator
ax.plot([abaR_x + abaR_w/2]*2, [abaR_y + 0.05, abaR_y + abaR_h - 0.05],
        color="black", lw=0.6, zorder=6)
ax.text(abaR_x + abaR_w*0.25, abaR_y + abaR_h/2, "AHL-bind\n(N)",
        ha="center", va="center", fontsize=6.5, color="black", zorder=6)
ax.text(abaR_x + abaR_w*0.75, abaR_y + abaR_h/2, "HTH-DNA\n(C)",
        ha="center", va="center", fontsize=6.5, color="black", zorder=6)
ax.text(abaR_x + abaR_w/2, abaR_y - 0.20, "AbaR (LuxR-type receptor)",
        ha="center", va="top", fontsize=7.5, fontweight="bold",
        color="#a35400")

# -----------------------------------------------------------------------------
# AbaM - small red triangle on top of AbaR (the brake)
# -----------------------------------------------------------------------------
abaM_cx = abaR_x + abaR_w / 2
abaM_cy = abaR_y + abaR_h + 0.32
tri = Polygon(
    [(abaM_cx - 0.30, abaM_cy + 0.20),
     (abaM_cx + 0.30, abaM_cy + 0.20),
     (abaM_cx, abaM_cy - 0.22)],
    closed=True, facecolor=COL_ABAM, edgecolor="black", lw=0.8, zorder=6,
)
ax.add_patch(tri)
ax.text(abaM_cx, abaM_cy + 0.04, "AbaM", ha="center", va="center",
        fontsize=6.8, fontweight="bold", color="white", zorder=7)
ax.text(abaM_cx + 0.45, abaM_cy, "(brake)", ha="left", va="center",
        fontsize=6.5, style="italic", color=COL_ABAM)

# T-bar inhibition from AbaM down to AbaR top edge
inh = FancyArrowPatch(
    (abaM_cx, abaM_cy - 0.22), (abaM_cx, abaR_y + abaR_h + 0.02),
    arrowstyle="]-", mutation_scale=7, color=COL_ABAM, lw=1.4, zorder=6,
)
ax.add_patch(inh)

# -----------------------------------------------------------------------------
# ABUW_1132 - small purple ellipse to the side
# -----------------------------------------------------------------------------
lysr_x, lysr_y = 2.75, 6.50
ax.add_patch(mpatches.Ellipse((lysr_x, lysr_y), width=1.10, height=0.36,
                              facecolor=COL_LYSR, edgecolor="black",
                              lw=0.9, zorder=5))
ax.text(lysr_x, lysr_y, "ABUW_1132", ha="center", va="center",
        fontsize=6.8, fontweight="bold", color="white", zorder=6)
ax.text(lysr_x + 0.72, lysr_y, "LysR-type", ha="left", va="center",
        fontsize=6, style="italic", color="#2e1a55", zorder=6)

# Arrow ABUW_1132 -> abaI (activation)
arr_lysr = FancyArrowPatch(
    (lysr_x - 0.35, lysr_y - 0.18), (abaI_xy[0] + 0.05, abaI_xy[1] + 0.42),
    arrowstyle="-|>", mutation_scale=8, color="black", lw=0.9, zorder=4,
    connectionstyle="arc3,rad=-0.35",
)
ax.add_patch(arr_lysr)
ax.text(1.85, 6.20, "activates", fontsize=6, style="italic", color="#333")

# -----------------------------------------------------------------------------
# RelA -> (p)ppGpp (stringent-response side icon)
# -----------------------------------------------------------------------------
rela_x, rela_y = 8.30, 6.20
ax.add_patch(Rectangle((rela_x - 0.45, rela_y - 0.18), 0.90, 0.36,
                       facecolor="#888888", edgecolor="black",
                       lw=0.8, zorder=5))
ax.text(rela_x, rela_y, "RelA", ha="center", va="center",
        fontsize=7.5, fontweight="bold", color="white", zorder=6)
arr_rela = FancyArrowPatch(
    (rela_x, rela_y - 0.22), (rela_x, rela_y - 0.55),
    arrowstyle="-|>", mutation_scale=8, color="black", lw=0.9, zorder=4,
)
ax.add_patch(arr_rela)
ax.add_patch(Circle((rela_x, rela_y - 0.78), 0.16,
                    facecolor=COL_PPGPP, edgecolor="black", lw=0.8, zorder=5))
ax.text(rela_x, rela_y - 0.78, "(p)ppGpp", ha="center", va="center",
        fontsize=5.5, fontweight="bold", color="white", zorder=6)
ax.text(rela_x, rela_y - 1.08, "nutritional /\nstringent sensing",
        ha="center", va="top", fontsize=5.8, style="italic", color="#555")

# -----------------------------------------------------------------------------
# Genome line (dashed black) with bold italic gene labels
# -----------------------------------------------------------------------------
genome_y = 3.65
ax.plot([0.7, 9.3], [genome_y, genome_y], color=COL_DNA,
        lw=1.4, ls=(0, (3, 1.5)), zorder=3)

# Gene boxes on genome
genes = [
    ("lux-box", 1.05, 0.55, "#ffe599", "black"),
    ("abaI",    1.65, 0.50, COL_ABAI,   "white"),
]
for name, gx, gw, fc, tc in genes:
    italic = name != "lux-box"
    ax.add_patch(Rectangle((gx, genome_y - 0.13), gw, 0.26,
                           facecolor=fc, edgecolor="black", lw=0.7, zorder=4))
    ax.text(gx + gw/2, genome_y, name,
            ha="center", va="center",
            fontsize=6.5, fontweight="bold",
            fontstyle="italic" if italic else "normal",
            color=tc, zorder=5)

# Target gene regulons
targets = ["csu", "bap", "pgaABCD", "adeFGH", "ompA"]
start_x = 3.35
gap = 1.15
for i, g in enumerate(targets):
    bx = start_x + i * gap
    ax.add_patch(Rectangle((bx, genome_y - 0.15), 0.85, 0.30,
                           facecolor=COL_TARGET, edgecolor="black",
                           lw=0.6, zorder=4))
    ax.text(bx + 0.425, genome_y, g,
            ha="center", va="center",
            fontsize=6.5, fontstyle="italic", fontweight="bold",
            color="black", zorder=5)

ax.text(6.50, 4.45,
        "downstream: biofilm, motility,\nvirulence, efflux",
        ha="center", fontsize=6, style="italic", color="#444", zorder=4)

# Arrow: AbaR -> lux-box/abaI (binds lux-box)
arr_tx = FancyArrowPatch(
    (abaR_x + 0.6, abaR_y), (1.40, genome_y + 0.18),
    arrowstyle="-|>", mutation_scale=8,
    color="black", lw=0.9, zorder=4,
    connectionstyle="arc3,rad=-0.25",
)
ax.add_patch(arr_tx)
ax.text(2.55, 4.20, "binds lux-box", fontsize=6, style="italic", color="#333")

# Arrow: AbaR -> downstream target regulons
arr_tx2 = FancyArrowPatch(
    (abaR_x + abaR_w - 0.15, abaR_y), (6.30, genome_y + 0.18),
    arrowstyle="-|>", mutation_scale=8,
    color="black", lw=0.9, zorder=4,
    connectionstyle="arc3,rad=0.20",
)
ax.add_patch(arr_tx2)

# Arrow: AbaI -> AHL pool (synthesis)
arr_synth = FancyArrowPatch(
    (abaI_xy[0], abaI_xy[1] - 0.45), (1.75, 2.55),
    arrowstyle="-|>", mutation_scale=8, color=COL_AHL,
    lw=1.0, zorder=4,
)
ax.add_patch(arr_synth)

# -----------------------------------------------------------------------------
# AHL molecule: stylised lactone ring + C12 chain via Path
# -----------------------------------------------------------------------------
def draw_ahl(ax, x, y, scale=1.0, label=False):
    """Draw a stylised 3-OH-C12-HSL: 5-membered lactone ring + zigzag tail."""
    r = 0.16 * scale
    # Lactone ring (pentagon-shaped filled patch with O label)
    ring = RegularPolygon((x, y), numVertices=5, radius=r,
                          orientation=np.pi/2,
                          facecolor=COL_AHL, edgecolor="black",
                          lw=0.6, zorder=5)
    ax.add_patch(ring)
    ax.text(x, y, "O", ha="center", va="center",
            fontsize=5, color="white", fontweight="bold", zorder=6)
    # C12 zigzag tail
    n_zig = 6
    step = 0.085 * scale
    amp = 0.045 * scale
    verts = [(x + r + 0.02, y)]
    for i in range(1, n_zig + 1):
        verts.append((x + r + 0.02 + i * step, y + (amp if i % 2 else -amp)))
    codes = [MPath.MOVETO] + [MPath.LINETO] * n_zig
    p = MPath(verts, codes)
    ax.add_patch(PathPatch(p, edgecolor=COL_AHL, lw=1.0, fill=False, zorder=5))
    # OH at tail end
    ax.text(verts[-1][0] + 0.04, verts[-1][1], "OH",
            fontsize=4.5, color=COL_AHL, va="center", zorder=5)
    if label:
        ax.text(x + 0.3, y - 0.35, "3-OH-C12-HSL",
                fontsize=6.5, fontweight="bold", color=COL_AHL,
                ha="center", va="top")


# AHLs in extracellular space
ahl_positions = [(1.85, 2.40), (3.30, 2.20), (4.70, 2.55),
                 (6.10, 2.25), (7.45, 2.40)]
for i, (x, y) in enumerate(ahl_positions):
    draw_ahl(ax, x, y, scale=1.0)

ax.text(4.70, 1.78, "3-OH-C12-HSL (AHL)", ha="center",
        fontsize=7.5, fontweight="bold", color=COL_AHL)

# Diffusion arrows across membrane (dashed blue, bidirectional, no arrowhead)
for x in [2.35, 4.35, 6.75]:
    a = FancyArrowPatch(
        (x, 2.75), (x, 3.55),
        arrowstyle="-", mutation_scale=6, color=COL_AHL,
        lw=0.8, ls=(0, (2, 1.5)), zorder=4,
    )
    ax.add_patch(a)

# AHL binds AbaR (dashed blue arrow back in)
arr_bind = FancyArrowPatch(
    (4.35, 3.70), (abaR_x + 0.35, abaR_y + 0.15),
    arrowstyle="-|>", mutation_scale=8, color=COL_AHL,
    lw=0.9, ls=(0, (2, 1.5)), zorder=4,
    connectionstyle="arc3,rad=0.2",
)
ax.add_patch(arr_bind)
ax.text(4.95, 4.40, "AHL binds AbaR", fontsize=6,
        style="italic", color=COL_AHL, zorder=5)

# -----------------------------------------------------------------------------
# Lactonases / acylase as purple "pacman" (Wedge) icons
# -----------------------------------------------------------------------------
qq_y = 1.10
qq_enzymes = [("MomL", 1.6), ("AaL", 3.05), ("AidA", 4.50), ("PvdQ", 7.45)]
for name, x in qq_enzymes:
    # Pacman: wedge cut out
    w = Wedge((x, qq_y), 0.20, 40, 320, facecolor=COL_QQ,
              edgecolor="black", lw=0.7, zorder=5)
    ax.add_patch(w)
    ax.text(x, qq_y - 0.35, name, ha="center", va="top",
            fontsize=6.5, fontweight="bold", color=COL_QQ, zorder=6)

ax.text(3.55, qq_y + 0.45,
        "Lactonases (MomL, AaL, AidA) + acylase (PvdQ) — cleave AHL",
        ha="center", fontsize=6.8, style="italic", color="#4a235a")

# Arrows: QQ enzyme -> nearest AHL (cleavage)
for ((name, x), (ax_x, ax_y)) in zip(qq_enzymes,
                                     [(1.85, 2.40), (3.30, 2.20),
                                      (4.70, 2.55), (7.45, 2.40)]):
    arr_q = FancyArrowPatch(
        (x, qq_y + 0.20), (ax_x, ax_y - 0.18),
        arrowstyle="-|>", mutation_scale=7, color=COL_QQ,
        lw=0.8, zorder=4,
    )
    ax.add_patch(arr_q)

# -----------------------------------------------------------------------------
# Legend (left half of footer)
# -----------------------------------------------------------------------------
leg_handles = [
    mpatches.Patch(color=COL_ABAI, label="AbaI (synthase)"),
    mpatches.Patch(color=COL_ABAR, label="AbaR (receptor)"),
    mpatches.Patch(color=COL_ABAM, label="AbaM (brake)"),
    mpatches.Patch(color=COL_AHL,  label="AHL signal"),
    mpatches.Patch(color=COL_QQ,   label="QQ enzymes"),
    Line2D([0], [0], color="black", lw=1.0,
           marker=">", markersize=5, label="activation"),
    Line2D([0], [0], color=COL_ABAM, lw=1.4,
           marker="_", markersize=8, label="inhibition"),
    Line2D([0], [0], color=COL_AHL, lw=0.9, linestyle=(0, (2, 1.5)),
           label="diffusion"),
]
leg = ax.legend(handles=leg_handles, loc="lower left",
                bbox_to_anchor=(0.005, -0.03),
                fontsize=6.0, frameon=False, ncol=4,
                handlelength=1.1, columnspacing=0.7,
                handletextpad=0.35)

# -----------------------------------------------------------------------------
# Numbered cycle line (single-line summary at very bottom)
# -----------------------------------------------------------------------------
steps = [
    ("1", "Synthesis"),
    ("2", "Diffusion"),
    ("3", "Accumulation"),
    ("4", "Binding"),
    ("5", "Transcription"),
    ("6", "Output"),
]
cycle_y = -0.40
ax.text(0.50, cycle_y, "QS cycle:",
        ha="left", va="center", fontsize=6.5,
        fontweight="bold", color="#222", zorder=11)
step_x0 = 1.55
step_gap = 1.35
for i, (num, title) in enumerate(steps):
    cx = step_x0 + i * step_gap
    ax.add_patch(Circle((cx, cycle_y), 0.10, facecolor="#333333",
                        edgecolor="black", lw=0.5, zorder=11))
    ax.text(cx, cycle_y, num, ha="center", va="center",
            fontsize=6, fontweight="bold", color="white", zorder=12)
    ax.text(cx + 0.13, cycle_y, title, ha="left", va="center",
            fontsize=6, color="#222", zorder=11)

# -----------------------------------------------------------------------------
# Save
# -----------------------------------------------------------------------------
png_path = os.path.join(OUT_DIR, "figure3a_qs_circuit.png")
svg_path = os.path.join(OUT_DIR, "figure3a_qs_circuit.svg")
plt.savefig(png_path, dpi=600, facecolor="white")
plt.savefig(svg_path, facecolor="white")
plt.close(fig)

print(f"Wrote: {png_path}  ({os.path.getsize(png_path):,} bytes)")
print(f"Wrote: {svg_path}  ({os.path.getsize(svg_path):,} bytes)")
