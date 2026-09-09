# Large Market Certificates

Renewable-certificate **virtual meters** for the AU electricity sites Downer contracted under the
FY26–28 renewal agreements, and everything behind them.

## Files

| File | What it is |
| --- | --- |
| `Virtual Meter Guide/Large_Market_Virtual_Meters.html` | **Start here.** Four sections in the order I work them: **1** accounts to close, **2** virtual accounts to make, **3** sites on hold because the contracted retailer has no account yet, **4** everything with no action. Ticks and notes save in the browser. Open it by double-clicking. |
| `Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx` | The review workbook: all 81 register rows with live formulas, the 69 accounts on `Prep` and the load tab (kept as the record of what each account looks like — **not uploaded**, see below), plus the `Manual Setup Checklist` and `LGCS Accounts to Check` tabs. The `Account_Setup_and_Data_Load_-_PM&C_` prefix is what Envizi processes on if a load is ever needed. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28.xlsx` | The renewal agreement site register (scope, retailers, contract dates) and the rate schedules with the LGC lines. |
| `Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` | The same workbook with the Envizi account mapping added to `Site Register` as columns V–AE, and an `Envizi mapping notes` tab explaining them. Everything left of column V is untouched. |
| `ElectricityEnviziSummaryjunejulyaug26.xlsx` | The Jun–Aug 26 Envizi summary — kWh, actual/accrued split, cost, CO2e and the green component. |
| `RTS_Market_Based_Check_Jul26.xlsx` | The RTS (Rail & Transit Systems) market-based check for Mar–Aug 26, built from the 6 Sep 26 electricity export. `Summary` reconciles the electricity to the RTS Scope 1 & 2 dashboard month by month, `Accounts` re-derives every CO2e from kWh × factor and checks each `_CERTS` account mirrors its source, `Sites` is the register rows for the RTS sites, `Issues` is the worklist. See [RTS check](#rts-check--the-july-spike) below. |

The accounts and locations extracts it reads are in `../FY27/` (`Extract_for_Accounts 05 Sep 26.csv`,
`Extract_for_Locations 26 Aug 26.csv`). Two Jun–Aug 26 energy exports sit one folder up: `../Electricity
download after bathurst and mogo virual accounts.xlsx` (4 Sep 26, the first two accounts) and `../Electricity
download after the first Claude in Chrome batches.xlsx` (taken between 4 and 5 Sep 26, once 42 accounts were
live — the one the guide page now reads its month figures from).

## Scope

The **green rows** in the Site Register are the renewable ones — 78 of the 81 `AU Large Electricity`
rows, the other three being the NT sites on Jacana standing offer. A green row gets a virtual meter
unless it is a named exclusion or already offset another way. 69 accounts get built in all: 60 permanent
and 9 temporary (section 3). As of the 05 Sep 26 extract, 43 are built.

**The meter class does not decide scope.** Category Management, 4 Sep 26, on a Mogo NMI I queried:

> sometimes when you take both to a retailer they will agree to supply both as large market sites —
> that's probably what's occurred here… from a metering perspective it may be considered a small site,
> but from an electricity supply agreement perspective, it's being treated as a large site.

So `Electricity Small Market` in Envizi is the **meter** classification and does not take a site out of
the renewal; the supply agreement does, and the register's green rows record it. 25 of the 60 accounts
sit on a small-market-styled source for this reason.

| Outcome | Rows |
| --- | --- |
| **Create — virtual certificate account** | **60** — 43 built, 17 to go |
| Create — temporary, the contracted retailer has no account on the NMI yet | 9 |
| Hold — no open electricity account on the NMI at all (Maryborough QGGG000320) | 1 |
| Exclude — already renewable via the account's green component (Alinta WA) | 7 |
| Exclude — named site (NT ×3, QTMP) | 4 |
| Total register rows reviewed | 81 |

By state the 60 are: NSW 36, VIC 10, QLD 7, SA 4, TAS 2, ACT 1. The full list, with the source account
and the field values for each, is on the guide page and on the workbook's `Manual Setup Checklist` tab.

**Changed since the 05 Sep review.** The two Perth Convention & Exhibition Centre rows (register 159 and
160) move from Exclude to Create, so it is 62 permanent and 5 green-component exclusions — see
[PCEC](#pcec--the-two-wa-alinta-meters-flipped-to-create) below. The workbook, the guide page and the
table above still read the 05 Sep decision; they pick the change up on the next rebuild.

## How the sites were matched

On the connection ID, not the region. The NMI is the text after the last underscore in an Envizi account
number, so each register row is matched to the active accounts on that NMI. Of those, the source is the
one **carrying the electricity from 1 July 2026** — actual data first, large market style as the
tie-break — and the location comes from that account. All 81 rows resolved.

## Is the renewable product LGCs?

For Engie and Origin, yes: `Rates & Source Data` prices both renewal contracts with an explicit LGC line
(FY27 0.395 c/kWh Engie, 0.375 Origin; FY28 0.375) plus a "renewable product $/yr". The Alinta (WA) and
Shell (TAS) contracts are modelled as an all-in delivered rate with no separate LGC line; Category
Management confirms they are renewable, and the Alinta accounts already show 100% green kWh in Envizi.

## Progress — 42 of the 43 verified against the export

`50002617964_NAAA00AC25_CERTS` (Asphalt Prod - Bathurst) and `50002769514_4001127731_CERTS`
(Asphalt Prod - Mogo) were created on 4 Sep 26, and the rest of the 43 followed in batches through Claude in
Chrome. The second export, taken after those batches, carries 42 of the 43 accounts the 05 Sep extract lists,
and every one of them mirrors its source exactly in July and August with no June row. Bathurst's figures
have not moved since the first export (53,778 / 41,470). Against the first export:

- **Mirroring is exact** — certificate kWh equals source kWh in every month, and it follows the source
  when a bill replaces an accrual (Bathurst's August moved from an accrued 49,402 to an actual 41,470).
- **The date bound works** — both opened 2026-07-01 and carry no June record, though both sources have
  June data.
- **The factor vintage is out** — certificates use `LGCs NSW 24-25` (−0.66 kg/kWh) against electricity on
  `25-26 New South Wales` (0.64), so a 100% meter over-offsets by about 3% and Bathurst nets −1.08 t in
  July instead of zero. Victoria has an `LGCs Victoria 25-26` factor; NSW needs its 25-26 equivalent
  added or mapped **before the remaining accounts are linked**.
- **Mogo settled the scope rule** — that one was built on `50002769514_4001127731`, which Envizi styles
  small market. Querying it produced the answer quoted above, so the account is right where it is and
  the rest of the small-market-styled sites stayed in scope.

**Mogo needs a look before the last batch.** `50002769514_4001127731_CERTS` was in the first export with
July and August data, but it is in neither the second export nor the 05 Sep extract. What the extract has
instead is `50002617992_4204072845_CERTS` — the other Mogo NMI, opened 01 Jul 2026 — and that one has no
rows in the second export, so it holds no data. Either the first account was renamed onto the wrong NMI
and unlinked, or it was deleted and the 4204072845 one created empty in its place. Both NMIs are in scope
and both need an account, so the outcome wanted is: `50002617992_4204072845_CERTS` linked to
`50002617992_4204072845` (it is empty, so it can be), and `50002769514_4001127731_CERTS` created again.
Prompt 0b in the prompts file reads the state; prompt 1 has the Mogo card.

**What the second export confirms is unchanged.** None of the 14 section 1 accounts is closed (Traralgon
still reads 30 Oct 2026); no Engie account has appeared on any of the 9 Queensland NMIs; and the
certificate accounts are still on the 24-25 factors (NSW/ACT −0.66, QLD −0.71, TAS −0.15) against
electricity on 25-26 (0.64, 0.67, 0.20), so Bathurst still nets −1.08 t in July. Only Victoria has a 25-26
certificate factor (−0.78, matching its scope 2). **Since fixed (08 Sep 26):** every state now has 24-25,
25-26 and 26-27 rows with Effective From / Effective To dates, so July 2026 on should land on 26-27 — to be
confirmed in the next export.

## How the new accounts are structured

Modelled on the Ecotricity virtual accounts (`Copy of Eco_ICP_..._CERTS`) and on the two already built:

| Field | Value |
| --- | --- |
| Location | The source account's location |
| Account style | `Certificates - Location - kWh` |
| Account number | `<source account>_CERTS` — keyed on the source, because `LGCS_<NMI>` is already taken at many sites |
| Account reference | The NMI |
| Supplier | `LGC Virtual Account` |
| Reader | blank |
| Opened On | `2026-07-01` — the contract start, and what bounds the meter to the renewal period |
| Records | **none** — the account must be empty to become a virtual meter |
| Virtual meter source | The account on the card, 100% |

50 of the 70 sources have data before 1 Jul 26, which is why Opened On matters: without it the meter
mirrors those years too, generating certificates for periods that were not renewable and doubling what
the old `LGCS_` accounts already record for 2025.

## A virtual meter has to be empty — so they are made by hand

Envizi only lets an account be set up as a virtual meter while it holds no records, and the PM&C template
cannot create an account without a record. So the load tab is **not uploaded**; it stays as the record of
what each account should look like. The `Manual Setup Checklist` tab (and the guide page) is the worklist.

Per account: **1.** Create it empty with the fields above, including Opened On. **2.** Open it and set it
up as a virtual meter, source = the account on the card, 100% — that one only. **3.** Check the new
account shows kWh equal to the source and the location's market-based CO2e drops to match.

## The existing `LGCS_` accounts — leave them

54 active certificate accounts sit at 40 of the in-scope locations. Checked in Envizi on 4 Sep 26: all
hold LGC data from **2025 and earlier**, so none is empty, none can be converted to a virtual meter, and
none covers the renewal period. They stay as the historical record and the new account sits beside them.
The `LGCS Accounts to Check` tab lists them with `Has data?` pre-set to Yes; set one to No and the Action
column switches to reuse.

## Section 1 — 14 accounts to close off

On 14 NMIs a second active account is still recording the months the source account already covers, so
the site's electricity is counted twice before any certificate is applied. Together they carry
**1,223,122 kWh / 734 tCO₂e** of July and August on top of what the source accounts report. Two causes:

**Retailer switched, old account left open (12).** These moved to Engie on 1 Jul 26 and the previous
retailer's account was never closed, so it keeps accruing while the Engie account bills the actuals:
Somerton (303), Utilities Derrimut, Shepparton (308), Bayswater (302), Traralgon (300), Dandenong - PAV,
Mulgrave, Wodonga (315), Gillman - PAV, Wingfield (523) and Largs Bay ×2. Traralgon's Origin account
already carries a Replaced On — but of **30 Oct 2026**, a future date, so it is still accruing today; it
needs moving back to 30 Jun 26. (A future Replaced On used to read as closed in my checks. It doesn't now.) I checked **column M (Contracted
Retailer)** first and Engie is correct on every one — tendered to Origin, contracted to Engie,
1 Jul 26 to 30 Jun 28, 24 months. The old account gets `Replaced On` = **30 June 2026**.
Worth 1,022,053 kWh / 599 tCO₂e.

**Second connector account on the same NMI (2).** Gympie and Archerfield (406) each carry a second
CS Energy account created by the Utilities Connector, accruing with no Opened On and no actuals. Nine of
its `5000021_` siblings have already been closed off at 31 Mar, 31 May and 30 Jun 26 — these two were
missed. Worth 201,069 kWh / 135 tCO₂e. I confirm the date against how the siblings were done rather than
assuming 30 Jun.

## Section 3 — 9 temporary accounts, to be remade later

These sites are contracted to a retailer that has no account on the NMI in Envizi yet, so they are still
recording against the old supply. On the Director's call we build the certificate accounts anyway, so
the renewable claim is in the numbers from July — but every one of them is **temporary**.

**Why they get deleted rather than repointed.** The account name keys off its source, so
`1003072_3051770385_CERTS` is only right while the meter follows `1003072_3051770385`. When the
contracted retailer's account appears the source changes and the name no longer matches it, so the
account is deleted and remade against the new one. The guide page carries a **delete register** listing
each temporary account, what it follows today and what it is waiting on, with a tick per row.

**Four that were parked are now allocated and built.** Brendale (423), MT-Carrara, Maryborough
(QGGG000010) and Mowbray (360) had the contracted retailer's account sitting in `Unallocated Accounts` in
the 03 Sep extract; by 05 Sep they were at their sites, so they were built as permanent accounts against
those:

| Location | NMI | Account to allocate | Supplier |
| --- | --- | --- | --- |
| Asphalt Prod - Brendale (423) | `3120725958` | `900018199_3120725958` | EngieAU |
| MT-Carrara | `QB06081428` | `900018198_QB06081428` | EngieAU |
| Maryborough | `QGGG000010` | `900018200_QGGG000010` | EngieAU |
| Asphalt Prod - Mowbray (360) | `8000326927` | `DEDI01_088_8000326927` | ShellEnergyAU |

The nine that remain are Queensland sites contracted to Engie with no Engie account at all — the
connector has not switched them. Gympie and Archerfield are also in section 1, where their duplicate
CS Energy account needs closing regardless. **Maryborough QGGG000320 is on hold**, not temporary: its CS
Energy account was closed at 30 Jun 26 between the two extracts and no Engie account exists, so no account
is recording July or August there and there is nothing for a virtual account to follow. The site is not
idle, though — its interval meter reads 12,413 kWh in July and 10,262 in August — so the consumption is
real and simply uncounted until Engie's account arrives.

**Maryborough QGGG000010 mirrors a gross figure.** The same location carries a Downer deduction account
(`electricity deduction_CQMS foundry meter_Maryborough`) of −141,380 kWh in July and −146,260 in August,
so the location's own consumption is about half the 277,212 kWh the certificate account copies. The
contract buys certificates for the whole NMI, but the inventory nets the foundry out — whether the
virtual account should follow the net (source less deduction) is a question for Category Management
before the FY27 numbers are relied on. It is the largest of the 43 by a wide margin.

In the workbook these rows carry the decision `Create - temporary, retailer's account not in Envizi yet`.
They are shaded amber on the Review tab and they are on the load tab and `Manual Setup Checklist` with
the other 56, because they are being built.

