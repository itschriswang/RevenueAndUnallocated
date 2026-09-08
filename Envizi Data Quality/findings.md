# Envizi data quality review — September 2026

Built from the four exports in the repo root, taken 7 Sep 26: `Setup_Virtual_Account_Relationships.csv`
(103 virtual-account links), `Accounts_Incomplete_Data.csv` (5,254 account-months, Sep 25 – Aug 26),
`Extract_for_Accounts (1).csv` (59,333 accounts) and `All Envizi data.xlsx` (107,304 account-months, Mar –
Aug 26, every category). Nothing in those files was changed. The account-level detail behind every
section is in `csv/`, and `tools/analyse.py` regenerates it.

Two things about how I read the files, because several conclusions depend on them:

- **"Open"** means no Replaced On (or one after 31 Aug 26) *and* not at a `_CLOSED_` location. Replaced On
  in the extract carries a trailing space; parse it without stripping and every account looks open.
- **Materiality** is measured on the Mar – Aug 26 data export only. Anything before March is invisible to
  me, so where a problem is older than that I give the run-rate and say so.

The six leads I was given did not all survive contact with the data. Three are confirmed and larger than
described (NZ certificates, days-over-month, unallocated), one is real but different in shape (the
Hamilton/Hastings ICP), one is a report limitation rather than a data fault (empty extract columns), and
one is not a problem at all (Cardiff apportionment). The wider sweep added the biggest items on the list.

## Executive summary

Ranked by what it does to the reported number.

| # | Issue | Accounts | Effect on Mar – Aug 26 figures | Action |
| --- | --- | --- | --- | --- |
| 1 | **Waste carries no emission factor.** Only two of 29 waste styles have one; 7,105 t of waste and 230,000 t of recycling report 0 tCO2e. | 571 waste + 317 recycled accounts | Scope 3 waste understated; indicatively ~3,200 tCO2e on general landfill alone if the 1.3 t/t C&I factor applied | Map factors to the waste styles, starting with `Waste (general solid) to landfill [t]` |
| 2 | **NZ certificates are undated and have stopped.** 22 `Copy of …_CERTS` accounts credit all history and produce nothing from July. | 22 | –395.8 t credited Mar – Jun (≈ –99 t/month, back to whenever the sources start); ~203 t of FY27 credit missing for Jul – Aug | Set Effective From 2026-07-01, rename, and find out why no Jul/Aug rows exist |
| 3 | **19 AU certificate accounts have nothing to mirror.** Their source accounts hold zero rows for all six months — 18 PPP sites on Origin/CS Energy plus Tamworth. | 19 | FY27 renewable claim for PPP Schools 2, SICEEP, HQJOC, Southbank TAFE and SCUH is currently zero, and so is their electricity | Chase the feeds; these are dead supplier accounts, not certificate faults |
| 4 | **Bitumen – Taranaki gas is double-covered.** 62 days recorded in 31-day months for 11 straight months. | 1 (+62 smaller) | ≈ 237 t overstated over five export months; 63 accounts in total, ≈ 299 t | Delete the overlapping gas records; fix the recurring NZ depot electricity overlaps |
| 5 | **Mackay's live account is marked replaced.** `A-11525536_3053135053` has Replaced On 1 Apr 26 and is the only Ergon account still recording. | 8 | 128 t of Apr – Aug electricity sits on a "closed" account; 50 t at Archerfield and Gympie is a genuine May double count | Clear Mackay's Replaced On; delete the May records on the two `5000021_` accounts |
| 6 | **Closed CS Energy accounts still carry overlapping data.** Setting Replaced On did not remove the Apr – Jun records at five QLD sites. | 5 NMIs, 10 accounts | 83.7 t double counted in FY26 (Apr – Jun) | Delete the overlap months on the closed accounts |
| 7 | **Same ICP at two NZ locations.** `Eco_ICP_0000024050WE5E2` is a live account at both Hamilton and Hastings, each with its own certificate account. | 2 (+3 other pairs) | 237,174 kWh / 24 t double counted Mar – Jul; net of certificates ≈ 4.6 t, but from July the Hastings copy is uncredited | Close the Hastings copy and its certificate account |
| 8 | **194 t at unallocated locations.** 1,698 accounts sit at six "Unallocated" locations; 1,587 are Cleanaway waste. | 1,698 | 82 t (BOC/Viva at Unallocated Accounts) + 113 t (E&U fuel) in the export are in no division's number | Allocate the 111 non-Cleanaway accounts; the Cleanaway ones report zero anyway until #1 is fixed |
| 9 | **121 open electricity and gas accounts have no data at all**, 119 of them on suppliers whose feeds are otherwise live (Origin 23, AGL 21, EnergyAustralia 9, Meridian 7). | 121 | Unknown — no consumption is recorded | Confirm each is really dead and close it, or chase the retailer |
| 10 | **Extract columns are empty by design of the report, not the data.** Cost centre and relationship columns are blank across all four extracts since 26 Aug while 103 relationships exist. | — | None on reported figures; the extract cannot be used to audit relationships | Re-run the extract with relationship and cost-centre output enabled, or keep using the relationships export |
| 11 | **Cardiff apportionment is fine.** The "two rules at 100%" are one kWh rule and one cost rule on the same tenant account; the tenant share is a steady 40.4%. Only one account in the extract exceeds 100% and it does so across two different usage types. | 0 | None | No action; note the extract's per-usage-type apportionment rows |

