# Claude in Chrome prompts — what is left

What I paste into Claude in Chrome with Envizi (`au001.envizi.com`) open in the active tab. Each form has
been run against the real screens; the quirks noted inside them are real. Keep Envizi in front while it
works — it only sees the active tab.

Position as of the 06 Sep 26 exports: **all 60 permanent accounts are built** and every one mirrors its
source exactly in July and August with no June row. The 12 old Origin accounts read Replaced On 30 Jun
2026 and no longer accrue. Mogo has both its accounts. The LGC factors are done as of 08 Sep 26 — 24-25
closed 30 Jun 2025, the 25-26 set finished and closed 30 Jun 2026, the 26-27 set live from 1 Jul 2026.
New since: all seven WA Alinta meters come off the exclusion list — prompt 5. The find ran on 09 Sep:
their green component is a capture field on the account style (C_7), not an account, so there is nothing
to convert and no per-account switch — and Power BI does not read it. Call made: build all seven. That
puts 69 of the 78 green register rows on a certificate account; prompt 2 takes it to 76, and QTMP and
Maryborough are blocked in Envizi. The double count it leaves behind is written up under prompt 5.
What remains, in the order I run it:

| # | Prompt | What it does |
| --- | --- | --- |
| 1 | Close the two connector accounts | Gympie and Archerfield still double count — 5000021_ accounts accruing beside the live 1003xxx ones |
| 2 | Build the 9 temporary accounts | Section 3 — the Queensland sites still on CS Energy with no Engie account. Run **after** prompt 1 |
| 3 | LGC factors tidy-up | All four vintages are in (08 Sep 26). Delete the stray `( Copy of LGCs NSW 23-24 )` and fix the Victoria 25-26 region |
| 4 | Fix two Account Refs | Bathurst and Mogo 4204072845 carry the account number where the NMI should be |
| 5 | The seven WA Alinta meters | All seven flipped from Exclude to Create — PCEC ×2, Beckenham, Maddington, Albany, Geraldton, Hope Valley. Their green component is not read by Power BI. Takes coverage to 69 of the 78 green rows |
| 6 | Read-only check | Confirm an account after it is built |

Prompt 2 assumes prompt 1 has run, so the 5000021_ accounts at Gympie and Archerfield are closed but
still listed. Prompt 5 stands on its own — nothing in 1–4 touches the WA sites. The earlier prompts (the 17 permanent accounts, the 12 Origin close-offs, the Mogo read)
are done and have been taken out; they are in the git history if I ever need the form again.

---

## 1 · Close the two connector accounts at Gympie and Archerfield

Two Utilities Connector accounts are still accruing beside the live CS Energy account on the same NMI.
The other nine `5000021_` accounts were closed the day before their `1003xxx` replacement opened
(31 Mar, 31 May or 30 Jun 2026), so the date is read off the live account rather than assumed.

