"""Build FY27_Electricity_Budget_Forecast_Email.html - the FY27 market-based electricity
forecast by business unit, from the 6 Sep 26 electricity export.

Reads   ../../Electricity Data as of 060926.xlsx   (repo root)
Writes  ../FY27_Electricity_Budget_Forecast_Email.html

Accounts only (meters are the feed behind them), Operational Control only. Market-based =
Scope 2 + Other, because Envizi puts the certificate credits in Other CO2e. The FY27 figure is
the Jul-Aug 26 average x 12 - a run-rate, not a model - and the caveats under the table say
what will move it.
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXPORT = os.path.join(ROOT, "Electricity Data as of 060926.xlsx")
OUT = os.path.join(HERE, "..", "FY27_Electricity_Budget_Forecast_Email.html")

df = pd.read_excel(EXPORT)
a = df[(df["Item Type"] == "Account") & (df["Level 1 Group"] == "Operational Control")].copy()
a["Month"] = a["Occurred_On"].dt.strftime("%b %y")
a["BU"] = a["Level 3 Group"].str.extract(r"\((.*?)\)")[0].fillna(a["Level 3 Group"])
a["Mkt"] = a["Scope 2 CO2e(t)"].fillna(0) + a["Other CO2e(t)"].fillna(0)
a["Loc"] = a["Scope 2 CO2e(t)"].fillna(0)
a["Cred"] = a["Other CO2e(t)"].fillna(0)

MONTHS = ["Jun 26", "Jul 26", "Aug 26"]


def pick(mask):
    s = a[mask]
    out = {m: s.loc[s.Month == m, "Mkt"].sum() for m in MONTHS}
    out["avg"] = (out["Jul 26"] + out["Aug 26"]) / 2
    out["fy27"] = out["avg"] * 12
    out["loc_avg"] = s.loc[s.Month.isin(["Jul 26", "Aug 26"]), "Loc"].sum() / 2
    out["cred_avg"] = s.loc[s.Month.isin(["Jul 26", "Aug 26"]), "Cred"].sum() / 2
    return out


AU, NZ = a.Country == "Australia", a.Country == "New Zealand"
rows = [
    ("T&I - Australia", pick((a.BU == "T&I") & AU), "sub"),
    ("T&I - New Zealand", pick((a.BU == "T&I") & NZ), "sub"),
    ("T&I total", pick(a.BU == "T&I"), "group"),
    ("RTS", pick(a.BU == "RTS"), ""),
    ("EU (AU, NZ and overseas)", pick(a.BU == "EU"), ""),
    ("SICS", pick(a.BU == "SICS"), ""),
    ("Corporate (AU and NZ)", pick(a.BU == "Corporate"), ""),
    ("Total market-based", pick(a.BU.notna()), "total"),
]
tot = rows[-1][1]
ti_au, ti_nz = rows[0][1], rows[1][1]

# Supporting figures quoted in the notes
nz_cred_jun = -a[(NZ) & (a["Data Type"] == "Certificates - Location [kWh]") & (a.Month == "Jun 26")]["Cred"].sum()
nz_cred_jul = -a[(NZ) & (a["Data Type"] == "Certificates - Location [kWh]") & (a.Month == "Jul 26")]["Cred"].sum()
au_certs_jul = a[(AU) & (a["Data Type"] == "Certificates - Location [kWh]") & (a.Month == "Jul 26")]["Item Number"].nunique()
au_certs_jun = a[(AU) & (a["Data Type"] == "Certificates - Location [kWh]") & (a.Month == "Jun 26")]["Item Number"].nunique()


def n(v):
    v = round(v)
    return f"({abs(v):,})" if v < 0 else f"{v:,}"


TD = 'style="padding:4px 8px;border:1px solid #bfbfbf;text-align:right;white-space:nowrap"'
TDL = 'style="padding:4px 8px;border:1px solid #bfbfbf"'
TH = 'style="padding:5px 8px;border:1px solid #bfbfbf;background:#1F3864;color:#fff;text-align:right"'
THL = TH.replace("right", "left")

html_rows = []
for label, r, kind in rows:
    style = ""
    if kind == "group":
        style = "background:#D9E1F2;font-weight:bold"
    elif kind == "total":
        style = "background:#1F3864;color:#fff;font-weight:bold"
    elif kind == "sub":
        label = "&nbsp;&nbsp;&nbsp;" + label
    cells = "".join(f"<td {TD}>{n(r[m])}</td>" for m in MONTHS)
    html_rows.append(
        f'<tr style="{style}"><td {TDL}>{label}</td>{cells}'
        f'<td {TD}>{n(r["avg"])}</td><td {TD}><b>{n(r["fy27"])}</b></td></tr>'
    )
html_rows.append(
    f'<tr style="color:#595959;font-style:italic"><td {TDL}>of which: location-based Scope 2 (before certificates)</td>'
    + "".join(f"<td {TD}>{n(a[(a.Month == m)]['Loc'].sum())}</td>" for m in MONTHS)
    + f'<td {TD}>{n(tot["loc_avg"])}</td><td {TD}>{n(tot["loc_avg"] * 12)}</td></tr>'
)
html_rows.append(
    f'<tr style="color:#595959;font-style:italic"><td {TDL}>of which: certificate and renewable credits</td>'
    + "".join(f"<td {TD}>{n(a[(a.Month == m)]['Cred'].sum())}</td>" for m in MONTHS)
    + f'<td {TD}>{n(tot["cred_avg"])}</td><td {TD}>{n(tot["cred_avg"] * 12)}</td></tr>'
)

body = f"""<div style="font-family:Arial,Helvetica,sans-serif;font-size:11pt;color:#000">
<p>Hi all,</p>

