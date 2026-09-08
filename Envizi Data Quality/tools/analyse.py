"""Envizi data-quality review, September 2026.

Reads the four exports in the repo root (never modifies them) and writes the account-level
detail CSVs that findings.md refers to.

    Setup_Virtual_Account_Relationships.csv     every virtual-account link (103 rows)
    Accounts_Incomplete_Data.csv                per account/month coverage flags, Sep 25 - Aug 26
    Extract_for_Accounts (1).csv                account master, 59,333 rows
    All Envizi data.xlsx                        every account/month record, Mar - Aug 26

Run from anywhere:  python3 analyse.py
"""
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "..", "csv")
os.makedirs(OUT, exist_ok=True)

EXPORT_START, EXPORT_END = pd.Timestamp("2026-03-01"), pd.Timestamp("2026-08-31")
FY27 = pd.Timestamp("2026-07-01")


def save(df, name):
    df.to_csv(os.path.join(OUT, name), index=False)
    print(f"  {name}: {len(df)} rows")


# ----------------------------------------------------------------------------- load
print("loading")
rel = pd.read_csv(os.path.join(ROOT, "Setup_Virtual_Account_Relationships.csv"), encoding="utf-8-sig", dtype=str)
inc = pd.read_csv(os.path.join(ROOT, "Accounts_Incomplete_Data.csv"), encoding="utf-8-sig", dtype=str)
ext = pd.read_csv(os.path.join(ROOT, "Extract_for_Accounts (1).csv"), encoding="utf-8-sig", dtype=str, low_memory=False)
data = pd.read_excel(os.path.join(ROOT, "All Envizi data.xlsx"))

# Replaced On carries a trailing space in the extract - strip before parsing or every date is NaT.
ext["rep"] = pd.to_datetime(ext["Replaced On"].str.strip(), format="%d %b %Y", errors="coerce")
ext["loc_closed"] = ext["Location"].str.startswith("_CLOSED")
# "Open" = no Replaced On (or one after the export window) and not sitting at a _CLOSED_ location.
ext["open"] = (ext["rep"].isna() | (ext["rep"] > EXPORT_END)) & ~ext["loc_closed"]
ext["Replaced On"] = ext["Replaced On"].str.strip()

for c in ["Days_In_Month", "Days_Of_Data", "Days_Mismatch"]:
    inc[c] = inc[c].astype(float)
inc["In"] = pd.to_numeric(inc["In"], errors="coerce")
inc["ps"] = pd.to_datetime(inc["Period_Starting"], format="%d %b %Y")

acc = data[data["Item Type"] == "Account"].copy()
acc["Item Number"] = acc["Item Number"].astype(str)
acc["month"] = acc["Occurred_On"].dt.strftime("%b%y")
elec = acc[acc["Data Type"] == "Electricity [kWh]"]
elec_nz = elec[elec["Total Data"] != 0]


def ident(s):
    return s.astype(str).str.split("_").str[-1].str.strip()


NMI = r"^(?:\d{10,11}|[A-Z]{2,4}\d{6,8}|[A-Z0-9]{10,11})$"
ICP = r"^\d{10}[A-Z0-9]{5}$"


def id_type(s):
    return np.where(s.str.match(ICP), "ICP", np.where(s.str.match(NMI) & s.str.contains(r"\d{5}"), "NMI", ""))


