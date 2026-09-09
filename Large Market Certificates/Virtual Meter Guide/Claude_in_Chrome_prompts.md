# Claude in Chrome prompts — what is left

What I paste into Claude in Chrome with Envizi (`au001.envizi.com`) open in the active tab. Each form has
been run against the real screens; the quirks noted inside them are real. Keep Envizi in front while it
works — it only sees the active tab.

Position as of the 06 Sep 26 exports: **all 60 permanent accounts are built** and every one mirrors its
source exactly in July and August with no June row. The 12 old Origin accounts read Replaced On 30 Jun
2026 and no longer accrue. Mogo has both its accounts. The LGC factors are done as of 08 Sep 26 — 24-25
closed 30 Jun 2025, the 25-26 set finished and closed 30 Jun 2026, the 26-27 set live from 1 Jul 2026.
New since: the two Perth Convention & Exhibition Centre meters come off the exclusion list — prompt 5,
which is a find-then-decide rather than a straight build. The green component there already carries the
offset, so the site ends up with one mechanism, not two.
What remains, in the order I run it:

| # | Prompt | What it does |
| --- | --- | --- |
| 1 | Close the two connector accounts | Gympie and Archerfield still double count — 5000021_ accounts accruing beside the live 1003xxx ones |
| 2 | Build the 9 temporary accounts | Section 3 — the Queensland sites still on CS Energy with no Engie account. Run **after** prompt 1 |
| 3 | LGC factors tidy-up | All four vintages are in (08 Sep 26). Delete the stray `( Copy of LGCs NSW 23-24 )` and fix the Victoria 25-26 region |
| 4 | Fix two Account Refs | Bathurst and Mogo 4204072845 carry the account number where the NMI should be |
| 5 | The two PCEC meters | Perth Convention & Exhibition Centre, flipped from Exclude to Create. Three forms: **5a** finds the green component and stops, then **5b** converts it or **5c** builds the two new accounts |
| 6 | Read-only check | Confirm an account after it is built |

Prompt 2 assumes prompt 1 has run, so the 5000021_ accounts at Gympie and Archerfield are closed but
still listed. Prompt 5 stands on its own — nothing in 1–4 touches Perth, and 5b and 5c are alternatives,
not a sequence. The earlier prompts (the 17 permanent accounts, the 12 Origin close-offs, the Mogo read)
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

## 5 · The two PCEC meters — find the green component, then convert or build

Perth Convention & Exhibition Centre is register rows 159 and 160 (review rows 75 and 76) — two of the
seven WA Alinta rows I excluded because the account's own green component already carries the offset.
These two are being flipped to **Create**. Both meters sit at one location, `LSE - Perth Convention &
Exhibition Centre (WA)`, Location Ref 9068.

Three forms, run in order, with me approving between each: **5a** finds the green component and stops,
then either **5b** converts it or **5c** builds the two new accounts.

### Why there is a decision here at all

The Alinta bill books 100% green kWh on each account's own green component from July 2026, which already
nets both accounts to zero:

| | Jun 26 | Jul 26 | Aug 26 |
| --- | ---: | ---: | ---: |
| `80013757_8001000591` consumption kWh | 175,667 actual | 174,253 actual | 188,584 accrued |
| …its green component kWh | 0 | 174,253 actual | 174,253 accrued |
| …net tCO2e today | +87.83 | 0.00 | +7.17 |
| `80013758_8001000592` consumption kWh | 117,687 actual | 143,301 actual | 143,301 accrued |
| …its green component kWh | 0 | 143,300 actual | 143,300 accrued |
| …net tCO2e today | +58.84 | 0.00 | 0.00 |

Build a certificate account on top of that and the same kWh is credited twice — at the WA (SWIS) 26-27
LGC factor of −0.45 that is **−292.25 t across July and August**, and it starts the moment the
relationship saves. So the site should end up with **one** mechanism, not two. Either the green side
becomes the certificate record (5b), or it stops and the new accounts carry the claim (5c).

### What the extracts say about where the green component lives

Not encouraging for the convert route, which is why 5a runs first.

- It is **not a separate account**. In the electricity export both accounts carry two Data Type rows —
  `Electricity [kWh]` and `Electricity - Green [kWh]` — under the *same* `Item Number`, the same
  `Electricity Large Market` style, `Item Type` = `Account`, the same `Account_Meter_Link` (6181010 and
  6181011). It is a **component of the account**, so it has no account number of its own to convert.
- The one green *account* at 9068 is `932806640`, style `Electricity Green`, Account Ref 8001000592 —
  **closed 30 Jun 2013**, no data in the current period, and there is no equivalent for 8001000591 at
  all. Converting it would convert thirteen-year-old history for one of the two meters.
- `Electricity Green` looks like a **retired pattern estate-wide**: 189 accounts carry that style and
  **every one of them is closed**, 129 of them in 2017. Downer moved off separate green accounts and
  onto the green component years ago.

