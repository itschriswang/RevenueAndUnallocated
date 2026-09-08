"""Build RTS_Market_Based_Check_Jul26.xlsx - the market-based electricity check for the
Rail & Transit Systems (RTS) sites, Mar-Aug 26, from the 6 Sep 26 electricity export.

Reads   ../../Electricity Data as of 060926.xlsx   (repo root)
Writes  ../RTS_Market_Based_Check_Jul26.xlsx

Every CO2e check on the Accounts tab is a live formula against the kWh and factor columns, so
a refreshed export can be pasted over the data and the checks re-run. Recalculate after
building (recalc.py from the xlsx skill, or open in Excel).
"""
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXPORT = os.path.join(ROOT, "Electricity Data as of 060926.xlsx")
OUT = os.path.join(HERE, "..", "RTS_Market_Based_Check_Jul26.xlsx")

MONTHS = ["Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26"]
# The dashboard's Scope 1 & 2 (market-based) monthly figures, read off the YTD chart.
CHART = {"Mar 26": 635.78, "Apr 26": 557.14, "May 26": 626.46, "Jun 26": 558.22, "Jul 26": 786.33}  # dashboard refreshed 8 Sep 26

FONT = "Arial"
F = lambda **k: Font(name=FONT, size=k.pop("size", 10), **k)
HDR_FILL = PatternFill("solid", fgColor="1F3864")
SUB_FILL = PatternFill("solid", fgColor="D9E1F2")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
NOTE_FILL = PatternFill("solid", fgColor="F2F2F2")
RED = PatternFill("solid", fgColor="F8CBAD")
AMBER = PatternFill("solid", fgColor="FFE699")
GREEN = PatternFill("solid", fgColor="C6E0B4")
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")


def header(ws, row, labels, widths=None):
    for i, lab in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=lab)
        c.font = F(bold=True, color="FFFFFF")
        c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BORDER
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 32