# ----------------------------------------------------------------------------- 1. certificate relationships
print("1 relationships")
e1 = ext.drop_duplicates("Account Link").set_index("Account Link")
r = rel.copy()
r["nz_copy"] = r["Virtual Account Name"].str.startswith("Copy of")
r["source_replaced_on"] = r["Source Link"].map(e1["Replaced On"])
r["source_style"] = r["Source Link"].map(e1["Account Style"])
r["source_supplier"] = r["Source Link"].map(e1["Supplier"])
r["source_location"] = r["Source Link"].map(e1["Location"])
r["identifier"] = ident(r["Source Name"])
# how many times the same source *account* (link) and the same source *name* appear
r["targets_on_same_source_link"] = r.groupby("Source Link")["Virtual Account Name"].transform("nunique")
r["targets_on_same_source_name"] = r.groupby("Source Name")["Virtual Account Name"].transform("nunique")
# other open, non-certificate electricity accounts on the same identifier
ids = ext[ext["Data Type"].str.contains("Electricity", na=False) & ~ext["Account Style"].str.contains("Certificates", na=False)].copy()
ids["identifier"] = ident(ids["Account Number"])
other_open = ids[ids["open"]].groupby("identifier")["Account Number"].apply(lambda x: " | ".join(sorted(set(x))))
r["open_accounts_on_identifier"] = r["identifier"].map(other_open)
# same account number at more than one open location
loc_n = ext[ext["open"]].groupby("Account Number")["Location"].nunique()
r["source_number_at_n_open_locations"] = r["Source Name"].map(loc_n).fillna(0).astype(int)
# data flow


def months_with(df, col="Item Number", loc=None):
    d = df[df["Total Data"] != 0]
    return d.groupby(col)["month"].apply(lambda x: ",".join(sorted(set(x), key=lambda m: pd.to_datetime(m, format="%b%y"))))


# Keyed on (account number, location): the same certificate name exists at two locations (Hamilton and Hastings).
tgt = acc[acc["Data Type"] == "Certificates - Location [kWh]"]
KEY = ["Item Number", "Location"]
src_m = elec_nz.groupby(KEY)["month"].apply(lambda x: ",".join(sorted(set(x), key=lambda m: pd.to_datetime(m, format="%b%y"))))
tgt_m = tgt[tgt["Total Data"] != 0].groupby(KEY)["month"].apply(lambda x: ",".join(sorted(set(x), key=lambda m: pd.to_datetime(m, format="%b%y"))))
sk = list(zip(r["Source Name"], r["source_location"]))
tk = list(zip(r["Virtual Account Name"], r["Location"]))


def look(series, keys, default=0):
    return pd.Series([series.get(k, default) for k in keys], index=r.index)


r["source_months_with_kwh"] = look(src_m, sk, "none")
r["target_months_with_kwh"] = look(tgt_m, tk, "none")
r["source_kwh_JulAug"] = look(elec[elec["Occurred_On"] >= FY27].groupby(KEY)["Total Data"].sum(), sk).round(0)
r["target_kwh_JulAug"] = look(tgt[tgt["Occurred_On"] >= FY27].groupby(KEY)["Total Data"].sum(), tk).round(0)
r["target_tco2e_JulAug"] = look(tgt[tgt["Occurred_On"] >= FY27].groupby(KEY)["Total CO2e(t)"].sum(), tk).round(2)
r["target_kwh_MarJun"] = look(tgt[tgt["Occurred_On"] < FY27].groupby(KEY)["Total Data"].sum(), tk).round(0)
r["target_tco2e_MarJun"] = look(tgt[tgt["Occurred_On"] < FY27].groupby(KEY)["Total CO2e(t)"].sum(), tk).round(2)
r["target_factor_JulAug"] = look(tgt[tgt["Occurred_On"] >= FY27].groupby(KEY)["Factor Name"].first(), tk, "")


def rel_flag(x):
    f = []
    if x["nz_copy"]:
        f.append("NZ 'Copy of' name, no Effective From")
    if pd.isna(x["Effective From YYYY-MM-DD"]) and not x["nz_copy"] and x["Rule Name"] == "100% Renewable Energy Certificates":
        f.append("AU certificate with no Effective From")
    if x["source_number_at_n_open_locations"] > 1:
        f.append("source account number exists at more than one open location")
    if pd.notna(x["source_replaced_on"]):
        f.append(f"source closed {x['source_replaced_on']}")
    if x["source_months_with_kwh"] == "none":
        f.append("source has no kWh in Mar-Aug 26 export")
    elif x["source_kwh_JulAug"] > 0 and x["target_kwh_JulAug"] == 0 and x["Rule Name"] == "100% Renewable Energy Certificates":
        f.append("source has Jul/Aug kWh but certificate account has none")
    if x["Rule Name"] == "100% Renewable Energy Certificates" and x["target_kwh_MarJun"] != 0:
        f.append("certificate credited before 1 Jul 26")
    return "; ".join(f) if f else "OK"


