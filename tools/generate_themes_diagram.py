#!/usr/bin/env python3
"""
Regenerate themes-over-time.{drawio,png} from the wiki's own concept pages.

Reads the `## <year>[ Q<n>] — ...` headings directly out of every concept
page in both wikis, so the diagram can never drift from what's actually
ingested. Re-run after any ingest batch that touches a concept page.

Usage: python3 tools/generate_themes_diagram.py
Outputs (repo root): themes-over-time.drawio, themes-over-time.png
"""
import re
import xml.sax.saxutils as sx
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# 1. Timeline columns: yearly resolution 2010-2014 and 2023-2026(partial),
#    quarterly resolution 2015-2022, per wiki/progress.md's dense-year rule.
# ---------------------------------------------------------------------------
YEARLY_EARLY = list(range(2010, 2015))
QUARTERLY = list(range(2015, 2023))
YEARLY_LATE = list(range(2023, 2027))

PERIODS = []  # list of (year, quarter_or_None)
for y in YEARLY_EARLY:
    PERIODS.append((y, None))
for y in QUARTERLY:
    for q in (1, 2, 3, 4):
        PERIODS.append((y, q))
for y in YEARLY_LATE:
    PERIODS.append((y, None))

PERIOD_INDEX = {p: i for i, p in enumerate(PERIODS)}

HEADING_RE = re.compile(r"^##\s+(\d{4})(?:\s+Q(\d))?\s+—")


def parse_periods(md_path: Path):
    """Return sorted list of period-index ints this page has an entry for."""
    found = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        year = int(m.group(1))
        quarter = int(m.group(2)) if m.group(2) else None
        key = (year, quarter)
        if key not in PERIOD_INDEX:
            raise ValueError(f"{md_path}: heading {key} not in known timeline")
        found.append(PERIOD_INDEX[key])
    return sorted(set(found))


def runs(indices):
    """Group sorted period-indices into contiguous [start, end] runs."""
    out = []
    for i in indices:
        if out and i == out[-1][1] + 1:
            out[-1] = (out[-1][0], i)
        else:
            out.append((i, i))
    return out


# ---------------------------------------------------------------------------
# 2. Rows: (label, file, category)
# ---------------------------------------------------------------------------
TESTING = ROOT / "wiki/testing/concepts"
PERSONAL = ROOT / "wiki/personal/concepts"

BLUE = "craft"        # testing craft & method
ORANGE = "identity"   # identity, culture & management
PURPLE = "gender"     # gender advocacy
GREEN = "personal"    # personal wiki

ROWS = [
    ("Exploratory Testing", TESTING / "exploratory-testing.md", BLUE),
    ("Checking vs. Testing", TESTING / "checking-vs-testing.md", BLUE),
    ("Documentation Skepticism", TESTING / "documentation-skepticism.md", BLUE),
    ("Test Manager vs. Project Manager", TESTING / "test-manager-vs-project-manager.md", BLUE),
    ("Empirical Research on Testing", TESTING / "testing-research.md", BLUE),
    ("Whole-Team Testing", TESTING / "whole-team-testing.md", BLUE),
    ("Experiential ET Training", TESTING / "experiential-testing-training.md", BLUE),
    ("AI in Testing", TESTING / "ai-in-testing.md", BLUE),
    ("Tester Identity, Not Role", TESTING / "tester-identity.md", ORANGE),
    ("Management Transition", TESTING / "management-transition.md", ORANGE),
    ("CDT Community Culture", TESTING / "cdt-community-culture.md", ORANGE),
    ("Gender in Tech/Testing", TESTING / "gender-in-tech.md", PURPLE),
    ("#PayToSpeak", TESTING / "pay-to-speak.md", PURPLE),
    ("Self-Understanding", PERSONAL / "self-understanding.md", GREEN),
    ("Career Direction", PERSONAL / "career-direction.md", GREEN),
    ("Writing a Book", PERSONAL / "writing-a-book.md", GREEN),
    ("Health & Accommodation Needs", PERSONAL / "health-accommodation.md", GREEN),
]