def style_body(ws, r0, r1, c1):
    for r in range(r0, r1 + 1):
        for c in range(1, c1 + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = F()
            cell.border = BORDER


# --------------------------------------------------------------------------- data
df = pd.read_excel(EXPORT)
rts = df[df["Level 3 Group"].str.contains("RTS", na=False) & (df["Item Type"] == "Account")].copy()
rts["Month"] = rts["Occurred_On"].dt.strftime("%b %y")
rts = rts.sort_values(["Location", "Item Number", "Data Type", "Occurred_On"])


def s(x):
    return "" if pd.isna(x) else x


def d(x):
    return "" if pd.isna(x) else x.strftime("%Y-%m-%d")


wb = Workbook()
wb.properties.creator = ""
wb.properties.lastModifiedBy = ""
wb.properties.title = ""

# --------------------------------------------------------------------------- Accounts tab
wa = wb.active
wa.title = "Accounts"
cols = ["Location", "Account", "Account Style", "Data Type", "Supplier", "Opened On", "Replaced On",
        "Month", "kWh", "Actual %", "Accrued %", "Factor Name", "Factor (kg/kWh)",
        "Scope 2 reported (t)", "Other reported (t)", "Total reported (t)",
        "Expected (t) = kWh x factor", "Variance (t)", "Factor vintage", "Source account", "Source kWh",
        "Mirror check", "Check"]
widths = [30, 34, 24, 26, 16, 11, 11, 8, 13, 8, 8, 40, 9, 11, 11, 11, 13, 10, 11, 26, 13, 12, 22]
header(wa, 1, cols, widths)
wa.freeze_panes = "C2"

r = 2
for _, x in rts.iterrows():
    acct = str(x["Item Number"])
    is_cert = x["Data Type"] == "Certificates - Location [kWh]"
    src = acct[:-6] if acct.endswith("_CERTS") else ""
    fname = s(x["Factor Name"])
    fval = x["Factor Value (kgCO2e/unit)"]
    vals = [x["Location"], acct, s(x["Account Style/Component"]), x["Data Type"], s(x["Supplier"]),
            d(x["Opened_On"]), d(x["Replaced_On"]), x["Month"], round(float(x["Total Data"]), 4),
            s(x["Actual Percent"]), s(x["Accrued Percent"]), fname, s(fval),
            s(x["Scope 2 CO2e(t)"]), s(x["Other CO2e(t)"]), s(x["Total CO2e(t)"])]
    for ci, v in enumerate(vals, 1):
        wa.cell(row=r, column=ci, value=v)
    # Expected CO2e and variance against what Envizi reported
    wa.cell(row=r, column=17, value=f'=IF(M{r}="","",I{r}*M{r}/1000)')
    wa.cell(row=r, column=18, value=f'=IF(Q{r}="","",Q{r}-N(P{r}))')
    # Factor vintage: the year in the factor name for electricity, or the LGC vintage
    wa.cell(row=r, column=19, value=(
        f'=IF(L{r}="","",IF(ISNUMBER(SEARCH("25-26",L{r})),"25-26",IF(ISNUMBER(SEARCH("24-25",L{r})),"24-25","other")))'))
    wa.cell(row=r, column=20, value=src)
    if is_cert and src:
        wa.cell(row=r, column=21, value=(
            f'=SUMIFS($I:$I,$B:$B,T{r},$H:$H,H{r},$D:$D,"Electricity [kWh]")'))
        wa.cell(row=r, column=22, value=f'=IF(ABS(I{r}-U{r})<0.5,"Mirrors source","kWh differs from source")')
    else:
        wa.cell(row=r, column=21, value="")
        wa.cell(row=r, column=22, value="")
    # Overall check
    wa.cell(row=r, column=23, value=(
        f'=IF(AND(R{r}<>"",ABS(R{r})>0.05),"CO2e not kWh x factor",'
        f'IF(V{r}="kWh differs from source","Virtual meter not mirroring",'
        f'IF(AND(D{r}="Certificates - Location [kWh]",S{r}="24-25"),"Certificate on 24-25 factor","OK")))'))
    r += 1
last = r - 1
style_body(wa, 2, last, len(cols))
for rr in range(2, last + 1):
    for c in (9, 21):
        wa.cell(row=rr, column=c).number_format = "#,##0"
    for c in (14, 15, 16, 17, 18):
        wa.cell(row=rr, column=c).number_format = "#,##0.00;(#,##0.00);-"
    wa.cell(row=rr, column=13).number_format = "0.00"
wa.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{last}"
rng = f"W2:W{last}"
wa.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"OK"'], fill=GREEN))
wa.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Certificate on 24-25 factor"'], fill=AMBER))
wa.conditional_formatting.add(rng, FormulaRule(formula=[f'AND(W2<>"OK",W2<>"Certificate on 24-25 factor")'], fill=RED))
wa.conditional_formatting.add(f"V2:V{last}", CellIsRule(operator="equal", formula=['"Mirrors source"'], fill=GREEN))
wa.conditional_formatting.add(f"V2:V{last}", CellIsRule(operator="equal", formula=['"kWh differs from source"'], fill=RED))
wa.cell(row=1, column=17).comment = Comment(
    "kWh x factor / 1000. Envizi puts electricity in Scope 2 and certificate credits in Other, "
    "so the comparison is against Total reported.", "")
wa.cell(row=1, column=21).comment = Comment(
    "For a _CERTS virtual account: the Electricity [kWh] on its source account in the same month. "
    "The two must be equal - the virtual meter copies its source at 100%.", "")

# --------------------------------------------------------------------------- Summary tab
ws = wb.create_sheet("Summary", 0)
ws.column_dimensions["A"].width = 34
for col in "BCDEFGH":
    ws.column_dimensions[col].width = 13
ws["A1"] = "RTS - market-based electricity check, Mar-Aug 26"
ws["A1"].font = F(bold=True, size=14)
ws["A2"] = ("Source: Envizi electricity export taken 6 Sep 26 (Electricity Data as of 060926.xlsx), accounts only, "
            "Level 3 Group = Rail & Transit Systems (RTS). Chart figures are the Scope 1 & 2 monthly values read "
            "off the GHG Emissions YTD dashboard.")
ws["A2"].font = F(italic=True, color="595959")
ws["A2"].alignment = WRAP
ws.merge_cells("A2:H2")
ws.row_dimensions[2].height = 42

ws["A4"] = "Reconciliation to the dashboard (tCO2e)"
ws["A4"].font = F(bold=True, size=11)
header(ws, 5, ["Line"] + MONTHS + ["Basis"])
ws.column_dimensions["H"].width = 60
lines = [
    ("Electricity - location-based Scope 2", 'SUMIFS(Accounts!$N:$N,Accounts!$H:$H,{m})', "Scope 2 reported, all RTS electricity accounts"),
    ("Certificates and renewable deductions (Other)", 'SUMIFS(Accounts!$O:$O,Accounts!$H:$H,{m})', "Other reported - the _CERTS virtual accounts and the Victorian 100% renewable deductions"),
    ("Electricity - market-based (Scope 2 + Other)", "{s2}+{oth}", "What the certificates leave to report"),
    ("Dashboard Scope 1 & 2 (market-based)", None, "Read off the chart; blank where the chart has no bar yet"),
    ("Dashboard less market-based electricity", "{chart}-{mkt}", "The non-electricity balance the dashboard implies (Scope 1 and anything else). Steady at ~110 t Mar-May and 86 t in Jun; 620 t in Jul"),
    ("Dashboard less location-based electricity", "{chart}-{s2}", "Same test with no certificate credit at all"),
]
rowmap = {}
for i, (lab, fml, basis) in enumerate(lines):
    rr = 6 + i
    rowmap[i] = rr
    ws.cell(row=rr, column=1, value=lab)
    for mi, m in enumerate(MONTHS):
        col = 2 + mi
        L = get_column_letter(col)
        if i == 0 or i == 1:
            ws.cell(row=rr, column=col, value="=" + fml.format(m=f'"{m}"'))
        elif i == 2:
            ws.cell(row=rr, column=col, value=f"={L}{rowmap[0]}+{L}{rowmap[1]}")
        elif i == 3:
            v = CHART.get(m)
            c = ws.cell(row=rr, column=col, value=v)
            c.font = F(color="0000FF")
            c.fill = INPUT_FILL
        elif i == 4:
            ws.cell(row=rr, column=col, value=f'=IF({L}{rowmap[3]}="","",{L}{rowmap[3]}-{L}{rowmap[2]})')
        elif i == 5:
            ws.cell(row=rr, column=col, value=f'=IF({L}{rowmap[3]}="","",{L}{rowmap[3]}-{L}{rowmap[0]})')
    ws.cell(row=rr, column=8, value=basis)
style_body(ws, 6, 11, 8)
for rr in range(6, 12):
    for col in range(2, 8):
        ws.cell(row=rr, column=col).number_format = "#,##0.0;(#,##0.0);-"
    ws.cell(row=rr, column=8).alignment = WRAP
    ws.cell(row=rr, column=8).font = F(size=9, color="595959")
ws.row_dimensions[10].height = 40
ws["A12"] = "Blue on yellow = typed in from the chart. Everything else is a formula over the Accounts tab."
ws["A12"].font = F(italic=True, size=9, color="595959")

# By-location market-based table
ws["A14"] = "Market-based electricity by RTS location (Scope 2 + Other, tCO2e)"
ws["A14"].font = F(bold=True, size=11)
header(ws, 15, ["Location"] + MONTHS + ["Jul less Jun"])
locs = sorted(rts["Location"].unique())
for i, loc in enumerate(locs):
    rr = 16 + i
    ws.cell(row=rr, column=1, value=loc)
    for mi, m in enumerate(MONTHS):
        ws.cell(row=rr, column=2 + mi, value=f'=SUMIFS(Accounts!$P:$P,Accounts!$A:$A,$A{rr},Accounts!$H:$H,"{m}")')
    ws.cell(row=rr, column=8, value=f"=F{rr}-E{rr}")
tr = 16 + len(locs)
ws.cell(row=tr, column=1, value="Total RTS")
for col in range(2, 9):
    L = get_column_letter(col)
    ws.cell(row=tr, column=col, value=f"=SUM({L}16:{L}{tr-1})")
    ws.cell(row=tr, column=col).font = F(bold=True)
ws.cell(row=tr, column=1).font = F(bold=True)
style_body(ws, 16, tr, 8)
for rr in range(16, tr + 1):
    for col in range(2, 9):
        ws.cell(row=rr, column=col).number_format = "#,##0.0;(#,##0.0);-"
    ws.cell(row=rr, column=1).font = F(bold=(rr == tr))
    for col in range(2, 9):
        ws.cell(row=rr, column=col).font = F(bold=(rr == tr))
ws.conditional_formatting.add(f"B16:G{tr-1}", CellIsRule(operator="lessThan", formula=["0"], fill=RED))
ws.conditional_formatting.add(f"H16:H{tr-1}", CellIsRule(operator="greaterThan", formula=["20"], fill=AMBER))
ws.cell(row=tr + 1, column=1, value="Red = a location netting below zero (over-credited). Amber = July more than 20 t above June.").font = F(italic=True, size=9, color="595959")

# Findings
fr = tr + 3
ws.cell(row=fr, column=1, value="What I found").font = F(bold=True, size=11)
findings = [
    "1. The three RTS virtual certificate accounts (Auburn x2, Maryborough QGGG000010) are calculating as set up: each mirrors its "
    "source kWh exactly in July and August, opened 1 Jul 26, no June row, and CO2e = kWh x factor. See Accounts, Check column.",
    "2. Market-based electricity for RTS FELL in July, from 471.9 t (Jun) to 166.3 t, because those three accounts started crediting on "
    "1 July. The July spike on the dashboard is not coming from the market-based electricity as it stands in the 6 Sep export.",
    "3. The 8 Sep refresh brought July down from 928 t to 786 t (the CS Energy accounts at Maryborough and Torbanlea closing at 30 Jun "
    "removed their July accruals), but July is still ~230 t above June when the electricity says it should be ~300 t below. The gap "
    "(~510 t over the Mar-Jun non-electricity run-rate) is close to the two new certificate accounts not being credited at all: Auburn "
    "204.8 t + Maryborough 196.8 t = 401.6 t, plus Torbanlea's high first Engie bill (+56 t). HCMT's deduction IS credited every month "
    "and the only structural difference is its factor - LGCs Victoria 25-26 - against the new accounts' 24-25 vintage. If the dashboard's "
    "market-based measure only picks up current-year factors, moving the accounts to 25-26 LGC factors fixes both this and item 4. Scope 1 "
    "is not in this repo, so a genuine July gas or fuel movement cannot be ruled out.",
    "4. All three certificate accounts are on 24-25 LGC factors (NSW -0.66, QLD -0.71) against electricity on 25-26 (0.64, 0.67), so "
    "each site nets slightly below zero: Auburn -6.2 t, Maryborough -11 t before the foundry issue. Needs the 25-26 LGC factors (already open).",
    "5. Maryborough is over-credited by ~95 t a month. The certificate account copies the gross NMI figure (277,212 kWh) but the location "
    "nets out the CQMS foundry deduction (-141,380 kWh), so the location reports -103 t in July and -106 t in August. Either the virtual "
    "meter follows the net figure or the deduction stops - a Category Management call, and material to the RTS number.",
    "6. Maryborough QGGG000320 has nothing recording since 30 Jun 26 (no Engie account yet). The interval meter reads 12,413 kWh in July and "
    "10,262 in August, about 8 t and 7 t of uncounted location-based emissions.",
    "7. Torbanlea - QTMP is a named exclusion, so no certificate account is correct. Its Engie account's first bill is 248,502 kWh for July, "
    "51% above June's 164,454 and well above August's 170,055 - worth confirming the bill period with Engie before relying on July.",
    "8. Two meter oddities at Auburn that do not affect the account-based emissions: the NEMMCO meter on 4103713125 reads exactly twice the "
    "account every month (as Wingfield does), and sub-meter DWR_MSB-5-LATHE reads 601,436 kWh in July against 3 kWh in June - about 385 t "
    "at the NSW factor, which is almost exactly the dashboard's June-to-July increase. If the dashboard reads meters as well as accounts, "
    "that is the spike.",
    "9. Cardiff - Rail (CleanPeak, small market), HCMT, Calder Park, Anzac Square and Hornsby are not in the renewal register. HCMT and Calder "
    "Park net to zero through their Victorian 100% renewable deductions on the 25-26 factor, which is correct.",
]
for i, t in enumerate(findings):
    c = ws.cell(row=fr + 1 + i, column=1, value=t)
    c.alignment = WRAP
    c.font = F()
    ws.merge_cells(start_row=fr + 1 + i, start_column=1, end_row=fr + 1 + i, end_column=8)
    ws.row_dimensions[fr + 1 + i].height = 58

# --------------------------------------------------------------------------- Sites tab
wsit = wb.create_sheet("Sites")
scols = ["Location", "NMI", "Register decision", "Contracted retailer", "Source account (Jul 26)", "Source style",
         "Certificate account", "Built?", "Factor on certificate", "Electricity factor", "Jul 26 kWh (source)",
         "Jul 26 location-based (t)", "Jul 26 certificate credit (t)", "Jul 26 location market-based (t)", "Status", "Note"]
header(wsit, 1, scols, [28, 12, 30, 12, 26, 20, 30, 8, 16, 16, 13, 13, 13, 14, 14, 70])
wsit.freeze_panes = "B2"
sites = [
    ("Auburn", "4103713125", "Create - virtual certificate account", "Origin", "50002617957_4103713125", "Electricity Large Market",
     "50002617957_4103713125_CERTS", "LGCs NSW 24-25", "77 - Electricity - 25-26 - New South Wales",
     "Mirrors source. On the 24-25 LGC factor, so it over-offsets by ~3% (-5.7 t in July)."),
    ("Auburn", "4103711576", "Create - virtual certificate account", "Origin", "50002617965_4103711576", "Electricity Large Market",
     "50002617965_4103711576_CERTS", "LGCs NSW 24-25", "77 - Electricity - 25-26 - New South Wales",
     "Mirrors source. Same factor vintage issue (-0.5 t in July). Usage fell from 204,615 kWh in Mar to 3,263 in May and is 26,500 in Jul."),
    ("Maryborough", "QGGG000010", "Create - virtual certificate account", "Engie", "900018200_QGGG000010", "Electricity Small Market",
     "900018200_QGGG000010_CERTS", "LGCs QLD 24-25", "79 - Electricity - 25-26 - Queensland",
     "Mirrors the gross NMI figure. The CQMS foundry deduction (-141,380 kWh) sits at the same location, so the site nets to about -103 t. "
     "Gross vs net is the open Category Management question. Also on the 24-25 factor (-0.71 vs 0.67)."),
    ("Maryborough", "QGGG000320", "Hold - no open account on the NMI", "Engie", "", "",
     "", "", "79 - Electricity - 25-26 - Queensland",
     "CS Energy account 1003082 closed 30 Jun 26, no Engie account yet. Meter reads 12,413 kWh in July and 10,262 in August - uncounted."),
    ("Torbanlea - QTMP", "3053253239", "Exclude - named site (QTMP)", "Engie", "900018201_3053253239", "Electricity Small Market",
     "", "", "79 - Electricity - 25-26 - Queensland",
     "No certificate account is correct for a named exclusion. July's Engie bill is 248,502 kWh against 164,454 in June and 170,055 in "
     "August - confirm the bill period. Old CS Energy account 1003571 closed 30 Jun 26 in the 5 Sep extract."),
    ("Cardiff - Rail", "ZZZZ001261", "Not in the renewal register", "CleanPeak", "700000536_ZZZZ001261", "Electricity Small Market",
     "", "", "77 - Electricity - 25-26 - New South Wales",
     "Small market on CleanPeak, tenant deduction of -104,582 kWh in July. Location-based only; nothing to check for certificates."),
    ("HCMT -  East Pakenham Depot", "", "Not in the renewal register", "", "68_Electricity – purchased from grid", "Purchased from grid",
     "HCMT 100% Renewable Deduction", "LGCs Victoria 25-26", "78 - Electricity - 25-26 - Victoria",
     "Deduction mirrors the grid account and the factor vintages match, so the site nets to zero every month. Correct."),
    ("Calder Park Light Service Facility", "", "Not in the renewal register", "", "Grid Electricity", "Purchased from grid",
     "Calder Park 100% Renewable Electricity", "LGCs Victoria 25-26", "78 - Electricity - 25-26 - Victoria",
     "As HCMT. Nets to zero. Correct."),
]
for i, st in enumerate(sites):
    rr = 2 + i
    loc, nmi, dec, ret, src, sty, cert, cfac, efac, note = st
    wsit.cell(row=rr, column=1, value=loc)
    wsit.cell(row=rr, column=2, value=nmi)
    wsit.cell(row=rr, column=3, value=dec)
    wsit.cell(row=rr, column=4, value=ret)
    wsit.cell(row=rr, column=5, value=src)
    wsit.cell(row=rr, column=6, value=sty)
    wsit.cell(row=rr, column=7, value=cert)
    wsit.cell(row=rr, column=8, value=(f'=IF(G{rr}="","n/a",IF(COUNTIFS(Accounts!$B:$B,G{rr})>0,"Yes","No"))'))
    wsit.cell(row=rr, column=9, value=cfac)
    wsit.cell(row=rr, column=10, value=efac)
    wsit.cell(row=rr, column=11, value=(f'=IF(E{rr}="","",SUMIFS(Accounts!$I:$I,Accounts!$B:$B,E{rr},Accounts!$H:$H,"Jul 26",Accounts!$D:$D,"Electricity [kWh]"))'))
    wsit.cell(row=rr, column=12, value=f'=SUMIFS(Accounts!$N:$N,Accounts!$A:$A,A{rr},Accounts!$H:$H,"Jul 26")')
    wsit.cell(row=rr, column=13, value=f'=SUMIFS(Accounts!$O:$O,Accounts!$A:$A,A{rr},Accounts!$H:$H,"Jul 26")')
    wsit.cell(row=rr, column=14, value=f"=L{rr}+M{rr}")
    status = {0: "Factor vintage", 1: "Factor vintage", 2: "Over-credited", 3: "Nothing recording", 4: "Confirm bill", 5: "OK", 6: "OK", 7: "OK"}[i]
    c = wsit.cell(row=rr, column=15, value=status)
    c.fill = INPUT_FILL
    wsit.cell(row=rr, column=16, value=note)
slast = 1 + len(sites)
style_body(wsit, 2, slast, len(scols))
for rr in range(2, slast + 1):
    wsit.cell(row=rr, column=11).number_format = "#,##0"
    for col in (12, 13, 14):
        wsit.cell(row=rr, column=col).number_format = "#,##0.0;(#,##0.0);-"
    wsit.cell(row=rr, column=16).alignment = WRAP
    wsit.cell(row=rr, column=15).fill = INPUT_FILL
    wsit.row_dimensions[rr].height = 44
dv = DataValidation(type="list", formula1='"OK,Factor vintage,Over-credited,Nothing recording,Confirm bill,Open"', allow_blank=True)
wsit.add_data_validation(dv)
dv.add(f"O2:O{slast}")
wsit.conditional_formatting.add(f"O2:O{slast}", CellIsRule(operator="equal", formula=['"OK"'], fill=GREEN))
wsit.conditional_formatting.add(f"O2:O{slast}", CellIsRule(operator="equal", formula=['"Factor vintage"'], fill=AMBER))
wsit.conditional_formatting.add(f"O2:O{slast}", CellIsRule(operator="equal", formula=['"Confirm bill"'], fill=AMBER))
wsit.conditional_formatting.add(f"O2:O{slast}", FormulaRule(formula=[f'OR(O2="Over-credited",O2="Nothing recording")'], fill=RED))
wsit.conditional_formatting.add(f"N2:N{slast}", CellIsRule(operator="lessThan", formula=["-1"], fill=RED))
wsit.conditional_formatting.add(f"H2:H{slast}", CellIsRule(operator="equal", formula=['"No"'], fill=RED))
wsit.cell(row=1, column=15).comment = Comment("Pick from the list. Yellow cells are the ones I update by hand; the rest are formulas over the Accounts tab.", "")
wsit.cell(row=slast + 2, column=1, value=(
    "Rows 2-6 are the five RTS rows in the FY26-28 renewal site register; rows 7-9 are the other RTS locations with electricity in the export. "
    "Yellow = hand-maintained status. Everything numeric is a formula over the Accounts tab.")).font = F(italic=True, size=9, color="595959")

# --------------------------------------------------------------------------- Issues tab
wi = wb.create_sheet("Issues")
icols = ["#", "Location", "Issue", "Effect on July (tCO2e)", "Action", "Owner", "Status", "Notes"]
header(wi, 1, icols, [4, 24, 60, 14, 50, 18, 12, 30])
issues = [
    ("Dashboard", "July 928 t does not reconcile to the market-based electricity in the 6 Sep export (166 t). Best fit is a refresh taken while the CS Energy accounts at Maryborough and Torbanlea were still accruing July alongside the Engie actuals, before the certificate accounts were linked.",
     282, "Refresh the dashboard from current data. If July stays high, pull RTS scope 1 (gas, fuel) for July - it is not in this repo.", "", "Open"),
    ("Maryborough", "Certificate account 900018200_QGGG000010_CERTS copies the gross NMI figure while the CQMS foundry deduction nets ~141,000 kWh off the location, so Maryborough reports about -103 t.",
     -95, "Category Management to confirm whether certificates are bought for the gross NMI or Downer's net share. If net, repoint the virtual meter or add a matching deduction on the certificate side.", "", "Open"),
    ("Auburn / Maryborough", "Certificate accounts sit on LGCs NSW 24-25 (-0.66) and LGCs QLD 24-25 (-0.71) against electricity on 25-26 (0.64, 0.67).",
     -17, "Add or map the 25-26 LGC factors for NSW and QLD (prompt 3 in the guide) and move the three accounts onto them.", "", "Open"),
    ("Maryborough", "QGGG000320: CS Energy account closed 30 Jun 26, no Engie account yet, so nothing is recording July or August. Meter shows 12,413 and 10,262 kWh.",
     -8, "Chase the Engie account for QGGG000320 through the connector, then allocate it to Maryborough.", "", "Open"),
    ("Torbanlea - QTMP", "Engie's first bill on 900018201_3053253239 is 248,502 kWh for July, 51% above June and 46% above August.",
     56, "Confirm the July bill period with Engie or Category Management; if it covers late June, split it.", "", "Open"),
    ("Auburn", "Sub-meter DWR_MSB-5-LATHE reads 601,436 kWh in July (3 kWh in June), about 385 t at the NSW factor. Meters carry no CO2e in the account export, but this matches the dashboard's June-to-July increase almost exactly.",
     0, "Check whether the RTS dashboard sums meters as well as accounts. Either way the sub-meter reading is a fault and should be raised with the Watt Watcher / metering provider.", "", "Open"),
    ("Auburn", "NEMMCO meter 4103713125 reads twice the Origin account every month (567,561 vs 283,780 kWh in July) - the Wingfield pattern.",
     0, "Note only; no effect on account-based emissions. Raise with metering if the meter is ever used for reporting.", "", "Open"),
]
for i, it in enumerate(issues):
    rr = 2 + i
    wi.cell(row=rr, column=1, value=i + 1)
    for ci, v in enumerate(it, 2):
        wi.cell(row=rr, column=ci, value=v)
ilast = 1 + len(issues)
style_body(wi, 2, ilast, len(icols))
for rr in range(2, ilast + 1):
    for col in (3, 5, 8):
        wi.cell(row=rr, column=col).alignment = WRAP
    wi.cell(row=rr, column=4).number_format = "#,##0;(#,##0);-"
    for col in (6, 7, 8):
        wi.cell(row=rr, column=col).fill = INPUT_FILL
    wi.row_dimensions[rr].height = 70
dv2 = DataValidation(type="list", formula1='"Open,In progress,Closed,Not an issue"', allow_blank=True)
wi.add_data_validation(dv2)
dv2.add(f"G2:G{ilast}")
wi.conditional_formatting.add(f"G2:G{ilast}", CellIsRule(operator="equal", formula=['"Open"'], fill=RED))
wi.conditional_formatting.add(f"G2:G{ilast}", CellIsRule(operator="equal", formula=['"In progress"'], fill=AMBER))
wi.conditional_formatting.add(f"G2:G{ilast}", FormulaRule(formula=[f'OR(G2="Closed",G2="Not an issue")'], fill=GREEN))
wi.cell(row=1, column=4).comment = Comment(
    "Approximate effect on the July RTS figure: positive = the figure is overstated by this much, negative = understated. "
    "Rounded from the Accounts tab.", "")
wi.cell(row=ilast + 2, column=1, value="Yellow = fill in as each item moves. Status is a list.").font = F(italic=True, size=9, color="595959")

for sh in wb.worksheets:
    sh.sheet_view.showGridLines = False if sh.title == "Summary" else True

wb.save(OUT)
print("wrote", os.path.abspath(OUT), "accounts rows", last - 1)