## PCEC — the two WA Alinta meters, flipped to Create

Perth Convention & Exhibition Centre is register rows 159 and 160 (review rows 75 and 76), NMIs
8001000591 and 8001000592, both at `LSE - Perth Convention & Exhibition Centre (WA)`, Location Ref 9068.
They were two of the seven WA Alinta rows excluded because the account's own green component already
carries the offset. They are being built anyway; the other five stay excluded.

| | Source account | Jul 26 kWh | Aug 26 kWh | Green Jul–Aug | New account |
| --- | --- | ---: | ---: | ---: | --- |
| 8001000591 | `80013757_8001000591` | 174,253 | 188,584 | 348,506 | `80013757_8001000591_CERTS` |
| 8001000592 | `80013758_8001000592` | 143,301 | 143,301 | 286,600 | `80013758_8001000592_CERTS` |

Same fields as the other 60 — style `Certificates - Location - kWh`, Account Ref the NMI, supplier
`LGC Virtual Account`, Reader blank, Opened On 1 Jul 2026, one source at 100%, Effective From July 2026.
The form is **prompt 5** in the prompts file. The find that preceded it ran on 09 Sep 26 and is written
up below; the find and conversion forms are in the git history.

Two things make this pair different from anything in section 2. **The offset is already there** — the
Alinta bill books 100% green kWh on each account's own green component from July 2026, netting both to
zero; that is the open item below. And **the sources have six years of history**: both have recorded
since 1 Feb 2020, so Effective From July 2026 is doing real work here — without it the certificate
accounts reach back to 2020.