```
You're helping me close off two accounts in IBM Envizi (au001.envizi.com). I'm
logged in on the Envizi tab. Two accounts, ONE AT A TIME, in order. There is a
read step first, and you STOP after it.

WHAT "CLOSE" MEANS HERE
Set the account's Replaced On date. Nothing else. Do NOT delete, move or merge
any account, and do NOT touch Opened On - it sits directly under Replaced On on
the same form and must stay as it is.

WHY
On each NMI a second CS Energy account created by the Utilities Connector is
still accruing every month with no Opened On and no actual bills, while the
live 1003xxx account bills the actuals. Closing the connector account stops the
site being counted twice.

THIS BATCH HAS DECOYS
The LIVE account sits at the same location under the same NMI - it is the
1003xxx one. Never open Edit Account on it. The account to close is always the
5000021_ one I name - match the full account number character for character.

=== STEP A · Read the live account first, then STOP ===
For each pair below, top-right search, dropdown set to "Accounts", paste the
LIVE 1003xxx account number and open it. Review -> Monthly Data. Tell me the
EARLIEST month that holds data, and whether that month is actual or accrued.
Read-only - change nothing. Do both, then stop and show me. I'll give you the
Replaced On date for each, then you do steps 1-4.

=== STEP 1 · Find the account to close ===
Top-right search, dropdown "Accounts". Paste the full 5000021_ account number,
open it. You land on the Account Summary page. Confirm three things: the
account number in the header and left panel is exactly mine, "Relates to" is
the location I give you, and the left panel reads "Replaced On : -". If any of
those disagree, stop and show me.

=== STEP 2 · Open the form ===
Click the blue "Actions" button (top right, next to Page Settings). The menu
has Capture Data, Edit Account and Account Settings. Choose "Edit Account".
Do NOT choose Capture Data.

=== STEP 3 · Set Replaced On ===
On the form find "Replaced On:" - a date field with a calendar icon. Click the
calendar icon. It opens on the current month, so page back to the month I
give you and click the day. The field should then read the date in m/d/yyyy
form (30 Jun 2026 shows as 6/30/2026). If typing works better, type it and
tab out, then read it back to check the month and day didn't swap.

Leave "Opened On:" exactly as it was - it is blank on both of these and stays
blank. Change nothing else on the form.

Save.

=== STEP 4 · Check it ===
Back on the Account Summary page, the left panel should now read
"Replaced On : <the date>". Then Review -> Monthly Data: months after the date
should no longer accrue. If the accruals are still there straight after saving,
note it - Envizi can take a refresh to drop them - and move on.

Report, per account: the account number, the location, what Replaced On read
before, what it reads now, and that Opened On is still blank.

======================== THE TWO PAIRS ========================

 1. Gympie (Location Ref 142)
    CLOSE:  5000021_3120129028      (accruing Jul 19,118 / Aug 19,955 kWh)
    LIVE:   1003085_3120129028      (leave it - read its earliest month in step A)

 2. Asphalt Prod - Archerfield (406) (Location Ref 406)
    CLOSE:  5000021_QB05383854      (accruing Jul 83,805 / Aug 78,191 kWh)
    LIVE:   1003081_QB05383854      (leave it - read its earliest month in step A)

RULES
- Replaced On only. Never delete, move, or edit anything else on any account.
- Never open Edit Account on the live 1003xxx account.
- If the 5000021_ account already has a Replaced On, stop and show me.
- If a screen doesn't match what I've described, stop and describe what you see.
```

Expected: the live account's earliest month is Apr, Jun or Jul 2026, and the Replaced On I give back is
the last day of the month before it. After the run both `5000021_` accounts read that date on their
Summary page and the next accounts extract carries it. Only then run prompt 2 — Gympie and Archerfield
are in that batch and their source is the `1003xxx` account.

---

## 2 · Build the 9 temporary accounts — section 3

These are Queensland sites contracted to Engie from 1 Jul 26 whose Engie account has not appeared in
Envizi, so the CS Energy account is still recording. On the Director's call they get a certificate
account anyway, built against the CS Energy account, so the renewable claim is in the FY27 numbers from
July. **Every one of these is temporary.** The account name keys off its source, so when the Engie
account arrives the account is deleted and remade against it — the delete register on the guide page
tracks that.