r["flags"] = r.apply(rel_flag, axis=1)
cols1 = ["Location", "Virtual Account Name", "Virtual Account Link", "Relationship Link", "Rule Name", "Rule Formula", "Variable Name",
         "Source Name", "Source Link", "Source Apportionment", "Effective From YYYY-MM-DD", "Effective To YYYY-MM-DD", "nz_copy",
         "source_style", "source_supplier", "source_location", "source_replaced_on", "identifier", "targets_on_same_source_link",
         "targets_on_same_source_name", "source_number_at_n_open_locations", "open_accounts_on_identifier", "source_months_with_kwh",
         "target_months_with_kwh", "source_kwh_JulAug", "target_kwh_JulAug", "target_tco2e_JulAug", "target_kwh_MarJun",
         "target_tco2e_MarJun", "target_factor_JulAug", "flags"]
save(r[cols1].sort_values(["Rule Name", "Location"]), "01_virtual_account_relationships_checked.csv")

# the Hamilton / Hastings ICP, month by month at each location
h = acc[acc["Item Number"].str.contains("0000024050WE5E2")]
h = h.pivot_table(index=["Location", "Item Number", "Data Type", "Account_Meter_Link"], columns="month", values=["Total Data", "Total CO2e(t)", "Accrued Percent"], aggfunc="sum").round(1)
h.columns = [f"{a}_{b}" for a, b in h.columns]
save(h.reset_index(), "01b_icp_0000024050WE5E2_by_location.csv")

# ----------------------------------------------------------------------------- 2. apportionment over 100%
print("2 apportionment")
ap = ext[ext["Usage Type"].notna()].copy()
ap["pct"] = ap["Apportionment"].astype(float)
ap["ef"] = ap["Effective From"].fillna("")
ap["et"] = ap["Effective To"].fillna("")
s = ap.groupby(["Account Link", "Account Number", "Location", "Account Style", "ef", "et"]).agg(
    rules=("pct", "size"), total_pct=("pct", "sum"), usage_types=("Usage Type", lambda x: " | ".join(x)), uses=("Use", lambda x: " | ".join(x))).reset_index()
s = s.rename(columns={"ef": "Effective From", "et": "Effective To"})
s["exceeds_100"] = s["total_pct"] > 100.0001
s["same_usage_type_twice"] = s["usage_types"].apply(lambda u: len(u.split(" | ")) != len(set(u.split(" | "))))
save(s[s["rules"] > 1].sort_values("total_pct", ascending=False), "02_extract_accounts_with_multiple_apportionment_rules.csv")
# virtual accounts with more than one relationship (the Cardiff pattern)
m = rel.groupby(["Location", "Virtual Account Name", "Virtual Account Link"]).agg(
    relationships=("Relationship Link", "size"), rules=("Rule Name", lambda x: " | ".join(x)), variables=("Variable Name", lambda x: " | ".join(x)),
    formulas=("Rule Formula", lambda x: " | ".join(x)), sources=("Source Name", lambda x: " | ".join(x)), apportionment=("Source Apportionment", lambda x: " | ".join(x)),
    effective_from=("Effective From YYYY-MM-DD", lambda x: " | ".join(x.fillna("blank")))).reset_index()
m = m[m["relationships"] > 1]
m["same_variable_twice"] = m["variables"].apply(lambda v: len(v.split(" | ")) != len(set(v.split(" | "))))
save(m, "02b_virtual_accounts_with_multiple_relationships.csv")
# Cardiff tenant share check
c = acc[(acc["Location"] == "Cardiff - Rail") & (acc["Data Type"] == "Electricity [kWh]")]
cp = c.pivot_table(index="Item Number", columns="month", values="Total Data", aggfunc="sum").round(0)
save(cp.reset_index(), "02c_cardiff_electricity_by_month.csv")

