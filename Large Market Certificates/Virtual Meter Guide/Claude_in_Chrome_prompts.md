# Claude in Chrome prompts — what is left

What I paste into a Claude dispatch session that drives Chrome. Each session starts with no context, so
every prompt opens with how to get to Envizi (`au001.envizi.com`) and what it is looking at, and ends with a
report block I paste back into my working session to decide the next step. The quirks noted inside them are
real — each form has been run against the real screens. Keep Envizi in front while it works; it only sees the
active tab.

Position as of the 06 Sep 26 exports: **all 60 permanent accounts are built** and every one mirrors its
source exactly in July and August with no June row. The 12 old Origin accounts read Replaced On 30 Jun
2026 and no longer accrue. Mogo has both its accounts. What remains, in the order I run it:

| # | Prompt | What it does |
| --- | --- | --- |
| 1 | Close the two connector accounts | Gympie and Archerfield still double count — 5000021_ accounts recording beside the live 1003xxx ones. Both close at 31 Mar 2026 |
| 2 | Build the 9 temporary accounts | Section 3 — the Queensland sites still on CS Energy with no Engie account. Run **after** prompt 1 |
| 3 | The 25-26 LGC factors | Everything outside Victoria is still offsetting on 24-25 |
| 4 | Fix two Account Refs | Bathurst and Mogo 4204072845 carry the account number where the NMI should be |
| 5 | Read-only check | Confirm a temporary after it is built |

Prompt 2 assumes prompt 1 has run, so the 5000021_ accounts at Gympie and Archerfield are closed but
still listed. The earlier prompts (the 17 permanent accounts, the 12 Origin close-offs, the Mogo read)
are done and have been taken out; they are in the git history if I ever need the form again.

---

## 1 · Close the two connector accounts at Gympie and Archerfield

Two Utilities Connector accounts are still accruing beside the live CS Energy account on the same NMI.
The other nine `5000021_` accounts were closed the day before their `1003xxx` replacement's first month
(31 Mar, 31 May or 30 Jun 2026). The Sep 25 – Aug 26 export shows both live accounts here hold actual
data from **April 2026**, so both close at **31 Mar 2026** — the same as the five siblings whose live
account also started in April. The export also shows the connector accounts carry the same May 2026
bill as the live account, so the double count runs from April, not just July; closing at 31 Mar clears
all of it.