SECTIONS = [("TESTING WIKI", 0, 13), ("PERSONAL WIKI", 13, 17)]

CATEGORY_COLORS = {
    BLUE: ("#dae8fc", "#6c8ebf"),
    ORANGE: ("#ffe6cc", "#d79b00"),
    PURPLE: ("#e1d5e7", "#9673a6"),
    GREEN: ("#d5e8d4", "#82b366"),
}
CATEGORY_LABELS = {
    BLUE: "Testing craft & method",
    ORANGE: "Identity, culture & management",
    PURPLE: "Gender advocacy",
    GREEN: "Personal wiki",
}

MILESTONES = [
    ((2014, None), "Bach block; tester-identity/gender-in-tech open"),
    ((2016, 3), "TMAcad; CDT culture named"),
    ((2018, 2), "becomes manager; ET Book published"),
    ((2019, 4), "Falco doxxing; F-Secure exit to Vaisala"),
    ((2021, 4), "Robot Framework dispute resolved"),
    ((2022, 3), "joins Selenium Leadership Committee"),
    ((2023, None), "Twitter deleted; speaking retirement"),
    ((2024, None), "CGI Director; Selenium turns 20"),
    ((2025, None), "burnout named; 12th award nomination"),
    ((2026, None), "kicked from AI-strategy session; #ReluctantManager"),
]

# ---------------------------------------------------------------------------
# 3. Geometry
# ---------------------------------------------------------------------------
LEFT_MARGIN = 300
COL_W = 100
QCOL_W = COL_W / 4
TOP = 20
TITLE_H = 32
SUBTITLE_H = 22
YEAR_ROW_Y = TOP + TITLE_H + SUBTITLE_H + 8
YEAR_ROW_H = 24
QTR_ROW_H = 16
GRID_TOP = YEAR_ROW_Y + YEAR_ROW_H + QTR_ROW_H
ROW_H = 27
SECTION_H = 24
BAR_PAD = 3

# every year occupies 4 quarter-units of x-space, whether it's rendered as
# one yearly box or four quarterly boxes
N_COLS = (len(YEARLY_EARLY) + len(QUARTERLY) + len(YEARLY_LATE)) * 4
GRID_W = N_COLS * QCOL_W
TOTAL_W = int(LEFT_MARGIN + GRID_W + 20)

n_rows_total = len(ROWS) + len(SECTIONS)
GRID_H = n_rows_total * ROW_H + len(SECTIONS) * (SECTION_H - ROW_H)
MILESTONE_H = 56
LEGEND_H = 130
TOTAL_H = int(GRID_TOP + GRID_H + MILESTONE_H + LEGEND_H)


def col_x(period_index):
    """Left-edge x of the quarter-column at this period index, in quarter-units."""
    # walk PERIODS to accumulate quarter-widths (yearly cols = 4 quarter-units wide)
    x = 0
    for i, (y, q) in enumerate(PERIODS):
        if i == period_index:
            return x
        x += 4 if q is None else 1
    return x


def col_span(period_index):
    y, q = PERIODS[period_index]
    return 4 if q is None else 1


ALL_YEARS = YEARLY_EARLY + QUARTERLY + YEARLY_LATE
YEAR_START_IDX = {}
for y in ALL_YEARS:
    if y in QUARTERLY:
        YEAR_START_IDX[y] = PERIOD_INDEX[(y, 1)]
    else:
        YEAR_START_IDX[y] = PERIOD_INDEX[(y, None)]


def year_x_units(y):
    """Left-edge x of a whole year, in quarter-units (every year is 4 units wide)."""
    return col_x(YEAR_START_IDX[y])


# ---------------------------------------------------------------------------
# 4. Build row bar data
# ---------------------------------------------------------------------------
row_bars = []  # list of list-of-(x0,x1) in quarter-units, per row
for label, path, cat in ROWS:
    idxs = parse_periods(path)
    bars = []
    for start, end in runs(idxs):
        x0 = col_x(start)
        x1 = col_x(end) + col_span(end)
        bars.append((x0, x1))
    row_bars.append(bars)

