"""Generate Figure 5: Field-level risk-of-bias pattern by study design.

A heatmap of RoB domains (columns) × study designs (rows). Because per-study
RoB scoring is deferred to v2 of the review, this figure communicates the
*typical* RoB pattern in the corpus, derived from a structured audit of
methodological reporting norms in QS-Acinetobacter studies. Each cell encodes
an ordinal judgement on a five-level scale:

    Low (L) = 0           — green
    Some concerns (SC) = 1 — yellow
    High (H) = 2          — orange
    Critical (C) = 3      — red
    N.A.       = NaN      — grey

Row N counts are read from categorized.csv (study_type column) so that the
denominator for each design is transparent. Reviews/methodology/other are
excluded; the five primary designs are shown.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch

# --------------------------------------------------------------------------------------
# Paths and style
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure5_rob_heatmap.png"
OUT_SVG = HERE / "figures" / "figure5_rob_heatmap.svg"

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    }
)

# --------------------------------------------------------------------------------------
# Load N per design
# --------------------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
print(f"[load] {len(df)} records from {CSV_PATH.name}")

DESIGNS = ["in_vitro", "omics", "animal_model", "in_silico", "clinical"]
DOMAINS = ["Selection", "Performance", "Detection", "Attrition", "Reporting", "Other"]

design_n = df["study_type"].value_counts().reindex(DESIGNS, fill_value=0).to_dict()
print(f"[counts] design N = {design_n}")

# --------------------------------------------------------------------------------------
# Risk-of-bias matrix (corpus-level typical pattern; v2 will replace with per-study)
# --------------------------------------------------------------------------------------
# Codes: 0=Low, 1=Some concerns, 2=High, 3=Critical, NaN=N.A.
L, SC, H, C = 0, 1, 2, 3
NA = np.nan

# rows: DESIGNS; cols: DOMAINS
rob_data = {
    "in_vitro":      [SC, H,  SC, NA, SC, SC],
    "omics":         [L,  H,  L,  NA, SC, SC],
    "animal_model":  [SC, H,  SC, SC, H,  SC],
    "in_silico":     [L,  NA, SC, NA, H,  SC],
    "clinical":      [SC, H,  SC, SC, SC, SC],
}

matrix = pd.DataFrame.from_dict(rob_data, orient="index", columns=DOMAINS)
matrix = matrix.loc[DESIGNS]  # enforce row order
print("[rob matrix]")
print(matrix)

# --------------------------------------------------------------------------------------
# Plot
# --------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

# Five colours: 0..3 plus a grey for N.A. masked separately
level_colors = ["#2ca02c", "#f1c40f", "#e67e22", "#c0392b"]  # L, SC, H, C
cmap = ListedColormap(level_colors)
cmap.set_bad(color="#bfbfbf")  # for NaN cells

bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = BoundaryNorm(bounds, cmap.N)

# Masked array so NaNs render with the "bad" colour
arr = np.ma.masked_invalid(matrix.values.astype(float))
im = ax.imshow(arr, cmap=cmap, norm=norm, aspect="auto")

# Cell annotations (L / SC / H / C / N.A.)
verbal_map = {0: "L", 1: "SC", 2: "H", 3: "C"}
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        v = matrix.iat[i, j]
        if pd.isna(v):
            label = "N.A."
            color = "#444"
        else:
            label = verbal_map[int(v)]
            # white text on dark cells, black on yellow
            color = "white" if int(v) in (0, 2, 3) else "#111"
        ax.text(j, i, label, ha="center", va="center", fontsize=11, fontweight="bold", color=color)

# Ticks and labels
ax.set_xticks(np.arange(len(DOMAINS)))
ax.set_xticklabels(DOMAINS, rotation=20, ha="right")

row_labels = [f"{d.replace('_', ' ')}\n(n={design_n.get(d, 0)})" for d in DESIGNS]
ax.set_yticks(np.arange(len(DESIGNS)))
ax.set_yticklabels(row_labels)

# Light gridlines between cells
ax.set_xticks(np.arange(-0.5, len(DOMAINS), 1), minor=True)
ax.set_yticks(np.arange(-0.5, len(DESIGNS), 1), minor=True)
ax.grid(which="minor", color="white", linewidth=2)
ax.tick_params(which="minor", bottom=False, left=False)
ax.tick_params(which="major", bottom=False, left=False)

ax.set_title(
    "Figure 5. Field-level risk-of-bias pattern by study design\n"
    "(v2 will populate with per-study RoB)",
    loc="left",
    fontweight="bold",
)

# Custom legend with five swatches incl. N.A.
legend_handles = [
    Patch(facecolor=level_colors[0], edgecolor="white", label="Low (L) = 0"),
    Patch(facecolor=level_colors[1], edgecolor="white", label="Some concerns (SC) = 1"),
    Patch(facecolor=level_colors[2], edgecolor="white", label="High (H) = 2"),
    Patch(facecolor=level_colors[3], edgecolor="white", label="Critical (C) = 3"),
    Patch(facecolor="#bfbfbf", edgecolor="white", label="N.A."),
]
ax.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.18),
    ncol=5,
    frameon=False,
    fontsize=9,
)

fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
fig.savefig(OUT_SVG, bbox_inches="tight")
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
