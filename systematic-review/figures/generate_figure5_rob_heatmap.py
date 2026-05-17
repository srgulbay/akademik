"""Generate Figure 5: Field-level risk-of-bias pattern by study design.

5-level ordinal scale:
    Low (L)          = 0  -> green
    Moderate-low     = 0.5 [reserved]
    Some concerns (SC) = 1 -> light green
    High concerns    = 2 -> yellow
    High (H)         = 3 -> orange
    Critical (C)     = 4 -> red
    N.A.             = grey
For this corpus the working levels are L, SC, H, C plus N.A. We add accessibility
symbols (●○◐◆) alongside the verbal codes. Row N annotations show per-design counts;
a rotated column header "Risk-of-bias domain" runs along the right side.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style

apply_style()

# --------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure5_rob_heatmap.png"
OUT_SVG = HERE / "figures" / "figure5_rob_heatmap.svg"

# --------------------------------------------------------------------------------------
# Load N per design
# --------------------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
print(f"[load] {len(df)} records")

DESIGNS = ["in_vitro", "omics", "animal_model", "in_silico", "clinical"]
DOMAINS = ["Selection", "Performance", "Detection", "Attrition", "Reporting", "Other"]

design_n = df["study_type"].value_counts().reindex(DESIGNS, fill_value=0).to_dict()

# --------------------------------------------------------------------------------------
# RoB matrix (corpus-level typical pattern)
# Five-level ordinal scale: 0=Low, 1=Some concerns, 2=High concerns,
# 3=High, 4=Critical, NaN=N.A.
# To keep the existing biological narrative we use four working levels (L=0, SC=1,
# H=2, C=3) plus N.A.; level 2 from the v1 was "High" so we map: L=0, SC=1, H=2, C=3.
# The ListedColormap below has 5 ordinal bins.
# --------------------------------------------------------------------------------------
L, SC, H, C = 0, 1, 2, 3
NA = np.nan

rob_data = {
    "in_vitro":      [SC, H,  SC, NA, SC, SC],
    "omics":         [L,  H,  L,  NA, SC, SC],
    "animal_model":  [SC, H,  SC, SC, H,  SC],
    "in_silico":     [L,  NA, SC, NA, H,  SC],
    "clinical":      [SC, H,  SC, SC, SC, SC],
}
matrix = pd.DataFrame.from_dict(rob_data, orient="index", columns=DOMAINS)
matrix = matrix.loc[DESIGNS]
print("[rob matrix]"); print(matrix)

# --------------------------------------------------------------------------------------
# Plot
# --------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.2))

# 5-level ordinal colour scale: green -> light green -> yellow -> orange -> red
# (we use 4 working levels: L, SC, H, C)
level_colors = [
    "#2e7d32",   # Low - green
    "#a5d6a7",   # Some concerns - light green
    "#fdd835",   # High concerns - yellow (we treat as 'H' below)
    "#fb8c00",   # High - orange
    "#c62828",   # Critical - red
]
# We only have 4 working codes (L,SC,H,C) -> indices 0,1,3,4
# Map: L->0, SC->1, H->3, C->4 (skipping the moderate yellow)
display_palette = [level_colors[0], level_colors[1], level_colors[3], level_colors[4]]
cmap = ListedColormap(display_palette)
cmap.set_bad(color="#bfbfbf")

bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = BoundaryNorm(bounds, cmap.N)

arr = np.ma.masked_invalid(matrix.values.astype(float))
im = ax.imshow(arr, cmap=cmap, norm=norm, aspect="auto")

# Cell annotations: verbal code + accessibility symbol
verbal_map = {0: "L", 1: "SC", 2: "H", 3: "C"}
symbol_map = {0: "●", 1: "◐", 2: "▲", 3: "○"}
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        v = matrix.iat[i, j]
        if pd.isna(v):
            label = "N.A."
            color = "#444"
            ax.text(j, i, label, ha="center", va="center",
                    fontsize=11, fontweight="bold", color=color)
        else:
            level = int(v)
            label = verbal_map[level]
            sym = symbol_map[level]
            color = "white" if level in (0, 3) else "#111"
            # Verbal code on top line, symbol underneath (larger)
            ax.text(j, i - 0.13, label, ha="center", va="center",
                    fontsize=12, fontweight="bold", color=color)
            ax.text(j, i + 0.22, sym, ha="center", va="center",
                    fontsize=12, color=color)

# Ticks
ax.set_xticks(np.arange(len(DOMAINS)))
ax.set_xticklabels(DOMAINS, rotation=20, ha="right")

row_labels = []
n_labels = {
    "in_vitro": "in vitro",
    "omics": "omics",
    "animal_model": "animal model",
    "in_silico": "in silico",
    "clinical": "clinical",
}
for d in DESIGNS:
    row_labels.append(f"{n_labels[d]}\n(n={design_n.get(d, 0)})")
ax.set_yticks(np.arange(len(DESIGNS)))
ax.set_yticklabels(row_labels)

ax.set_xticks(np.arange(-0.5, len(DOMAINS), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(DESIGNS), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="minor", bottom=False, left=False)
ax.tick_params(which="major", bottom=False, left=False)

# Rotated right-side column header
ax2 = ax.secondary_yaxis("right")
ax2.set_yticks([])
ax2.set_ylabel("Risk-of-bias domain (corpus-level)", rotation=270, labelpad=18,
               fontsize=9, fontweight="bold", color="#333")

# Suptitle (Figure 5 caption header)
fig.suptitle(
    "Figure 5. Field-level risk-of-bias pattern by study design",
    y=0.995,
)

# Custom legend
legend_handles = [
    Patch(facecolor=display_palette[0], edgecolor="white", label="Low (L)  ●"),
    Patch(facecolor=display_palette[1], edgecolor="white", label="Some concerns (SC)  ◐"),
    Patch(facecolor=display_palette[2], edgecolor="white", label="High (H)  ▲"),
    Patch(facecolor=display_palette[3], edgecolor="white", label="Critical (C)  ○"),
    Patch(facecolor="#bfbfbf", edgecolor="white", label="N.A."),
]
ax.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.20),
    ncol=5,
    frameon=False,
    fontsize=8.5,
)

fig.tight_layout(rect=(0, 0, 1, 0.94))
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=600)
fig.savefig(OUT_SVG)
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