```
You're helping me set up renewable-certificate virtual accounts in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Work through the accounts
listed at the bottom ONE AT A TIME, in order.

THE ONE RULE THAT MATTERS
An account can only be set up as a virtual account while it holds NO records. So
the account is created first and saved empty, and only then linked. Never add
data to it.

THIS BATCH HAS DECOYS
At Gympie and Archerfield a second CS Energy account (5000021_...) sits at the
same location under the same NMI. I closed it earlier, but a closed account is
still listed and still holds data, so it still shows up in the account list and
in the Source data tree. It is NOT the source. The source is always the account
I name - the 1003xxx one - never the 5000021_ one. Match the full account number
character for character.

While you're in the account list (step 2) at those two sites, glance at the
decoy's Replaced On column. It should read a date. If it's blank, the close-off
didn't take - finish the account you're on, but tell me.

MULTIPLE ACCOUNTS AT ONE LOCATION
RPQ Spray Seal needs two. Find the location once, then repeat steps 3-6 for each.

=== STEP 1 · Find the location ===
Top-right search, dropdown set to "Locations". Search the location name, open it.
Confirm the Location Ref on the Summary page matches the ref I give you - several
locations share a name, the ref is what disambiguates. If the ref doesn't match, stop.

=== STEP 2 · Open the account list ===
From the location Summary page: Quick links -> Accounts. Click "Show All Accounts".
Before creating anything, filter the Account Number column on "CERTS" and confirm
MY EXACT TARGET NUMBER isn't there, then clear the filter. The filter sometimes
renders as a search textbox and sometimes as a multi-select checkbox list. LGCS_
rows at the location are expected - leave them. If my exact target exists, stop
and tell me - do not edit or reuse it.

=== STEP 3 · Create the account, empty ===
Click the blue "Create New..." button and set:

  Account style      Certificates - Location - kWh
  Account number     as listed below
  Account Ref        the NMI as listed below - the NMI, NOT the account number
  Supplier           LGC Virtual Account
  Reader             leave blank
  Opened On          2026-07-01   (field displays as 7/1/2026)

Leave Reader, Linked Meter, Replaced On and Sub Type blank. Account Style is a jqx
DIV, not a native select - form_input will fail on it. Click it open and type into
its internal Search box, then click the filtered result. The Opened On calendar
opens on the current month, so page back to July 2026 and click 1.
Save. Do NOT add any records, monthly data or capture data.

=== STEP 4 · Open Virtual Account Setup ===
Back in the account list, tick the checkbox on the row for the account you just
created, then click the blue "Actions" button and choose "Virtual Account Setup".

That same Actions menu also holds "Delete Account(s)", "Close Account(s)" and
"Move Account". Do not click any of those, ever. Screenshot the menu and confirm
before clicking. If you're not certain, stop and show me.

The grid sometimes shows a second row as pre-ticked - a display artifact. Confirm
the breadcrumb on the Virtual Account Relationships page names my new _CERTS
account and the grid reads 0 Row. If it names anything else, stop.

=== STEP 5 · Create the relationship ===
On "Virtual Account Relationships" click the blue "Create New...". A "Virtual
relationship" dialog opens with three tabs. Fill all three BEFORE saving:

- Select rule - Measure: Total Certificates. Data Rule: 100% Renewable Energy
  Certificates (subtitle "Kilowatt hours*Value Variable"). The Measure dropdown
  occasionally renders empty on first click; click it again.

- Source data - Left pane "Available", right pane "Selected". Expand "Kilowatt
  hours", then the location, then click the plus next to the SOURCE ACCOUNT I
  name. Zoom in and match the FULL account number character for character. Add
  that one account and nothing else. The Selected pane should show Kilowatt
  hours -> the location -> the one account, then "*" and "Value Variable" -
  leave those exactly as the rule sets them.

- Condition (optional) - Effective From: July 2026 (the picker shows "2026 July").
  Effective To: leave blank. This is what stops the virtual account reaching back
  before the renewal. It is not optional for us.

Then SAVE. Confirm the grid reads 1 Row with Formula "Kilowatt hours*Value Va...",
Effective From 7/1/2026, Effective To blank.

=== STEP 6 · Check it ===
Open the new account and confirm Opened On reads 7/1/2026, Account Ref reads the
NMI, and there is exactly one relationship. Read the figures via Review ->
Monthly Data in the account nav - the Summary chart tooltips don't render.
Confirm Jul and Aug 2026 kWh match the "Expect" line and there is NO June 2026
row. If June has a value, Effective From didn't take - stop and tell me. The
"Expect" figures are the 1003xxx account's own kWh, all of them accrued; at
Gympie and Archerfield the closed 5000021_ account's July and August (a
different, larger number) should not appear anywhere in the new account.

================= THE ACCOUNTS · 9 across 8 locations, all QLD =================

### RPQ Spray Seal - ref 171230   (2 accounts)
    Leave alone here: LGCS_3051770385, LGCS_3120014382, LGCS_3120136120
 1. 1003072_3051770385_CERTS · ref 3051770385 · src 1003072_3051770385
    Expect Jun none · Jul 15,721 · Aug 17,432
 2. 1003070_3120014382_CERTS · ref 3120014382 · src 1003070_3120014382
    Expect Jun none · Jul 29,259 · Aug 30,991

### RPQ Swanbank - ref 171505
    Leave alone here: LGCS_3120070486
 3. 1003071_3120070486_CERTS · ref 3120070486 · src 1003071_3120070486
    Expect Jun none · Jul 22,030 · Aug 31,514

### Asphalt Prod - Bli Bli (408) - ref 408
    Leave alone here: LGCS_3120103988
 4. 1003079_3120103988_CERTS · ref 3120103988 · src 1003079_3120103988
    Expect Jun none · Jul 63,426 · Aug 63,426

### Gympie - ref 142
    Leave alone here: LGCS_3120129028
 5. 1003085_3120129028_CERTS · ref 3120129028 · src 1003085_3120129028
    Expect Jun none · Jul 14,156 · Aug 14,156
    DECOY, do NOT pick (closed, still listed): 5000021_3120129028

### Asphalt Prod - Archerfield (406) - ref 406
    Leave alone here: LGCS_QB05383854
 6. 1003081_QB05383854_CERTS · ref QB05383854 · src 1003081_QB05383854
    Expect Jun none · Jul 75,559 · Aug 75,559
    DECOY, do NOT pick (closed, still listed): 5000021_QB05383854

### Teneriffe - Brisbane (QLD) - ref 1020
    Leave alone here: LGCS_3117134943
 7. 1003084_3117134943_CERTS · ref 3117134943 · src 1003084_3117134943
    Expect Jun none · Jul 8,731 · Aug 8,731

### PPP - Southbank TAFE (QLD) - ref 9108
    No LGCS_ account here.
 8. 1003074_3116382269_CERTS · ref 3116382269 · src 1003074_3116382269
    Expect Jun none · Jul 628,450 · Aug 649,281
    (By far the largest of the nine - check the figures twice.)

### PPP - Sunshine Coast University Hospital - ref 9078
    No LGCS_ account here.
 9. 1003075_3120143385_CERTS · ref 3120143385 · src 1003075_3120143385
    Expect Jun none · Jul 18,686 · Aug 19,189

================================================================================

After each account, report: the account number created, Account Ref, Opened On,
the exact source account you selected, Effective From, and the Jun/Jul/Aug
figures against what I expected. Do number 1, then stop and show me before
starting number 2 - once I've confirmed it I'll tell you to run the rest
without stopping.

RULES
- Never delete, close, move or edit the SOURCE account, a decoy, or any LGCS_ account.
- If my exact target account number already exists, stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.
- Never click Save or Delete on a form you're unsure about.

WORKED EXAMPLE
900018199_3120725958_CERTS at Asphalt Prod - Brendale (423) is done and correct -
source 900018199_3120725958, measure Total Certificates, rule 100% Renewable
Energy Certificates, Effective From July 2026.
```

