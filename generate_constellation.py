"""
GitHub-safe animated constellation SVG.
Uses SMIL <animate> (not CSS @keyframes) and feMerge glow filters (not feComposite).
Both are fully permitted by GitHub's SVG sanitizer.
"""
import math, random

W, H = 860, 480
random.seed(42)

constellations = [
    {
        "name": "LANGUAGES", "color": "#a78bfa", "glow": "167,139,250",
        "nodes": [
            {"x": 0.14, "y": 0.20, "label": "Python",    "r": 7.5},
            {"x": 0.07, "y": 0.42, "label": "R",          "r": 6.0},
            {"x": 0.22, "y": 0.38, "label": "SQL",        "r": 6.5},
            {"x": 0.12, "y": 0.60, "label": "Statistics", "r": 5.5},
        ],
        "edges": [[0,1],[0,2],[1,3],[2,3]]
    },
    {
        "name": "ML &amp; STATS", "color": "#38bdf8", "glow": "56,189,248",
        "nodes": [
            {"x": 0.42, "y": 0.13, "label": "scikit-learn",    "r": 7.0},
            {"x": 0.33, "y": 0.30, "label": "Machine Learning","r": 8.0},
            {"x": 0.50, "y": 0.27, "label": "Feature Eng.",    "r": 6.0},
            {"x": 0.37, "y": 0.48, "label": "Model Interpret.","r": 6.5},
            {"x": 0.54, "y": 0.44, "label": "Calibration",     "r": 5.0},
        ],
        "edges": [[0,1],[0,2],[1,2],[1,3],[2,4],[3,4]]
    },
    {
        "name": "VISUALIZATION", "color": "#34d399", "glow": "52,211,153",
        "nodes": [
            {"x": 0.75, "y": 0.16, "label": "Power BI",         "r": 6.5},
            {"x": 0.88, "y": 0.28, "label": "Tableau",          "r": 6.5},
            {"x": 0.82, "y": 0.44, "label": "Data Storytelling","r": 6.0},
            {"x": 0.70, "y": 0.34, "label": "Dashboard Design", "r": 5.5},
        ],
        "edges": [[0,1],[0,3],[1,2],[2,3]]
    },
    {
        "name": "DATA ENG.", "color": "#fb923c", "glow": "251,146,60",
        "nodes": [
            {"x": 0.28, "y": 0.70, "label": "Pandas",      "r": 6.5},
            {"x": 0.17, "y": 0.80, "label": "NumPy",       "r": 5.5},
            {"x": 0.36, "y": 0.82, "label": "Data Cleaning","r": 5.5},
            {"x": 0.11, "y": 0.68, "label": "EDA",         "r": 5.5},
        ],
        "edges": [[0,1],[0,2],[0,3],[1,3]]
    },
    {
        "name": "ANALYTICS", "color": "#f472b6", "glow": "244,114,182",
        "nodes": [
            {"x": 0.62, "y": 0.63, "label": "Streamlit",       "r": 7.0},
            {"x": 0.74, "y": 0.74, "label": "Interpretable AI","r": 6.5},
            {"x": 0.59, "y": 0.82, "label": "Decision Support","r": 6.0},
            {"x": 0.84, "y": 0.62, "label": "Analytics Eng.",  "r": 5.5},
        ],
        "edges": [[0,1],[0,2],[1,3],[2,3]]
    },
]

# flatten
all_nodes = []
for c in constellations:
    for n in c["nodes"]:
        all_nodes.append({**n, "px": n["x"]*W, "py": n["y"]*H,
                          "color": c["color"], "glow": c["glow"]})

all_edges = []
offset = 0
for c in constellations:
    for a_, b_ in c["edges"]:
        na = all_nodes[offset+a_]
        nb = all_nodes[offset+b_]
        length = math.sqrt((nb["px"]-na["px"])**2 + (nb["py"]-na["py"])**2)
        all_edges.append({"x1":na["px"],"y1":na["py"],"x2":nb["px"],"y2":nb["py"],
                           "color":c["color"],"length":length})
    offset += len(c["nodes"])

