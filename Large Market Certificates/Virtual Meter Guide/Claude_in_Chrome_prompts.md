# Claude in Chrome prompts — what is left

What I paste into Claude in Chrome with Envizi (`au001.envizi.com`) open in the active tab. Each form has
been run against the real screens; the quirks noted inside them are real. Keep Envizi in front while it
works — it only sees the active tab.

Position as of the 06 Sep 26 exports: **all 60 permanent accounts are built** and every one mirrors its
source exactly in July and August with no June row. The 12 old Origin accounts read Replaced On 30 Jun
2026 and no longer accrue. Mogo has both its accounts. The LGC factors are done as of 08 Sep 26 — 24-25
closed 30 Jun 2025, the 25-26 set finished and closed 30 Jun 2026, the 26-27 set live from 1 Jul 2026.
New since: the two Perth Convention & Exhibition Centre meters come off the exclusion list — prompt 5.
The find ran on 09 Sep: the green component is a capture field on the account style, not an account, so
there is nothing to convert and no per-account switch. Call made — build both, because the green side is
not being read where it counts. The double count it leaves in Envizi is written up under prompt 5.
What remains, in the order I run it:

| # | Prompt | What it does |
| --- | --- | --- |
| 1 | Close the two connector accounts | Gympie and Archerfield still double count — 5000021_ accounts accruing beside the live 1003xxx ones |
| 2 | Build the 9 temporary accounts | Section 3 — the Queensland sites still on CS Energy with no Engie account. Run **after** prompt 1 |
| 3 | LGC factors tidy-up | All four vintages are in (08 Sep 26). Delete the stray `( Copy of LGCs NSW 23-24 )` and fix the Victoria 25-26 region |
| 4 | Fix two Account Refs | Bathurst and Mogo 4204072845 carry the account number where the NMI should be |
| 5 | The two PCEC meters | Perth Convention & Exhibition Centre, flipped from Exclude to Create. The find is done (09 Sep) and the call is made — build both, the green side is not being read where it counts |
| 6 | Read-only check | Confirm an account after it is built |

Prompt 2 assumes prompt 1 has run, so the 5000021_ accounts at Gympie and Archerfield are closed but
still listed. Prompt 5 stands on its own — nothing in 1–4 touches Perth. The earlier prompts (the 17 permanent accounts, the 12 Origin close-offs, the Mogo read)
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

## 5 · The two PCEC meters — build the two certificate accounts

Perth Convention & Exhibition Centre is register rows 159 and 160 (review rows 75 and 76) — two of the
seven WA Alinta rows I excluded because the account's own green component already carries the offset.
These two are being flipped to **Create**. Both meters sit at one location, `LSE - Perth Convention &
Exhibition Centre (WA)`, Location Ref 9068.

I ran the find first (5a, 09 Sep 26). It came back clear enough to settle the route, so the build form
below is the only one left. 5a and the conversion form 5b are out of this file and in the git history.

### What the find turned up — 09 Sep 26

**The green side has no account of its own, so there is nothing to convert.** `Manage -> Accounts` with
Show All on — 23,520 accounts — filtered on Data Type = `Electricity - Green` returns **0 rows**.
Filtering on just "Green" returns 34, all `Waste Recycled - Green Waste`. No account style carries the
green data type, and `Admin -> Data Configuration -> Data Types` has no green electricity entry either.
The old green account at 9068, `932806640`, stops at Jun 2013 and holds nothing from 2020 on.

**It is a capture field on the account style.** `Admin -> Data Configuration -> Account Styles ->
Bid-Electricity Large Market -> Fields` tab, field **"Retail green power/FiT kWh"**, code **C_7**, with
Column set to **"C_7 GREEN KWH ONLY"**. That flag is what makes Envizi emit the second derived monthly
row with a mirrored negative factor. Not an account, not the interval meter — a field on the style.

**It was on screen the whole time, one horizontal scroll away.** Search dropdown `Accounts` → paste the
number → open → `Review` → `Monthly Data` → **drag the grid's horizontal scrollbar to the far right**.
Data Type is the last column and sits off-screen by default, and the mouse wheel will not move the grid
sideways. Green rows are spottable before you scroll: same kWh as the electricity row, negative
emissions, 0 GJ.

**There is no per-account lever.** `Actions -> Account Settings` opens a modal actually titled "Edit
account" — the same form as Edit Account — with no green or renewable percentage and no per-account
component switch. `Review` offers only Records and Monthly Data, and Records lists only
`Electricity [kWh]`. Account Styles is under **Manage**, not Admin; green is not in that classic list,
and the real 40-field component list is the newer `Admin -> Data Configuration` screen.