The location also holds eleven electricity accounts, nine of them closed or out of scope, and a closed
Alinta account sits on each of the two NMIs (`80005748_8001000591`, `80007482_8001000592`). There is no
`LGCS_` account here. Prompt 5 lists all nine as decoys.

**Where the green component sits — checked in Envizi, 09 Sep 26.** It has no account of its own, so
there was never anything to convert onto the certificate style:

- `Manage -> Accounts` with Show All on — 23,520 accounts — filtered on Data Type `Electricity - Green`
  returns **0 rows**. Filtering on just "Green" returns 34, all `Waste Recycled - Green Waste`. No
  account style carries the green data type, and `Admin -> Data Configuration -> Data Types` has no green
  electricity entry.
- It is a **capture field on the account style**: `Admin -> Data Configuration -> Account Styles ->
  Bid-Electricity Large Market -> Fields`, field **"Retail green power/FiT kWh"**, code **C_7**, Column
  set to **"C_7 GREEN KWH ONLY"**. That flag makes Envizi emit the second derived monthly row with a
  mirrored negative factor.
- **There is no per-account lever.** `Actions -> Account Settings` opens a modal titled "Edit account" —
  the same form as Edit Account — with no green or renewable percentage and no component switch. `Review`
  offers only Records and Monthly Data, and Records lists `Electricity [kWh]` alone.
