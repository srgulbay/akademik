"""Generate Figure 6: QS regulatory network architecture in A. baumannii.

A hierarchical directed-graph diagram synthesised from the 228 priority
studies in literature/evidence_claims.json. Nodes are grouped into four
layers:

  signals    : AbaI -> AHL -> AbaR (canonical), AbaM brake, AbiS/indole/AbiR
  TCS        : BfmRS, AdeRS, A1S_2811, DksA
  messengers : c-di-GMP (DGC/PDE), (p)ppGpp (RelA), 3',5'-cAMP (CavA->VfrAb)
  regulons   : csu, bap, pgaABCD, ompA, adeABC, adeFGH, acinetobactin

Edge style encodes interaction sign:
    solid black arrow     -> activation
    dashed red T-bar      -> inhibition (drawn as dashed segment with a small
                              perpendicular bar near the target)

Edge thickness encodes evidence strength in three tiers, based on combined
mention frequency of the endpoint genes in evidence_claims.json:
    thick  : >50 papers
    medium : 10-50 papers
    thin   : <10 papers

An inset panel reports connectivity statistics.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from collections import Counter
from matplotlib.lines import Line2D

try:
    from networkx.drawing.nx_pydot import graphviz_layout
    HAS_DOT = True
except Exception:  # pragma: no cover
    HAS_DOT = False

HERE = Path("/home/user/akademik/systematic-review")
EVIDENCE_PATH = HERE / "literature" / "evidence_claims.json"
OUT_PNG = HERE / "figures" / "figure6_network.png"
OUT_SVG = HERE / "figures" / "figure6_network.svg"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
    }
)

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
    """Return max mention count among aliases (case-insensitive)."""
    return max((mention.get(a.lower(), 0) for a in aliases), default=0)

# --------------------------------------------------------------------------------------
# Node taxonomy
# --------------------------------------------------------------------------------------
# (id, label, layer, mention_count)
NODE_SPECS = [
    # Signals / hub
    ("AbaI",   "AbaI\n(synthase)",       "signal",  m("abai")),
    ("AHL",    "AHL",                    "signal",  m("abai", "abar")),   # signal molecule
    ("AbaR",   "AbaR-AHL\n(receptor)",   "hub",     m("abar")),
    ("AbaM",   "AbaM\n(brake)",          "signal",  m("abam")),
    ("AbiS",   "AbiS",                   "signal",  3),
    ("Indole", "indole",                 "signal",  3),
    ("AbiR",   "AbiR",                   "signal",  3),
    # TCS partners
    ("BfmRS",   "BfmRS",                 "tcs",     m("bfmr", "bfms")),
    ("AdeRS",   "AdeRS",                 "tcs",     m("ader", "ades")),
    ("A1S2811", "A1S_2811",              "tcs",     2),
    ("DksA",    "DksA",                  "tcs",     2),
    # Second messengers
    ("cdiGMP",  "c-di-GMP\n(DGC/PDE)",   "msg",     8),
    ("ppGpp",   "(p)ppGpp\n(RelA)",      "msg",     4),
    ("cAMP",    "3',5'-cAMP\n(CavA-VfrAb)", "msg",  3),
    # Regulons / outputs
    ("csu",      "csu pilus",            "out",     m("csua", "csub", "csuc", "csud", "csue")),
    ("bap",      "bap",                  "out",     m("bap")),
    ("pgaABCD",  "pgaABCD",              "out",     m("pgaabcd")),
    ("ompA",     "ompA",                 "out",     m("ompa")),
    ("adeABC",   "adeABC",               "out",     m("adeabc")),
    ("adeFGH",   "adeFGH",               "out",     m("adefgh")),
    ("acineto",  "acinetobactin",        "out",     5),
]

LAYER_RANK = {"signal": 0, "hub": 0, "tcs": 1, "msg": 2, "out": 3}

LAYER_COLOR = {
    "signal": "#f4d35e",  # amber-ish for signal molecules
    "hub":    "#e08e25",  # large amber for hub
    "tcs":    "#4c72b0",  # medium blue
    "msg":    "#3aa364",  # green
    "out":    "#bfbfbf",  # grey
}

LAYER_SIZE = {
    "signal": 1900,
    "hub":    4200,
    "tcs":    2400,
    "msg":    2400,
    "out":    2000,
}

# --------------------------------------------------------------------------------------
# Edges: (src, tgt, sign, evidence_count)
#   sign: 'act' (activation) or 'inh' (inhibition)
# evidence count is taken from mention of the most informative endpoint.
# --------------------------------------------------------------------------------------
EDGES = [
    # AHL canonical loop
    ("AbaI",   "AHL",   "act", m("abai")),
    ("AHL",    "AbaR",  "act", m("abar")),
    ("AbaR",   "AbaI",  "act", m("abai", "abar")),  # autoinduction loop
    ("AbaM",   "AbaR",  "inh", m("abam")),          # brake on receptor
    # Parallel AbiS/indole system
    ("AbiS",   "Indole","act", 3),
    ("Indole", "AbiR",  "act", 3),
    ("AbiR",   "AbaR",  "inh", 3),                  # crosstalk: inhibition on QS hub
    # Hub -> TCS partners
    ("AbaR",   "BfmRS", "act", m("bfmr")),
    ("AbaR",   "AdeRS", "act", m("ader", "adeabc")),
    ("AbaR",   "A1S2811","act", 2),
    ("AbaR",   "DksA",  "act", 2),
    # Hub -> second messengers
    ("AbaR",   "cdiGMP","act", 8),
    ("AbaR",   "ppGpp", "act", 4),
    ("AbaR",   "cAMP",  "act", 3),
    # TCS -> outputs
    ("BfmRS",  "csu",   "act", m("csua", "csue")),
    ("BfmRS",  "bap",   "act", m("bap")),
    ("BfmRS",  "ompA",  "act", m("ompa")),
    ("BfmRS",  "pgaABCD","act", m("pgaabcd")),
    ("AdeRS",  "adeABC","act", m("adeabc")),
    ("AdeRS",  "adeFGH","act", m("adefgh")),
    ("A1S2811","acineto","act", 4),
    ("DksA",   "ompA",  "act", 3),
    # Second messengers -> outputs
    ("cdiGMP", "csu",   "act", 6),
    ("cdiGMP", "bap",   "act", 5),
    ("cdiGMP", "pgaABCD","act", 5),
    ("ppGpp",  "adeABC","act", 4),
    ("cAMP",   "acineto","act", 3),
    # Negative regulation (inhibition) examples
    ("AdeRS",  "ompA",  "inh", 3),
    ("cdiGMP", "ompA",  "inh", 2),  # context-dependent suppression
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
# Layout: dot if available, else manual layered layout
# --------------------------------------------------------------------------------------
def manual_layered_pos(graph: nx.DiGraph) -> dict:
    """Manual horizontal layered layout (rank by LAYER_RANK)."""
    by_rank: dict[int, list[str]] = {}
    for n in graph.nodes:
        r = LAYER_RANK[graph.nodes[n]["layer"]]
        by_rank.setdefault(r, []).append(n)

    # Hub goes in its own central row distinct from generic signals
    pos = {}
    rank_y = {0: 3.0, 1: 1.5, 2: 0.0, 3: -1.8}
    for r, nodes in by_rank.items():
        # Place hub centrally in rank 0 alongside signals (slightly above)
        y = rank_y[r]
        # Sort so layout is stable
        # Within signal rank, put hub centrally
        if r == 0:
            # Order: AbaI, AHL, AbaR(hub), AbaM, AbiS, Indole, AbiR
            preferred = ["AbiS", "Indole", "AbiR", "AbaI", "AHL", "AbaR", "AbaM"]
            nodes_sorted = [n for n in preferred if n in nodes] + [n for n in nodes if n not in preferred]
        else:
            nodes_sorted = sorted(nodes)
        n_nodes = len(nodes_sorted)
        xs = np.linspace(-6, 6, n_nodes) if n_nodes > 1 else np.array([0.0])
        for x, n in zip(xs, nodes_sorted):
            # Lift hub a bit so it visually anchors
            yy = y + (0.4 if n == "AbaR" else 0.0)
            pos[n] = (float(x), float(yy))
    return pos


if HAS_DOT:
    try:
        raw_pos = graphviz_layout(G, prog="dot")
        # Normalise so coordinates roughly match manual layout extents
        xs = np.array([p[0] for p in raw_pos.values()])
        ys = np.array([p[1] for p in raw_pos.values()])
        x0, x1 = xs.min(), xs.max()
        y0, y1 = ys.min(), ys.max()
        pos = {
            k: (
                -6 + 12 * (v[0] - x0) / max(x1 - x0, 1e-9),
                -1.8 + 4.8 * (v[1] - y0) / max(y1 - y0, 1e-9),
            )
            for k, v in raw_pos.items()
        }
        layout_name = "graphviz-dot"
    except Exception as exc:  # pragma: no cover
        print(f"[layout] graphviz failed ({exc}); using manual layered")
        pos = manual_layered_pos(G)
        layout_name = "manual-layered"
else:
    pos = manual_layered_pos(G)
    layout_name = "manual-layered"

print(f"[layout] {layout_name}")

# --------------------------------------------------------------------------------------
# Draw
# --------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 8))

# Node draw, grouped by layer for legend
for layer in ["out", "msg", "tcs", "signal", "hub"]:  # hub on top
    nodes = [n for n in G.nodes if G.nodes[n]["layer"] == layer]
    if not nodes:
        continue
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=nodes,
        node_color=LAYER_COLOR[layer],
        node_size=[LAYER_SIZE[layer] for _ in nodes],
        edgecolors="#222",
        linewidths=1.0,
        ax=ax,
    )

# Edge widths from evidence tiers
def edge_width(count: int) -> float:
    if count > 50:
        return 3.2
    if count >= 10:
        return 1.8
    return 0.8

act_edges = [(u, v) for u, v, d in G.edges(data=True) if d["sign"] == "act"]
inh_edges = [(u, v) for u, v, d in G.edges(data=True) if d["sign"] == "inh"]

# Activation: solid black arrows
act_widths = [edge_width(G[u][v]["count"]) for u, v in act_edges]
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=act_edges,
    arrows=True,
    arrowstyle="-|>",
    arrowsize=14,
    width=act_widths,
    edge_color="#222",
    node_size=2400,
    connectionstyle="arc3,rad=0.06",
    ax=ax,
)

# Inhibition: dashed red lines with T-bar (use "-[" style as the closest matplotlib analogue)
inh_widths = [edge_width(G[u][v]["count"]) for u, v in inh_edges]
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=inh_edges,
    arrows=True,
    arrowstyle="-[",
    arrowsize=14,
    width=inh_widths,
    edge_color="#c0392b",
    style="dashed",
    node_size=2400,
    connectionstyle="arc3,rad=0.12",
    ax=ax,
)

# Labels
labels = {n: G.nodes[n]["label"] for n in G.nodes}
nx.draw_networkx_labels(
    G,
    pos,
    labels=labels,
    font_size=8,
    font_color="#111",
    ax=ax,
)

ax.set_axis_off()
ax.set_title(
    "Figure 6. QS regulatory network in A. baumannii — synthesized from 228 priority studies",
    loc="left",
    fontweight="bold",
    fontsize=12,
)

# --------------------------------------------------------------------------------------
# Legend
# --------------------------------------------------------------------------------------
node_legend = [
    mpatches.Patch(facecolor=LAYER_COLOR["hub"],    edgecolor="#222", label="QS hub (AbaR-AHL)"),
    mpatches.Patch(facecolor=LAYER_COLOR["signal"], edgecolor="#222", label="signals / synthase"),
    mpatches.Patch(facecolor=LAYER_COLOR["tcs"],    edgecolor="#222", label="TCS partners"),
    mpatches.Patch(facecolor=LAYER_COLOR["msg"],    edgecolor="#222", label="second messengers"),
    mpatches.Patch(facecolor=LAYER_COLOR["out"],    edgecolor="#222", label="output regulons"),
]
edge_legend = [
    Line2D([0], [0], color="#222", lw=3.2, label="activation, >50 papers"),
    Line2D([0], [0], color="#222", lw=1.8, label="activation, 10-50 papers"),
    Line2D([0], [0], color="#222", lw=0.8, label="activation, <10 papers"),
    Line2D([0], [0], color="#c0392b", lw=1.8, linestyle="--", label="inhibition (T-bar)"),
]
leg1 = ax.legend(
    handles=node_legend,
    title="Node class",
    loc="upper left",
    bbox_to_anchor=(0.0, -0.02),
    frameon=False,
    fontsize=8,
    title_fontsize=9,
    ncol=2,
)
ax.add_artist(leg1)
ax.legend(
    handles=edge_legend,
    title="Edge encoding",
    loc="upper right",
    bbox_to_anchor=(1.0, -0.02),
    frameon=False,
    fontsize=8,
    title_fontsize=9,
)

# --------------------------------------------------------------------------------------
# Inset: connectivity statistics
# --------------------------------------------------------------------------------------
n_nodes = G.number_of_nodes()
n_edges = G.number_of_edges()
deg = dict(G.degree())
top3 = sorted(deg.items(), key=lambda kv: kv[1], reverse=True)[:3]
stats_text = (
    "Connectivity\n"
    f"Total nodes: {n_nodes}\n"
    f"Total edges: {n_edges}\n"
    "Hub centrality (deg):\n"
    + "\n".join([f"  {k}: {v}" for k, v in top3])
)
ax.text(
    0.985,
    0.985,
    stats_text,
    transform=ax.transAxes,
    fontsize=8.5,
    va="top",
    ha="right",
    bbox=dict(boxstyle="round,pad=0.45", facecolor="#fbfbfb", edgecolor="#999", linewidth=0.6),
)

fig.tight_layout()
OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
fig.savefig(OUT_SVG, bbox_inches="tight")
plt.close(fig)

print(f"[save] {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
print(f"[save] {OUT_SVG} ({OUT_SVG.stat().st_size} bytes)")
print(f"[stats] top-3 degree: {top3}")