```
TASK: close two accounts in IBM Envizi by setting their "Replaced On" date.
You are starting with no context, so read all of this before touching anything.

=== SETUP · get to Envizi ===
1. Open a NEW Chrome tab and go to https://au001.envizi.com
2. If it shows a login page, STOP and tell me - I will log in, then say
   "continue". Do not type credentials yourself.
3. Once you see the Envizi home page (a horizontal top bar reading Manage /
   Monitor / Optimize / Report / Admin, and a search box top-right), you're in.
   Keep this tab in front the whole time - you only see the active tab.

=== BACKGROUND · what you're looking at ===
Envizi is an emissions-reporting system. It holds LOCATIONS (sites), and each
location holds ACCOUNTS (an electricity account is one meter/bill stream). An
account number ends in the NMI, the meter's national ID, after the last
underscore. Two accounts can share an NMI - that's the problem here.

At two sites a stale account created by an automated "Utilities Connector" is
still recording every month alongside the real billed account on the same NMI,
so the site's electricity is counted twice. The fix is to CLOSE the stale one at
31 March 2026: the real account has billed every month from April 2026, and the
stale one carried the genuine bills up to March, so closing it at 31 March
leaves exactly one account per month with nothing lost.

"Close" in Envizi = set the account's "Replaced On" date. Nothing is deleted.

=== THE TWO ACCOUNTS ===
Do them ONE AT A TIME, in this order. Each has a decoy - the real account,
which sits at the same location on the same NMI. NEVER edit the decoy.

 1. CLOSE:  5000021_3120129028
    Location: Gympie  (Location Ref 142)
    DECOY - do not touch:  1003085_3120129028

 2. CLOSE:  5000021_QB05383854
    Location: Asphalt Prod - Archerfield (406)  (Location Ref 406)
    DECOY - do not touch:  1003081_QB05383854

Match the account number character for character. The one to close always
starts 5000021_. The decoy always starts 1003.

=== STEP 1 · Find the account to close ===
Top-right of Envizi is a search box with a dropdown next to it. Set the
dropdown to "Accounts". Paste the full 5000021_ account number and press Enter
or click the result. You land on the Account Summary page: account number in
the page header, a left-hand panel of details, blue "Actions" button top right.

Before going further, confirm THREE things and screenshot them:
  a. The account number in the header and left panel is EXACTLY the one I gave.
  b. The left panel's "Relates to" is the location I gave.
  c. The left panel reads "Replaced On : -"  (a dash = not closed).
If any of the three disagree, STOP and show me. Do not continue.

=== STEP 2 · Open the edit form ===
Click the blue "Actions" button (top right, next to "Page Settings"). A small
menu opens with three items: Capture Data, Edit Account, Account Settings.
Click "Edit Account". Do NOT click Capture Data - that adds data.
An "Edit Account" form opens with fields like Account Style, Account Number,
Account Ref, Supplier, Reader, Opened On, Replaced On, Sub Type.

=== STEP 3 · Set Replaced On ===
Find "Replaced On:" - a date field with a small calendar icon. It sits right
above "Opened On:". Click the calendar icon. The calendar opens on the current
month; use its back arrow to page to March 2026, then click 31.
The field must now read  3/31/2026  (US order, month/day/year).
Use the calendar picker ONLY. Do not type the date - typing 3/31/2026 into the
field mis-parses to 12/31/2026. Read the field back before saving.

Leave "Opened On:" exactly as it is - it is blank on both accounts and stays
blank. Change NOTHING else on the form. Screenshot the form, then click Save.

=== STEP 4 · Check it ===
You're back on the Account Summary page. The left panel should now read
"Replaced On : 3/31/2026". Screenshot it.
Then on the account page's tab row go Review -> Monthly Data. April 2026
onwards should no longer be listed for this account (Sep 2025 to Mar 2026 stay).
If April onwards is still showing straight after saving, note it - Envizi
sometimes needs a refresh to drop them - and move on.

=== PACING ===
Do account 1 fully (steps 1-4), then STOP and show me the screenshots. Wait for
me to say "continue" before starting account 2.

=== WHEN BOTH ARE DONE · the report I paste back into my other session ===
End with a plain-text block headed "PROMPT 1 REPORT" laid out exactly like this,
one line per field, no commentary outside it:

  PROMPT 1 REPORT - connector close-offs - <today's date>
  1. 5000021_3120129028 @ Gympie
     Replaced On before: <-/date>   after: <date>   Opened On: <blank/date>
     Monthly Data after save: <Apr 2026 onwards gone / still showing / not checked>
  2. 5000021_QB05383854 @ Asphalt Prod - Archerfield (406)
     Replaced On before: <-/date>   after: <date>   Opened On: <blank/date>
     Monthly Data after save: <Apr 2026 onwards gone / still showing / not checked>
  Screens that did not match the prompt: <none / describe>
  Anything I touched other than Replaced On: <nothing / describe>
  Accounts I could not find or did not finish: <none / list>
  Ready for prompt 2 (build the 9 temporary accounts): <YES / NO - reason>

"Ready for prompt 2" is YES only if both accounts read Replaced On 3/31/2026 and
nothing else changed. If you stopped early for any reason, still produce the
report with what you have.

=== RULES ===
- Replaced On only. Never delete, move, close-via-menu, or edit anything else
  on any account. Never use "Delete Account(s)" or "Close Account(s)" from any
  Actions menu - we close by setting the date on the Edit Account form.
- Never open Edit Account on the 1003xxx decoy.
- If the 5000021_ account already shows a Replaced On date, STOP and show me.
- If any screen doesn't match what I've described, STOP and describe what you
  see with a screenshot. Never guess at a form you're unsure about.
- Never type credentials. If you get logged out, stop and tell me.
```

**Run 06 Sep 26 — done.** Both read Replaced On 3/31/2026, Opened On still blank, nothing else touched.
Monthly Data still listed April onwards straight after saving (the usual refresh lag; the next export
confirms). Two things the session found that every later prompt now carries: the Envizi nav is a
**horizontal top bar** (Manage / Monitor / Optimize / Report / Admin), and **typing a date mis-parses**
(3/31/2026 became 12/31/2026), so dates are set with the calendar picker only.

---

## 2 · Build the 9 temporary accounts — section 3

These are Queensland sites contracted to Engie from 1 Jul 26 whose Engie account has not appeared in
Envizi, so the CS Energy account is still recording. On the Director's call they get a certificate
account anyway, built against the CS Energy account, so the renewable claim is in the FY27 numbers from
July. **Every one of these is temporary.** The account name keys off its source, so when the Engie
account arrives the account is deleted and remade against it — the delete register on the guide page
tracks that.

