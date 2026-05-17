"""Generate Figure 4: QS-targeting interventions by translational maturity.

A stacked horizontal bar chart in which each row represents an intervention
class (natural_product, phage, peptide, enzyme_qq, nanoparticle,
synthetic_compound, repurposed_drug, antibody_vaccine) and the stacked
segments enumerate the study designs through which that intervention has been
evaluated (in_silico, in_vitro, omics, animal_model, clinical). A vertical
reference line marks the in-vivo translation frontier (where animal+clinical
counts begin), and each row is annotated with its maturity index
(animal+clinical)/total.

The categorized.csv `interventions` column is pipe-separated multi-label;
papers may belong to more than one intervention class. Each paper contributes
its study_type to every intervention class it tags. Rows are sorted by total
descending. Reviews/methodology/other are excluded from maturity stages but
counted into the row total via an "other" column not shown (we only stack the
five maturity stages).
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------------------
# Paths and style
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure4_interventions.png"
OUT_SVG = HERE / "figures" / "figure4_interventions.svg"

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 10,
        "legend.fontsize": 9,
    }
)

# --------------------------------------------------------------------------------------
# Load and parse
# --------------------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
print(f"[load] {len(df)} records from {CSV_PATH.name}")

INTERVENTIONS = [
    "natural_product",
    "phage",
    "peptide",
    "enzyme_qq",
    "nanoparticle",
    "synthetic_compound",
    "repurposed_drug",
    "antibody_vaccine",
]

# Five maturity stages, ordered from least translational to most
STAGES = ["in_silico", "in_vitro", "omics", "animal_model", "clinical"]

STAGE_COLORS = {
    "in_silico": "#cfd2d6",      # light grey
    "in_vitro": "#4c72b0",       # medium blue
    "omics": "#1f9897",          # teal
    "animal_model": "#e8893c",   # orange (in vivo step)
    "clinical": "#8b1a1a",       # dark red (clinical step)
}

STAGE_LABEL = {
    "in_silico": "in silico",
    "in_vitro": "in vitro",
    "omics": "omics",
    "animal_model": "animal model (in vivo)",
    "clinical": "clinical",
}

# Build counts: rows=intervention class, cols=stage
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

# Build the stacked matrix
matrix = pd.DataFrame(0, index=INTERVENTIONS, columns=STAGES, dtype=int)
for iv in INTERVENTIONS:
    for st in STAGES:
        matrix.at[iv, st] = counts[iv][st]

# Sort by total descending
matrix["__total__"] = matrix.sum(axis=1)
matrix = matrix.sort_values("__total__", ascending=False)
totals = matrix["__total__"].values
matrix = matrix.drop(columns="__total__")

print(f"[parse] skipped rows with null interventions: {parse_skipped}")
print("[matrix] stage counts per intervention (only 5 maturity stages):")
for iv in matrix.index:
    print(f"  {iv}: total={int(matrix.loc[iv].sum())}, dist={matrix.loc[iv].to_dict()}")

# Maturity index = (animal + clinical) / total (using maturity-stage total)
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
        ypos,
        widths,
        left=left,
        color=STAGE_COLORS[st],
        edgecolor="white",
        linewidth=0.6,
        label=STAGE_LABEL[st],
    )
    # Inline numeric labels for non-trivial segments
    for i, w in enumerate(widths):
        if w >= 4:
            ax.text(
                left[i] + w / 2,
                ypos[i],
                f"{int(w)}",
                ha="center",
                va="center",
                fontsize=8,
                color="white" if st in ("clinical", "animal_model", "omics", "in_vitro") else "#222",
                fontweight="bold",
            )
    left += widths

# Translation frontier: vertical line at the median location where animal+clinical begin
# across rows (i.e., mean of in_silico+in_vitro+omics widths).
pre_translational = matrix[["in_silico", "in_vitro", "omics"]].sum(axis=1).values
frontier_x = float(np.mean(pre_translational))
ax.axvline(
    frontier_x,
    color="#555",
    linestyle="--",
    linewidth=1.0,
    alpha=0.85,
    zorder=1,
)
ax.text(
    frontier_x,
    -0.85,
    f"translation frontier (mean pre-translational = {frontier_x:.1f})",
    color="#555",
    fontsize=8,
    ha="center",
    va="bottom",
    style="italic",
)

# Maturity index annotations on the right
max_total = max(totals) if len(totals) else 1
for i, iv in enumerate(matrix.index):
    mi = maturity_index(iv)
    tot = int(matrix.loc[iv].sum())
    ax.text(
        tot + max_total * 0.015,
        i,
        f"MI={mi*100:.0f}%  (n={tot})",
        va="center",
        ha="left",
        fontsize=9,
        color="#222",
    )

ax.set_yticks(ypos)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel("Papers (a paper may appear in >1 intervention class)")
ax.set_xlim(0, max_total * 1.32)
ax.set_title(
    "Figure 4. QS-targeting interventions by translational maturity",
    loc="left",
    fontweight="bold",
)

ax.legend(
    loc="lower right",
    frameon=True,
    title="Study design",
    title_fontsize=9,
)

fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
fig.savefig(OUT_SVG, bbox_inches="tight")
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