Two things I could not settle from these files and have left as assumptions: whether Envizi's reports exclude
data recorded after an account's Replaced On (the export does not, so I have assumed reports do not either),
and whether the pre-July NZ certificate credit was intended (Ecotricity is a renewable retailer, so it may be
right in substance even though the relationships are undated).

---

## 1. Waste has no emission factor

**What it is.** In the Mar – Aug export, 1,958 of 2,048 `Waste` rows, all 1,085 `Waste Recycled` rows and
all 73 `Landfill` / `No Recovery` rows have a blank factor and zero CO2e in every scope column. The only
waste styles carrying a factor are `Waste General (kg)` (1.3 kg/kg, six rows at Unitywater Noosa) and
`Waste - Commercial and Industrial - [t]` (1,300 kg/t, 84 rows, all zero quantity). Cleanaway supplies 2,824
of the unfactored rows.

**Scale.** 7,104.7 t of waste with no factor, of which 2,470 t is `Waste (general solid) to landfill [t]`
across 1,141 rows, 2,641 t asbestos to landfill and 690 t commingled. Recycling styles add 229,963 t, of
which 229,313 t is `RAP used [t]` — recycled asphalt, which arguably should not carry a landfill factor at
all. Applying the C&I factor already in the system (1.3 tCO2e/t) to general landfill alone gives roughly
3,200 tCO2e over six months. That is indicative only; the correct factors are per NGA waste type.

**Assumption.** Waste is a Scope 3 category and may sit outside the Scope 1 & 2 dashboards, which is why it
has not shown up as a spike anywhere. It still means the waste inventory is zero.

**Action.** Map factors to the waste styles, general solid landfill first, then check whether the
Cleanaway load is landing on styles that will never carry a factor. Detail: `csv/10_waste_factor_coverage.csv`.

## 2. NZ certificate accounts — undated, and silent since June

**What it is.** All 22 NZ certificate relationships are still named `Copy of Eco_ICP_…_CERTS` and have no
Effective From, against 69 AU ones dated 2026-07-01. The 12 other blank-dated rows are the Cardiff tenant
apportionments and the two Victorian 100% renewable deductions, which are meant to apply to history.

**Retrospective credit.** 21 of the 22 accounts hold data in the export (the 22nd,
`Eco_ICP_0141534532LCA70`, has a zero-kWh source). Between them they credited **–395.8 tCO2e** across Mar –
Jun 26 on the `RECs NZ - 2026` factor (–0.101 kg/kWh), a run-rate of **–99 t a month**. The source accounts
were set up in Dec 2023, so if their history is full the retrospective credit is of the order of 30 months
at that rate, roughly –3,000 t; I can only see four of those months.

**The bigger surprise.** None of the 22 has a July or August row, while 20 of their sources recorded
2,008,386 kWh across those two months. The AU certificate accounts do have July and August rows, so it is
not the export. On the `RECs NZ - 2026` factor that is **≈ 203 t of FY27 credit missing** so far, growing
by ~100 t a month.

**Assumption.** I have assumed the missing rows are the factor: `RECs NZ - 2026` is the only NZ certificate
factor in the export and its name suggests a calendar or fiscal 2026 bound. If it ends 30 Jun 26 and there
is no successor, Envizi has nothing to calculate and writes no row. The README already notes the AU LGC
factors were rebuilt on 8 Sep with 26-27 rows; the NZ REC factor needs the same treatment.