```
TASK: create 9 empty "certificate" accounts in IBM Envizi and set each one up as
a virtual account that mirrors an existing electricity account. You are starting
with no context, so read all of this before touching anything.

=== SETUP · get to Envizi ===
1. Open a NEW Chrome tab and go to https://au001.envizi.com
2. If it shows a login page, STOP and tell me - I will log in, then say
   "continue". Do not type credentials yourself.
3. You're in when you see a horizontal top bar reading Manage / Monitor /
   Optimize / Report / Admin, with a search box top-right. Keep this tab in
   front the whole time - you only see the active tab.

=== BACKGROUND · what you're doing and why ===
Envizi holds LOCATIONS (sites); each location holds ACCOUNTS. An electricity
account number ends in the NMI (the meter's national ID) after the last
underscore. These 9 sites buy 100% renewable electricity under a contract that
started 1 July 2026, so each needs a renewable-certificate account that copies
the site's electricity kWh month by month from July 2026 on. Envizi does that
with a VIRTUAL ACCOUNT: an empty account with a rule that says "equal 100% of
account X". Nothing is typed into it - it fills itself.

THE ONE RULE THAT MATTERS: an account can only be set up as a virtual account
while it holds NO records. So each account is created and saved EMPTY, and only
then linked. Never add data to it. Never use "Capture Data".

Two of the sites (Gympie, Archerfield) also carry a second, closed electricity
account on the same NMI (starts 5000021_). It still appears in lists and in
the source-picker tree. It is a DECOY. The source is always the account I name
- the one starting 1003. Match the full account number character for character.

DATES: set every date with the calendar picker. Never type a date - typing
mis-parses (3/31/2026 becomes 12/31/2026). Read the field back before saving.

=== FOR EACH ACCOUNT · STEP 1 · Find the location ===
Top-right search box: set its dropdown to "Locations", search the location
name, open it. On the location Summary page confirm the Location Ref matches
the ref I give - several locations share a name; the ref disambiguates. If the
ref doesn't match, STOP and show me.

=== STEP 2 · Open the location's account list ===
On the location Summary page find "Quick links" and choose "Accounts". Click
"Show All Accounts". Before creating anything, filter the Account Number column
on "CERTS" and confirm MY EXACT TARGET NUMBER is not already there, then clear
the filter. (The filter renders as a search textbox or as a checkbox list.)
Rows starting LGCS_ are old certificate accounts - expected, leave them.
If my exact target already exists, STOP and tell me - do not edit or reuse it.

=== STEP 3 · Create the account, EMPTY ===
Click the blue "Create New..." button. Fill in:

  Account style      Certificates - Location - kWh
  Account number     as listed below  (ends _CERTS)
  Account Ref        the NMI as listed below - the NMI only, NOT the account number
  Supplier           LGC Virtual Account
  Reader             leave blank
  Opened On          1 July 2026  (displays 7/1/2026) - calendar picker, page
                     back to July 2026, click 1
  Linked Meter, Replaced On, Sub Type    leave blank

Account Style is a custom dropdown, not a native select - click it open, type
into its internal search box, click the filtered result. Screenshot the form,
then Save. Do NOT add any records, monthly data or capture data.

=== STEP 4 · Open Virtual Account Setup ===
Back in the location's account list, tick the checkbox on the row of the
account you just created, then click the blue "Actions" button and choose
"Virtual Account Setup".

WARNING: that same Actions menu also holds "Delete Account(s)", "Close
Account(s)" and "Move Account". Never click those. Screenshot the menu before
you click. If unsure, STOP and show me.

The grid sometimes shows a second row pre-ticked - a display artifact. Confirm
the breadcrumb on the "Virtual Account Relationships" page names my new _CERTS
account and the grid reads 0 Row. If it names anything else, STOP.

=== STEP 5 · Create the relationship ===
On "Virtual Account Relationships" click the blue "Create New...". A "Virtual
relationship" dialog opens with three tabs. Fill ALL THREE before saving:

- Select rule:  Measure = "Total Certificates".
                Data Rule = "100% Renewable Energy Certificates"
                (subtitle "Kilowatt hours*Value Variable").
                The Measure dropdown sometimes renders empty on first click -
                click it again.

- Source data:  Left pane "Available", right pane "Selected". Expand "Kilowatt
                hours", then the location, then click the plus next to the
                SOURCE ACCOUNT I name. Zoom in; match the FULL account number.
                Add that ONE account and nothing else. The Selected pane should
                read: Kilowatt hours -> the location -> the one account, then
                "*" and "Value Variable" - leave those as the rule set them.
                At Gympie and Archerfield the 5000021_ decoy is in this tree
                too. Do not pick it.

- Condition:    Effective From = July 2026 (picker shows "2026 July").
                Effective To = leave blank.
                This is what stops the account reaching back before the
                contract. It is NOT optional.

Save. Confirm the grid now reads 1 Row, Formula "Kilowatt hours*Value Va...",
Effective From 7/1/2026, Effective To blank. Screenshot it.

=== STEP 6 · Check it ===
Open the new account. Confirm Opened On reads 7/1/2026, Account Ref reads the
NMI, and there is exactly one relationship. On the account page's tab row go
Review -> Monthly Data (the Summary chart tooltips don't render). Confirm:
  - NO June 2026 row (if June has a value, Effective From didn't take - STOP)
  - Jul 2026 and Aug 2026 kWh match the "Expect" line below, to the nearest
    few kWh. A small drift is the source having moved since I read it; the
    test is that the new account EQUALS the source account's own figure,
    whatever that is. A large gap or a zero is a wrong source - STOP.

=== PACING ===
Do account 1 fully (steps 1-6), then STOP and show me the screenshots. Wait for
me to say "continue" before doing the rest. After that, run 2-9 without
stopping unless a rule says stop.

======================= THE ACCOUNTS · 9 across 8 locations, all QLD =======================

### RPQ Spray Seal - Location Ref 171230   (TWO accounts - find the location once)
    Leave alone here: LGCS_3051770385, LGCS_3120014382, LGCS_3120136120
 1. Create 1003072_3051770385_CERTS · Account Ref 3051770385
    Source 1003072_3051770385
    Expect Jun none · Jul 15,721 · Aug 17,432
 2. Create 1003070_3120014382_CERTS · Account Ref 3120014382
    Source 1003070_3120014382
    Expect Jun none · Jul 29,259 · Aug 30,991

### RPQ Swanbank - Location Ref 171505
    Leave alone here: LGCS_3120070486
 3. Create 1003071_3120070486_CERTS · Account Ref 3120070486
    Source 1003071_3120070486
    Expect Jun none · Jul 22,030 · Aug 31,514

### Asphalt Prod - Bli Bli (408) - Location Ref 408
    Leave alone here: LGCS_3120103988
 4. Create 1003079_3120103988_CERTS · Account Ref 3120103988
    Source 1003079_3120103988
    Expect Jun none · Jul 63,426 · Aug 63,426

### Gympie - Location Ref 142
    Leave alone here: LGCS_3120129028
    DECOY in the list and the source tree - do NOT pick: 5000021_3120129028
 5. Create 1003085_3120129028_CERTS · Account Ref 3120129028
    Source 1003085_3120129028
    Expect Jun none · Jul 14,156 · Aug 14,156

### Asphalt Prod - Archerfield (406) - Location Ref 406
    Leave alone here: LGCS_QB05383854
    DECOY in the list and the source tree - do NOT pick: 5000021_QB05383854
 6. Create 1003081_QB05383854_CERTS · Account Ref QB05383854
    Source 1003081_QB05383854
    Expect Jun none · Jul 75,559 · Aug 75,559

### Teneriffe - Brisbane (QLD) - Location Ref 1020
    Leave alone here: LGCS_3117134943
 7. Create 1003084_3117134943_CERTS · Account Ref 3117134943
    Source 1003084_3117134943
    Expect Jun none · Jul 8,731 · Aug 8,731

### PPP - Southbank TAFE (QLD) - Location Ref 9108
    No LGCS_ account here.
 8. Create 1003074_3116382269_CERTS · Account Ref 3116382269
    Source 1003074_3116382269
    Expect Jun none · Jul 628,450 · Aug 649,281   (by far the largest - check twice)

### PPP - Sunshine Coast University Hospital - Location Ref 9078
    No LGCS_ account here.
 9. Create 1003075_3120143385_CERTS · Account Ref 3120143385
    Source 1003075_3120143385
    Expect Jun none · Jul 18,686 · Aug 19,189

=============================================================================================

=== WHEN DONE · the report I paste back into my other session ===
End with a plain-text block headed "PROMPT 2 REPORT" laid out exactly like this,
one line per field, no commentary outside it. One entry per account, all 9,
including any you did not finish:

  PROMPT 2 REPORT - temporary certificate accounts - <today's date>
  1. 1003072_3051770385_CERTS @ RPQ Spray Seal
     Created: <yes/no/already existed>  Opened On: <date>  Account Ref: <value>
     Source linked: <full account number>  Effective From: <date>  Rows: <n>
     Monthly Data: Jun <none/value>  Jul <value>  Aug <value>
     Matches expect: <yes/no - detail>
  2. ... (same five lines, for each of 2 to 9)
  Screens that did not match the prompt: <none / describe>
  Anything I touched other than the 9 new accounts: <nothing / describe>
  Accounts I could not finish and where I stopped: <none / list>
  Decoy picked anywhere: <no / which>
  Ready for prompt 3 (emission factors): <YES / NO - reason>

"Ready for prompt 3" is YES only if all 9 exist, each has exactly one
relationship to the named source with Effective From 7/1/2026, and none has a
June row. If you stopped early, still produce the report with what you have.

=== RULES ===
- Never delete, close, move or edit a SOURCE account, a decoy, or any LGCS_
  account. Never use Delete / Close / Move from any Actions menu.
- Never add data to a new account. Never click Capture Data.
- If my exact target account number already exists, STOP and tell me.
- If any screen doesn't match what I've described, STOP and describe what you
  see with a screenshot. Never click Save on a form you're unsure about.
- Never type credentials. If you get logged out, stop and tell me.
```