- The old green account here, `932806640`, stops at Jun 2013 and holds nothing from 2020 on. Estate-wide
  `Electricity Green` is a retired style: 189 accounts carry it and every one is closed, 129 in 2017.

**It is visible on screen, one horizontal scroll away.** `Review -> Monthly Data`, then drag the grid's
horizontal scrollbar to the far right — Data Type is the last column, off-screen by default, and the
mouse wheel will not move the grid sideways. Green rows read the same kWh as the electricity row with
negative emissions and 0 GJ. Worth knowing: `Account Styles` is under **Manage**, not Admin, and green is
not in that classic list — the full 40-field component list is the newer `Admin -> Data Configuration`
screen.

**Why the style matters.** The Power BI dashboard reads the account style: it picks up
`Certificates - Location - kWh` and does not pick up `Electricity - Green [kWh]`. So PCEC is recording
100% green kWh in Envizi and still showing as unabated downstream.

**The call, 09 Sep 26: build both.** The green side is not being read where it needs to be, so the claim
has to sit on an account the dashboard can see. The tidier version is not available — no green account to
convert, and no per-account switch, since the only control is C_7 on the style and that is estate-wide.

What that leaves behind: **the green component keeps offsetting in Envizi and the new accounts offset
again** — at the WA (SWIS) 26-27 LGC factor of −0.45, −292.25 t counted twice across July and August. The
dashboard volume will be right; PCEC's Envizi emissions will not be, until either Power BI reads
`Electricity - Green [kWh]` as well or these two accounts move onto a neutral factor. Known going in, and
listed under **Still open**.

