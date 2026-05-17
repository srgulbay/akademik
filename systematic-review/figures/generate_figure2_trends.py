"""Generate Figure 2: Literature landscape of QS in A. baumannii (2003-2025).

Multi-panel figure (2x2):
  A. Annual publication count with landmark annotations (custom blue gradient)
  B. Study-type distribution donut (5-colour palette)
  C. Topic-by-era frequency heatmap (YlGnBu, zeros blank, sorted by total)
  D. Intervention-class horizontal bar chart (same palette as B)
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE, panel_label

apply_style()

# --------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------
HERE = Path("/home/user/akademik/systematic-review")
CSV_PATH = HERE / "literature" / "categorized.csv"
OUT_PNG = HERE / "figures" / "figure2_trends.png"
OUT_SVG = HERE / "figures" / "figure2_trends.svg"

# --------------------------------------------------------------------------------------
# Five-colour palette used in panels B and D (colourblind-safe)
# --------------------------------------------------------------------------------------
FIVE_COLOURS = [
    PALETTE["blue"],    # in_vitro / phage
    PALETTE["amber"],   # omics / natural_product
    PALETTE["teal"],    # animal_model / peptide
    PALETTE["red"],     # in_silico / enzyme_qq
    PALETTE["purple"],  # review / nanoparticle
]
# Extension palette for additional categories (greyed)
EXT_COLOURS = ["#9aa6b2", "#7d8a98", "#5d6b7a"]


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
# Panel A - Annual publication count (custom blue gradient #cfe2f3 -> #1f3a93)
# --------------------------------------------------------------------------------------
year_min, year_max = 2003, 2025
year_range = np.arange(year_min, year_max + 1)
year_counts = df["year"].value_counts().reindex(year_range, fill_value=0).sort_index()

blue_grad = LinearSegmentedColormap.from_list(
    "blue_grad", ["#cfe2f3", "#1f3a93"]
)
norm = Normalize(vmin=year_min, vmax=year_max)
colours = blue_grad(norm(year_range))
axA.bar(year_range, year_counts.values, color=colours,
        edgecolor="white", linewidth=0.4)

# Landmark annotations
landmarks = [
    (2008, "2008\nNiu et al.\nabaI characterized", 0.55),
    (2018, "2018\nAHL lactonase\ninflection point", 0.40),
    (2024, "2024\n>40 papers", 0.20),
]
y_top = year_counts.max()
for yr, label, frac in landmarks:
    y = year_counts.get(yr, 0)
    axA.annotate(
        label,
        xy=(yr, y),
        xytext=(yr, y + y_top * frac),
        ha="center", va="bottom",
        fontsize=6.8,
        arrowprops=dict(arrowstyle="->", color="#333", lw=0.7,
                        shrinkA=0, shrinkB=2),
    )

# Cleaner year ticks: every 4 years
axA.set_xticks(np.arange(year_min, year_max + 1, 4))
axA.set_xlim(year_min - 0.7, year_max + 0.7)
axA.set_ylim(0, y_top * 1.55)
axA.set_ylabel("Publications")
axA.set_xlabel("Year")
axA.set_title(f"Annual publication count (n={len(df)})", loc="left")
panel_label(axA, "A")

# --------------------------------------------------------------------------------------
# Panel B - Study-type donut
# --------------------------------------------------------------------------------------
study_order = [
    "in_vitro", "omics", "animal_model", "in_silico", "review",
    "methodology", "clinical", "other",
]
study_counts = (
    df["study_type"].fillna("other").value_counts()
      .reindex(study_order, fill_value=0)
)

study_palette = FIVE_COLOURS + EXT_COLOURS  # 8 colours
study_colour = dict(zip(study_order, study_palette))

# Bring in_vitro segment to start at 90 deg for visual balance.
# matplotlib pie starts at startangle and goes counterclock=False (clockwise).
wedges, _texts = axB.pie(
    study_counts.values,
    labels=None,
    colors=[study_colour[s] for s in study_order],
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.42, edgecolor="white", linewidth=1.2),
)
axB.set(aspect="equal")
axB.set_title("Study designs", loc="left")
panel_label(axB, "B")
axB.text(0, 0, f"n={int(study_counts.sum())}",
         ha="center", va="center", fontsize=11, fontweight="bold")

legend_labels = [f"{s.replace('_', ' ')} ({study_counts[s]})" for s in study_order]
axB.legend(
    wedges, legend_labels,
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    ncol=1,
    frameon=False,
    fontsize=7.5,
)

# --------------------------------------------------------------------------------------
# Panel C - Topic-by-era heatmap (zeros blank, sorted by total)
# --------------------------------------------------------------------------------------
topics_order = [
    "biofilm", "abaI_abaR_axis", "ahl_chemistry", "natural_product",
    "phage_therapy", "qsi_discovery", "quorum_quenching", "nanoparticle",
    "polymicrobial", "drug_repurposing", "vaccine_immune", "gene_regulation",
    "virulence_factors", "antibiotic_resistance",
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

# Sort rows by total descending
heat["__total__"] = heat.sum(axis=1)
heat = heat.sort_values("__total__", ascending=False).drop(columns="__total__")

# Annotate only non-zero cells
annot = heat.astype(object).copy()
for r in heat.index:
    for c in heat.columns:
        annot.at[r, c] = str(int(heat.at[r, c])) if heat.at[r, c] > 0 else ""

sns.heatmap(
    heat, ax=axC,
    cmap="YlGnBu",
    annot=annot.values, fmt="s",
    cbar=True,
    cbar_kws={"label": "Papers", "shrink": 0.7},
    linewidths=0.4, linecolor="white",
    annot_kws={"fontsize": 7.5},
)
axC.set_title("Topic frequency by era", loc="left")
panel_label(axC, "C")
axC.set_xlabel("Era")
axC.set_ylabel("")
axC.tick_params(axis="y", rotation=0)
axC.set_yticklabels([t.replace("_", " ") for t in heat.index], fontsize=7.5)

# --------------------------------------------------------------------------------------
# Panel D - Intervention class breakdown (same 5-colour palette as B)
# --------------------------------------------------------------------------------------
intervention_order = [
    "natural_product", "phage", "peptide", "enzyme_qq", "nanoparticle",
    "synthetic_compound", "repurposed_drug", "antibody_vaccine",
]

intervention_counts: Counter[str] = Counter()
for val in df["interventions"].dropna():
    tokens = {t.strip() for t in str(val).split("|") if t.strip()}
    for tok in tokens:
        if tok in intervention_order:
            intervention_counts[tok] += 1

# Sort by count descending
ordered = sorted(intervention_order,
                 key=lambda k: intervention_counts.get(k, 0), reverse=True)
ordered_counts = [intervention_counts.get(k, 0) for k in ordered]

# Top-5 use the 5-colour palette; remaining 3 use extension greys
iv_palette = FIVE_COLOURS + EXT_COLOURS
bar_colours = [iv_palette[i] for i in range(len(ordered))]

ypos = np.arange(len(ordered))
axD.barh(ypos, ordered_counts, color=bar_colours,
         edgecolor="white", linewidth=0.5, height=0.65)
axD.set_yticks(ypos)
axD.set_yticklabels([k.replace("_", " ") for k in ordered], fontsize=8)
axD.invert_yaxis()
axD.set_xlabel("Papers")
axD.set_title("QS-targeting intervention classes", loc="left")
panel_label(axD, "D")

for i, c in enumerate(ordered_counts):
    axD.text(c + max(ordered_counts) * 0.012, i, str(c),
             va="center", fontsize=8, fontweight="bold")

axD.set_xlim(0, max(ordered_counts) * 1.15)

# --------------------------------------------------------------------------------------
# Suptitle + layout + save
# --------------------------------------------------------------------------------------
fig.suptitle(
    "Figure 2. Literature landscape of QS in A. baumannii (2003-2025)",
    y=0.995,
)
fig.tight_layout(rect=(0, 0, 1, 0.965))

OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=600)
fig.savefig(OUT_SVG)
plt.close(fig)

print(f"[panelA] year span {year_min}-{year_max}, sum={int(year_counts.sum())}")
print(f"[panelB] study_type sum={int(study_counts.sum())}")
print(f"[panelC] heatmap shape={heat.shape}; rows sorted desc")
print(f"[panelD] interventions={dict(zip(ordered, ordered_counts))}")
print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
