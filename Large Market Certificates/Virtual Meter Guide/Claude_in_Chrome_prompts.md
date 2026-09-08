# Claude in Chrome prompts — what is left

What I paste into Claude in Chrome with Envizi (`au001.envizi.com`) open in the active tab. Each form has
been run against the real screens; the quirks noted inside them are real. Keep Envizi in front while it
works — it only sees the active tab.

Position as of the 06 Sep 26 exports: **all 60 permanent accounts are built** and every one mirrors its
source exactly in July and August with no June row. The 12 old Origin accounts read Replaced On 30 Jun
2026 and no longer accrue. Mogo has both its accounts. What remains, in the order I run it:

| # | Prompt | What it does |
| --- | --- | --- |
| 1 | Close the two connector accounts | Gympie and Archerfield still double count — 5000021_ accounts accruing beside the live 1003xxx ones |
| 2 | Build the 9 temporary accounts | Section 3 — the Queensland sites still on CS Energy with no Engie account. Run **after** prompt 1 |
| 3 | The LGC factors | Close 24-25, turn the seven `( Copy of … )` rows into 25-26, copy those to 26-27 now NGA 2026 is out |
| 4 | Fix two Account Refs | Bathurst and Mogo 4204072845 carry the account number where the NMI should be |
| 5 | Read-only check | Confirm a temporary after it is built |

Prompt 2 assumes prompt 1 has run, so the 5000021_ accounts at Gympie and Archerfield are closed but
still listed. The earlier prompts (the 17 permanent accounts, the 12 Origin close-offs, the Mogo read)
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

## 3 · The LGC emission factors — close 24-25, finish 25-26, add 26-27

Where this stands: seven `( Copy of LGCs <state> 24-25 )` rows were made in Custom Factors but never
edited — they still carry the 24-25 value and their Region reads `*Select Region*` (Envizi's Copy action
clears the region). Victoria never needed a copy because `LGCs Victoria 25-26` (−0.78) already exists.
Meanwhile the 24-25 rows have no Replaced On, so every certificate account outside Victoria is still
offsetting on 24-25. National Greenhouse Accounts Factors 2026 is out now as well, so the 26-27 set can
go in at the same time.

The vintages, each the NEGATIVE of the state's Scope 2 location-based factor:

| State | 24-25 (NGA 2024, closing) | 25-26 (NGA 2025) | 26-27 (NGA 2026) |
| --- | --- | --- | --- |
| NSW | −0.66 | −0.64 | −0.60 |
| ACT | −0.66 | −0.64 | −0.60 |
| Victoria | −0.79 | −0.78 (exists) | −0.74 |
| QLD | −0.71 | −0.67 | −0.65 |
| SA | −0.23 | −0.22 | −0.21 |
| WA (SWIS) | −0.51 | −0.50 | −0.45 |
| Tasmania | −0.15 | −0.20 | −0.23 |
| NT (DKIS) | −0.56 | −0.56 | −0.55 |

Dates follow the FY the vintage is named for: 24-25 closes 30 Jun 2025, 25-26 runs 1 Jul 2025 to
30 Jun 2026, 26-27 opens 1 Jul 2026 and stays open. Three stages, in order, with a stop after each.