**The other five Alinta sites.** All seven Alinta rows are on the agreement — register rows 159–165, a
contiguous block, all WA, all green-highlighted, all starting 1 Jul 2026, and priced in
`Rates & Source Data` rows 1453–1461 at an all-in $0.31176/kWh for FY27 and FY28 with no separate LGC
line. The five besides PCEC behave identically in Envizi: zero green in June, 100% of consumption as
green from July, netting to about zero.

| Register | Site | Jul 26 kWh | Green Jul 26 | Net tCO2e Jul |
| ---: | --- | ---: | ---: | ---: |
| 161 | Cannington Emulsion Plant (Beckenham) | 37,958 | 37,958 | 0.00 |
| 162 | Maddington - BIT | 12,275 | 12,275 | 0.00 |
| 163 | Asphalt Prod - Albany (601) | 17,463 | 17,462 | 0.00 |
| 164 | Asphalt Prod - Geraldton (602) | 1,525 | 1,525 | 0.00 |
| 165 | Asphalt Prod - Hope Valley (628) | 43,313 | 43,313 | 0.00 |

They are invisible to the dashboard for exactly the same reason as PCEC and are **not** being built — only
PCEC is. About 112,500 kWh a month between them, against PCEC's 317,500.

**One Alinta account is not on the agreement.** `80013748_8001011791` at Kalgoorlie is the eighth live
Alinta electricity account in Envizi. It is absent from the Site Register, absent from the budget workbook
entirely, and records **zero green kWh** in June, July and August (2,038 kWh in July, +1.02 t) — so it
reads as genuine non-renewable supply rather than a gap. Worth a glance from Category Management if
Kalgoorlie was expected to be in the tender.

One more, confirmed on screen as well as in the 06 Sep export: the green rows on both accounts still
price on `81 - Electricity Green - 25-26 - Western Australia (SWIS)` at −0.5 for July and August 2026,
and the electricity rows on `81 - Electricity - 25-26 - Western Australia (SWIS)` at 0.5. Neither has
rolled to 26-27, any more than the LGC set had before the 08 Sep run.

## The EnergyAction rows are meters, not accounts