# ---------------------------------------------------------------------------
# 5. Render PNG (supersampled 2x then downscaled for crisp text)
# ---------------------------------------------------------------------------
SS = 2
img = Image.new("RGB", (TOTAL_W * SS, TOTAL_H * SS), "white")
d = ImageDraw.Draw(img)


def font(size, bold=False, italic=False):
    name = "Arial"
    if bold and italic:
        name = "Arial Bold Italic"
    elif bold:
        name = "Arial Bold"
    elif italic:
        name = "Arial Italic"
    path = f"/System/Library/Fonts/Supplemental/{name}.ttf"
    return ImageFont.truetype(path, size * SS)


F_TITLE = font(19, bold=True)
F_SUB = font(11, italic=True)
F_YEAR = font(12, bold=True)
F_QTR = font(7)
F_ROW = font(11)
F_SECTION = font(11, bold=True)
F_MILE = font(8)
F_LEGEND = font(10)


def X(x):
    return int(round(x * SS))


def text(xy, s, f, fill, anchor="la"):
    d.text((X(xy[0]), X(xy[1])), s, font=f, fill=fill, anchor=anchor)


def rect(x0, y0, x1, y1, fill=None, outline=None, width=1):
    d.rectangle([X(x0), X(y0), X(x1), X(y1)], fill=fill, outline=outline, width=max(1, width * SS))


def rrect(x0, y0, x1, y1, fill=None, outline=None, width=1, radius=4):
    d.rounded_rectangle(
        [X(x0), X(y0), X(x1), X(y1)], radius=radius * SS, fill=fill, outline=outline, width=max(1, width * SS)
    )


# Title / subtitle
text((10, TOP), "Themes Over Time — Wiki Concepts (2010–2026)", F_TITLE, "#222222")
text(
    (10, TOP + TITLE_H),
    "Ingested batches 2010–2026 (@maaretp public post history) — fully ingested "
    "through 2026-08 (current end of the raw archive; 2026 is partial). Bars mark periods "
    "where a concept page has an entry; gaps are quiet periods, not absence of belief.",
    F_SUB,
    "#666666",
)

# Year header + quarter labels
for y in ALL_YEARS:
    gx = LEFT_MARGIN + year_x_units(y) * QCOL_W
    w = COL_W
    rect(gx, YEAR_ROW_Y, gx + w - 2, YEAR_ROW_Y + YEAR_ROW_H, fill="#f0f0f0", outline="#b3b3b3")
    label = f"{y}*" if y == 2026 else str(y)
    text((gx + w / 2, YEAR_ROW_Y + YEAR_ROW_H / 2), label, F_YEAR, "#333333", anchor="mm")
    if y in QUARTERLY:
        for qq in range(1, 5):
            qx = gx + (qq - 1) * QCOL_W
            rect(
                qx, YEAR_ROW_Y + YEAR_ROW_H, qx + QCOL_W - 1, YEAR_ROW_Y + YEAR_ROW_H + QTR_ROW_H,
                outline="#dddddd",
            )
            text(
                (qx + QCOL_W / 2, YEAR_ROW_Y + YEAR_ROW_H + QTR_ROW_H / 2), f"Q{qq}", F_QTR, "#999999",
                anchor="mm",
            )

# vertical gridlines across the whole grid at year boundaries
grid_bottom = GRID_TOP + GRID_H
for y in ALL_YEARS:
    gx = LEFT_MARGIN + year_x_units(y) * QCOL_W
    d.line([X(gx), X(YEAR_ROW_Y), X(gx), X(grid_bottom)], fill="#e6e6e6", width=SS)
gx_end = LEFT_MARGIN + N_COLS * QCOL_W
d.line([X(gx_end), X(YEAR_ROW_Y), X(gx_end), X(grid_bottom)], fill="#b3b3b3", width=SS)