The "Expect" figures are the July and August accruals on the CS Energy accounts as at the 06 Sep 26
export. They move when a bill lands, so a small difference on the day is the source having moved, not
the link being wrong — the test is that the new account equals the source, whatever the source reads.

When the Engie account appears on one of these NMIs, that site's temporary account comes off: delete
`1003xxx_<NMI>_CERTS`, then build `9000182xx_<NMI>_CERTS` against the Engie account with this same
form. The delete register on the guide page carries the tick per row.

---

## 3 · The LGC emission factors — tidy-up after the 08 Sep 26 run

The three-stage run (close 24-25, finish the 25-26 copies, add 26-27) is done. Custom Factors now holds
33 LGC rows: four bands of eight plus one stray. On the Custom Factor form the dates are **Effective
From** and **Effective To**, not Opened On / Replaced On — the 23-24 rows carry an Effective To with no
Effective From, and the three later bands carry both.

| State | 23-24 (to 30/06/2024) | 24-25 (01/07/2024 – 30/06/2025) | 25-26 (01/07/2025 – 30/06/2026) | 26-27 (from 01/07/2026, live) |
| --- | --- | --- | --- | --- |
| NSW | −0.68 | −0.66 | −0.64 | −0.60 |
| ACT | −0.68 | −0.66 | −0.64 | −0.60 |
| Victoria | −0.79 | −0.77 | −0.78 | −0.74 |
| QLD | −0.73 | −0.71 | −0.67 | −0.65 |
| SA | −0.25 | −0.23 | −0.22 | −0.21 |
| WA (SWIS) | −0.53 | −0.51 | −0.50 | −0.45 |
| Tasmania | −0.12 | −0.15 | −0.20 | −0.23 |
| NT (DKIS) | −0.54 | −0.56 | −0.56 | −0.55 |

Every value is the negative of the state's Scope 2 location-based factor for the NGA Factors edition of
that vintage. One that does not match: `LGCs Victoria 24-25` reads −0.77 where NGA Factors 2024 gives
Victoria 0.79. It is closed history now and its months have been reported, so it stays; noting it here so
nobody "corrects" it to match the table above.

Regions read `Australia - <State>` throughout except `LGCs Victoria 25-26`, which still reads plain
`Australia`. Two things left, one prompt:

```
You're helping me tidy up custom emission factors in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Admin -> Custom Factors,
wait out the loading spinner, Name filter "lgc". Two rows, one at a time.
Nothing else on the screen gets touched.

=== 1 · Delete the stray copy ===
Find the row whose Name is exactly "( Copy of LGCs NSW 23-24 )" - brackets
and spaces included, Region "*Select Region*", Total CO2e -0.68, Effective To
30/06/2024. Open it and screenshot the form so I can see every field, then
stop and show me. Once I say go, delete that row. Do NOT delete "LGCs NSW
23-24" (Region "Australia - New South Wales") - that is the real one and it
stays. If the Copy row's name isn't found character for character, stop and
tell me what you do see.

=== 2 · Fix the Victoria 25-26 region ===
Open "LGCs Victoria 25-26" (Total CO2e -0.78, Effective From 01/07/2025,
Effective To 30/06/2026, Region "Australia"). Set Region to "Australia -
Victoria" and save. Change nothing else - the value and both dates stay.
Read the saved row back to me.

=== OUTPUT ===
Filter "lgc" again and confirm: 32 rows, none named "( Copy of", none with
Region "*Select Region*" or plain "Australia".
```

