"""Generate Figure 2: Literature landscape of QS in A. baumannii (2003-2025).

Multi-panel figure (2x2):
  A. Annual publication count with landmark annotations
  B. Study-type distribution donut
  C. Topic-by-era frequency heatmap
  D. Intervention-class horizontal bar chart
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import Normalize

# --------------------------------------------------------------------------------------
# Paths and style
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure2_trends.png"
OUT_SVG = HERE / "figures" / "figure2_trends.svg"

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
    }
)

# --------------------------------------------------------------------------------------
# Load data
# --------------------------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df.dropna(subset=["year"]).copy()
df["year"] = df["year"].astype(int)

print(f"[load] {len(df)} records, years {df['year'].min()}-{df['year'].max()}")

# --------------------------------------------------------------------------------------
# Figure scaffold
# --------------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axA, axB = axes[0]
axC, axD = axes[1]

# --------------------------------------------------------------------------------------
# Panel A — Annual publication count
# --------------------------------------------------------------------------------------
year_min, year_max = 2003, 2025
year_range = np.arange(year_min, year_max + 1)
year_counts = df["year"].value_counts().reindex(year_range, fill_value=0).sort_index()

norm = Normalize(vmin=year_min, vmax=year_max)
colors = cm.viridis(norm(year_range))
axA.bar(year_range, year_counts.values, color=colors, edgecolor="white", linewidth=0.5)

# Landmark annotations
landmarks = [
    (2008, "2008\nNiu et al.\nabaI characterized"),
    (2018, "2018\nMayer AHL lactonase\ninflection point"),
    (2024, "2024\n>40 papers\nrecent expansion"),
]
y_top = year_counts.max()
for yr, label in landmarks:
    y = year_counts.get(yr, 0)
    axA.annotate(
        label,
        xy=(yr, y),
        xytext=(yr, y + y_top * 0.35),
        ha="center",
        va="bottom",
        fontsize=7,
        arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8, shrinkA=0, shrinkB=2),
    )

axA.set_xticks(np.arange(year_min, year_max + 1, 2))
axA.set_xlim(year_min - 0.7, year_max + 0.7)
axA.set_ylim(0, y_top * 1.55)
axA.set_ylabel("Publications")
axA.set_xlabel("Year")
axA.set_title(f"A — Annual publication count (n={len(df)})", loc="left", fontweight="bold")
axA.tick_params(axis="x", rotation=0)

# --------------------------------------------------------------------------------------
# Panel B — Study-type donut
# --------------------------------------------------------------------------------------
study_order = [
    "in_vitro",
    "omics",
    "animal_model",
    "in_silico",
    "review",
    "methodology",
    "clinical",
    "other",
]
study_counts = (
    df["study_type"].fillna("other").value_counts().reindex(study_order, fill_value=0)
)

# Palette: tab10-derived (distinct, also feeds Panel D)
palette_B = sns.color_palette("tab10", n_colors=len(study_order))
study_color = dict(zip(study_order, palette_B))

wedges, _texts = axB.pie(
    study_counts.values,
    labels=None,
    colors=[study_color[s] for s in study_order],
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.42, edgecolor="white", linewidth=1.2),
)
axB.set(aspect="equal")
axB.set_title("B — Study designs", loc="left", fontweight="bold")
axB.text(0, 0, f"n={int(study_counts.sum())}", ha="center", va="center", fontsize=11, fontweight="bold")

legend_labels = [f"{s.replace('_', ' ')} ({study_counts[s]})" for s in study_order]
axB.legend(
    wedges,
    legend_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.02),
    ncol=2,
    frameon=False,
    fontsize=8,
)

# --------------------------------------------------------------------------------------
# Panel C — Topic-by-era heatmap
# --------------------------------------------------------------------------------------
topics_order = [
    "biofilm",
    "abaI_abaR_axis",
    "ahl_chemistry",
    "natural_product",
    "phage_therapy",
    "qsi_discovery",
    "quorum_quenching",
    "nanoparticle",
    "polymicrobial",
    "drug_repurposing",
    "vaccine_immune",
    "gene_regulation",
    "virulence_factors",
    "antibiotic_resistance",
]
era_bins = [
    ("2003-2010", 2003, 2010),
    ("2011-2018", 2011, 2018),
    ("2019-2023", 2019, 2023),
    ("2024-2025", 2024, 2025),
]


def era_for(year: int) -> str | None:
    for label, lo, hi in era_bins:
        if lo <= year <= hi:
            return label
    return None


df["era"] = df["year"].apply(era_for)

heat = pd.DataFrame(
    0, index=topics_order, columns=[lbl for lbl, _, _ in era_bins], dtype=int
)
parse_issues = 0
for _, row in df.iterrows():
    era = row["era"]
    if era is None or pd.isna(row.get("topics")):
        if pd.isna(row.get("topics")):
            parse_issues += 1
        continue
    tokens = {t.strip() for t in str(row["topics"]).split("|") if t.strip()}
    for topic in topics_order:
        if topic in tokens:
            heat.at[topic, era] += 1

sns.heatmap(
    heat,
    ax=axC,
    cmap="YlGnBu",
    annot=True,
    fmt="d",
    cbar=True,
    cbar_kws={"label": "Papers", "shrink": 0.7},
    linewidths=0.4,
    linecolor="white",
    annot_kws={"fontsize": 8},
)
axC.set_title("C — Topic frequency by era", loc="left", fontweight="bold")
axC.set_xlabel("Era")
axC.set_ylabel("")
axC.tick_params(axis="y", rotation=0)
axC.set_yticklabels([t.replace("_", " ") for t in topics_order], fontsize=8)

# --------------------------------------------------------------------------------------
# Panel D — Intervention class breakdown
# --------------------------------------------------------------------------------------
intervention_order = [
    "natural_product",
    "phage",
    "peptide",
    "enzyme_qq",
    "nanoparticle",
    "synthetic_compound",
    "repurposed_drug",
    "antibody_vaccine",
]

intervention_counts: Counter[str] = Counter()
for val in df["interventions"].dropna():
    tokens = {t.strip() for t in str(val).split("|") if t.strip()}
    for tok in tokens:
        if tok in intervention_order:
            intervention_counts[tok] += 1

# Order by count descending
ordered = sorted(intervention_order, key=lambda k: intervention_counts.get(k, 0), reverse=True)
ordered_counts = [intervention_counts.get(k, 0) for k in ordered]

# Reuse Panel B palette mapping where shared keys exist; otherwise extend with tab10
shared_palette = sns.color_palette("tab10", n_colors=max(len(intervention_order), len(study_order)))
intervention_color = {}
for i, k in enumerate(intervention_order):
    if k in study_color:
        intervention_color[k] = study_color[k]
    else:
        intervention_color[k] = shared_palette[i]

bar_colors = [intervention_color[k] for k in ordered]

ypos = np.arange(len(ordered))
axD.barh(ypos, ordered_counts, color=bar_colors, edgecolor="white", linewidth=0.6)
axD.set_yticks(ypos)
axD.set_yticklabels([k.replace("_", " ") for k in ordered], fontsize=8)
axD.invert_yaxis()
axD.set_xlabel("Papers")
axD.set_title("D — QS-targeting intervention classes", loc="left", fontweight="bold")

for i, c in enumerate(ordered_counts):
    axD.text(c + max(ordered_counts) * 0.01, i, str(c), va="center", fontsize=8)

axD.set_xlim(0, max(ordered_counts) * 1.12)

# --------------------------------------------------------------------------------------
# Suptitle + layout + save
# --------------------------------------------------------------------------------------
fig.suptitle(
    "Figure 2. Literature landscape of QS in A. baumannii (2003-2025)",
    fontsize=12,
    fontweight="bold",
    y=0.995,
)
fig.tight_layout(rect=(0, 0, 1, 0.965))

OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
fig.savefig(OUT_SVG, bbox_inches="tight")
plt.close(fig)

# --------------------------------------------------------------------------------------
# Diagnostics
# --------------------------------------------------------------------------------------
print(f"[panelA] year span {year_min}-{year_max}, total bars={len(year_range)}, sum={int(year_counts.sum())}")
print(f"[panelB] study_type sum={int(study_counts.sum())}; counts={study_counts.to_dict()}")
print(f"[panelC] heatmap shape={heat.shape}; total cells filled={(heat>0).sum().sum()}; null topic rows={parse_issues}")
print(f"[panelD] interventions={dict(zip(ordered, ordered_counts))}")
print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
