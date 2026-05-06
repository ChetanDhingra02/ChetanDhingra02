import math
import random
import os

WIDTH = 1400
HEIGHT = 760
OUT = "assets/skill-constellation.svg"

os.makedirs("assets", exist_ok=True)
random.seed(42)

constellations = [
    {
        "name": "LANGUAGES",
        "color": "#a78bfa",
        "cx": 290,
        "cy": 250,
        "nodes": [
            ("Python", 210, 150, 9),
            ("R", 120, 250, 7),
            ("SQL", 330, 325, 8),
            ("Statistics", 230, 405, 7),
        ],
        "edges": [(0, 1), (0, 2), (1, 3), (2, 3)],
    },
    {
        "name": "ML &amp; STATS",
        "color": "#38bdf8",
        "cx": 710,
        "cy": 275,
        "nodes": [
            ("scikit-learn", 620, 115, 8),
            ("Machine Learning", 520, 260, 10),
            ("Feature Eng.", 770, 235, 8),
            ("Model Interpret.", 625, 410, 8),
            ("Calibration", 835, 390, 7),
        ],
        "edges": [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)],
    },
    {
        "name": "VISUALIZATION",
        "color": "#34d399",
        "cx": 1090,
        "cy": 255,
        "nodes": [
            ("Power BI", 1030, 110, 8),
            ("Tableau", 1210, 210, 8),
            ("Dashboard Design", 1010, 330, 7),
            ("Data Storytelling", 1185, 395, 7),
        ],
        "edges": [(0, 1), (0, 2), (1, 3), (2, 3)],
    },
    {
        "name": "DATA ENGINEERING",
        "color": "#fb923c",
        "cx": 430,
        "cy": 595,
        "nodes": [
            ("Pandas", 380, 510, 8),
            ("NumPy", 250, 610, 7),
            ("Data Cleaning", 500, 665, 7),
            ("EDA", 545, 555, 7),
        ],
        "edges": [(0, 1), (0, 2), (0, 3), (2, 3)],
    },
    {
        "name": "ANALYTICS",
        "color": "#f472b6",
        "cx": 965,
        "cy": 585,
        "nodes": [
            ("Streamlit", 875, 510, 9),
            ("Interpretable AI", 1065, 500, 8),
            ("Decision Support", 850, 665, 8),
            ("Analytics Eng.", 1115, 650, 7),
        ],
        "edges": [(0, 1), (0, 2), (1, 3), (2, 3)],
    },
]

def glow_id(i):
    return f"glow{i}"

svg = []
svg.append(f'''<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <radialGradient id="bgNebula" cx="50%" cy="45%" r="75%">
    <stop offset="0%" stop-color="#1e1b4b"/>
    <stop offset="38%" stop-color="#0f172a"/>
    <stop offset="100%" stop-color="#020617"/>
  </radialGradient>

  <filter id="softGlow" x="-80%" y="-80%" width="260%" height="260%">
    <feGaussianBlur stdDeviation="8" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <filter id="strongGlow" x="-120%" y="-120%" width="340%" height="340%">
    <feGaussianBlur stdDeviation="14" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <linearGradient id="borderGrad" x1="0" y1="0" x2="{WIDTH}" y2="{HEIGHT}">
    <stop stop-color="#38bdf8"/>
    <stop offset="0.45" stop-color="#a78bfa"/>
    <stop offset="1" stop-color="#fbbf24"/>
  </linearGradient>

  <style>
    .label {{
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
      font-size: 15px;
      fill: #e0f2fe;
      letter-spacing: 0.03em;
      paint-order: stroke;
      stroke: #020617;
      stroke-width: 4px;
      stroke-linejoin: round;
    }}
    .group {{
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
      font-size: 12px;
      fill: #94a3b8;
      letter-spacing: 0.18em;
    }}
    .edge {{
      stroke-linecap: round;
      stroke-dasharray: 500;
      stroke-dashoffset: 500;
      animation: draw 3.2s ease forwards;
    }}
    .node {{
      transform-box: fill-box;
      transform-origin: center;
      animation: pulse 2.8s ease-in-out infinite;
    }}
    .star {{
      animation: twinkle 3.5s ease-in-out infinite;
      transform-box: fill-box;
      transform-origin: center;
    }}
    .float {{
      animation: drift 8s ease-in-out infinite;
    }}
    @keyframes draw {{
      to {{ stroke-dashoffset: 0; }}
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 0.86; transform: scale(1); }}
      50% {{ opacity: 1; transform: scale(1.18); }}
    }}
    @keyframes twinkle {{
      0%, 100% {{ opacity: 0.22; transform: scale(1); }}
      50% {{ opacity: 0.9; transform: scale(1.45); }}
    }}
    @keyframes drift {{
      0%, 100% {{ transform: translate(0, 0); }}
      50% {{ transform: translate(10px, -8px); }}
    }}
  </style>
</defs>

<rect width="100%" height="100%" rx="26" fill="url(#bgNebula)"/>
<rect x="10" y="10" width="{WIDTH-20}" height="{HEIGHT-20}" rx="24" stroke="url(#borderGrad)" stroke-opacity="0.55" stroke-width="2"/>
<rect x="24" y="24" width="{WIDTH-48}" height="{HEIGHT-48}" rx="20" fill="#020617" opacity="0.38"/>

<g class="float">
  <circle cx="310" cy="175" r="180" fill="#7c3aed" opacity="0.08"/>
  <circle cx="1030" cy="510" r="210" fill="#0891b2" opacity="0.08"/>
  <circle cx="720" cy="350" r="260" fill="#c084fc" opacity="0.045"/>
</g>
''')