# ----------------------------------------------------------------------------- 3. NZ certificates undated
print("3 NZ certificates")
nz = r[r["nz_copy"]].copy()
src_by_m = elec.groupby(KEY + ["month"])["Total Data"].sum()
tgt_by_m = tgt.groupby(KEY + ["month"])["Total CO2e(t)"].sum()
order = ["Mar26", "Apr26", "May26", "Jun26", "Jul26", "Aug26"]
for mo in order:
    nz[f"source_kwh_{mo}"] = [round(src_by_m.get((a, l, mo), 0)) for a, l in zip(nz["Source Name"], nz["source_location"])]
    nz[f"certificate_tco2e_{mo}"] = [round(tgt_by_m.get((a, l, mo), 0), 2) for a, l in zip(nz["Virtual Account Name"], nz["Location"])]
nz["credit_before_FY27_tco2e"] = nz[[f"certificate_tco2e_{m}" for m in order[:4]]].sum(axis=1).round(2)
nz["monthly_run_rate_tco2e"] = (nz["credit_before_FY27_tco2e"] / 4).round(2)
nzf = tgt[tgt["Item Number"].str.startswith("Copy of")]["Factor Value (kgCO2e/unit)"].dropna().iloc[0]
nz["FY27_credit_missing_JulAug_tco2e"] = (-(nz["source_kwh_Jul26"] + nz["source_kwh_Aug26"]) * nzf / 1000).round(2)
cols3 = ["Location", "Virtual Account Name", "Source Name", "Effective From YYYY-MM-DD", "source_supplier", "source_replaced_on"] + \
    [f"source_kwh_{m}" for m in order] + [f"certificate_tco2e_{m}" for m in order] + ["credit_before_FY27_tco2e", "monthly_run_rate_tco2e", "FY27_credit_missing_JulAug_tco2e", "flags"]
save(nz[cols3].sort_values("credit_before_FY27_tco2e"), "03_nz_certificates_undated.csv")

# ----------------------------------------------------------------------------- 4. days covered > days in month
print("4 days > month")
ov = inc[inc["Days_Of_Data"] > inc["Days_In_Month"]].copy()
ov["is_revenue"] = ov["Data Type"].str.contains("Revenue")
key = acc["Item Number"] + "|" + acc["Location"] + "|" + acc["Occurred_On"].dt.strftime("%Y-%m")
dk = acc.assign(key=key).groupby("key").agg(export_qty=("Total Data", "sum"), export_tco2e=("Total CO2e(t)", "sum"), export_total_days=("Total Days", "max"))
ov["key"] = ov["Account_Number"] + "|" + ov["Location"] + "|" + ov["ps"].dt.strftime("%Y-%m")
ov = ov.join(dk, on="key")
ov["excess_share"] = ((ov["Days_Of_Data"] - ov["Days_In_Month"]) / ov["Days_Of_Data"]).round(3)
ov["est_excess_qty"] = (ov["export_qty"] * ov["excess_share"]).round(1)
ov["est_excess_tco2e"] = (ov["export_tco2e"] * ov["excess_share"]).round(3)
rows4 = ["Location", "Account_Number", "Supplier", "Data Type", "Replaced_On", "Period_Starting", "Days_In_Month", "Days_Of_Data", "Days_Mismatch", "In", "Units",
         "export_qty", "export_tco2e", "export_total_days", "excess_share", "est_excess_qty", "est_excess_tco2e", "is_revenue"]