The figures tie out to the 06 Sep export exactly:

| Account | | Jun 26 | Jul 26 | Aug 26 |
| --- | --- | ---: | ---: | ---: |
| `80013757_8001000591` | electricity kWh | 175,667 actual | 174,253 actual | 188,584.40 accrued |
| | tCO2e | 87.8335 | 87.1265 | 94.2922 |
| | green kWh | 0 actual | 174,253 actual | 174,252.9995 accrued |
| | tCO2e | 0 | −87.1265 | −87.1265 |
| `80013758_8001000592` | electricity kWh | 117,687 actual | 143,301 actual | 143,301.00 accrued |
| | tCO2e | 58.8435 | 71.6505 | 71.6505 |
| | green kWh | 0 actual | 143,300 actual | 143,299.9986 accrued |
| | tCO2e | 0 | −71.65 | −71.65 |

Factor names identical on both accounts every month: electricity
`81 - Electricity - 25-26 - Western Australia (SWIS)` at 0.5, green
`81 - Electricity Green - 25-26 - Western Australia (SWIS)` at −0.5. Both still on the **25-26** vintage
in July and August 2026, so that factor set has not rolled to 26-27 any more than the LGC set had before
the 08 Sep run.

Two quirks worth keeping in view. June's green is zero on both accounts while July and August are
near-full offsets — the offset starts with the 1 Jul 26 contract. And August is accrued on both sides,
but the green accrual carried July's volume across while the electricity side accrued to a different
figure, which is why August on the 591 account nets to **+7.17 tCO2e** rather than roughly zero.

### The call — build them (09 Sep 26)

**Building both.** The green component is not being read where it needs to be, so leaving the claim
sitting on it keeps PCEC showing as unabated, and a `Certificates - Location - kWh` account is what fixes
that. Power BI reads the account style: it picks up `Certificates - Location - kWh` and does not pick up
`Electricity - Green [kWh]`.

The find ruled out the tidier version. There is no green account to convert onto the certificate style,
and no per-account switch to turn the green side off — the only control is field C_7 on the
`Bid-Electricity Large Market` style, which is estate-wide and would stop the green component on every
account carrying that style. Not a PCEC change, and not in this file.

So, what building leaves behind, written down so it is not a surprise later: **the green component keeps
offsetting in Envizi, and the new accounts offset again.** At the WA (SWIS) 26-27 LGC factor of −0.45
that is **−292.25 t counted twice across July and August**. The dashboard volume will be right; Envizi's
own emissions number for PCEC will not be, until either Power BI reads the green rows as well or these
two accounts are moved onto a neutral factor. It is on the list under **Still open** in the README.

The same sits behind the other five WA Alinta sites — register rows 161–165, all on the agreement from
1 Jul 2026, all showing zero green in June and 100% from July, all netting to about zero. They are not
being built; only PCEC is.

Two other things about this pair. Both source accounts have recorded since **1 Feb 2020**, so Effective
From July 2026 is what keeps the certificate accounts off six years of history — it matters more here
than anywhere in section 2. And the location holds **eleven** electricity accounts, nine of them closed
or out of scope, several sharing the NMI with the account I want; the account numbers differ by one digit
in two places, so the full string is what to match on.