stars = []
for i in range(200):
    random.seed(i*7+3)
    stars.append({
        "x": round(random.random()*W,1), "y": round(random.random()*H,1),
        "r": round(random.random()*1.0+0.3,1),
        "dur": round(random.random()*3+2,1),
        "delay": round(random.random()*5,1)
    })

group_label_positions = [
    (0.13,0.09),(0.40,0.04),(0.77,0.07),(0.17,0.92),(0.68,0.54)
]

L = []
def a(s): L.append(s)

a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')

# ── DEFS ──────────────────────────────────────────────────────────
a('<defs>')
# bg gradient
a('''<radialGradient id="bgG" cx="50%" cy="50%" r="70%">
  <stop offset="0%"   stop-color="#0d0820"/>
  <stop offset="100%" stop-color="#05040f"/>
</radialGradient>''')
# nebulae
a('''<radialGradient id="nb1" cx="35%" cy="35%" r="35%">
  <stop offset="0%"   stop-color="#5028a0" stop-opacity="0.13"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>
<radialGradient id="nb2" cx="72%" cy="65%" r="28%">
  <stop offset="0%"   stop-color="#1e5078" stop-opacity="0.10"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>
<radialGradient id="nb3" cx="18%" cy="76%" r="22%">
  <stop offset="0%"   stop-color="#7c3a6e" stop-opacity="0.09"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>''')

# glow filters — feMerge ONLY (no feComposite, fully GitHub-safe)
seen = set()
for c in constellations:
    gid = c["color"].replace("#","")
    if gid not in seen:
        seen.add(gid)
        a(f'<filter id="gS_{gid}" x="-60%" y="-60%" width="220%" height="220%">')
        a(f'  <feGaussianBlur in="SourceGraphic" stdDeviation="3.5" result="blur"/>')
        a(f'  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
        a(f'</filter>')
        a(f'<filter id="gL_{gid}" x="-100%" y="-100%" width="300%" height="300%">')
        a(f'  <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="blur"/>')
        a(f'  <feMerge><feMergeNode in="blur"/><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
        a(f'</filter>')

a('</defs>')

# ── BACKGROUND ────────────────────────────────────────────────────
a(f'<rect width="{W}" height="{H}" fill="url(#bgG)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#nb1)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#nb2)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#nb3)"/>')

# ── STARS — SMIL animate ──────────────────────────────────────────
a('<g id="stars">')
for s in stars:
    a(f'<circle cx="{s["x"]}" cy="{s["y"]}" r="{s["r"]}" fill="rgba(210,200,255,0.7)">')
    a(f'  <animate attributeName="opacity" values="0.1;0.75;0.1" dur="{s["dur"]}s" begin="{s["delay"]}s" repeatCount="indefinite"/>')
    a(f'</circle>')
a('</g>')

# ── EDGES — stroke-dashoffset draw-on ────────────────────────────
a('<g id="edges">')
for i, e in enumerate(all_edges):
    begin = 0.3 + i*0.11
    a(f'<line x1="{e["x1"]:.1f}" y1="{e["y1"]:.1f}" x2="{e["x2"]:.1f}" y2="{e["y2"]:.1f}"'
      f' stroke="{e["color"]}" stroke-width="0.85" stroke-opacity="0.38"'
      f' stroke-dasharray="{e["length"]:.1f}" stroke-dashoffset="{e["length"]:.1f}">')
    a(f'  <animate attributeName="stroke-dashoffset" from="{e["length"]:.1f}" to="0"'
      f' begin="{begin:.2f}s" dur="1.1s" fill="freeze"/>')
    a(f'</line>')
a('</g>')

# ── NODES — SMIL pulse ────────────────────────────────────────────
a('<g id="nodes">')
offset2 = 0
for ci, c in enumerate(constellations):
    gid = c["color"].replace("#","")
    for ni, n in enumerate(c["nodes"]):
        idx = offset2 + ni
        px, py, r = n["x"]*W, n["y"]*H, n["r"]
        appear = 0.1 + idx*0.13
        dur = 2.6 + (idx%5)*0.35

        # outer glow halo (large, soft)
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r*2.6:.1f}"'
          f' fill="rgba({c["glow"]},0.18)" filter="url(#gL_{gid})" opacity="0">')
        a(f'  <animate attributeName="opacity" from="0" to="1"'
          f' begin="{appear:.2f}s" dur="0.6s" fill="freeze"/>')
        a(f'  <animate attributeName="opacity" values="0.5;1;0.5" dur="{dur}s"'
          f' begin="{appear+0.6:.2f}s" repeatCount="indefinite"/>')
        a(f'</circle>')

        # core star with pulse
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{c["color"]}"'
          f' filter="url(#gS_{gid})" opacity="0">')
        a(f'  <animate attributeName="opacity" from="0" to="0.9"'
          f' begin="{appear:.2f}s" dur="0.5s" fill="freeze"/>')
        a(f'  <animate attributeName="r" values="{r};{r*1.17:.1f};{r}" dur="{dur}s"'
          f' begin="{appear+0.5:.2f}s" repeatCount="indefinite"/>')
        a(f'  <animate attributeName="opacity" values="0.85;1;0.85" dur="{dur}s"'
          f' begin="{appear+0.5:.2f}s" repeatCount="indefinite"/>')
        a(f'</circle>')
    offset2 += len(c["nodes"])