**Action.** Date all 22 relationships 2026-07-01, drop the `Copy of` prefix, add the FY27 NZ REC factor, and
then decide whether the pre-July credit stands (Ecotricity is renewable, so it may be right) or is removed.
Detail: `csv/03_nz_certificates_undated.csv`.

## 3. Nineteen AU certificate accounts with nothing to mirror

**What it is.** Of the 71 AU relationships on the `100% Renewable Energy Certificates` rule, 50 are
producing July and August credits (5,032,008 kWh, –3,298.5 t). The other 19 have no rows at all because
their **source accounts have no rows at all** for Mar – Aug 26: the twelve PPP NSW Schools 2 sites, the four
SICEEP accounts and HQJOC (all Origin), Southbank TAFE and Sunshine Coast University Hospital (CS Energy),
plus Tamworth, whose Origin source last recorded in March.

**Why it matters.** These are the large-market PPP sites, and it is not a certificate problem: the
electricity itself is missing from the inventory for six months. Whatever the cause (feed not switched to
the new Origin contract, connector not mapped), the FY27 renewable claim for those sites is zero and so is
their Scope 2.

**Action.** Treat as dead supplier feeds and chase Origin / CS Energy through the connector. The
certificate accounts are correctly built and will start mirroring the moment data lands. Detail:
`csv/11_certificate_accounts_with_no_FY27_data.csv` (the 22 NZ rows from §2 are in the same file).

Also worth knowing: the export still shows every AU certificate on a **24-25 factor** in July and August
(NSW/ACT –0.66, QLD –0.71, SA –0.23, Tas –0.15) while electricity is on 25-26. That predates the 8 Sep
factor rebuild noted in the Large Market Certificates README, so the next export should show 26-27.

## 4. Days of data exceeding days in the month

**What it is.** The incomplete-data report flags 481 account-months where Days_Of_Data exceeds
Days_In_Month. 180 of those are revenue accounts and are expected (below). The remaining 301 rows sit on
**63 metered accounts**: 53 electricity, 9 natural gas, one hydrogen.

**Porirua.** `_CLOSED_Porirua CCWRT` (`UN0001_Electricity - Purchased from grid`) shows 83, 93, 84 and then
196 days across Dec 25 – Mar 26, then a –231 kWh March record and 470 kWh in April, after its 31 Mar
Replaced On. It is real but immaterial (–0.02 t).

**Where the tonnes are.** Estimating the overstatement as the over-covered share of each month's CO2e
(`(Days_Of_Data − Days_In_Month) / Days_Of_Data`):

| Account | Pattern | Months flagged | Est. excess |
| --- | --- | --- | --- |
| Bitumen – Taranaki `3045_Natural Gas` | 62 days every month, Sep 25 – Jul 26 | 11 | **237 t** (of 475 t in the export) |
| RPQ NSW Chinderah `A-7098FD44_4407159044` | up to 93 days | 7 | 13 t |
| Wharf Road Coromandel `9009_…` | up to 124 days | 9 | 5 t |
| Cardiff – Rail `700000536_ZZZZ001261` | 32 days in May | 1 | 4.5 t |
| 27 NZ depot electricity accounts (`55xxx_`, `91xxx_`) | 60 – 568 days, most months | 1 – 10 each | 30 t combined |
| Remaining 32 | | | 9 t |

Total ≈ 299 t over the export window. Taranaki is a single gas account being loaded twice each month
(two 31-day records) and is worth fixing first. The NZ depot pattern — `MMA 883005` peaks at 568 days in
a 30-day month — looks like overlapping invoice periods on manually loaded accounts, so each month's bill
is landing on top of the previous estimate rather than replacing it.

**Revenue accounts are different.** 27 of 64 `FY26REV_` / `FY27REV_` accounts show 2 – 8 records per
month (Government & IFM 248 days in a 31-day month = 8 records). That is the sub-LOB revenue load
putting several lines on one account each month; it is how the load is designed, and the sum is right.
The report will keep flagging them, so treat the revenue rows in this report as noise.

**Assumption.** The data export's `Total Days` for fuel accounts sums record-days across every transaction
in the month (Telco – Recharge shows 78,926 days), so I have not used it as an overlap test outside
metered categories.

**Action.** Delete the duplicate gas records at Taranaki; review the 27 NZ depot accounts for the
estimate-then-actual pattern and set them to replace rather than append. Detail:
`csv/04_days_exceed_month_by_account.csv`, rows in `04b_…`, revenue pattern in `04c_…`.