save(ov[rows4].sort_values(["is_revenue", "Days_Of_Data"], ascending=[True, False]), "04b_days_exceed_month_rows.csv")
g4 = ov[~ov["is_revenue"]].groupby(["Location", "Account_Number", "Supplier", "Data Type", "Replaced_On"], dropna=False).agg(
    months_flagged=("ps", "nunique"), first_month=("ps", "min"), last_month=("ps", "max"), max_days_of_data=("Days_Of_Data", "max"),
    months_in_export=("export_tco2e", "count"), export_qty=("export_qty", "sum"), export_tco2e=("export_tco2e", "sum"),
    est_excess_qty=("est_excess_qty", "sum"), est_excess_tco2e=("est_excess_tco2e", "sum")).reset_index()
g4["first_month"] = g4["first_month"].dt.strftime("%b %y")
g4["last_month"] = g4["last_month"].dt.strftime("%b %y")
save(g4.round(2).sort_values("est_excess_tco2e", ascending=False), "04_days_exceed_month_by_account.csv")
rv = inc[inc["Data Type"].str.contains("Revenue")].pivot_table(index=["Location", "Account_Number"], columns=inc["ps"].dt.strftime("%b%y"), values="Days_Of_Data", aggfunc="sum")
rv["records_per_month"] = (rv.div(inc.groupby(inc["ps"].dt.strftime("%b%y"))["Days_In_Month"].first(), axis=1).max(axis=1)).round(0)
save(rv.reset_index(), "04c_revenue_accounts_records_per_month.csv")

# ----------------------------------------------------------------------------- 5. empty extract columns
print("5 extract columns")
files = {"Extract_for_Accounts (1).csv (07 Sep 26)": os.path.join(ROOT, "Extract_for_Accounts (1).csv"),
         "Extract_for_Accounts 05 Sep 26.csv": os.path.join(ROOT, "FY27", "Extract_for_Accounts 05 Sep 26.csv"),
         "Extract_for_Accounts 03 Sep 26.csv": os.path.join(ROOT, "FY27", "Extract_for_Accounts 03 Sep 26.csv"),
         "Extract_for_Accounts 26 Aug 26.csv": os.path.join(ROOT, "FY27", "Extract_for_Accounts 26 Aug 26.csv")}
rows5 = []
for name, p in files.items():
    d = pd.read_csv(p, encoding="utf-8-sig", dtype=str, low_memory=False)
    for col in d.columns:
        rows5.append(dict(extract=name, rows=len(d), column=col, populated=int(d[col].notna().sum()), populated_pct=round(100 * d[col].notna().mean(), 1)))
save(pd.DataFrame(rows5), "05_extract_column_population.csv")

# ----------------------------------------------------------------------------- 6. unallocated
print("6 unallocated")
u = ext[ext["Location"].str.contains("nalloc", case=False, na=False)].drop_duplicates("Account Link").copy()
du = acc[acc["Location"].str.contains("nalloc", case=False, na=False)]
dq = du.groupby(["Item Number", "Location"]).agg(export_qty=("Total Data", "sum"), export_tco2e=("Total CO2e(t)", "sum"), export_months=("Occurred_On", "nunique"))
u = u.join(dq, on=["Account Number", "Location"])
u["export_qty"] = u["export_qty"].fillna(0).round(1)
u["export_tco2e"] = u["export_tco2e"].fillna(0).round(3)
u["export_months"] = u["export_months"].fillna(0).astype(int)
u["group"] = np.where(u["Location"] == "Unallocated Cleanaway", "Cleanaway waste", "Other unallocated")
cols6 = ["group", "Location", "Account Number", "Account Reference", "Supplier", "Account Style", "Data Type", "Opened On", "Replaced On", "open", "Updated On", "export_months", "export_qty", "export_tco2e"]
save(u[cols6].sort_values(["group", "Location", "Supplier", "Account Style"]), "06_unallocated_accounts.csv")
save(u.groupby(["group", "Location", "Supplier", "Account Style"], dropna=False).agg(accounts=("Account Link", "size"), open=("open", "sum"), export_tco2e=("export_tco2e", "sum")).reset_index().round(2),
     "06b_unallocated_summary.csv")