# Rows (with section headers)
row_y = GRID_TOP
row_i = 0
section_starts = {s[1]: s[0] for s in SECTIONS}
for section_label, start, end in SECTIONS:
    rect(0, row_y, TOTAL_W - 20, row_y + SECTION_H, fill="#e8e8e8", outline="#cccccc")
    text((8, row_y + SECTION_H / 2), section_label, F_SECTION, "#333333", anchor="lm")
    row_y += SECTION_H
    for r in range(start, end):
        label, path, cat = ROWS[r]
        y0, y1 = row_y, row_y + ROW_H
        rect(0, y0, TOTAL_W - 20, y1, outline="#eeeeee")
        text((16, y0 + ROW_H / 2), label, F_ROW, "#222222", anchor="lm")
        fill, stroke = CATEGORY_COLORS[cat]
        for x0, x1 in row_bars[r]:
            bx0 = LEFT_MARGIN + x0 * QCOL_W + BAR_PAD
            bx1 = LEFT_MARGIN + x1 * QCOL_W - BAR_PAD
            rrect(bx0, y0 + 4, bx1, y1 - 4, fill=fill, outline=stroke, width=1, radius=5)
        row_y += ROW_H

# Milestones strip
mrow_y = row_y + 10
d.line([X(10), X(mrow_y - 6), X(TOTAL_W - 20), X(mrow_y - 6)], fill="#dddddd", width=SS)
for (y, q), text_ in MILESTONES:
    idx = PERIOD_INDEX[(y, q)]
    x = LEFT_MARGIN + col_x(idx) * QCOL_W + (col_span(idx) * QCOL_W) / 2
    d.line([X(x), X(mrow_y - 6), X(x), X(mrow_y)], fill="#999999", width=SS)
    # rotate-free: wrap by drawing multiline centered text under a tick
    text((x, mrow_y + 2), str(y), F_MILE, "#888888", anchor="ma")
    words = text_.split(" ")
    line = ""
    lines = []
    for w in words:
        trial = (line + " " + w).strip()
        if len(trial) > 20:
            lines.append(line)
            line = w
        else:
            line = trial
    if line:
        lines.append(line)
    for li, ln in enumerate(lines[:3]):
        text((x, mrow_y + 12 + li * 9), ln, F_MILE, "#777777", anchor="ma")

# Legend
ly = mrow_y + MILESTONE_H - 10
text((10, ly), "Legend", font(11, bold=True), "#333333")
ly += 18
for cat in (BLUE, ORANGE, PURPLE, GREEN):
    fill, stroke = CATEGORY_COLORS[cat]
    rrect(10, ly, 34, ly + 14, fill=fill, outline=stroke, radius=4)
    text((40, ly + 7), CATEGORY_LABELS[cat], F_LEGEND, "#333333", anchor="lm")
    ly += 20

img = img.resize((TOTAL_W, TOTAL_H), Image.LANCZOS)
png_path = ROOT / "themes-over-time.png"
img.save(png_path)
print(f"wrote {png_path} ({TOTAL_W}x{TOTAL_H})")

# ---------------------------------------------------------------------------
# 6. Render drawio XML (editable source, same geometry/data)
# ---------------------------------------------------------------------------
cells = []
cid = [200]


def new_id():
    cid[0] += 1
    return f"n{cid[0]}"


def esc(s):
    return sx.escape(s, {"\n": "&#10;"})


def cell_text(value, x, y, w, h, style):
    return (
        f'<mxCell id="{new_id()}" value="{esc(value)}" style="{style}" vertex="1" parent="1">'
        f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>'
    )


cells.append(
    cell_text(
        "Themes Over Time — Wiki Concepts (2010–2026)",
        10,
        TOP,
        900,
        TITLE_H,
        "text;html=1;fontSize=20;fontStyle=1;align=left;verticalAlign=middle;fontColor=#222222;",
    )
)
cells.append(
    cell_text(
        "Ingested batches 2010–2026 (@maaretp public post history) — fully ingested through "
        "2026-08 (current end of the raw archive; 2026 is partial). Bars mark periods where a concept "
        "page has an entry; gaps are quiet periods, not absence of belief.",
        10,
        TOP + TITLE_H,
        1400,
        SUBTITLE_H,
        "text;html=1;fontSize=11;fontStyle=2;align=left;verticalAlign=middle;fontColor=#666666;",
    )
)