## 5. Data recorded after Replaced On

**What it is.** Eight accounts hold non-zero records in months after their Replaced On date.

| Account | Replaced On | Data after | Qty | tCO2e | Reading |
| --- | --- | --- | --- | --- | --- |
| Asphalt Prod – Mackay `A-11525536_3053135053` | 1 Apr 26 | May – Aug 26 | 191,183 kWh | 128.1 | The **only** Ergon account still recording at Mackay (the other two were replaced Jun 24 and Jan 26). The Replaced On is wrong, not the data. |
| Archerfield `5000021_QB05383854` | 31 Mar 26 | May 26 | 64,727 kWh | 43.4 | Alongside `1003081_QB05383854` — a genuine May double count |
| Gympie `5000021_3120129028` | 31 Mar 26 | May 26 | 10,718 kWh | 7.2 | Same pattern |
| Five closed-project fuel / Porirua rows | Dec 25 – Mar 26 | | | 2.9 | Trailing transactions |

**Assumption.** The data export includes these records, so I have assumed Envizi's reports do too; if a
report *does* honour Replaced On, Mackay's 128 t is currently dropping out of the inventory instead.

**Action.** Clear Mackay's Replaced On (or set it to the date the replacement actually starts recording);
delete the May records on the two `5000021_` accounts. Detail: `csv/08_data_after_replaced_on.csv`.

## 6. Duplicate NMIs and ICPs

**How I tested it.** For the 1,430 electricity accounts whose number ends in something shaped like an NMI or
ICP, I grouped by that identifier and compared the months each account holds kWh in the export.

| Classification | Identifiers |
| --- | --- |
| Legitimate succession — a closed predecessor and one live account, no shared months | 430 |
| Overlap in the export, but one side now carries a Replaced On | 5 |
| Live double count — more than one open account with data in the same months | 4 |
| Both open, only one recording | 3 |

**The five that overlap despite being closed** are the QLD CS Energy switch: Archerfield (`5000021_` vs
`1003081_`, May, 43.4 t), Teneriffe (Apr – May, 16.9 t), MT-Carrara (Apr – May, 8.7 t), Richlands (Apr –
Jun, 7.5 t) and Gympie (May, 7.2 t). Setting Replaced On closed the accounts but left the overlapping
months in place — **83.7 t of FY26 double count** that will stay until the records are deleted.

**The four live double counts:**

- `0000024050WE5E2` — Hamilton / Hastings, §7 below. 237,174 kWh, 24.0 t.
- `3036098256` — RPQ Mackay Depot, two open Ergon accounts (`A-313CFBA6`, `A-9F0E2528`) both recording
  Jun – Aug. 5,471 kWh, 3.7 t. One should be replaced.
- `0003140222AAD30` — the same bare-ICP Meridian account at *68 Ihumatao Road Mangere* and *Downer Cranes
  Auckland*, both recording May – Aug. 10,287 kWh, 1.0 t. One location is wrong.
- `ZZZZ001261` — Cardiff's tenant deduction shares the NMI with its source by design. Not a double count.

**Both open, only one recording:** `0088966150PCC88` (Ahititi / Urenui, neither recording),
`ICP_1000620792PC805` (Roadmarking Lower South / Tauriko West, only Tauriko recording) and four Ergon
accounts on `3051446111` at RPQ Townsville, none recording. Tidy-ups, no tonnes.

Detail, all 442 identifiers: `csv/07_duplicate_nmi_icp.csv`.

## 7. One ICP, two locations, two certificate accounts (Hamilton / Hastings)

**What the lead said.** That `Eco_ICP_0000024050WE5E2` feeds two virtual accounts at 100% each and overlaps
in all 24 months.

**What the data says.** There is no source *account* feeding two targets anywhere in the relationships
file — every Source Link is unique. What exists is two **separate** accounts with the same number:
`Eco_ICP_0000024050WE5E2` at Asphalt Prod – Hamilton (link 6223426, set up Dec 2023) and again at Hastings
Depot (link 6391000, set up Nov 2025), each with its own `Copy of …_CERTS` virtual account. The ICP's `WE`
prefix is a Waikato network code, so Hamilton is the real site.