Expected afterwards: the next certificates export shows `LGCs NSW 26-27` (−0.60) on the NSW accounts
for July 2026 on, and Bathurst nets to zero in July instead of −1.08 t. The historical `LGCS_` accounts
recalculate onto whichever vintage their month now falls in — intended, but the FY25 and FY26 totals on
those accounts are worth a glance in that export. If the accounts stay on 24-25 after the dates are in,
the factor set's date handling or region mapping needs a look — that is a separate, read-only step.
---

## 4 · Fix the two Account Refs

Two of the 60 carry the account number in Account Ref where the other 58 carry the NMI. Cosmetic, but
the field is what the register matches on, so they get corrected.

```
You're helping me correct one field on two accounts in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Two accounts, ONE AT A
TIME.

WHAT CHANGES
Account Ref only. It currently holds a copy of the account number; it should
hold the NMI. Do NOT touch Opened On, Replaced On, Supplier, Account Style, the
virtual account relationship, or anything else on the form. Do NOT add any
records.

=== STEP 1 · Find the account ===
Top-right search, dropdown "Accounts". Paste the full account number, open it.
On the Account Summary page confirm the account number in the header is exactly
mine, "Relates to" is the location I give you, and Opened On reads 7/1/2026.
If any of those disagree, stop and show me.

=== STEP 2 · Open the form ===
Blue "Actions" button (top right) -> "Edit Account". Not Capture Data.

=== STEP 3 · Set Account Ref ===
Find "Account Ref" on the form. It reads the account number. Replace the whole
value with the NMI I give you - nothing else in the field. Change nothing else.
Save.

=== STEP 4 · Check it ===
Back on the Summary page confirm Account Ref reads the NMI and Opened On still
reads 7/1/2026. Then tick the account in the location's account list, Actions
-> Virtual Account Setup, and confirm the grid still reads 1 Row with the same
source. Do not click Create New, Delete, Close or Move there.

=========================== THE TWO ===========================

 1. 50002617964_NAAA00AC25_CERTS   Asphalt Prod - Bathurst (156), Location Ref 170156
    Account Ref now: 50002617964_NAAA00AC25_CERTS   ->   set to: NAAA00AC25

 2. 50002617992_4204072845_CERTS   Asphalt Prod - Mogo (154), Location Ref 154
    Account Ref now: 50002617992_4204072845_CERTS   ->   set to: 4204072845
    (Mogo has a second certificate account, 50002769514_4001127731_CERTS, whose
    Account Ref is already right. Leave it.)

Report, per account: what Account Ref read before, what it reads now, that
Opened On is unchanged, and that the relationship grid still reads 1 Row.

RULES
- Account Ref only. If the form looks different from what I've described, stop.
- Never delete, close or move anything.
```

---

## 5 · Certificate accounts for every green site — the seven WA Alinta meters

The goal is that **every green row in the contract register has a `Certificates - Location - kWh`
account**, because that is the data type Power BI reads. It picks up `Certificates - Location - kWh` and
it does not pick up `Electricity - Green [kWh]`, so a site can be recording 100% green kWh in Envizi and
still show as unabated on the dashboard.

The register has 78 green rows of 81 (the three NT rows are not green and are named exclusions anyway).
Where they stand:

| | Green rows | Certificate account | Where |
| --- | ---: | --- | --- |
| The 60 permanent | 60 | **built** — verified 06 Sep 26 | section 2, done |
| WA Alinta | **7** | **built by this prompt** | below |
| QLD, retailer not in Envizi yet | 9 | temporary accounts | **prompt 2**, run after prompt 1 |
| QTMP Torbanlea `3053253239` | 1 | cannot yet | its location `Torbanlea - QTMP` is absent from the locations extract |
| Rail - Maryborough `QGGG000320` | 1 | cannot yet | no active electricity account on the NMI, so nothing for a virtual account to follow |
| | **78** | | |

So this prompt plus prompt 2 takes it to **76 of 78**. The last two are blocked on Envizi, not on the
form — QTMP needs its location to exist, Maryborough needs something recording on the NMI. Both are on
the **Still open** list.