# ----------------------------------------------------------------------------- 7. duplicate identifiers
print("7 duplicate identifiers")
elstyles = ["Electricity Large Market", "Electricity Small Market", "Electricity – purchased from grid [kWh]", "Electricity Simple", "Electricity Green",
            "Energetics - Large Market", "Energetics - Small Market"]
el = ext[ext["Account Style"].isin(elstyles)].copy()
el["identifier"] = ident(el["Account Number"])
el["id_type"] = id_type(el["identifier"])
v = el[el["id_type"] != ""].copy()
ml = elec_nz.groupby(["Item Number", "Location"])["month"].apply(lambda x: set(x))
v["months"] = [ml.get((a, l), set()) for a, l in zip(v["Account Number"], v["Location"])]
rows7 = []
for i, grp in v.groupby("identifier"):
    if len(grp) < 2:
        continue
    opens = grp[grp["open"]]
    allm = list(grp["months"])
    ovm = set()
    for a in range(len(allm)):
        for b in range(a + 1, len(allm)):
            ovm |= allm[a] & allm[b]
    om = list(opens["months"])
    oov = set()
    for a in range(len(om)):
        for b in range(a + 1, len(om)):
            oov |= om[a] & om[b]
    if len(opens) > 1 and oov:
        cls = "Live double count - both open, data in the same months"
    elif ovm:
        cls = "Overlap in the export, but one side now carries a Replaced On"
    elif len(opens) > 1:
        cls = "Both open, only one recording"
    else:
        cls = "Legitimate succession - closed predecessor plus live replacement"
    sur_t = sur_k = 0.0
    for mo in ovm:
        sub = elec_nz[elec_nz["Item Number"].isin(grp["Account Number"]) & (elec_nz["month"] == mo)]
        if len(sub) > 1:
            sur_t += sub["Total CO2e(t)"].sum() - sub["Total CO2e(t)"].max()
            sur_k += sub["Total Data"].sum() - sub["Total Data"].max()
    srt = lambda ms: ",".join(sorted(ms, key=lambda m: pd.to_datetime(m, format="%b%y")))
    rows7.append(dict(identifier=i, id_type=grp["id_type"].iloc[0], n_accounts=len(grp), n_open=int(len(opens)),
                      accounts=" | ".join(grp["Account Number"]), locations=" | ".join(grp["Location"]),
                      suppliers=" | ".join(grp["Supplier"].fillna("").astype(str)), account_styles=" | ".join(grp["Account Style"]),
                      replaced_on=" | ".join(grp["Replaced On"].fillna("open")), months_with_kwh=" | ".join(srt(m) if m else "none" for m in grp["months"]),
                      overlap_months=srt(ovm), surplus_kwh=round(sur_k), surplus_tco2e=round(sur_t, 2), classification=cls))
dup = pd.DataFrame(rows7)
order7 = {"Live double count - both open, data in the same months": 0, "Overlap in the export, but one side now carries a Replaced On": 1, "Both open, only one recording": 2,
          "Legitimate succession - closed predecessor plus live replacement": 3}
dup["o"] = dup["classification"].map(order7)
save(dup.sort_values(["o", "surplus_tco2e"], ascending=[True, False]).drop(columns="o"), "07_duplicate_nmi_icp.csv")

# ----------------------------------------------------------------------------- 8. data after Replaced On
print("8 replaced on")
a8 = acc.copy()
a8["rep"] = pd.to_datetime(a8["Replaced_On"])
after = a8[a8["rep"].notna() & (a8["Occurred_On"] > a8["rep"]) & (a8["Total Data"] != 0)]
g8 = after.groupby(["Location", "Item Number", "Account Style/Component", "Supplier", "Category", "Replaced_On"], dropna=False).agg(
    months_after=("Occurred_On", "nunique"), first=("Occurred_On", "min"), last=("Occurred_On", "max"), qty=("Total Data", "sum"), tco2e=("Total CO2e(t)", "sum")).reset_index()
