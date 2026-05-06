"""
generate_constellation.py
─────────────────────────────────────────────────────────────────────
Generates skills-constellation.svg for Chetan's GitHub profile README.
Run locally or via GitHub Actions (.github/workflows/constellation.yml).

Pure stdlib — no dependencies required.
"""

import math
import random

W, H = 860, 480
random.seed(42)

# ── SKILL DATA ────────────────────────────────────────────────────────────
constellations = [
    {
        "name": "LANGUAGES", "color": "#a78bfa", "glow": "167,139,250",
        "nodes": [
            {"x": 0.14, "y": 0.20, "label": "Python",     "r": 7.5},
            {"x": 0.07, "y": 0.42, "label": "R",           "r": 6.0},
            {"x": 0.22, "y": 0.38, "label": "SQL",         "r": 6.5},
            {"x": 0.12, "y": 0.60, "label": "Statistics",  "r": 5.5},
        ],
        "edges": [[0,1],[0,2],[1,3],[2,3]]
    },
    {
        "name": "ML & STATS", "color": "#38bdf8", "glow": "56,189,248",
        "nodes": [
            {"x": 0.42, "y": 0.13, "label": "scikit-learn",      "r": 7.0},
            {"x": 0.33, "y": 0.30, "label": "Machine Learning",   "r": 8.0},
            {"x": 0.50, "y": 0.27, "label": "Feature Eng.",       "r": 6.0},
            {"x": 0.37, "y": 0.48, "label": "Model Interpret.",   "r": 6.5},
            {"x": 0.54, "y": 0.44, "label": "Calibration",        "r": 5.0},
        ],
        "edges": [[0,1],[0,2],[1,2],[1,3],[2,4],[3,4]]
    },
    {
        "name": "VISUALIZATION", "color": "#34d399", "glow": "52,211,153",
        "nodes": [
            {"x": 0.75, "y": 0.16, "label": "Power BI",        "r": 6.5},
            {"x": 0.88, "y": 0.28, "label": "Tableau",         "r": 6.5},
            {"x": 0.82, "y": 0.44, "label": "Data Storytelling","r": 6.0},
            {"x": 0.70, "y": 0.34, "label": "Dashboard Design","r": 5.5},
        ],
        "edges": [[0,1],[0,3],[1,2],[2,3]]
    },
    {
        "name": "DATA ENG.", "color": "#fb923c", "glow": "251,146,60",
        "nodes": [
            {"x": 0.28, "y": 0.70, "label": "Pandas",       "r": 6.5},
            {"x": 0.17, "y": 0.80, "label": "NumPy",        "r": 5.5},
            {"x": 0.36, "y": 0.82, "label": "Data Cleaning","r": 5.5},
            {"x": 0.11, "y": 0.68, "label": "EDA",          "r": 5.5},
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

# ── FLATTEN NODES ─────────────────────────────────────────────────────────
all_nodes = []
for c in constellations:
    for n in c["nodes"]:
        all_nodes.append({
            **n,
            "px": n["x"] * W,
            "py": n["y"] * H,
            "color": c["color"],
            "glow":  c["glow"],
        })

# ── FLATTEN EDGES ─────────────────────────────────────────────────────────
all_edges = []
offset = 0
for c in constellations:
    for a, b in c["edges"]:
        na = all_nodes[offset + a]
        nb = all_nodes[offset + b]
        length = math.sqrt((nb["px"]-na["px"])**2 + (nb["py"]-na["py"])**2)
        all_edges.append({
            "x1": na["px"], "y1": na["py"],
            "x2": nb["px"], "y2": nb["py"],
            "color": c["color"],
            "length": length,
        })
    offset += len(c["nodes"])

# ── BACKGROUND STARS ─────────────────────────────────────────────────────
stars = []
for i in range(220):
    random.seed(i * 7 + 3)
    stars.append({
        "x":     round(random.random() * W, 1),
        "y":     round(random.random() * H, 1),
        "r":     round(random.random() * 1.1 + 0.2, 1),
        "dur":   round(random.random() * 3 + 2, 1),
        "delay": round(random.random() * 4, 1),
    })

# ── GROUP LABEL POSITIONS ─────────────────────────────────────────────────
group_label_positions = [
    (0.13, 0.10), (0.40, 0.04), (0.77, 0.07),
    (0.17, 0.90), (0.68, 0.53),
]

# ── BUILD SVG ─────────────────────────────────────────────────────────────
lines = []
a = lines.append


def hex_to_rgb(hex_color):
    h = hex_color.lstrip("#")
    return f"{int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)}"


a(f'<svg xmlns="http://www.w3.org/2000/svg" '
  f'viewBox="0 0 {W} {H}" width="{W}" height="{H}">')

# ── DEFS ──────────────────────────────────────────────────────────────────
a('<defs>')

# Background gradient
a('''<radialGradient id="bgGrad" cx="50%" cy="50%" r="70%">
  <stop offset="0%"   stop-color="#0d0820"/>
  <stop offset="100%" stop-color="#05040f"/>
</radialGradient>''')

# Nebulae
a('''<radialGradient id="neb1" cx="35%" cy="35%" r="35%">
  <stop offset="0%"   stop-color="#5028a0" stop-opacity="0.12"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>
<radialGradient id="neb2" cx="72%" cy="65%" r="28%">
  <stop offset="0%"   stop-color="#1e5078" stop-opacity="0.10"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>
<radialGradient id="neb3" cx="20%" cy="75%" r="22%">
  <stop offset="0%"   stop-color="#7c3a6e" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#05040f" stop-opacity="0"/>
</radialGradient>''')

# Glow filters per constellation colour
seen = set()
for c in constellations:
    gid = c["color"].replace("#", "")
    if gid not in seen:
        seen.add(gid)
        a(f'<filter id="glow_{gid}" x="-80%" y="-80%" width="260%" height="260%">')
        a(f'  <feGaussianBlur stdDeviation="3.5" result="blur"/>')
        a(f'  <feComposite in="SourceGraphic" in2="blur" operator="over"/>')
        a(f'</filter>')
        a(f'<filter id="glowbig_{gid}" x="-120%" y="-120%" width="340%" height="340%">')
        a(f'  <feGaussianBlur stdDeviation="6" result="blur"/>')
        a(f'  <feComposite in="SourceGraphic" in2="blur" operator="over"/>')
        a(f'</filter>')

# CSS animations
a('<style>')
a('''
@keyframes twinkle   { 0%,100%{opacity:0.15} 50%{opacity:0.85} }
@keyframes nodeGlow  { 0%,100%{opacity:0.55} 50%{opacity:1}    }
@keyframes fadeIn    { from{opacity:0}        to{opacity:1}     }
@keyframes drawEdge  { from{stroke-dashoffset:1} to{stroke-dashoffset:0} }
@keyframes floatLbl  { 0%,100%{opacity:0.78;transform:translateY(0)}
                       50%{opacity:1;transform:translateY(-1px)} }
''')
# Per-node pulse keyframes
offset2 = 0
for ci, c in enumerate(constellations):
    for ni, n in enumerate(c["nodes"]):
        idx = offset2 + ni
        r = n["r"]
        a(f'@keyframes pn{idx}{{')
        a(f'  0%,100%{{r:{r}px;opacity:0.88}}')
        a(f'  50%{{r:{r*1.18:.1f}px;opacity:1}}')
        a(f'}}')
    offset2 += len(c["nodes"])
a('</style>')
a('</defs>')

# ── BACKGROUND LAYERS ─────────────────────────────────────────────────────
a(f'<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#neb1)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#neb2)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#neb3)"/>')

# ── BACKGROUND STARS ─────────────────────────────────────────────────────
a('<g id="stars">')
for s in stars:
    a(f'<circle cx="{s["x"]}" cy="{s["y"]}" r="{s["r"]}" '
      f'fill="rgba(210,200,255,0.8)" '
      f'style="animation:twinkle {s["dur"]}s {s["delay"]}s ease-in-out infinite;opacity:0.15"/>')
a('</g>')

# ── EDGES ─────────────────────────────────────────────────────────────────
a('<g id="edges">')
for i, e in enumerate(all_edges):
    delay = 0.4 + i * 0.12
    a(f'<line x1="{e["x1"]:.1f}" y1="{e["y1"]:.1f}" '
      f'x2="{e["x2"]:.1f}" y2="{e["y2"]:.1f}" '
      f'stroke="{e["color"]}" stroke-width="0.9" stroke-opacity="0.35" '
      f'stroke-dasharray="{e["length"]:.1f}" stroke-dashoffset="{e["length"]:.1f}" '
      f'style="animation:drawEdge 1.2s {delay:.2f}s ease forwards"/>')
a('</g>')

# ── NODES ─────────────────────────────────────────────────────────────────
a('<g id="nodes">')
offset3 = 0
for ci, c in enumerate(constellations):
    gid = c["color"].replace("#", "")
    for ni, n in enumerate(c["nodes"]):
        idx  = offset3 + ni
        px, py, r = n["x"]*W, n["y"]*H, n["r"]
        delay = 0.1 + idx * 0.13
        dur   = 2.8 + (idx % 5) * 0.4

        # outer glow halo
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r*2.8:.1f}" '
          f'fill="rgba({c["glow"]},0.15)" filter="url(#glowbig_{gid})" '
          f'style="animation:nodeGlow {dur}s {delay:.2f}s ease-in-out infinite;opacity:0"/>')
        # inner glow
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r*1.6:.1f}" '
          f'fill="rgba({c["glow"]},0.30)" filter="url(#glow_{gid})" '
          f'style="animation:nodeGlow {dur*0.8:.1f}s {delay:.2f}s ease-in-out infinite;opacity:0"/>')
        # core star
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" '
          f'fill="{c["color"]}" '
          f'style="animation:pn{idx} {dur}s {delay:.2f}s ease-in-out infinite;opacity:0"/>')
    offset3 += len(c["nodes"])
