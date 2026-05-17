"""Generate a 3x3 thumbnail grid of all 7 final figures.

Output: figures/all_figures_preview.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style

apply_style()

HERE = Path(__file__).resolve().parent

FIGS = [
    ("Figure 1 — PRISMA flow",                    HERE / "figure1_prisma_flow.png"),
    ("Figure 2 — Literature trends",              HERE / "figure2_trends.png"),
    ("Figure 3A — QS circuit",                    HERE / "figure3a_qs_circuit.png"),
    ("Figure 3B — Second messengers",             HERE / "figure3b_second_messengers.png"),
    ("Figure 4 — Interventions",                  HERE / "figure4_interventions.png"),
    ("Figure 5 — Risk of bias",                   HERE / "figure5_rob_heatmap.png"),
    ("Figure 6 — Regulatory network",             HERE / "figure6_network.png"),
]

fig, axes = plt.subplots(3, 3, figsize=(12, 11), dpi=200)
axes = axes.flatten()

for ax, (title, path) in zip(axes, FIGS):
    img = mpimg.imread(path)
    ax.imshow(img)
    ax.set_title(title, fontsize=10, fontweight="bold", loc="left")
    ax.axis("off")

# Blank remaining axes
for ax in axes[len(FIGS):]:
    ax.axis("off")

fig.suptitle("Systematic review figures — preview montage", fontsize=13,
             fontweight="bold", y=0.995)
fig.tight_layout(rect=(0, 0, 1, 0.97))

out = HERE / "all_figures_preview.png"
fig.savefig(out, dpi=200, facecolor="white")
plt.close(fig)
print(f"Wrote: {out}  ({out.stat().st_size:,} bytes)")