for y in ALL_YEARS:
    gx = LEFT_MARGIN + year_x_units(y) * QCOL_W
    w = COL_W
    label = f"{y}*" if y == 2026 else str(y)
    cells.append(
        cell_text(
            label,
            gx,
            YEAR_ROW_Y,
            w - 2,
            YEAR_ROW_H,
            "text;html=1;fontSize=12;fontStyle=1;align=center;verticalAlign=middle;"
            "fontColor=#333333;strokeColor=#b3b3b3;fillColor=#f0f0f0;",
        )
    )
    if y in QUARTERLY:
        for qq in range(1, 5):
            qx = gx + (qq - 1) * QCOL_W
            cells.append(
                cell_text(
                    f"Q{qq}",
                    qx,
                    YEAR_ROW_Y + YEAR_ROW_H,
                    QCOL_W - 1,
                    QTR_ROW_H,
                    "text;html=1;fontSize=8;align=center;verticalAlign=middle;"
                    "fontColor=#999999;strokeColor=#dddddd;fillColor=none;",
                )
            )

row_y = GRID_TOP
for section_label, start, end in SECTIONS:
    cells.append(
        cell_text(
            section_label,
            0,
            row_y,
            TOTAL_W - 20,
            SECTION_H,
            "text;html=1;fontSize=11;fontStyle=1;align=left;verticalAlign=middle;"
            "fontColor=#333333;strokeColor=#cccccc;fillColor=#e8e8e8;spacingLeft=8;",
        )
    )
    row_y += SECTION_H
    for r in range(start, end):
        label, path, cat = ROWS[r]
        cells.append(
            cell_text(
                label,
                0,
                row_y,
                LEFT_MARGIN - 4,
                ROW_H,
                "text;html=1;fontSize=11;align=left;verticalAlign=middle;"
                "fontColor=#222222;strokeColor=none;fillColor=none;spacingLeft=16;",
            )
        )
        fill, stroke = CATEGORY_COLORS[cat]
        for x0, x1 in row_bars[r]:
            bx0 = LEFT_MARGIN + x0 * QCOL_W + BAR_PAD
            bx1 = LEFT_MARGIN + x1 * QCOL_W - BAR_PAD
            cells.append(
                f'<mxCell id="{new_id()}" style="rounded=1;arcSize=30;whiteSpace=wrap;html=1;'
                f'fillColor={fill};strokeColor={stroke};" vertex="1" parent="1">'
                f'<mxGeometry x="{bx0:.0f}" y="{row_y+4:.0f}" width="{bx1-bx0:.0f}" '
                f'height="{ROW_H-8:.0f}" as="geometry"/></mxCell>'
            )
        row_y += ROW_H

ly = row_y + MILESTONE_H
cells.append(
    cell_text("Legend", 10, ly, 200, 18, "text;html=1;fontSize=11;fontStyle=1;fontColor=#333333;")
)
ly += 20
for cat in (BLUE, ORANGE, PURPLE, GREEN):
    fill, stroke = CATEGORY_COLORS[cat]
    cells.append(
        f'<mxCell id="{new_id()}" style="rounded=1;arcSize=30;fillColor={fill};strokeColor={stroke};" '
        f'vertex="1" parent="1"><mxGeometry x="10" y="{ly:.0f}" width="24" height="14" as="geometry"/></mxCell>'
    )
    cells.append(
        cell_text(CATEGORY_LABELS[cat], 40, ly - 3, 260, 20, "text;html=1;fontSize=10;fontColor=#333333;")
    )
    ly += 20

drawio = f"""<mxfile host="app.diagrams.net" agent="claude-code" version="24.0.0">
  <diagram id="themes-over-time" name="Themes Over Time">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{TOTAL_W}" pageHeight="{TOTAL_H}" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        {chr(10).join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""
drawio_path = ROOT / "themes-over-time.drawio"
drawio_path.write_text(drawio, encoding="utf-8")
print(f"wrote {drawio_path}")
