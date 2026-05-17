"""Generate Figure 4: QS-targeting interventions by translational maturity.

Stacked horizontal bar chart, one row per intervention class, with stacks
encoding the five study designs ordered from least to most translational.
Stack colours use a sequential ramp (lighter -> darker) so the visual order
mirrors translational progression. A vertical reference line marks the
mean pre-translational frontier; the total N is bolded at the end of each bar
along with the maturity index MI = (animal+clinical)/total.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, panel_label

apply_style()

# --------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure4_interventions.png"
OUT_SVG = HERE / "figures" / "figure4_interventions.svg"

# --------------------------------------------------------------------------------------
# Load
# --------------------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
print(f"[load] {len(df)} records from {CSV_PATH.name}")

INTERVENTIONS = [
    "natural_product", "phage", "peptide", "enzyme_qq", "nanoparticle",
    "synthetic_compound", "repurposed_drug", "antibody_vaccine",
]

# Five maturity stages, ordered from least translational to most translational
STAGES = ["in_silico", "in_vitro", "omics", "animal_model", "clinical"]

# Sequential blue->red ramp so visual order = translational progression
# (light blue = early in silico ... dark red = clinical)
STAGE_COLORS = {
    "in_silico":    "#cfe2f3",   # very light blue
    "in_vitro":     "#6fa8dc",   # medium blue
    "omics":        "#3a78b8",   # deep blue
    "animal_model": "#cc6d3a",   # warm orange
    "clinical":     "#7a1818",   # dark red (most advanced)
}

STAGE_LABEL = {
    "in_silico":    "in silico",
    "in_vitro":     "in vitro",
    "omics":        "omics",
    "animal_model": "animal model (in vivo)",
    "clinical":     "clinical",
}

# --------------------------------------------------------------------------------------
# Counts
# --------------------------------------------------------------------------------------
counts = {iv: Counter() for iv in INTERVENTIONS}
parse_skipped = 0
for _, row in df.iterrows():
    iv_field = row.get("interventions")
    st = row.get("study_type")
    if pd.isna(iv_field):
        parse_skipped += 1
        continue
    tokens = {t.strip() for t in str(iv_field).split("|") if t.strip()}
    if not tokens:
        parse_skipped += 1
        continue
    for tok in tokens:
        if tok in INTERVENTIONS and st in STAGES:
            counts[tok][st] += 1

matrix = pd.DataFrame(0, index=INTERVENTIONS, columns=STAGES, dtype=int)
for iv in INTERVENTIONS:
    for st in STAGES:
        matrix.at[iv, st] = counts[iv][st]

matrix["__total__"] = matrix.sum(axis=1)
matrix = matrix.sort_values("__total__", ascending=False)
totals = matrix["__total__"].values
matrix = matrix.drop(columns="__total__")

print(f"[parse] skipped {parse_skipped} rows")


def maturity_index(iv: str) -> float:
    tot = matrix.loc[iv].sum()
    if tot == 0:
        return 0.0
    return (matrix.at[iv, "animal_model"] + matrix.at[iv, "clinical"]) / tot


# --------------------------------------------------------------------------------------
# Figure
# --------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ypos = np.arange(len(matrix.index))
labels = [iv.replace("_", " ") for iv in matrix.index]

left = np.zeros(len(matrix.index), dtype=float)
for st in STAGES:
    widths = matrix[st].values.astype(float)
    ax.barh(
        ypos, widths,
        left=left,
        color=STAGE_COLORS[st],
        edgecolor="white",
        linewidth=0.5,
        height=0.6,
        label=STAGE_LABEL[st],
    )
    for i, w in enumerate(widths):
        if w >= 4:
            ax.text(
                left[i] + w / 2, ypos[i],
                f"{int(w)}",
                ha="center", va="center",
                fontsize=8,
                color="white" if st in ("clinical", "omics", "animal_model") else "#222",
                fontweight="bold",
            )
    left += widths

# Translational frontier
pre_translational = matrix[["in_silico", "in_vitro", "omics"]].sum(axis=1).values
frontier_x = float(np.mean(pre_translational))
ax.axvline(frontier_x, color="#444", linestyle="--", linewidth=1.0,
           alpha=0.85, zorder=1)
ax.text(
    frontier_x + 0.3, len(matrix.index) - 0.4,
    f"Translational frontier\n(in vivo + clinical)\nmean = {frontier_x:.1f}",
    color="#444", fontsize=7.0,
    ha="left", va="bottom", style="italic",
)

# Bold total N + MI at the end of each bar
max_total = max(totals) if len(totals) else 1
for i, iv in enumerate(matrix.index):
    mi = maturity_index(iv)
    tot = int(matrix.loc[iv].sum())
    ax.text(
        tot + max_total * 0.012, i,
        f"N={tot}  (MI={mi*100:.0f}%)",
        va="center", ha="left",
        fontsize=8.5, fontweight="bold", color="#222",
    )

ax.set_yticks(ypos)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel("Papers (a paper may appear in >1 intervention class)")
ax.set_xlim(0, max_total * 1.32)
ax.set_ylim(len(matrix.index) + 0.5, -0.7)
ax.set_title("")  # title handled via suptitle

ax.legend(
    loc="lower right",
    frameon=False,
    title="Study design",
    title_fontsize=8.5,
    fontsize=8,
)

fig.suptitle("Figure 4. QS-targeting interventions by translational maturity",
             y=0.995)
fig.tight_layout(rect=(0, 0, 1, 0.95))

OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=600)
fig.savefig(OUT_SVG)
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
