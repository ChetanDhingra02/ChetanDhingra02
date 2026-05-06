import svgwrite
import math
import random

WIDTH = 1400
HEIGHT = 800

dwg = svgwrite.Drawing(
    "assets/skill-constellation.svg",
    size=(WIDTH, HEIGHT)
)

# Background
dwg.add(
    dwg.rect(
        insert=(0, 0),
        size=("100%", "100%"),
        fill="#020617"
    )
)

# Nebula glow
for _ in range(40):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(2, 5)

    dwg.add(
        dwg.circle(
            center=(x, y),
            r=r,
            fill="#8BE9FD",
            opacity=random.uniform(0.1, 0.5)
        )
    )

center_x = WIDTH // 2
center_y = HEIGHT // 2

skills = {
    "Python": (0, "#38BDF8"),
    "R": (45, "#C084FC"),
    "SQL": (90, "#FBBF24"),
    "Machine Learning": (135, "#F472B6"),
    "Statistics": (180, "#22D3EE"),
    "Streamlit": (225, "#F43F5E"),
    "Power BI": (270, "#60A5FA"),
    "Tableau": (315, "#FACC15"),
}

radius = 250

# Center node
dwg.add(
    dwg.circle(
        center=(center_x, center_y),
        r=40,
        fill="#E2E8F0",
        opacity=0.9
    )
)

dwg.add(
    dwg.text(
        "COSMOS",
        insert=(center_x - 38, center_y + 5),
        fill="#020617",
        font_size="20px",
        font_family="Arial"
    )
)

for skill, (angle, color) in skills.items():

    rad = math.radians(angle)

    x = center_x + radius * math.cos(rad)
    y = center_y + radius * math.sin(rad)

    # Line
    dwg.add(
        dwg.line(
            start=(center_x, center_y),
            end=(x, y),
            stroke=color,
            stroke_width=4,
            opacity=0.7
        )
    )

    # Node
    dwg.add(
        dwg.circle(
            center=(x, y),
            r=22,
            fill=color
        )
    )

    # Glow
    dwg.add(
        dwg.circle(
            center=(x, y),
            r=38,
            fill=color,
            opacity=0.15
        )
    )

    # Label
    dwg.add(
        dwg.text(
            skill,
            insert=(x + 30, y + 5),
            fill="#E2E8F0",
            font_size="20px",
            font_family="Arial"
        )
    )

dwg.save()