Both accounts are 100% accrued every month. Hamilton's accruals move (44,968 – 52,667 kWh); Hastings'
alternate between exactly 48,669.12 and 47,099.15 kWh with the same two cost figures, which is an
accrual pattern with no bill behind it. Hastings recorded Mar – Jul (237,174 kWh, 24.0 t) and nothing in
August. Its certificate account offset –19.4 t of that through June, so the net pre-July effect is small;
from July the Hastings copy is uncredited (§2) and counts in full.

The incomplete-data report shows overlap only in Sep 25 at Hamilton (60 days), not 24 months; the report
only covers 12.

**Action.** Close the Hastings `Eco_ICP_0000024050WE5E2` and its certificate account and delete their
records. Detail: `csv/01b_icp_0000024050WE5E2_by_location.csv`; the same check across all 103
relationships is `csv/01_virtual_account_relationships_checked.csv`, where the `flags` column also picks
up the six Cardiff tenant rules whose sources closed between 2020 and 2025 (historical, no action).

## 8. Unallocated accounts

**The 1,698.** The extract has six locations whose name contains "Unallocated":

| Location | Accounts | Open | tCO2e in export |
| --- | --- | --- | --- |
| Unallocated Cleanaway | 1,587 | 1,221 | 0.0 (no factor, §1) |
| `_CLOSED_Unallocated JDE Accounts` | 77 | 0 | 0 |
| Unallocated Accounts | 15 | 13 | **81.7** |
| E&U Unallocated fuel expenses | 10 | 10 | **112.6** |
| `_CLOSED_FY24 Interim_Unallocated Scope 3 Category 2` | 6 | 0 | 0 |
| Unallocated Plant OSM | 3 | 0 | 0 |

**The 111 that are not Cleanaway**, by supplier: Subcontractor 53 (all diesel, all at the closed JDE
location), Downer 19, BOC 12, Downer manual entry 8, Finance 6, blank 6, Fuel Card 3, FTC Finance Report 2,
Air Liquide 1, Viva 1. By style: diesel transport 60, acetylene 7, petrol 5, LPG stationary 5, diesel
stationary 4, electricity 3, lubricants 3, the rest ones and twos.

**What is actually live.** Only two of the six locations hold data in the export: `Unallocated Accounts`
(six BOC/Viva stationary accounts, 81.7 t) and `E&U Unallocated fuel expenses` (nine manual-entry fuel
accounts, 112.6 t). The two FTC accounts still at Unallocated Accounts (`16017960_Diesel`, `170944_Petrol`)
hold no data; the FTC move has otherwise landed — the 2,713 FTC accounts sit at `Fuel Cards - …`
locations, with 209 at `Unmapped AU Fuel Cards`.

**Cleanaway.** 1,587 accounts across 27 waste styles, 1,221 still open, none with a factor, so they carry no
CO2e wherever they sit. The allocation is a housekeeping job until §1 is fixed, at which point it becomes
a scope 3 allocation job. Detail: `csv/06_unallocated_accounts.csv` and `06b_…summary.csv`.

## 9. Open accounts with no records

**Scope.** 23,437 accounts are open. 8,054 have non-zero data in Mar – Aug 26; 10,637 appear only as zero
rows; 4,746 have no rows at all. So **15,383 open accounts recorded nothing** in six months.

**Most of that is design.** 14,622 are activity accounts on suppliers whose feeds are otherwise live:
10,405 per-subcontractor diesel placeholders, 990 Cleanaway, 755 FTC fuel cards, 686 Downer manual, 551
WEX. They exist so a transaction has somewhere to land. 569 are on suppliers with nothing live in Jul –
Aug, 65 of them the historical `LGCS_` accounts, and 192 are spend (Scope 3) accounts.

**The ones to chase.** 121 open electricity and gas accounts with no data. 119 are on suppliers that are
delivering elsewhere — Origin 23, AGL 21, EnergyAustralia 9, Meridian 7, plus a handful on Downer, CS
Energy, Ergon, Ecotricity and Shell — and two are HorizonPower, which has no live data at all. The 18 PPP
accounts in §3 are among the Origin/CS Energy ones. Detail: `csv/09_open_accounts_no_records.csv`
(15,383 rows) and `09b_…summary.csv`.

## 10. The empty extract columns

Eleven columns — `Cost Centre Group Chain`, `Cost Centre`, `Report Percent`, the cost-centre dates and
description, `Relationship`, `Related Account`, `Relationship Percent` and the relationship dates — are
blank in **all 59,333 rows**, and were equally blank in the 26 Aug, 3 Sep and 5 Sep extracts
(`csv/05_extract_column_population.csv`).