# background stars
for i in range(190):
    x = random.randint(35, WIDTH - 35)
    y = random.randint(35, HEIGHT - 35)
    r = random.choice([1, 1.2, 1.5, 2, 2.4])
    opacity = random.uniform(0.15, 0.65)
    delay = random.uniform(0, 3.5)
    color = random.choice(["#e0f2fe", "#a78bfa", "#38bdf8", "#f8fafc"])
    svg.append(
        f'<circle class="star" cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="{opacity}" style="animation-delay:{delay:.2f}s"/>'
    )

svg.append('''
<text x="50%" y="52" text-anchor="middle" fill="#f8fafc"
      font-family="JetBrains Mono, Fira Code, Consolas, monospace"
      font-size="28" font-weight="700" letter-spacing="0.08em">
  SKILL CONSTELLATION
</text>
<text x="50%" y="82" text-anchor="middle" fill="#94a3b8"
      font-family="JetBrains Mono, Fira Code, Consolas, monospace"
      font-size="13" letter-spacing="0.16em">
  DATA SCIENCE · MACHINE LEARNING · ANALYTICS SYSTEMS
</text>
''')

# faint inter-constellation links between group centers
for i in range(len(constellations)):
    for j in range(i + 1, len(constellations)):
        c1 = constellations[i]
        c2 = constellations[j]
        if random.random() < 0.35:
            svg.append(
                f'<line x1="{c1["cx"]}" y1="{c1["cy"]}" x2="{c2["cx"]}" y2="{c2["cy"]}" '
                f'stroke="#64748b" stroke-width="1" opacity="0.10"/>'
            )

# draw constellations
for ci, c in enumerate(constellations):
    color = c["color"]
    nodes = c["nodes"]

    # group halo
    svg.append(
        f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="115" fill="{color}" opacity="0.035" filter="url(#softGlow)"/>'
    )

    # group label
    svg.append(
        f'<text class="group" x="{c["cx"]}" y="{c["cy"] - 125}" text-anchor="middle">{c["name"]}</text>'
    )

    # edges
    for ei, (a, b) in enumerate(c["edges"]):
        x1, y1 = nodes[a][1], nodes[a][2]
        x2, y2 = nodes[b][1], nodes[b][2]
        delay = 0.15 * (ci + ei)
        svg.append(
            f'<line class="edge" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="2.4" opacity="0.72" '
            f'filter="url(#softGlow)" style="animation-delay:{delay:.2f}s"/>'
        )

    # center group node
    svg.append(
        f'<circle cx="{c["cx"]}" cy="{c["cy"]}" r="13" fill="{color}" opacity="0.65" filter="url(#strongGlow)"/>'
    )

    # nodes
    for ni, (name, x, y, r) in enumerate(nodes):
        delay = (ci * 0.25) + (ni * 0.18)
        label_x = x + 18
        label_y = y + 5

        # glow ring
        svg.append(
            f'<circle class="node" cx="{x}" cy="{y}" r="{r*3.8}" fill="{color}" opacity="0.16" '
            f'filter="url(#strongGlow)" style="animation-delay:{delay:.2f}s"/>'
        )

        # outer ring
        svg.append(
            f'<circle cx="{x}" cy="{y}" r="{r+8}" fill="none" stroke="{color}" '
            f'stroke-opacity="0.32" stroke-width="1.4"/>'
        )

        # main star
        svg.append(
            f'<circle class="node" cx="{x}" cy="{y}" r="{r}" fill="{color}" '
            f'filter="url(#strongGlow)" style="animation-delay:{delay:.2f}s"/>'
        )

        # tiny white core
        svg.append(
            f'<circle cx="{x}" cy="{y}" r="{max(2.5, r*0.32):.1f}" fill="#f8fafc" opacity="0.80"/>'
        )

        # label placement adjustment
        if x > WIDTH - 250:
            label_x = x - 18
            anchor = "end"
        else:
            anchor = "start"

        svg.append(
            f'<text class="label" x="{label_x}" y="{label_y}" text-anchor="{anchor}">{name}</text>'
        )

# pixel/satellite details
for i in range(36):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(95, HEIGHT - 55)
    size = random.choice([3, 4, 5])
    color = random.choice(["#38bdf8", "#a78bfa", "#f472b6", "#fbbf24"])
    svg.append(
        f'<rect class="star" x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" opacity="0.28" rx="1"/>'
    )

# bottom legend
legend_y = HEIGHT - 42
legend_x = 260
for ci, c in enumerate(constellations):
    x = legend_x + ci * 190
    svg.append(f'<circle cx="{x}" cy="{legend_y}" r="5" fill="{c["color"]}" filter="url(#softGlow)"/>')
    svg.append(
        f'<text x="{x+13}" y="{legend_y+4}" fill="#cbd5e1" '
        f'font-family="JetBrains Mono, Fira Code, Consolas, monospace" font-size="11">{c["name"]}</text>'
    )

svg.append("</svg>")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Generated {OUT}")