```
You're helping me maintain custom emission factors in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Admin -> Custom Factors.
Wait out the loading spinner. In the Name filter search "lgc" so only the LGC
rows show. There are THREE STAGES. Do them in order, one row at a time, and
STOP where I say so.

The rows all share: Data Type "Certificates - Location [kWh]", Factor Set
"Custom - Downer", Sub Type "Default". Do not change any of those. Every
factor value is NEGATIVE - if a field won't take a minus, stop and show me.
Never delete a factor. Only touch the rows I name; match names character for
character (there are 23-24 rows and Victoria rows that stay as they are unless
I list them).

Dates: type them and tab out, then read the field back and confirm the month
and day didn't swap (30 Jun 2025 shows as 6/30/2025). If the form's end-date
field isn't called "Replaced On" (e.g. "End Date", "Valid To"), or there is
no date field at all, stop and show me the form before changing anything.

=== STAGE 1 · Close the 24-25 factors ===
Open each of these and set Replaced On = 30 Jun 2025. Change nothing else.

  LGCs NSW 24-25
  LGCs ACT 24-25
  LGCs QLD 24-25
  LGCs SA 24-25
  LGCs WA 24-25
  LGCs Tasmania 24-25
  LGCs NT 24-25
  LGCs Victoria 24-25

Before saving the first one (NSW), screenshot the Edit form so I can see every
field and what the start date reads, then stop and show me. Once I say go, do
the rest. If a 24-25 row already has a Replaced On, leave it and tell me what
it reads. If a name isn't found, say so and move on - don't pick a near match.

=== STAGE 2 · Turn the seven copies into the 25-26 set ===
The rows to edit are named "( Copy of LGCs NSW 24-25 )" etc. - brackets and
spaces are part of the name, Region reads "*Select Region*". Open each and set
Name, Region and Total CO2e exactly as below, plus Replaced On = 30 Jun 2026
(the 26-27 set takes over from 1 Jul 2026). If the form has a start / opened
date, set it to 1 Jul 2025.

  Copy row                              New name                Region                                     Total CO2e
  ( Copy of LGCs NSW 24-25 )            LGCs NSW 25-26          Australia - New South Wales                 -0.64
  ( Copy of LGCs ACT 24-25 )            LGCs ACT 25-26          Australia - Australian Capital Territory    -0.64
  ( Copy of LGCs QLD 24-25 )            LGCs QLD 25-26          Australia - Queensland                      -0.67
  ( Copy of LGCs SA 24-25 )             LGCs SA 25-26           Australia - South Australia                 -0.22
  ( Copy of LGCs WA 24-25 )             LGCs WA 25-26           Australia - Western Australia               -0.50
  ( Copy of LGCs Tasmania 24-25 )       LGCs Tasmania 25-26     Australia - Tasmania                        -0.20
  ( Copy of LGCs NT 24-25 )             LGCs NT 25-26           Australia - Northern Territory              -0.56

Then open the existing "LGCs Victoria 25-26" and set Replaced On = 30 Jun 2026
only. Leave its Region as it is (it reads plain "Australia" - I'll deal with
that separately) and leave the value at -0.78.

Check before each edit that no row with the new name already exists; if one
does, skip and tell me. Do NSW first, stop and show me the saved row, then the
rest.

=== STAGE 3 · Copy the 25-26 set to make 26-27 ===
Use the same Copy action that made the "( Copy of ... )" rows. Copy each 25-26
row (the eight from Stage 2, Victoria included) and edit the copy to:

  Copy from                New name                Region                                     Total CO2e
  LGCs NSW 25-26           LGCs NSW 26-27          Australia - New South Wales                 -0.60
  LGCs ACT 25-26           LGCs ACT 26-27          Australia - Australian Capital Territory    -0.60
  LGCs Victoria 25-26      LGCs Victoria 26-27     Australia - Victoria                        -0.74
  LGCs QLD 25-26           LGCs QLD 26-27          Australia - Queensland                      -0.65
  LGCs SA 25-26            LGCs SA 26-27           Australia - South Australia                 -0.21
  LGCs WA 25-26            LGCs WA 26-27           Australia - Western Australia               -0.45
  LGCs Tasmania 25-26      LGCs Tasmania 26-27     Australia - Tasmania                        -0.23
  LGCs NT 25-26            LGCs NT 26-27           Australia - Northern Territory              -0.55

Copy clears the Region, so set it on every one. Start / opened date 1 Jul 2026
if the form has one. Replaced On stays BLANK - these are the live set. Copying
carries the 30 Jun 2026 Replaced On across from the 25-26 row, so clear it on
each copy and read the field back to make sure it's empty. Do NSW first, stop
and show me, then the rest.

=== OUTPUT ===
When all three stages are done, filter Name "lgc" again and give me one table
of every LGC row: Name | Region | Total CO2e | start date | Replaced On. I'm
expecting 24 rows across 24-25 / 25-26 / 26-27 plus the 23-24 rows, no
"( Copy of" names left, and no "*Select Region*" left.
```

Expected afterwards: the next certificates export shows `LGCs NSW 26-27` (−0.60) on the NSW accounts
for July 2026 on, and Bathurst nets to zero in July instead of −1.08 t. The historical `LGCS_` accounts
will recalculate onto whichever vintage their month falls in — that is the intended outcome, but the
next export is worth a glance at FY25 and FY26 totals for those accounts. If the accounts stay on 24-25
after the dates are in, the factor set's date handling or region mapping needs a look — that is a
separate, read-only step.
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

## 5 · Read-only check on a finished account

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