That is the report, not the data. The relationships export lists 103 live relationships, so `Relationship`
/ `Related Account` have things to show and show none. The same extract does populate its other optional
block — `Usage Type`, `Use` and `Apportionment` on 12,040 rows, with a second row per account where two
usage types apply — so it is emitting per-account sub-tables when they are switched on. **Assumption:** the
Envizi account extract only returns the relationship and cost-centre sections when those options are
selected at run time, and they have not been. For cost centres I cannot prove either way; nothing in any
of the four files, or in the locations extract, references a cost centre, so they may simply be unused.

**Action.** Re-run the extract with the relationship and cost-centre options on and check one account that
is known to have a relationship (`50002617957_4103713125_CERTS`). Until then the relationships export is
the only audit trail for virtual meters.

## 11. Apportionment over 100% — not confirmed

**Cardiff.** `Tenant 700000536_ZZZZ001261` and `Tenant Electricity_Cardiff Rail` each have two relationship
rows at 100%, but they are two *different rules on different variables*: `Cardiff Tenant Apportionment` on
kilowatt-hours (`(-{6000020})*{6000021}`) and `Cardiff Electricity Apportionment` on total cost
(`-({6000024})*{6000025}`). One rule gives the tenant account its kWh, the other its cost. The result is a
tenant deduction of a steady 40.4% of the source every month (–104,582 of 258,867 kWh in July), which is a
single share, not a doubled one. `Electricity_Cardiff Rail` itself was replaced in Feb 2023 and has no
data, so its two rules are dormant. Neither `700000536_ZZZZ001261` nor `Electricity_Cardiff Rail` has an
apportionment row in the account extract at all.

**The extract.** Across the 12,040 apportionment rows, 28 accounts carry two rows. One sums past 100%:
`HIGGINS CONTRACTORS` at *113 - Hawkins Limited CENTRAL_Other Subcontractors*, 100% `Consolidation` plus
100% `Decarbonisation Pathway`. **Assumption:** usage types are separate reporting lenses (the other 27
two-row accounts pair the same two types and sum to 100 because the pathway row is 0%), so this is a
pathway-view setting, not a double count in the consolidated number. Worth a look because it is the only
one, but no tonnes attach to it. Detail: `csv/02_…`, `02b_…`, `02c_…`.

---

## Files

| File | Rows | What it is |
| --- | --- | --- |
| `csv/01_virtual_account_relationships_checked.csv` | 103 | Every relationship with source status, data flow and a `flags` column |
| `csv/01b_icp_0000024050WE5E2_by_location.csv` | 4 | The Hamilton / Hastings ICP month by month |
| `csv/02_extract_accounts_with_multiple_apportionment_rules.csv` | 2 | Extract accounts with two apportionment rows |
| `csv/02b_virtual_accounts_with_multiple_relationships.csv` | 2 | The two Cardiff tenant accounts |
| `csv/02c_cardiff_electricity_by_month.csv` | 2 | Cardiff source and tenant kWh |
| `csv/03_nz_certificates_undated.csv` | 22 | NZ certificates: credit by month, FY27 credit missing |
| `csv/04_days_exceed_month_by_account.csv` | 63 | Metered accounts over-covered, with estimated excess |
| `csv/04b_days_exceed_month_rows.csv` | 481 | Every flagged account-month, revenue included |
| `csv/04c_revenue_accounts_records_per_month.csv` | 64 | Records per month on the revenue accounts |
| `csv/05_extract_column_population.csv` | 140 | Column fill rates across the four extracts |
| `csv/06_unallocated_accounts.csv` | 1,698 | Every account at an Unallocated location |
| `csv/06b_unallocated_summary.csv` | 67 | The same by location, supplier and style |
| `csv/07_duplicate_nmi_icp.csv` | 442 | Every identifier on more than one account, classified |
| `csv/08_data_after_replaced_on.csv` | 8 | Accounts recording after their Replaced On |
| `csv/09_open_accounts_no_records.csv` | 15,383 | Open accounts with no non-zero data Mar – Aug 26 |
| `csv/09b_open_accounts_no_records_summary.csv` | 129 | The same by data type and feed status |
| `csv/10_waste_factor_coverage.csv` | 43 | Waste styles with and without a factor |
| `csv/11_certificate_accounts_with_no_FY27_data.csv` | 41 | Certificate accounts with no July / August rows |
| `tools/analyse.py` | — | Regenerates everything above from the four exports |
