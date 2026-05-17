"""Generate Figure 6: Quorum-sensing regulatory network in A. baumannii.

Updates over v1:
- Node sizes proportional to degree centrality (instead of layer-uniform).
- Colour by category:
    QS regulators (orange), TCS partners (blue), second messengers (green),
    output regulons (gray).
- Edge weights in 3 tiers (thin / medium / thick) by mention frequency.
- Inhibition edges: red, thicker T-bar, dashed.
- Stats inset table: top-5 hubs by degree.
- Title: "Quorum-sensing regulatory network in A. baumannii".
- Manual layered layout for clarity (instead of graphviz dot which overlapped).
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.lines import Line2D

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, PALETTE

apply_style()

HERE = Path("/home/user/akademik/systematic-review")
EVIDENCE_PATH = HERE / "literature" / "evidence_claims.json"
OUT_PNG = HERE / "figures" / "figure6_network.png"
OUT_SVG = HERE / "figures" / "figure6_network.svg"

# --------------------------------------------------------------------------------------
# Tally gene mentions for edge weights
# --------------------------------------------------------------------------------------
with open(EVIDENCE_PATH) as f:
    evidence = json.load(f)
print(f"[load] {len(evidence)} priority records")

mention = Counter()
for rec in evidence.values():
    for g in rec.get("genes_mentioned", []) or []:
        mention[g.lower()] += 1


def m(*aliases: str) -> int:
    return max((mention.get(a.lower(), 0) for a in aliases), default=0)


# --------------------------------------------------------------------------------------
# Node taxonomy
# --------------------------------------------------------------------------------------
NODE_SPECS = [
    ("AbaI",    "AbaI",                  "signal", m("abai")),
    ("AHL",     "AHL",                   "signal", m("abai", "abar")),
    ("AbaR",    "AbaR",                  "hub",    m("abar")),
    ("AbaM",    "AbaM",                  "signal", m("abam")),
    ("AbiS",    "AbiS",                  "signal", 3),
    ("Indole",  "indole",                "signal", 3),
    ("AbiR",    "AbiR",                  "signal", 3),
    ("BfmRS",   "BfmRS",                 "tcs",    m("bfmr", "bfms")),
    ("AdeRS",   "AdeRS",                 "tcs",    m("ader", "ades")),
    ("A1S2811", "A1S_2811",              "tcs",    2),
    ("DksA",    "DksA",                  "tcs",    2),
    ("cdiGMP",  "c-di-GMP",              "msg",    8),
    ("ppGpp",   "(p)ppGpp",              "msg",    4),
    ("cAMP",    "3',5'-cAMP",            "msg",    3),
    ("csu",     "csu",                   "out",    m("csua", "csub", "csuc", "csud", "csue")),
    ("bap",     "bap",                   "out",    m("bap")),
    ("pgaABCD", "pgaABCD",               "out",    m("pgaabcd")),
    ("ompA",    "ompA",                  "out",    m("ompa")),
    ("adeABC",  "adeABC",                "out",    m("adeabc")),
    ("adeFGH",  "adeFGH",                "out",    m("adefgh")),
    ("acineto", "acinetobactin",         "out",    5),
]

# Category palette
LAYER_COLOR = {
    "signal": PALETTE["amber"],      # QS regulators (orange)
    "hub":    "#b8551c",              # darker orange for the AbaR hub
    "tcs":    PALETTE["blue"],        # TCS partners
    "msg":    "#3a8a4d",              # second messengers
    "out":    "#bdbdbd",              # output regulons
}

EDGES = [
    ("AbaI",   "AHL",   "act", m("abai")),
    ("AHL",    "AbaR",  "act", m("abar")),
    ("AbaR",   "AbaI",  "act", m("abai", "abar")),
    ("AbaM",   "AbaR",  "inh", m("abam")),
    ("AbiS",   "Indole","act", 3),
    ("Indole", "AbiR",  "act", 3),
    ("AbiR",   "AbaR",  "inh", 3),
    ("AbaR",   "BfmRS", "act", m("bfmr")),
    ("AbaR",   "AdeRS", "act", m("ader", "adeabc")),
    ("AbaR",   "A1S2811","act", 2),
    ("AbaR",   "DksA",  "act", 2),
    ("AbaR",   "cdiGMP","act", 8),
    ("AbaR",   "ppGpp", "act", 4),
    ("AbaR",   "cAMP",  "act", 3),
    ("BfmRS",  "csu",   "act", m("csua", "csue")),
    ("BfmRS",  "bap",   "act", m("bap")),
    ("BfmRS",  "ompA",  "act", m("ompa")),
    ("BfmRS",  "pgaABCD","act", m("pgaabcd")),
    ("AdeRS",  "adeABC","act", m("adeabc")),
    ("AdeRS",  "adeFGH","act", m("adefgh")),
    ("A1S2811","acineto","act", 4),
    ("DksA",   "ompA",  "act", 3),
    ("cdiGMP", "csu",   "act", 6),
    ("cdiGMP", "bap",   "act", 5),
    ("cdiGMP", "pgaABCD","act", 5),
    ("ppGpp",  "adeABC","act", 4),
    ("cAMP",   "acineto","act", 3),
    ("AdeRS",  "ompA",  "inh", 3),
    ("cdiGMP", "ompA",  "inh", 2),
]

# --------------------------------------------------------------------------------------
# Build graph
# --------------------------------------------------------------------------------------
G = nx.DiGraph()
for nid, label, layer, count in NODE_SPECS:
    G.add_node(nid, label=label, layer=layer, count=count)
for src, tgt, sign, count in EDGES:
    G.add_edge(src, tgt, sign=sign, count=count)
print(f"[graph] nodes={G.number_of_nodes()}, edges={G.number_of_edges()}")

# --------------------------------------------------------------------------------------
# Manual layered layout (clearer than graphviz dot for this fixed topology)
# --------------------------------------------------------------------------------------
LAYER_Y = {"signal": 3.0, "hub": 2.0, "tcs": 0.8, "msg": 0.0, "out": -1.6}

def manual_pos(G):
    by_layer: dict[str, list[str]] = {}
    for n in G.nodes:
        by_layer.setdefault(G.nodes[n]["layer"], []).append(n)
    pos = {}
    # Custom orders to minimise crossings
    order_signal = ["AbiS", "Indole", "AbiR", "AbaI", "AHL", "AbaM"]
    order_tcs    = ["BfmRS", "AdeRS", "DksA", "A1S2811"]
    order_msg    = ["cdiGMP", "ppGpp", "cAMP"]
    order_out    = ["csu", "bap", "pgaABCD", "ompA", "adeABC", "adeFGH", "acineto"]

    def place(nodes, y, xspan=12.0):
        n = len(nodes)
        if n == 1:
            xs = [0.0]
        else:
            xs = list(np.linspace(-xspan/2, xspan/2, n))
        for x, name in zip(xs, nodes):
            pos[name] = (float(x), float(y))

    # signals (excluding hub which we'll place centrally)
    signals_ordered = [n for n in order_signal if n in by_layer.get("signal", [])]
    place(signals_ordered, LAYER_Y["signal"], xspan=10.0)
    # Hub (AbaR)
    pos["AbaR"] = (0.0, LAYER_Y["hub"])
    # TCS
    tcs_ordered = [n for n in order_tcs if n in by_layer.get("tcs", [])]
    place(tcs_ordered, LAYER_Y["tcs"], xspan=6.0)
    # Messengers (right of TCS)
    msg_ordered = [n for n in order_msg if n in by_layer.get("msg", [])]
    # Offset to the right so they don't sit directly under TCS
    for i, name in enumerate(msg_ordered):
        pos[name] = (3.5 + i * 1.7, LAYER_Y["msg"])
    # Shift TCS slightly left for symmetry
    for name in tcs_ordered:
        x, y = pos[name]
        pos[name] = (x - 2.5, y)
    # Outputs
    out_ordered = [n for n in order_out if n in by_layer.get("out", [])]
    place(out_ordered, LAYER_Y["out"], xspan=12.0)
    return pos


pos = manual_pos(G)

# --------------------------------------------------------------------------------------
# Node sizes proportional to (undirected) degree centrality
# --------------------------------------------------------------------------------------
deg = dict(G.degree())
deg_vals = np.array(list(deg.values()), dtype=float)
size_min, size_max = 900.0, 3200.0
deg_norm = (deg_vals - deg_vals.min()) / max(deg_vals.max() - deg_vals.min(), 1)
size_map = {n: float(size_min + (size_max - size_min) * deg_norm[i])
            for i, n in enumerate(deg.keys())}

# --------------------------------------------------------------------------------------
# Draw
# --------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 7.5))

# Nodes by layer (so legend handles work)
for layer in ["out", "msg", "tcs", "signal", "hub"]:
    nodes = [n for n in G.nodes if G.nodes[n]["layer"] == layer]
    if not nodes:
        continue
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=nodes,
        node_color=LAYER_COLOR[layer],
        node_size=[size_map[n] for n in nodes],
        edgecolors="#222",
        linewidths=0.9,
        ax=ax,
    )


def edge_width(count: int) -> float:
    if count > 50:
        return 3.0
    if count >= 10:
        return 1.6
    return 0.7


act_edges = [(u, v) for u, v, d in G.edges(data=True) if d["sign"] == "act"]
inh_edges = [(u, v) for u, v, d in G.edges(data=True) if d["sign"] == "inh"]

act_widths = [edge_width(G[u][v]["count"]) for u, v in act_edges]
nx.draw_networkx_edges(
    G, pos,
    edgelist=act_edges,
    arrows=True, arrowstyle="-|>", arrowsize=12,
    width=act_widths,
    edge_color="#222",
    node_size=[size_map[n] for n in G.nodes],
    connectionstyle="arc3,rad=0.06",
    ax=ax,
)

# Inhibition edges: red, dashed, thicker T-bar
inh_widths = [edge_width(G[u][v]["count"]) + 0.6 for u, v in inh_edges]
nx.draw_networkx_edges(
    G, pos,
    edgelist=inh_edges,
    arrows=True, arrowstyle="-[", arrowsize=16,
    width=inh_widths,
    edge_color=PALETTE["red"],
    style="dashed",
    node_size=[size_map[n] for n in G.nodes],
    connectionstyle="arc3,rad=0.18",
    ax=ax,
)

# Labels
labels = {n: G.nodes[n]["label"] for n in G.nodes}
nx.draw_networkx_labels(
    G, pos,
    labels=labels,
    font_size=8,
    font_color="#111",
    font_weight="bold",
    ax=ax,
)

ax.set_axis_off()
ax.set_title(
    "Figure 6. Quorum-sensing regulatory network in Acinetobacter baumannii",
    loc="left",
    fontsize=11, fontweight="bold",
)

# --------------------------------------------------------------------------------------
# Legends
# --------------------------------------------------------------------------------------
node_legend = [
    mpatches.Patch(facecolor=LAYER_COLOR["hub"],    edgecolor="#222", label="QS hub (AbaR-AHL)"),
    mpatches.Patch(facecolor=LAYER_COLOR["signal"], edgecolor="#222", label="QS regulators / signals"),
    mpatches.Patch(facecolor=LAYER_COLOR["tcs"],    edgecolor="#222", label="TCS partners"),
    mpatches.Patch(facecolor=LAYER_COLOR["msg"],    edgecolor="#222", label="Second messengers"),
    mpatches.Patch(facecolor=LAYER_COLOR["out"],    edgecolor="#222", label="Output regulons"),
]
edge_legend = [
    Line2D([0], [0], color="#222", lw=3.0, label="activation, >50 papers"),
    Line2D([0], [0], color="#222", lw=1.6, label="activation, 10-50 papers"),
    Line2D([0], [0], color="#222", lw=0.7, label="activation, <10 papers"),
    Line2D([0], [0], color=PALETTE["red"], lw=2.0, linestyle="--",
           label="inhibition (T-bar)"),
]
leg1 = ax.legend(
    handles=node_legend,
    title="Node class",
    loc="lower left",
    bbox_to_anchor=(0.0, -0.06),
    frameon=False, fontsize=7.5, title_fontsize=8.5,
    ncol=3,
)
ax.add_artist(leg1)
ax.legend(
    handles=edge_legend,
    title="Edge encoding",
    loc="lower right",
    bbox_to_anchor=(1.0, -0.06),
    frameon=False, fontsize=7.5, title_fontsize=8.5,
    ncol=2,
)

# --------------------------------------------------------------------------------------
# Stats inset: top-5 hubs by degree
# --------------------------------------------------------------------------------------
deg_sorted = sorted(deg.items(), key=lambda kv: kv[1], reverse=True)
top5 = deg_sorted[:5]
n_nodes = G.number_of_nodes()
n_edges = G.number_of_edges()

# Build a small text table
lines = [
    f"Total nodes: {n_nodes}",
    f"Total edges: {n_edges}",
    "",
    "Top-5 hubs by degree:",
]
for k, v in top5:
    label = G.nodes[k]["label"]
    lines.append(f"  {label}: deg {v}")

stats_text = "\n".join(lines)
ax.text(
    0.985, 0.985, stats_text,
    transform=ax.transAxes,
    fontsize=7.5,
    va="top", ha="right",
    family="monospace",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#fafafa",
              edgecolor="#999", linewidth=0.7),
)

fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=600)
fig.savefig(OUT_SVG)
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
print(f"[stats] top-5 degree: {top5}")