a('</g>')

# ── SKILL LABELS ──────────────────────────────────────────────────────────
a('<g id="labels" font-family="\'Courier New\', Courier, monospace">')
offset4 = 0
for ci, c in enumerate(constellations):
    for ni, n in enumerate(c["nodes"]):
        idx  = offset4 + ni
        px, py, r = n["x"]*W, n["y"]*H, n["r"]
        delay = 0.9 + idx * 0.13
        dur   = 3.2 + (idx % 4) * 0.5
        lx = px + r + 8
        ly = py + 4

        # FadeIn first (solid), then float animation layered on top
        a(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10.5" '
          f'fill="{c["color"]}" font-weight="500" letter-spacing="0.04em" opacity="0" '
          f'style="animation:fadeIn 0.6s {delay:.2f}s ease forwards, '
          f'floatLbl {dur}s {delay+0.6:.2f}s ease-in-out infinite">'
          f'{n["label"]}</text>')
    offset4 += len(c["nodes"])
a('</g>')

# ── CONSTELLATION GROUP LABELS ────────────────────────────────────────────
a('<g id="group-labels" font-family="\'Courier New\', Courier, monospace">')
for ci, c in enumerate(constellations):
    gx, gy = group_label_positions[ci]
    px, py = gx * W, gy * H
    delay  = 1.5 + ci * 0.2
    a(f'<text x="{px:.1f}" y="{py:.1f}" font-size="8.5" fill="{c["color"]}" '
      f'font-weight="700" letter-spacing="0.18em" text-anchor="middle" opacity="0" '
      f'style="animation:fadeIn 0.8s {delay:.2f}s ease forwards">{c["name"]}</text>')
a('</g>')

# ── LEGEND ────────────────────────────────────────────────────────────────
a('<g id="legend" font-family="\'Courier New\', Courier, monospace">')
for i, c in enumerate(constellations):
    lx = 80 + i * 160
    ly = H - 20
    a(f'<circle cx="{lx}" cy="{ly}" r="3.5" fill="{c["color"]}" opacity="0.85"/>')
    a(f'<text x="{lx+9}" y="{ly+4}" font-size="9" fill="{c["color"]}" '
      f'letter-spacing="0.08em" opacity="0.75">{c["name"]}</text>')
a('</g>')

# ── BORDER FRAME ──────────────────────────────────────────────────────────
a(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" ry="10" '
  f'fill="none" stroke="rgba(140,100,255,0.25)" stroke-width="1"/>')

a('</svg>')

# ── WRITE FILE ────────────────────────────────────────────────────────────
output = "\n".join(lines)
with open("skills-constellation.svg", "w", encoding="utf-8") as f:
    f.write(output)

print(f"✓ skills-constellation.svg written ({len(output):,} bytes, {len(lines)} elements)")