The "Expect" figures are the July and August accruals on the CS Energy accounts as at the 06 Sep 26
export. They move when a bill lands, so a small difference on the day is the source having moved, not
the link being wrong — the test is that the new account equals the source, whatever the source reads.

When the Engie account appears on one of these NMIs, that site's temporary account comes off: delete
`1003xxx_<NMI>_CERTS`, then build `9000182xx_<NMI>_CERTS` against the Engie account with this same
form. The delete register on the guide page carries the tick per row.

---

## 3 · The 25-26 LGC emission factors

Every certificate account outside Victoria is still on a 24-25 factor (NSW/ACT −0.66, QLD −0.71, SA
−0.23, TAS −0.15) against electricity on 25-26 (0.64, 0.67, 0.22, 0.20), so a 100% meter over-offsets
in NSW, ACT and QLD and under-offsets in SA and TAS. Victoria already has `LGCs Victoria 25-26` (−0.78).

```
You're helping me add custom emission factors in IBM Envizi (au001.envizi.com).

We already have LGC certificate factors for 23-24 and 24-25, and one for 25-26
(Victoria only). I need the rest of the 25-26 set. Each is the NEGATIVE of that
state's Scope 2 factor from National Greenhouse Accounts Factors 2025.

Admin -> Custom Factors. Wait out the loading spinner. In the Name filter search
"lgc" and open LGCs NSW 24-25 (Region "Australia - New South Wales", -0.66) as
the template - note every field and screenshot it. Do NOT use LGCs Victoria
25-26 as the template: its Region reads plain "Australia", which is wrong.

Existing rows read: Data Type Certificates - Location - kWh, Factor Set Custom -
Downer, Sub Type Default.

Create New for each, identical to the template except:

  Name              Region                                     Total CO2e
  LGCs NSW 25-26    Australia - New South Wales                 -0.64
  LGCs ACT 25-26    Australia - Australian Capital Territory    -0.64
  LGCs QLD 25-26    Australia - Queensland                      -0.67
  LGCs SA 25-26     Australia - South Australia                 -0.22
  LGCs TAS 25-26    Australia - Tasmania                        -0.20
  LGCs NT 25-26     Australia - Northern Territory              -0.56
  LGCs WA 25-26     Australia - Western Australia               -0.50

Match each name's abbreviation to that state's own existing rows. Every value is
NEGATIVE - if a field won't take a minus, stop. Check for an existing 25-26 row
for the region first; skip and tell me if one exists. Never edit or delete an
existing factor. Do NSW first, stop and show me, then the rest.
```

Expected afterwards: the next certificates export shows `LGCs NSW 25-26` (−0.64) on the NSW accounts
and Bathurst nets to zero in July instead of −1.08 t. If the accounts stay on 24-25 after the factors
exist, the factor set's date range or region mapping needs a look — that is a separate, read-only step.

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