Step 0 below re-counts the certificate accounts before building anything, so the 60 are proved rather
than assumed, and anything already built is skipped rather than duplicated.

### Why the seven Alinta sites were excluded, and why they are being built now

All seven are on the agreement — register rows **159–165**, a contiguous block, all WA, all
green-highlighted, all starting 1 Jul 2026, priced in `Rates & Source Data` rows 1453–1461 at an all-in
**$0.31176/kWh** for FY27 and FY28 with no separate LGC line. They were excluded from the original 60
because each account's own green component already carries the offset: zero green in June, then 100% of
consumption from July, netting each account to about zero.

That offset is invisible where it counts, so they are being built. **Decision, 09 Sep 26: build all
seven.**

### What the find established — 09 Sep 26

**The green side has no account of its own, so nothing can be converted.** `Manage -> Accounts` with Show
All on — 23,520 accounts — filtered on Data Type `Electricity - Green` returns **0 rows**. Filtering on
just "Green" returns 34, all `Waste Recycled - Green Waste`. `Admin -> Data Configuration -> Data Types`
has no green electricity entry.

**It is a capture field on the account style**: `Admin -> Data Configuration -> Account Styles ->
Bid-Electricity Large Market -> Fields`, field **"Retail green power/FiT kWh"**, code **C_7**, Column set
to **"C_7 GREEN KWH ONLY"**. That flag is what makes Envizi emit the second derived monthly row with a
mirrored negative factor. It is on the style, so it is **estate-wide** — there is no per-account switch,
and `Actions -> Account Settings` turns out to be the Edit Account modal under another name, with no
green or renewable percentage on it.

**It is visible on screen, one horizontal scroll away.** `Review -> Monthly Data`, then drag the grid's
horizontal scrollbar to the far right — Data Type is the last column, off-screen by default, and the
mouse wheel will not move the grid sideways. Green rows read the same kWh as the electricity row with
negative emissions and 0 GJ. Also worth knowing: `Account Styles` is under **Manage**, not Admin, and
green is not in that classic list — the 40-field component list is the newer `Admin -> Data
Configuration` screen.

### What building leaves behind

Because C_7 cannot be switched off for these accounts alone, **the green component keeps offsetting and
the new certificate accounts offset again**. On the July and August figures, at the WA (SWIS) 26-27 LGC
factor of −0.45, that is **−392.81 t counted twice across all seven** (PCEC −292.25 t of it). The
dashboard volume will be right; the Envizi emissions for these seven will not be, until either Power BI
reads `Electricity - Green [kWh]` as well or these accounts move onto a neutral factor. Known going in,
and on the **Still open** list.

Two things that apply to every one of the seven. All seven source accounts have recorded since **2020 or
earlier**, so Effective From July 2026 is what keeps the certificate accounts off years of history — it
matters more here than anywhere in section 2. And every one of the six locations has a **closed Alinta
account on the same NMI** sitting next to the source, so the full account number is what to match on.

None of the six locations has an `LGCS_` account or an existing certificate account as at the 05 Sep
extract.