The Jun–Aug 26 energy export carries bare-NMI rows with supplier `EnergyAction` that never appear in
the accounts extract. They are **NEMMCO interval meters** (`Item Type` = Meter, style *NEMMCO 12 KWH
Meter with Sub-Metering*), the metering feed behind each account, tied to it by `Account_Meter_Link`.
They are not double counts and take no part in scope or source selection — the review reads accounts
only. One is worth a look on its own: the Wingfield (523) meter reads 236,293 kWh in July against the
Engie account's 118,252 — twice the bill, and the same twofold gap in June (222,315 against Origin's
111,209) and August. The "fourfold" I had earlier was the export listing that meter twice (identical rows,
one `Account_Meter_Link`), so it is a doubled row, not a doubled reading. At every other Engie site with an
interval meter (Somerton, Derrimut, Bayswater, Wodonga, Largs Bay) the meter and the Engie account agree
to the kWh, which makes Wingfield the odd one out.

Two more things the export shows at in-scope locations. **Roads - Tamworth's register NMI `4001158058`
has recorded 0 kWh in every month since June**, meter and account alike, while the Tamworth location's
electricity (43,191 kWh in July) sits on `A-0B2330E0_4001174306`, an Origin account on an NMI that is not
in the register. Its certificate account is built and mirrors zero. And several in-scope locations carry
small AGL or Origin accounts on other NMIs (Shepparton ×3, Wingfield, Mulgrave, Hexham, Chinderah) that
the register does not list — small market supply outside the renewal, left alone.

## The site register, mapped to Envizi

`Downer_Energy_Contracting_and_Budget_Summary_FY26-28_with_Envizi_accounts.xlsx` adds ten columns to
`Site Register` — the same 341 rows, all commodities and both countries, with the Envizi account each
Connection ID resolves to:

| Col | Contents |
| --- | --- |
| V | **Envizi Account Number** — the account the virtual meter follows where there is one, else the active account for that commodity, or `Not found` |
| W–Y | Account Style, Data Type, Supplier |
| Z–AA | Location, Location Ref |
| AB | Account Status — Active or Replaced *date* |
| AC | Match Basis |
| AD | Other Envizi accounts on the same ID |
| AE | Certificate / virtual meter account — the new one (live, still to create, or `TEMPORARY` where it will have to be remade against the contracted retailer's account), and any historical `LGCS_` at the location |

Shading: red in V–AE where no Envizi account ends in that Connection ID, amber in AB for a closed
account, peach in AD for an ID that is being double counted, green in AE where the certificate account is
already live and amber in AE where the account is temporary. The `Envizi mapping notes` tab carries the same explanation and the double-count list.

**283 of 341 rows matched.** The 58 that did not are 48 NZ electricity ICPs and 10 NZ gas rows — NZ
per-ICP accounts were replaced in 2023 by one account per location.

Two notes on the file. Saving through the spreadsheet library rewrites a few Annual Consumption values in
column K with a shorter decimal representation (worst difference 4.5e-16 relative, about a nano-kWh); the
stored numbers are identical at Excel's own precision and no other cell left of column V changes. And
`Budget FY26-28` uses `XLOOKUP`, which LibreOffice does not evaluate — it recalculates identically in the
original file, so it is a LibreOffice limitation, not something the mapping introduced.

## New Zealand

All NZ electricity is renewable under the new arrangements (TOU on Ecotricity since 1 Jul 26; NTOU moving
to Ecotricity 1 Jan 27). 114 of the 158 NZ green ICPs resolve to 80 open Envizi locations; 29 of those
already have a CERTS account; 44 cannot be placed from the extracts. Nothing NZ is set up yet — the NTOU
contract has not started, and for a site whose consumption sits on a per-location account rather than an
`Eco_ICP_` account, what the virtual meter should copy needs deciding first.

## RTS check — the July spike

The RTS Scope 1 & 2 dashboard showed July 26 at 928 t against 542 t in June on 7 Sep; refreshed on 8 Sep it
reads 786 t against 558 t. Checked against the 6 Sep 26 electricity export (`RTS_Market_Based_Check_Jul26.xlsx`):

- **The three RTS certificate accounts are calculating as set up.** `50002617957_4103713125_CERTS` and
  `50002617965_4103711576_CERTS` (Auburn, Origin large market) and `900018200_QGGG000010_CERTS`
  (Maryborough, Engie) each mirror their source kWh exactly in July and August, opened 1 Jul 26, no June row,
  and CO2e = kWh × factor. Certificate credits sit in **Other CO2e**, not Scope 2, so market-based is
  Scope 2 + Other.
- **RTS market-based electricity fell in July**, 471.9 t (Jun) to 166.3 t, because those accounts started
  crediting. The dashboard minus market-based electricity is a steady ~110 t Mar–May and 86 t in June, then
  620 t in July — the spike is not in the electricity as it stands now.
- **The 8 Sep refresh took 142 t off July** — the CS Energy accounts at Maryborough (`1003077`, `1003082`)
  and Torbanlea (`1003571`) closing at 30 Jun 26 removed their July accruals. What is left, ~510 t over the
  run-rate, is close to the two new certificate accounts not being credited at all (Auburn 204.8 t +
  Maryborough 196.8 t) plus Torbanlea's high first bill (+56 t). HCMT's deduction is credited every month and
  the only structural difference is its factor, `LGCs Victoria 25-26`, against the new accounts' 24-25
  vintage — if the dashboard's market-based measure only picks up current-year factors, the 25-26 LGC
  factors fix both. Scope 1 is not in this repo.
- **Maryborough is over-credited by ~95 t a month.** The certificate account copies the gross NMI figure
  while the CQMS foundry deduction (−141,380 kWh) nets the location, so Maryborough reports −103 t in July.
  Gross or net is the Category Management question already listed below.
- The three accounts are on **24-25 LGC factors** (NSW −0.66, QLD −0.71) against 25-26 electricity
  (0.64, 0.67), so Auburn nets −6.2 t. Maryborough `QGGG000320` has nothing recording since 30 Jun (meter:
  12,413 kWh in July). Torbanlea (a named exclusion, correctly with no certificate account) has a first
  Engie bill of 248,502 kWh for July, 51% above June — confirm the bill period.
- Two Auburn **meter** oddities with no effect on account-based CO2e: the NEMMCO meter on `4103713125`
  reads twice the account every month (the Wingfield pattern), and sub-meter `DWR_MSB-5-LATHE` reads
  601,436 kWh in July against 3 kWh in June — ~385 t at the NSW factor, almost exactly the dashboard's
  June-to-July increase. If the dashboard sums meters as well as accounts, that is the spike.

## Still open

- The LGC emission factors are in as of 08 Sep 26: 24-25 closed (Effective To 30 Jun 2025), the 25-26 set
  finished and closed 30 Jun 2026, the 26-27 set live from 1 Jul 2026 (NSW/ACT −0.60, Vic −0.74, QLD −0.65,
  SA −0.21, WA −0.45, Tas −0.23, NT −0.55). Left: delete the stray `( Copy of LGCs NSW 23-24 )` and set the
  Victoria 25-26 region to `Australia - Victoria` — prompt 3. Then check the next export shows 26-27 on the
  July rows and that the historical `LGCS_` accounts' FY25 / FY26 totals still look right.
- PCEC: build the two accounts (prompt 5) — decided 09 Sep 26. Then the double count: the green component
  keeps offsetting (C_7 is on the `Bid-Electricity Large Market` style, estate-wide, no per-account
  switch), so both records coexist and PCEC's Envizi emissions read about −292 t light for Jul–Aug. Fix is
  either Power BI reading `Electricity - Green [kWh]` as well — which would also cover the other five
  Alinta sites — or a neutral factor on the two new accounts.
- Kalgoorlie `80013748_8001011791`: live Alinta account, not in the Site Register or the budget workbook,
  no green kWh. Confirm with Category Management that it is meant to be outside the renewal.
- Mogo: read the two certificate accounts (prompt 0b), link the empty 4204072845 one, remake 4001127731.
- Section 2: the last 17 permanent accounts.
- Section 1: close the 14 old accounts (Traralgon's Replaced On back from 30 Oct to 30 Jun 26), and
  confirm the date for the two CS Energy ones.
- Section 3: chase the 9 Queensland sites still on CS Energy, then delete and remake the temporary
  accounts against the right source. Maryborough QGGG000320 has nothing recording at all — raise it.
- The Wingfield meter reading twice its account, and Tamworth's register NMI reading nothing.
- Maryborough QGGG000010: gross or net of the CQMS foundry deduction.
- NZ, once the Ecotricity switch is confirmed.
- The Envizi Account Style Link for the certificates style, only if the load tab is ever uploaded.