So on the evidence, 5c is the likely route and the green component has to be stopped at the data-load
end. What 5a might still turn up, and the extracts cannot show, is a **per-account component setting** —
a green / renewable / GreenPower percentage or a component toggle on `Account Settings`. If that exists,
it is the lever that stops the green side without touching any other account, and 5b becomes possible.

Two other things about this pair, whichever route wins. Both source accounts have recorded since
**1 Feb 2020**, so Effective From July 2026 is what keeps a certificate account off six years of history
— it matters more here than anywhere in section 2. And the location holds **eleven** electricity
accounts, nine of them closed or out of scope, several sharing the NMI with the account I want; the
account numbers differ by one digit in two places, so the full string is what to match on.

Also worth noting from the 06 Sep export: the green rows still price on
`81 - Electricity Green - 25-26 - Western Australia (SWIS)` in July and August 2026, so that factor set
has not rolled to 26-27 either.

---

### 5a · Find the green component and show me — read-only

```
You're helping me find something in IBM Envizi (au001.envizi.com). I'm logged
in on the Envizi tab. This whole form is READ-ONLY. Create, edit, save and
delete nothing. There is no step after it until I say so.

WHAT I'M LOOKING FOR
Two accounts at Perth Convention & Exhibition Centre carry a SECOND data type,
"Electricity - Green [kWh]", alongside the ordinary "Electricity [kWh]". Same
account number, same account style, Item Type "Account" - so it is a component
of the account itself, not a separate account and not the interval meter. In
July 2026 it reads 174,253 kWh on 80013757_8001000591 and 143,300 kWh on
80013758_8001000592. I can see it in the data export but not on screen. Find
where it lives in the interface and show me.

Start with 80013757_8001000591. Top-right search, dropdown set to "Accounts",
paste the full account number, open it.

--- A · on the account. Try these in order, stop at the first that shows it ---

 A1. Review -> Monthly Data. The green figure may be a COLUMN rather than a
     row, so scroll the grid sideways to the end. Look above the grid for a
     data type / component selector or a second tab, and try every option in
     it. Screenshot the grid with all columns visible.

 A2. The rest of the account nav under Review - anything named Data, Detail,
     Components, Consumption or similar. Screenshot what each one shows.

 A3. Actions -> Account Settings. NOT Edit Account, NOT Capture Data. Read
     what it says about components or data types, and tell me whether there is
     a green, renewable or GreenPower percentage set anywhere on that screen,
     and whether any component can be switched off per account. Read only -
     back out without saving.

Do NOT open Capture Data to go looking. It is a data entry form on a live
account and I do not want it opened.

--- B · on the account style. Do this one whether or not A worked ---

 A4. Admin -> Account Styles. Find "Electricity Large Market" and list every
     component it carries, with the exact component names, and say whether the
     green component is defined there. Read only - do not edit the style.

--- C · the question that decides what I do next ---

 A5. Does the green side have an ACCOUNT NUMBER of its own, or is it only ever
     a component of 80013757_8001000591 and 80013758_8001000592? Answer this
     one explicitly - it is the whole point of the exercise.

     While you're deciding: at this location there is an old account
     932806640, style "Electricity Green", Account Ref 8001000592, Replaced On
     30 Jun 2013. Open it read-only and tell me its latest month of data and
     whether it holds anything from 2025 or 2026. Do not edit it.

--- D · only if A1-A3 all came up empty ---

 A6. Find where the electricity data export lives - the one that produces a
     "Data Type" column with "Electricity - Green [kWh]" rows in it. Tell me
     the menu path. Don't run a full export, just show me the screen.

--- WHAT TO REPORT ---

First, and most important: does the green side have its own account number
(A5), and exactly where in the interface the green figure is visible, click by
click - or that it is not visible on screen at all and what each screen showed
instead.

Then, for BOTH accounts and for Jun, Jul and Aug 2026:

  - Electricity kWh, and whether it is actual or accrued
  - Electricity - Green kWh, same question
  - the tCO2e against each, and the emission factor name on each

If the green figures aren't reachable on screen, give me the Electricity ones
and say the green side is export-only.

Then stop and show me all of it. Nothing else happens until I've read it.
```

---

### 5b · Route 1 — convert the green account · **only if 5a finds one**

Run this **only** if 5a came back with a green side that has its own account number and its own row in
the account list, and I've said go. If 5a says the green side is a component of the electricity account
— which is what the export says — this form does not apply and 5c is the route.

**The dangerous confusion.** The green figure lives *on* `80013757_8001000591` and
`80013758_8001000592`. Those two accounts hold the **consumption** and six years of history. Changing
the Account Style on either of them would reinterpret all of it. The form says so three times because it
is the one way this goes badly wrong.