```
You're helping me set up renewable-certificate virtual accounts in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. There is a counting step
first, then seven accounts across six locations, ONE AT A TIME, in order.

THE ONE RULE THAT MATTERS
An account can only be set up as a virtual account while it holds NO records.
So the account is created first and saved empty, and only then linked. Never
add data to it.

IF ONE ALREADY EXISTS
If my exact target account number is already there, do NOT touch it, do NOT
edit or reuse it. Note it as already done and move to the next one. Only build
what is missing.

EVERY LOCATION HERE HAS A DECOY ON THE SAME NMI
At each site a CLOSED Alinta account sits on the same NMI as the live one, and
the numbers differ by a few digits. Match the FULL account number character for
character, every time. The closed one is named on each card below.

=== STEP 0 · Count what already exists, then tell me ===
Read-only. Manage -> Accounts, turn Show All on, and filter Account Style on
"Certificates - Location - kWh". Tell me how many rows come back and, if the
grid will show it, list the account numbers. I am expecting about 60. Report
the number before you build anything - if it is well under 60, stop and tell
me, because something I think is built is not.

=== STEP 1 · Find the location ===
Top-right search, dropdown set to "Locations". Search the location name, open
it. Confirm the Location Ref on the Summary page matches the ref on the card -
several locations share a name and the ref is what disambiguates. If the ref
doesn't match, stop.

=== STEP 2 · Open the account list ===
From the location Summary page: Quick links -> Accounts. Click "Show All
Accounts". Before creating anything, filter the Account Number column on
"CERTS" and confirm my exact target isn't there, then clear the filter. The
filter sometimes renders as a search textbox and sometimes as a multi-select
checkbox list. If my exact target already exists, skip this site per the rule
above and tell me.

=== STEP 3 · Create the account, empty ===
Click the blue "Create New..." button and set:

  Account style      Certificates - Location - kWh
  Account number     as listed on the card
  Account Ref        the NMI on the card - the NMI, NOT the account number
  Supplier           LGC Virtual Account
  Reader             leave blank
  Opened On          2026-07-01   (field displays as 7/1/2026)

Leave Reader, Linked Meter, Replaced On and Sub Type blank. Account Style is a
jqx DIV, not a native select - form_input will fail on it. Click it open and
type into its internal Search box, then click the filtered result. The Opened
On calendar opens on the current month, so page back to July 2026 and click 1.
Save. Do NOT add any records, monthly data or capture data.

=== STEP 4 · Open Virtual Account Setup ===
Back in the account list, tick the checkbox on the row for the account you just
created, then click the blue "Actions" button and choose "Virtual Account
Setup".

That same Actions menu also holds "Delete Account(s)", "Close Account(s)" and
"Move Account". Do not click any of those, ever. Screenshot the menu and
confirm before clicking. If you're not certain, stop and show me.

The grid sometimes shows a second row as pre-ticked - a display artifact.
Confirm the breadcrumb on the Virtual Account Relationships page names my new
_CERTS account and the grid reads 0 Row. If it names anything else, stop.

=== STEP 5 · Create the relationship ===
On "Virtual Account Relationships" click the blue "Create New...". A "Virtual
relationship" dialog opens with three tabs. Fill all three BEFORE saving:

- Select rule - Measure: Total Certificates. Data Rule: 100% Renewable Energy
  Certificates (subtitle "Kilowatt hours*Value Variable"). The Measure dropdown
  occasionally renders empty on first click; click it again.

- Source data - Left pane "Available", right pane "Selected". Expand "Kilowatt
  hours", then the location, then click the plus next to the SOURCE ACCOUNT on
  the card. Zoom in and match the FULL account number character for character -
  the closed Alinta account on the same NMI will be sitting right next to it in
  the tree. Add that one account and nothing else. The Selected pane should
  show Kilowatt hours -> the location -> the one account, then "*" and "Value
  Variable" - leave those exactly as the rule sets them.

- Condition (optional) - Effective From: July 2026 (the picker shows
  "2026 July"). Effective To: leave blank. THIS MATTERS ON EVERY ONE OF THESE:
  every source has recorded since 2020 or earlier, so without it the new
  account reaches back years. It is not optional for us.

Then SAVE. Confirm the grid reads 1 Row with Formula "Kilowatt hours*Value
Va...", Effective From 7/1/2026, Effective To blank.

=== STEP 6 · Check it ===
Open the new account and confirm Opened On reads 7/1/2026, Account Ref reads
the NMI, and there is exactly one relationship. Read the figures via Review ->
Monthly Data in the account nav - the Summary chart tooltips don't render.

On that grid, DRAG THE HORIZONTAL SCROLLBAR to the far right. Data Type is the
last column and it sits off-screen by default, and the mouse wheel will not
move the grid sideways. I need to see it, and I want it to read
"Certificates - Location - kWh".

Confirm Jul and Aug 2026 kWh match the "Expect" line and there is NO June 2026
row and nothing before July 2026. If any earlier month has a value, Effective
From didn't take - stop and tell me.

============ THE SEVEN · all WA, all Alinta, seven accounts at six locations ============

### LSE - Perth Convention & Exhibition Centre (WA) - Location Ref 9068   (2 accounts)
    Leave alone here: 932806640, 414267220_8001905073, 80005748_80010005910_CLOSED,
    80005748_80010005926, 80007482_CLOSED, 600751_80010005910, 600751_80010005926
 1. 80013757_8001000591_CERTS · ref 8001000591 · src 80013757_8001000591
    Expect Jun none · Jul 174,253 · Aug 188,584
    Closed decoy, SAME NMI, do NOT pick: 80005748_8001000591
 2. 80013758_8001000592_CERTS · ref 8001000592 · src 80013758_8001000592
    Expect Jun none · Jul 143,301 · Aug 143,301
    Closed decoy, SAME NMI, do NOT pick: 80007482_8001000592

### Cannington Emulsion Plant - Location Ref 39   (register: Roads - Beckenham)
 3. 80013752_8001010840_CERTS · ref 8001010840 · src 80013752_8001010840
    Expect Jun none · Jul 37,958 · Aug 37,525
    Closed decoy, SAME NMI, do NOT pick: 80005436_8001010840

### Maddington - BIT - Location Ref 171   (register: Roads - Maddington)
    Careful: prompt 2 has an RPQ Spray Seal at ref 171230. This one is ref 171.
 4. 80013749_8001015167_CERTS · ref 8001015167 · src 80013749_8001015167
    Expect Jun none · Jul 12,275 · Aug 12,360
    Closed decoy, SAME NMI, do NOT pick: 80005437_8001015167

### Asphalt Prod - Albany (601) - Location Ref 601   (register: Roads - Warrenup)
 5. 80013750_8001016501_CERTS · ref 8001016501 · src 80013750_8001016501
    Expect Jun none · Jul 17,463 · Aug 16,858
    Closed decoy, SAME NMI, do NOT pick: 80003702_8001016501

### Asphalt Prod - Geraldton (602) - Location Ref 602   (register: Roads - Narngulu)
    This location also has a LIVE small market account on a DIFFERENT NMI -
    023384950_8002057153. It is not in the renewal. Do not pick it as a source.
 6. 80013754_8001356541_CERTS · ref 8001356541 · src 80013754_8001356541
    Expect Jun none · Jul 1,525 · Aug 1,542   (much the smallest of the seven)
    Closed decoy, SAME NMI, do NOT pick: 80005435_8001356541

### Asphalt Prod - Hope Valley (628) - Location Ref 628   (register: Roads - Hope Valley)
 7. 80013755_8002193716_CERTS · ref 8002193716 · src 80013755_8002193716
    Expect Jun none · Jul 43,313 · Aug 42,646
    Closed decoy, SAME NMI, do NOT pick: 80010451_8002193716

========================================================================================

None of these six locations has an LGCS_ account. If you find one, leave it
alone and tell me.

Do step 0, then number 1, then stop and show me. Once I've confirmed the first
one I'll tell you to run the rest without stopping.

After each account, report: the account number created, Account Ref, Opened On,
the exact source account you selected, Effective From, the Data Type shown on
Monthly Data, the Jun/Jul/Aug figures against what I expected, and that nothing
appears before July 2026.

RULES
- Never delete, close, move or edit a SOURCE account or any decoy.
- Never open Edit Account on anything except the account you just created.
- If my exact target already exists, skip it and tell me - never edit or reuse.
- If a screen doesn't match what I've described, stop and describe what you see.
- Never click Save or Delete on a form you're unsure about.

WORKED EXAMPLE
900018199_3120725958_CERTS at Asphalt Prod - Brendale (423) is done and correct
- source 900018199_3120725958, measure Total Certificates, rule 100% Renewable
Energy Certificates, Effective From July 2026.
```