```
You're helping me set up two renewable-certificate virtual accounts in IBM
Envizi (au001.envizi.com). I'm logged in on the Envizi tab. Both accounts are
at ONE location. Work them ONE AT A TIME, in order.

THE ONE RULE THAT MATTERS
An account can only be set up as a virtual account while it holds NO records.
So the account is created first and saved empty, and only then linked. Never
add data to it.

THIS LOCATION IS FULL OF DECOYS
There are eleven electricity accounts here. Only two are mine and they are the
only two still open on the large market style. Match the FULL account number
character for character - the live account and a closed one share the same NMI,
and my two differ from each other by one digit in two places.

  MINE, the sources:   80013757_8001000591   and   80013758_8001000592
                       (Alinta, Electricity Large Market, Opened 2/1/2020,
                        Replaced On blank)

  NOT mine - do not open Edit Account, do not pick as a source:
    80005748_8001000591            Alinta, closed 31 Jan 2020, SAME NMI as mine
    80007482_8001000592            Alinta, closed 31 Jan 2020, SAME NMI as mine
    932806640                      Electricity Green, closed 30 Jun 2013
    414267220_8001905073           Synergy, Small Market, a different NMI
    80005748_80010005910_CLOSED    Electricity Simple, closed
    80005748_80010005926           Electricity Simple, closed
    80007482_CLOSED                Electricity Simple, closed
    600751_80010005910             Electricity Simple, closed
    600751_80010005926             Electricity Simple, closed

There is no LGCS_ account at this location. If you find one, stop and tell me.

=== STEP 1 · Find the location ===
Top-right search, dropdown set to "Locations". Search "Perth Convention" and
open it. Confirm the Location Ref on the Summary page reads 9068. If it does
not, stop.

=== STEP 2 · Open the account list ===
From the location Summary page: Quick links -> Accounts. Click "Show All
Accounts". Before creating anything, filter the Account Number column on
"CERTS" and confirm there is nothing there, then clear the filter. The filter
sometimes renders as a search textbox and sometimes as a multi-select checkbox
list. If either of my target numbers already exists, stop and tell me - do not
edit or reuse it.

=== STEP 3 · Create the account, empty ===
Click the blue "Create New..." button and set:

  Account style      Certificates - Location - kWh
  Account number     as listed below
  Account Ref        the NMI as listed below - the NMI, NOT the account number
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
  hours", then the location, then click the plus next to the SOURCE ACCOUNT I
  name. Zoom in and match the FULL account number character for character -
  this location has a closed account on the same NMI and it will be sitting
  right next to mine in the tree. Add that one account and nothing else. The
  Selected pane should show Kilowatt hours -> the location -> the one account,
  then "*" and "Value Variable" - leave those exactly as the rule sets them.

- Condition (optional) - Effective From: July 2026 (the picker shows
  "2026 July"). Effective To: leave blank. THIS ONE MATTERS MORE THAN USUAL:
  the source has recorded since February 2020, so without it the new account
  reaches back six years. It is not optional for us.

Then SAVE. Confirm the grid reads 1 Row with Formula "Kilowatt hours*Value
Va...", Effective From 7/1/2026, Effective To blank.

=== STEP 6 · Check it ===
Open the new account and confirm Opened On reads 7/1/2026, Account Ref reads
the NMI, and there is exactly one relationship. Read the figures via Review ->
Monthly Data in the account nav - the Summary chart tooltips don't render.

On that grid, DRAG THE HORIZONTAL SCROLLBAR to the far right. Data Type is the
last column and it sits off-screen by default, and the mouse wheel will not
move the grid sideways. I need to see it.

Confirm Jul and Aug 2026 kWh match the "Expect" line and there is NO June 2026
row and nothing in 2020-2025. If any month before July 2026 has a value,
Effective From didn't take - stop and tell me.

========================= THE TWO · both at Location Ref 9068 =========================

 1. 80013757_8001000591_CERTS · ref 8001000591 · src 80013757_8001000591
    Expect Jun none · Jul 174,253 · Aug 188,584 · nothing before Jul 26
    Closed decoy on this same NMI, do NOT pick: 80005748_8001000591

 2. 80013758_8001000592_CERTS · ref 8001000592 · src 80013758_8001000592
    Expect Jun none · Jul 143,301 · Aug 143,301 · nothing before Jul 26
    Closed decoy on this same NMI, do NOT pick: 80007482_8001000592

======================================================================================

Do number 1, then stop and show me before starting number 2.

After each account, report: the account number created, Account Ref, Opened On,
the exact source account you selected, Effective From, the Jun/Jul/Aug figures
against what I expected, that nothing appears before July 2026, and the
emission factor name and value on the July row.

RULES
- Never delete, close, move or edit the SOURCE accounts or any decoy.
- Never open Edit Account on anything except the account you just created.
- If my exact target account number already exists, stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.
- Never click Save or Delete on a form you're unsure about.

WORKED EXAMPLE
900018199_3120725958_CERTS at Asphalt Prod - Brendale (423) is done and correct
- source 900018199_3120725958, measure Total Certificates, rule 100% Renewable
Energy Certificates, Effective From July 2026.
```

Expected: two `Certificates - Location - kWh` accounts at 9068, each mirroring one Alinta account from
July 2026 and nothing earlier, on the WA (SWIS) 26-27 LGC factor of −0.45. The July and August kWh will
move as the Alinta bills land — the test is that each new account equals its source, whatever the source
reads.

Then the green component, still recording on the style field and not switchable per account, so PCEC's
Envizi emissions read about −292 t better than they should for July and August until the factor or the
dashboard is dealt with. Known and accepted going in. Prompt 6 read against either account will show the
factor and the kWh side by side.

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