```
You're helping me convert an account in IBM Envizi (au001.envizi.com). I'm
logged in on the Envizi tab. ONE account at a time. I will give you the exact
account number - only ever the one I name.

WHAT CHANGES
Account Style, Supplier, and nothing else. Then a read of the virtual account
details. No records are added, nothing is deleted, no account is closed.

  Account Style   ->  Certificates - Location - kWh
  Supplier        ->  LGC Virtual Account

NEVER TOUCH THESE TWO
  80013757_8001000591
  80013758_8001000592
They are the live Alinta electricity accounts and they hold the site's
consumption back to February 2020. Do NOT open Edit Account on either of them.
Do NOT change the Account Style on either of them. If the account number I
give you is one of these two, STOP and tell me I've made a mistake - I have.

=== STEP 1 · Find it and record what it looks like now ===
Top-right search, dropdown "Accounts", paste the full account number, open it.
Confirm the account number in the header is exactly mine and "Relates to" is
LSE - Perth Convention & Exhibition Centre (WA). If not, stop.

Before changing anything, screenshot the Account Summary page and Review ->
Monthly Data, and tell me: current Account Style, Supplier, Account Ref,
Reader, Opened On, Replaced On, the earliest and latest month holding data,
and the kWh and tCO2e for the latest three months. I need this to compare
against afterwards.

=== STEP 2 · Check whether the style is even changeable ===
Blue "Actions" button -> "Edit Account". Not Capture Data.
Find the Account Style field. Before touching it, tell me whether it is
editable or greyed out, and screenshot the whole form.

If it is greyed out, or if Envizi warns that the account holds records, STOP
and show me the message. Do not accept, dismiss or work around a warning. That
answer is what I need, not a saved change.

=== STEP 3 · Set the two fields ===
Only if step 2 came back clean and I've said go.

Account Style is a jqx DIV, not a native select - form_input will fail on it.
Click it open, type "Certificates" into its internal Search box, and click
"Certificates - Location - kWh".

Supplier: replace whatever is there with  LGC Virtual Account

Leave everything else exactly as it is - Account Number, Account Ref, Reader,
Opened On, Replaced On, Sub Type. Do not reopen a closed account.

Screenshot the completed form and show me BEFORE you save. Save only when I
say so.

=== STEP 4 · Check what the change did to the history ===
Back on the Account Summary page, confirm Account Style and Supplier read the
new values and that Opened On and Replaced On are unchanged.

Then Review -> Monthly Data again, and compare against your step 1 reading.
Tell me for the same three months: the kWh, the tCO2e, and the emission factor
name. I am specifically looking for whether the historical months have been
re-priced or flipped sign now the style is different. If they have, say so
loudly - that is a problem and I need to know immediately.

=== STEP 5 · Check the virtual account details ===
Go to the location: top-right search, dropdown "Locations", "Perth
Convention", confirm Location Ref 9068. Quick links -> Accounts -> "Show All
Accounts". Tick the checkbox on the row for the converted account, click the
blue "Actions" button and choose "Virtual Account Setup".

That same Actions menu also holds "Delete Account(s)", "Close Account(s)" and
"Move Account". Do not click any of those, ever. Screenshot the menu and
confirm before clicking. If you're not certain, stop and show me.

READ ONLY on this screen. Tell me: how many rows the grid holds, and for each
one the Formula, the source account, the percentage, Effective From and
Effective To. Do NOT click "Create New...". Do NOT edit or delete a row.

If the grid reads 0 Row, say so - that is expected and it is not a problem to
fix here. An account that already holds records cannot be made a virtual
account anyway, which is exactly why we are converting this one instead of
linking it.

=== REPORT ===
Per account: what Account Style and Supplier read before and after, that
Opened On and Replaced On are unchanged, the three-month kWh / tCO2e / factor
before and after, and the full contents of the Virtual Account Setup grid.

RULES
- Only the account number I name. Never 80013757_8001000591 or
  80013758_8001000592.
- Account Style and Supplier only. Nothing else on the form.
- Never delete, close, move or reopen an account.
- Any warning about existing records: stop, screenshot, do not proceed.
- If a screen doesn't match what I've described, stop and describe what you see.
```

---

### 5c · Route 2 — build the two new certificate accounts

The default, and what the export evidence points to: the green side is a component with no account of
its own, so nothing can be converted and the two accounts get built the way the other 60 were. The green
component then has to be stopped at the data-load end, or these two accounts stay out of the FY27
market-based number.

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

Expected after 5c: two `Certificates - Location - kWh` accounts at 9068, each mirroring one Alinta
account from July 2026 and nothing earlier, on the WA (SWIS) 26-27 LGC factor of −0.45. The July and
August kWh will move as the Alinta bills land — the test is that each new account equals its source,
whatever the source reads.

Then the green component, still. Until it is settled, PCEC reads about −292 t better than it should for
July and August, and the two accounts should not go into an FY27 market-based number. Prompt 6 read
against either account will show the factor and the kWh side by side.

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
```

Expected for a right account: `Certificates - Location - kWh` · `LGC Virtual Account` / Reader blank ·
Account Ref = the NMI · Opened On 7/1/2026 · virtual, one source at 100% · Effective From 7/1/2026 ·
**no June**, July and August equal to the source · the state's LGCs factor (25-26 once prompt 3 is in).