g8["first"] = g8["first"].dt.strftime("%b %y")
g8["last"] = g8["last"].dt.strftime("%b %y")
g8["identifier"] = ident(g8["Item Number"])
g8["other_open_accounts_on_identifier"] = g8["identifier"].map(other_open)
save(g8.round(2).sort_values("tco2e", ascending=False), "08_data_after_replaced_on.csv")

# ----------------------------------------------------------------------------- 9. open accounts with no records
print("9 no records")
has = set(zip(acc[acc["Total Data"] != 0]["Item Number"], acc[acc["Total Data"] != 0]["Location"]))
anyrow = set(zip(acc["Item Number"], acc["Location"]))
o = ext[ext["open"]].drop_duplicates("Account Link").copy()
o["k"] = list(zip(o["Account Number"], o["Location"]))
o["rows_in_export"] = o["k"].isin(anyrow)
o["nonzero_in_export"] = o["k"].isin(has)
live = set(acc[(acc["Total Data"] != 0) & (acc["Occurred_On"] >= FY27)]["Supplier"].dropna().astype(str))
o["supplier_feed_live_JulAug"] = o["Supplier"].astype(str).isin(live)
o["is_spend_account"] = o["Data Type"].str.contains(r"\[USD\]|\[AUD|\[NZD", regex=True, na=False)
nr = o[~o["nonzero_in_export"]].copy()
cols9 = ["Location", "Account Number", "Account Reference", "Data Type", "Account Style", "Supplier", "Opened On", "Replaced On", "Updated On",
         "rows_in_export", "supplier_feed_live_JulAug", "is_spend_account"]
save(nr[cols9].sort_values(["is_spend_account", "supplier_feed_live_JulAug", "Data Type", "Supplier"]), "09_open_accounts_no_records.csv")
save(nr.groupby(["is_spend_account", "supplier_feed_live_JulAug", "Data Type"]).size().reset_index(name="accounts").sort_values("accounts", ascending=False),
     "09b_open_accounts_no_records_summary.csv")

# ----------------------------------------------------------------------------- 10. waste with no factor
print("10 waste factors")
w = acc[acc["Category"].isin(["Waste", "Waste Recycled", "Landfill", "No Recovery"])].copy()
w["has_factor"] = w["Factor Value (kgCO2e/unit)"].notna()
g10 = w.groupby(["Category", "Account Style/Component", "Supplier", "has_factor"], dropna=False).agg(accounts=("Item Number", "nunique"), rows=("Total Data", "size"), qty=("Total Data", "sum"), tco2e=("Total CO2e(t)", "sum")).reset_index().round(1)
save(g10.sort_values("qty", ascending=False), "10_waste_factor_coverage.csv")

# ----------------------------------------------------------------------------- 11. certificates not flowing
print("11 certificates not flowing")
# A location's reporting boundary comes from its Classification membership (locations also carry a
# Portfolio membership, so filtering on Group_Type matters). Certificates at Y_Non Operational Control
# locations have nothing to offset - the inventory never carries those emissions.
locs = pd.read_csv(os.path.join(ROOT, "FY27", "Extract_for_Locations 26 Aug 26.csv"), encoding="utf-8-sig", dtype=str)
cls = locs[locs["Group_Type"] == "Classification"].drop_duplicates("Location_Name").set_index("Location_Name")["Group Level 1"]
r["location_boundary"] = r["Location"].map(cls).fillna("Not in locations extract")
nf = r[(r["Rule Name"] == "100% Renewable Energy Certificates") & (r["target_kwh_JulAug"] == 0)]
save(nf[cols1 + ["location_boundary"]], "11_certificate_accounts_with_no_FY27_data.csv")
save(r[r["Rule Name"] == "100% Renewable Energy Certificates"].groupby(
    ["location_boundary", "nz_copy"]).size().reset_index(name="certificate_accounts"),
    "11b_certificates_by_reporting_boundary.csv")

print("done")