a('</g>')

# ── LABELS — SMIL fadeIn + gentle float ──────────────────────────
a('<g id="labels" font-family="\'Courier New\', Courier, monospace">')
offset3 = 0
for ci, c in enumerate(constellations):
    for ni, n in enumerate(c["nodes"]):
        idx = offset3 + ni
        px, py, r = n["x"]*W, n["y"]*H, n["r"]
        appear = 0.9 + idx*0.13
        lx = px + r + 8
        ly = py + 4
        a(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10.5" fill="{c["color"]}"'
          f' font-weight="500" letter-spacing="0.04em" opacity="0">')
        a(f'  <animate attributeName="opacity" from="0" to="0.88"'
          f' begin="{appear:.2f}s" dur="0.6s" fill="freeze"/>')
        a(f'  {n["label"]}')
        a(f'</text>')
    offset3 += len(c["nodes"])
a('</g>')

# ── GROUP CATEGORY LABELS ─────────────────────────────────────────
a('<g id="group-labels" font-family="\'Courier New\', Courier, monospace">')
for ci, c in enumerate(constellations):
    gx, gy = group_label_positions[ci]
    px, py = gx*W, gy*H
    appear = 1.4 + ci*0.2
    a(f'<text x="{px:.1f}" y="{py:.1f}" font-size="8.5" fill="{c["color"]}"'
      f' font-weight="700" letter-spacing="0.18em" text-anchor="middle" opacity="0">')
    a(f'  <animate attributeName="opacity" from="0" to="0.7"'
      f' begin="{appear:.2f}s" dur="0.7s" fill="freeze"/>')
    a(f'  {c["name"]}')
    a(f'</text>')
a('</g>')

# ── LEGEND ────────────────────────────────────────────────────────
a('<g id="legend" font-family="\'Courier New\', Courier, monospace">')
for i, c in enumerate(constellations):
    lx = 82 + i*160
    ly = H - 18
    a(f'<circle cx="{lx}" cy="{ly}" r="3.5" fill="{c["color"]}" opacity="0.82"/>')
    a(f'<text x="{lx+9}" y="{ly+4}" font-size="9" fill="{c["color"]}"'
      f' letter-spacing="0.08em" opacity="0.72">{c["name"]}</text>')
a('</g>')

# ── BORDER ────────────────────────────────────────────────────────
a(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" ry="10"'
  f' fill="none" stroke="rgba(140,100,255,0.22)" stroke-width="1"/>')

a('</svg>')

svg = "\n".join(L)

# Sanity check — must not contain any blocked elements
blocked = ["feComposite","<style","@keyframes","javascript","<script"]
for b in blocked:
    if b in svg:
        print(f"WARNING: found blocked element: {b}")

with open("skills-constellation.svg", "w") as f:
    f.write(svg)

print(f"Done: {len(svg):,} bytes, {len(L)} lines")
print("Blocked element check: CLEAN" if not any(b in svg for b in blocked) else "HAS ISSUES")