<p>Below is the FY27 electricity emissions forecast for the budget, on the market-based method, by
business unit. I have split T&amp;I into Australia and New Zealand because the two are on different
renewable arrangements and are moving in opposite directions at the moment. The last row is the
total market-based figure.</p>

<p>The numbers come from the Envizi electricity export taken 6 Sep 26, Operational Control accounts
only. June is the last month before the renewal agreements started; July and August are the first two
months under them. The FY27 column is the July&ndash;August average multiplied by 12, so it is a
run-rate rather than a model, and the notes under the table say what will move it.</p>

<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;font-size:10pt">
<tr><th {THL}>tCO2e, market-based</th><th {TH}>Jun 26</th><th {TH}>Jul 26</th><th {TH}>Aug 26</th><th {TH}>Jul&ndash;Aug avg / month</th><th {TH}>FY27 forecast (avg &times; 12)</th></tr>
{''.join(html_rows)}
</table>

<p style="font-size:9pt;color:#595959">Market-based = Scope 2 + Other CO2e as reported by Envizi; the
certificate credits sit in Other. Brackets are credits. Figures are rounded to the tonne, so the sub-rows may not add exactly.</p>

<p><b>What the table is telling us</b></p>
<ul>
<li><b>T&amp;I Australia has come down from about {n(ti_au['Jun 26'])} t a month to about {n(ti_au['avg'])} t.</b>
{au_certs_jul} certificate accounts are now crediting against the large market sites (there were {au_certs_jun} before July).
17 permanent accounts and 9 temporary ones are still to be built, so the run-rate will fall further once those are in.</li>
<li><b>T&amp;I New Zealand has gone the other way, from about {n(ti_nz['Jun 26'])} t to about {n(ti_nz['avg'])} t a month.</b>
This is not real. The 21 Ecotricity certificate accounts are still mirroring their kWh, but the NZ REC factor
(<i>RECs NZ - 2026</i>) has no value from 1 July, so the credit that was worth about {n(nz_cred_jun)} t in June is
{n(nz_cred_jul)} t in July and August. Category Management confirmed all NZ electricity is renewable from 1 Jul 26
(TOU on Ecotricity now, NTOU from 1 Jan 27), so once a FY27 NZ factor is loaded and the NTOU sites are set up, the
NZ figure should be close to zero. For the budget I would carry NZ at the June level or lower, not the July run-rate.</li>
<li><b>The July and August Australian figures are still overstated.</b> Fourteen old retailer accounts are accruing
alongside the Engie accounts that replaced them (about 367 t a month across the two months, mostly T&amp;I
asphalt sites), and they carry no certificate credit. They are being closed off at 30 Jun 26, which takes that out.</li>
<li><b>Two things go the other way.</b> Most Australian certificate accounts are on 24-25 LGC factors against
25-26 electricity factors, so they over-credit by about 3% until the 25-26 factors are loaded, and the Maryborough
account in RTS copies the gross NMI figure while the CQMS foundry deduction nets the location, which over-credits RTS by
about 95 t a month until the gross-or-net question is settled.</li>
<li><b>NT and the named rail exclusions</b> stay on grid factors under the agreements, so they are the floor for
T&amp;I Australia and RTS.</li>
</ul>

<p>Net of all that, I would budget T&amp;I Australia and RTS somewhat below the run-rate in the table, NZ well
below it, and EU, SICS and Corporate at about the run-rate. I will refresh the table once the remaining accounts
are built and the NZ factor is in, which should be the October data.</p>

<p>Happy to walk through the workings; the source workbook and the export are in the shared folder.</p>

<p>Kind regards,<br>Chris</p>
</div>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write("<title>FY27 electricity budget forecast</title>\n" + body)
print("wrote", os.path.abspath(OUT))
for label, r, _ in rows:
    print(f"{label:32s} " + " ".join(f"{n(r[m]):>8s}" for m in MONTHS) + f" {n(r['avg']):>8s} {n(r['fy27']):>8s}")
print("nz cred jun/jul", round(nz_cred_jun, 1), round(nz_cred_jul, 1), "au certs jun/jul", au_certs_jun, au_certs_jul)
