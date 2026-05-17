"""Generate a 3x3 thumbnail grid of the 7 final figures + graphical abstract.

Layout (3x3):
   Row 1: Fig 1 PRISMA          | Fig 2 Trends         | Fig 3A Circuit
   Row 2: Fig 3B 2nd messengers | Fig 4 Interventions  | Fig 5 RoB
   Row 3: Fig 6 Network         | Graphical Abstract   | Summary text cell

Output: figures/all_figures_preview.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE

apply_style()

HERE = Path(__file__).resolve().parent

# Order matches the 3x3 layout specified in the task brief.
CELLS = [
    ("Figure 1 — PRISMA flow",            HERE / "figure1_prisma_flow.png"),
    ("Figure 2 — Literature landscape",   HERE / "figure2_trends.png"),
    ("Figure 3A — QS circuit",            HERE / "figure3a_qs_circuit.png"),
    ("Figure 3B — Second messengers",     HERE / "figure3b_second_messengers.png"),
    ("Figure 4 — Interventions",          HERE / "figure4_interventions.png"),
    ("Figure 5 — Risk of bias",           HERE / "figure5_rob_heatmap.png"),
    ("Figure 6 — Regulatory network",     HERE / "figure6_network.png"),
    ("Graphical abstract",                HERE / "graphical_abstract.png"),
    # Last cell: summary text only (None signals text cell)
    ("Submission package", None),
]

fig, axes = plt.subplots(3, 3, figsize=(13, 12), dpi=200)
axes = axes.flatten()

for ax, (title, path) in zip(axes, CELLS):
    if path is None:
        ax.axis("off")
        # Soft background and border
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.add_patch(Rectangle((0.04, 0.05), 0.92, 0.90,
                               facecolor="#f4f8fc",
                               edgecolor=PALETTE["blue"],
                               linewidth=1.4))
        ax.text(0.50, 0.83, "Submission package",
                ha="center", va="center",
                fontsize=14, fontweight="bold", color=PALETTE["blue"])
        summary = (
            "7 main figures + graphical abstract\n\n"
            "600 DPI PNG + SVG (editable text)\n\n"
            "IJAA submission package\n\n"
            "340 papers · 22 years · 3 databases"
        )
        ax.text(0.50, 0.40, summary,
                ha="center", va="center",
                fontsize=11, color="#222", linespacing=1.4)
        continue

    img = mpimg.imread(path)
    ax.imshow(img)
    ax.set_title(title, fontsize=10, fontweight="bold", loc="left",
                 color=PALETTE["blue"])
    ax.axis("off")

fig.suptitle(
    "Systematic review figures — preview montage",
    fontsize=14, fontweight="bold", y=0.995,
)
fig.tight_layout(rect=(0, 0, 1, 0.97))

out = HERE / "all_figures_preview.png"
fig.savefig(out, dpi=200, facecolor="white")
plt.close(fig)
print(f"Wrote: {out}  ({out.stat().st_size:,} bytes)")
