#!/usr/bin/env python3
"""Generate ai-productivity-roi-calculator.xlsx, the demo's source material.

This is the spreadsheet a requestor would hand you: real structure, real
formulas, real benchmark figures, and every assumption exposed as an editable
cell. It exists so the workshop demo has something to specify AGAINST rather
than a blank page, which is the situation the team is actually in when a
request arrives.

On macros. There are none, deliberately. A .xlsm triggers a security prompt
and is blocked outright by plenty of enterprise policy, and everything this
model does is expressible as a formula. A macro here would buy nothing and
cost the ability to open the file.

The numbers in Benchmarks are cited and dated. They are industry figures for
software developers, and this team is not one, which is the single most
important caveat in the file and is why the realization factor exists as its
own input rather than being folded into the hours figure.

Run: python3 fixtures/build_roi_calculator.py
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

NAVY = "FF005073"
BLUE = "FF049FD9"
TINT = "FFF3F9FD"
GREY = "FFF5F7F8"
AMBER = "FFB26A00"
WHITE = "FFFFFFFF"

H1 = Font(name="Calibri", size=14, bold=True, color=NAVY)
H2 = Font(name="Calibri", size=11, bold=True, color=WHITE)
BOLD = Font(name="Calibri", size=11, bold=True)
BODY = Font(name="Calibri", size=11)
SMALL = Font(name="Calibri", size=9, color="FF6B7280")
INPUT_FONT = Font(name="Calibri", size=11, bold=True, color="FF0B6E99")

HEAD_FILL = PatternFill("solid", fgColor=NAVY)
INPUT_FILL = PatternFill("solid", fgColor="FFFFF6E5")
TINT_FILL = PatternFill("solid", fgColor=TINT)
GREY_FILL = PatternFill("solid", fgColor=GREY)

THIN = Side(style="thin", color="FFD5E4EE")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

WRAP = Alignment(wrap_text=True, vertical="top")

wb = Workbook()


def header_row(ws, row, labels, widths=None):
    for i, label in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=label)
        c.font = H2
        c.fill = HEAD_FILL
        c.border = BOX
        c.alignment = Alignment(vertical="center", wrap_text=True)
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w


# ---------------------------------------------------------------- README
ws = wb.active
ws.title = "Read me"
ws.column_dimensions["A"].width = 104
ws.sheet_view.showGridLines = False

lines = [
    ("AI productivity ROI calculator", H1),
    ("", BODY),
    ("What this is. A working model for the value of giving a team agentic AI tooling, built on the "
     "Forrester Total Economic Impact shape: benefits, costs, and a risk adjustment applied to both. "
     "It reports two numbers because leadership asks for one and finance asks for the other.", BODY),
    ("", BODY),
    ("THE TWO NUMBERS, AND WHY BOTH ARE HERE", BOLD),
    ("Benefit dollars is the gross annual value created. It is the number most people mean when they "
     "say ROI in conversation.", BODY),
    ("ROI percent is (benefit minus cost) divided by cost. It is what the word actually means, and it "
     "is what a finance reviewer will check.", BODY),
    ("Quoting one when your audience wanted the other is the most common way this conversation goes "
     "wrong. The model shows both, side by side, so you never have to pick in the room.", BODY),
    ("", BODY),
    ("HOW TO USE IT", BOLD),
    ("Edit only the shaded cells on the Inputs sheet. Everything on Model is a formula and will "
     "recalculate. Nothing here connects to a live system, so you can put any numbers in it.", BODY),
    ("", BODY),
    ("THE ASSUMPTION THAT MATTERS MOST", BOLD),
    ("The realization factor. Time saved is not the same thing as value created. An hour freed up "
     "only becomes money if it goes into work that matters, and published studies repeatedly find "
     "teams capturing a fraction of their measured time savings. The default here is deliberately "
     "conservative. Raising it is the single easiest way to make this model say whatever you want, "
     "which is exactly why it is a visible input rather than buried in a coefficient.", BODY),
    ("", BODY),
    ("THE CAVEAT TO SAY OUT LOUD", BOLD),
    ("Every benchmark on the Benchmarks sheet measures software developers. This model is being "
     "applied to a team that mostly does not write software for a living. The hours-saved figure is "
     "therefore an anchor and not an estimate, and it should be replaced with a measured number from "
     "your own team as soon as one exists. Until then, say so when you present it.", BODY),
    ("", BODY),
    ("No macros. Everything is formulas, so the file opens anywhere without a security prompt.", SMALL),
]
for i, (text, font) in enumerate(lines, start=1):
    c = ws.cell(row=i, column=1, value=text)
    c.font = font
    c.alignment = WRAP
ws.row_dimensions[1].height = 22

# ---------------------------------------------------------------- INPUTS
ws = wb.create_sheet("Inputs")
ws.sheet_view.showGridLines = False
header_row(ws, 1, ["Assumption", "Value", "Unit", "Where this comes from"], [40, 14, 14, 62])

inputs = [
    ("People in scope", 5, "people", "How many get a seat. Change this first."),
    ("Fully loaded cost per person", 185000, "USD/year", "Salary plus benefits, overhead and employer taxes. Ask finance for the real multiplier rather than guessing at 1.3x."),
    ("Working hours per year", 1880, "hours", "47 working weeks at 40 hours, which nets off holiday and leave."),
    ("Hours saved per person per week", 3.6, "hours", "Benchmarks!A4. Developer figure. Replace with a measured number for this team as soon as one exists."),
    ("Adoption rate", 0.70, "share", "Share of seats in genuine weekly use. A seat nobody opens produces nothing and still costs."),
    ("Realization factor", 0.40, "share", "Share of freed time that becomes work of comparable value. The most contested input in the model. See Read me."),
    ("Seat cost per person", 1000, "USD/month", "The platform spending limit per seat. This is a ceiling and not a forecast."),
    ("Expected usage per person", 150, "USD/month", "What is actually consumed. Keep this separate from the ceiling or the model overstates cost by several times."),
    ("Token and API spend outside seats", 0, "USD/month", "Automated runs, evaluations and CI. These cannot sit on a human seat. Leaving this at zero is the most common way an AI ROI model flatters itself."),
    ("Enablement cost, one off", 12000, "USD", "Training, the hours spent learning, and the sessions that teach it. Year one only."),
    ("Risk adjustment", 0.20, "share", "Forrester TEI applies a haircut to benefits for delivery risk. 20 percent is a common starting point for a first deployment."),
    ("Discount rate", 0.10, "share", "For the three year net present value. Use whatever finance uses."),
]
for r, (label, val, unit, note) in enumerate(inputs, start=2):
    ws.cell(row=r, column=1, value=label).font = BODY
    c = ws.cell(row=r, column=2, value=val)
    c.font = INPUT_FONT
    c.fill = INPUT_FILL
    c.border = BOX
    if unit == "share":
        c.number_format = "0%"
    elif "USD" in unit:
        c.number_format = '#,##0'
    else:
        c.number_format = "0.0" if isinstance(val, float) else "0"
    ws.cell(row=r, column=3, value=unit).font = SMALL
    n = ws.cell(row=r, column=4, value=note)
    n.font = SMALL
    n.alignment = WRAP
    ws.row_dimensions[r].height = 30

ws.cell(row=len(inputs) + 3, column=1,
        value="Shaded cells are yours to change. Nothing else on this sheet is an input.").font = SMALL

# ---------------------------------------------------------------- MODEL
ws = wb.create_sheet("Model")
ws.sheet_view.showGridLines = False
ws.column_dimensions["A"].width = 44
for col in "BCD":
    ws.column_dimensions[col].width = 16
ws.column_dimensions["E"].width = 54

I = "Inputs!$B$"  # noqa: E741  short on purpose, this is a spreadsheet formula prefix

ws.cell(row=1, column=1, value="Three year model, risk adjusted").font = H1
header_row(ws, 3, ["Line", "Year 1", "Year 2", "Year 3", "How it is calculated"], [44, 16, 16, 16, 54])

hourly = f"({I}3/{I}4)"          # loaded cost / working hours
weekly = f"{I}5"                  # hours saved per person per week
people = f"{I}2"
adopt = f"{I}6"
realize = f"{I}7"
risk = f"{I}12"

gross = f"{people}*{weekly}*47*{hourly}*{adopt}"
benefit = f"{gross}*{realize}*(1-{risk})"

seat_cost = f"{people}*{I}9*12"
token_cost = f"{I}10*12"

# Row numbers are recorded as the sheet is written rather than counted by hand.
#
# The first version of this file hardcoded them, and the write loop skips a row
# for each section header, so every dependent formula landed two rows high.
# Total cost read $9,648 against a real year one cost of $21,000, ROI came out
# blank, and payback said 0.0 months. The workbook opened without complaint and
# the numbers looked plausible, which is the whole problem: a wrong total in
# the right format is indistinguishable from a right one until you recompute
# it. Caught by converting the file and reading the values back, not by
# rereading the code.
at = {}


def emit(label, y1, y2, y3, how, kind):
    """Write one row, remember where it landed, and return its row number."""
    global r
    if kind == "head":
        c = ws.cell(row=r, column=1, value=label)
        c.font = BOLD
        for col in range(1, 6):
            ws.cell(row=r, column=col).fill = TINT_FILL
            ws.cell(row=r, column=col).border = BOX
        r += 1
        return None
    ws.cell(row=r, column=1, value=label).font = BOLD if "bold" in kind else BODY
    for col, val in zip((2, 3, 4), (y1, y2, y3)):
        c = ws.cell(row=r, column=col, value=val)
        c.border = BOX
        c.font = BOLD if "bold" in kind else BODY
        if kind.startswith("usd"):
            c.number_format = '$#,##0;($#,##0)'
        elif kind.startswith("pct"):
            c.number_format = "0%"
        else:
            c.number_format = "#,##0"
    h = ws.cell(row=r, column=5, value=how)
    h.font = SMALL
    h.alignment = WRAP
    at[label] = r
    r += 1
    return r - 1


r = 4
emit("BENEFITS", None, None, None, None, "head")
emit("Hours freed per year", *[f"={people}*{weekly}*47*{adopt}"] * 3,
     "People x hours per week x 47 weeks x adoption", "num")
emit("Gross value of freed time", *[f"={gross}"] * 3,
     "Hours freed x fully loaded hourly rate", "usd")
emit("Value actually captured", *[f"={gross}*{realize}"] * 3,
     "Gross value x realization factor", "usd")
rb = emit("Risk adjusted benefit", *[f"={benefit}"] * 3,
          "Captured value less the risk haircut. THIS IS THE BENEFIT NUMBER.", "usdbold")

emit("COSTS", None, None, None, None, "head")
c1 = emit("Seat usage", *[f"=-{seat_cost}"] * 3,
          "Expected usage per person x 12. Not the ceiling.", "usd")
c2 = emit("Token and API spend outside seats", *[f"=-{token_cost}"] * 3,
          "Automation and evaluation runs, which cannot sit on a human seat", "usd")
c3 = emit("Enablement", f"=-{I}11", 0, 0, "One off, year one", "usd")
tc = emit("Total cost",
          *[f"={L}{c1}+{L}{c2}+{L}{c3}" for L in "BCD"],
          "Sum of the three above. Negative, because it is a cost.", "usdbold")

emit("RESULT", None, None, None, None, "head")
nb = emit("Net benefit", *[f"={L}{rb}+{L}{tc}" for L in "BCD"],
          "Risk adjusted benefit less total cost", "usdbold")
emit("ROI percent",
     *[f'=IF({L}{tc}=0,"",({L}{rb}+{L}{tc})/-{L}{tc})' for L in "BCD"],
     "Net benefit divided by cost. THIS IS THE ROI NUMBER.", "pctbold")

summary_row = r + 1
ws.cell(row=summary_row, column=1, value="Three year net present value").font = BOLD
npv = ws.cell(row=summary_row, column=2,
              value=f"=NPV({I}13,B{nb},C{nb},D{nb})")
npv.number_format = '$#,##0;($#,##0)'
npv.font = BOLD
ws.cell(row=summary_row, column=5,
        value="Net benefit discounted at the rate on Inputs").font = SMALL

ws.cell(row=summary_row + 1, column=1, value="Payback, months").font = BOLD
pb = ws.cell(row=summary_row + 1, column=2,
             value=f'=IF(B{rb}<=0,"never at these inputs",12*(-B{tc})/B{rb})')
pb.number_format = "0.0"
pb.font = BOLD
ws.cell(row=summary_row + 1, column=5,
        value="Year one cost divided by the monthly rate of risk adjusted benefit").font = SMALL

note = ws.cell(row=summary_row + 3, column=1,
               value="Every figure here is driven by the Inputs sheet. If a number looks wrong, the "
                     "argument is about an assumption, which is the conversation worth having.")
note.font = SMALL
note.alignment = WRAP

# ---------------------------------------------------------------- BENCHMARKS
ws = wb.create_sheet("Benchmarks")
ws.sheet_view.showGridLines = False
header_row(ws, 1, ["Figure", "Value", "What it measures", "Source", "Captured"], [30, 16, 46, 44, 14])

bm = [
    ("Hours saved per week", "3.6", "Across 135,000 plus developers. The most widely cited baseline.", "faros.ai analysis", "2026-09-23"),
    ("Hours saved, daily users", "4.1", "Developers using AI tooling every day rather than occasionally.", "faros.ai analysis", "2026-09-23"),
    ("Healthy ROI range", "2.5x to 3.5x", "Average. Top quartile reaches 4x to 6x. Only holds when the cost side includes token spend rather than seat fees alone.", "Enterprise AI coding ROI survey round-up", "2026-09-23"),
    ("Typical productivity gain", "10 to 15 percent", "Gains that do NOT reliably convert into business value.", "Enterprise AI coding ROI survey round-up", "2026-09-23"),
    ("Gain when workflows are rebuilt", "25 to 30 percent", "Organisations that redesigned how work flows rather than adding a tool to it.", "Enterprise AI coding ROI survey round-up", "2026-09-23"),
    ("Time to measurable ROI", "3 to 6 months", "Most enterprise deployments.", "Enterprise AI coding ROI survey round-up", "2026-09-23"),
    ("Framework", "Forrester TEI", "Benefits, costs, flexibility and risk, with a risk adjustment applied to both sides and results expressed as risk adjusted ROI, NPV and payback.", "Forrester Total Economic Impact methodology", "2026-09-23"),
]
for r, row in enumerate(bm, start=2):
    for col, val in enumerate(row, start=1):
        c = ws.cell(row=r, column=col, value=val)
        c.font = SMALL if col in (3, 4, 5) else BODY
        c.alignment = WRAP
        c.border = BOX
    ws.row_dimensions[r].height = 34

warn = ws.cell(row=len(bm) + 3, column=1,
               value="EVERY FIGURE ON THIS SHEET MEASURES SOFTWARE DEVELOPERS. This team is not one. "
                     "Treat them as an anchor for a conversation, not as an estimate of what this team "
                     "will save, and replace them with a measured number as soon as one exists.")
warn.font = Font(name="Calibri", size=10, bold=True, color=AMBER)
warn.alignment = WRAP
ws.merge_cells(start_row=len(bm) + 3, start_column=1, end_row=len(bm) + 3, end_column=5)

out = "fixtures/ai-productivity-roi-calculator.xlsx"
wb.save(out)
print("wrote", out)