Expected: seven `Certificates - Location - kWh` accounts across the six WA locations, each mirroring one
Alinta account from July 2026 and nothing earlier, on the WA (SWIS) 26-27 LGC factor of −0.45. August is
accrued on every one of them, so the figures move as the bills land — the test is that each new account
equals its source, whatever the source reads.

Coverage after this prompt: **69 of 78** green rows have a certificate account. Prompt 2 takes it to 76;
QTMP and Maryborough are the two that cannot be built yet.

Then the green component, still recording on the style field and not switchable per account, so these
seven read about −393 t better than they should for July and August until the factor or the dashboard is
dealt with. Known and accepted going in. Prompt 6 read against any of them will show the factor and the
kWh side by side.

---

## 6 · Read-only check on a finished account

For confirming any one account after a batch, or on a day I want to know an account is still right.

```
On the Envizi tab. Read-only - create, edit, save or delete nothing.
Find <account number> and tell me: its location, account style, supplier and
whether Reader is blank, Account Ref, Opened On, whether it's a virtual account
and the source and percentage, Effective From on the relationship, its kWh for
Jun/Jul/Aug 2026, and the emission factor name and value. Then tell me how you
found it.

Read the figures from Review -> Monthly Data, and DRAG THE HORIZONTAL SCROLLBAR
to the far right - Data Type is the last column, off-screen by default, and the
mouse wheel won't move the grid sideways. Tell me every Data Type you can see
on the account, not just the first.
```

Expected for a right account: `Certificates - Location - kWh` · `LGC Virtual Account` / Reader blank ·
Account Ref = the NMI · Opened On 7/1/2026 · virtual, one source at 100% · Effective From 7/1/2026 ·
**no June**, July and August equal to the source · the state's LGCs factor (25-26 once prompt 3 is in).
