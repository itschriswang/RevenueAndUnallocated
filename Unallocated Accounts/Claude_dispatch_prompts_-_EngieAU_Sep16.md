# Claude dispatch prompts - EngieAU electricity accounts, Sep16 grid_data extract

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
work the 7 EngieAU electricity accounts sitting at `Unallocated Accounts` in
`grid_data_2026Sep16_16h5m10s.csv`. Run in order: a **read-only survey** (done, 16 Sep 26 - see "Survey
results" below), then **1** allocate, **2** close the superseded CS Energy meters, an optional **2b** to
fix two mis-dated close-outs the survey turned up, and **3** retire the 7 Section 3 temporary certificate
accounts the survey found and rebuild them against the Engie source. Keep Envizi in front while it works -
it only sees the active tab.

## Where these came from

`grid_data_2026Sep16_16h5m10s.csv` is a fresh Unallocated Accounts extract. Of its 20 rows, 12 are BOC /
Viva fuel and gas accounts already tracked on `3 - BOC Viva`, one (`170944_Petrol`) is the FTC row already
on hold waiting for a successor location (see `Claude_dispatch_prompts_-_Fuel_Cards_FTC.md`), and 7 are
new `EngieAU` `Electricity Small Market` accounts created by the Utilities Connector - the same pattern the
Aug-26 and Sep-26 cycles worked through (`README.md`'s "Five electricity accounts have appeared" note),
filling more gaps in the `900018189-900018219` series. This dispatch is for those 7 only.

Matched by NMI (the text after the last underscore in the account number) against the 05 Sep 26 accounts
extract, every one resolves to exactly one location, already carrying a CS Energy account on the same NMI
created by the Utilities Connector - the same CS Energy -> Engie handover the earlier batches went
through. Two of the seven locations (Gympie, Archerfield) also carry a second, older CS Energy connector
account on the same NMI that the Large Market Certificates review already flagged as a missed close-out
(`Large Market Certificates/README.md`, "Section 1 - 14 accounts to close off").

**Superseded by the 16 Sep 26 survey run - see below.** Prompt 0 has now actually been run in Envizi.
Three of the assumptions above turned out wrong: a `_CERTS` account already exists at every one of the 7
locations - they are the Section 3 **temporary** accounts built against the CS Energy source while the
Engie account was awaited, and the documented route is to delete and rebuild them; the new EngieAU
accounts already hold actual July/August data rather than starting empty; and the two `5000021_`
duplicates at Gympie and Archerfield are already closed. Prompts 2 and 3 below are rewritten to match
what the survey actually found; the "Survey results" section is the record of what changed and why.

## The 7 accounts

| # | Account | Location | Location ref | NMI | CS Energy account(s) to replace |
| --- | --- | --- | --- | --- | --- |
| 1 | `900018189_3051770385` | RPQ Spray Seal | 171230 | 3051770385 | `1003072_3051770385` |
| 2 | `900018190_3120014382` | RPQ Spray Seal | 171230 | 3120014382 | `1003070_3120014382` |
| 3 | `900018191_3120070486` | RPQ Swanbank | 171505 | 3120070486 | `1003071_3120070486` |
| 4 | `900018195_3120129028` | Gympie | 142 | 3120129028 | `1003085_3120129028` **and** `5000021_3120129028` (older duplicate connector account, still open - see below) |
| 5 | `900018196_3120103988` | Asphalt Prod - Bli Bli (408) | 408 | 3120103988 | `1003079_3120103988` only - its `5000021_3120103988` sibling already carries Replaced On 31 Mar 2026 |
| 6 | `900018197_QB05383854` | Asphalt Prod - Archerfield (406) | 406 | QB05383854 | `1003081_QB05383854` **and** `5000021_QB05383854` (older duplicate connector account, still open - see below) |
| 7 | `900018203_3120143385` | PPP - Sunshine Coast University Hospital | 9078 | 3120143385 | `1003075_3120143385` |

Rows 4 and 6 are the two the LMC review already named: "Gympie and Archerfield (406) each carry a second
CS Energy account created by the Utilities Connector, accruing with no Opened On and no actuals. Nine of
its `5000021_` siblings have already been closed off at 31 Mar, 31 May and 30 Jun 26 - these two were
missed." The survey reads each `5000021_` account's records before a close date is picked, rather than
assuming 30 Jun like the others - the README is explicit that the date should match how the siblings were
closed, not be guessed.

---

## Survey results - 16 Sep 26 run

Prompt 0 was run read-only against all 7 cards. Nothing was changed. Three findings overturn assumptions
this dispatch was built on, and prompts 2 and 3 below are rewritten around them.

**1. A real `_CERTS` account already exists at every one of the 7 locations - none is missing.** They are
named after the OLD (CS Energy) account, not the new EngieAU one:

`1003072_3051770385_CERTS` · `1003070_3120014382_CERTS` · `1003071_3120070486_CERTS` ·
`1003085_3120129028_CERTS` · `1003079_3120103988_CERTS` · `1003081_QB05383854_CERTS` ·
`1003075_3120143385_CERTS`

All are Supplier `LGC Virtual Account`, Type Virtual, Status Open, Opened On 1 Jul 2026, zero records.

**These are not a naming mistake - they are the Section 3 temporary accounts, and they were always meant
to be deleted.** They were built by prompt 2 of
`../Large Market Certificates/Virtual Meter Guide/Claude_in_Chrome_prompts.md` ("Build the 9 temporary
accounts - section 3"): Queensland sites contracted to Engie from 1 Jul 26 whose Engie account had not
yet appeared in Envizi, so on the Director's call a certificate account was built against the **CS Energy**
account as an interim, to keep the renewable claim in the FY27 numbers from July. That prompt's own closing
note says what happens next, and it is not a rename:

> "When the Engie account appears on one of these NMIs, that site's temporary account comes off: delete
> `1003xxx_<NMI>_CERTS`, then build `9000182xx_<NMI>_CERTS` against the Engie account with this same form.
> The delete register on the guide page carries the tick per row."

`Large Market Certificates/README.md` gives the reasoning under "Why they get deleted rather than
repointed" - the account name keys off its source, so it is only right while the meter follows that
source. Card 1's `1003072_3051770385_CERTS` is the very example the README uses. The 7 EngieAU accounts in
this dispatch are those Engie accounts arriving, so prompt 3 below is **delete and rebuild**, matching the
documented route, not the repoint/rename I originally drafted.

Mapping the nine temporary accounts against this dispatch: **7 of the 9 are now unblocked** (cards 1-7),
and **2 stay temporary** because no Engie account has appeared on their NMI yet:

| Temporary account | Location | Status |
| --- | --- | --- |
| `1003084_3117134943_CERTS` | Teneriffe - Brisbane (QLD), ref 1020 | stays - no Engie account on `3117134943` |
| `1003074_3116382269_CERTS` | PPP - Southbank TAFE (QLD), ref 9108 | stays - no Engie account on `3116382269` |

**And they have done nothing.** Prompt 2's build form expected each to mirror its CS Energy source's
July/August accruals (RPQ Spray Seal Jul 15,721 / Aug 17,432, Bli Bli 63,426 / 63,426, Archerfield 75,559
/ 75,559, and so on). All 7 read **zero records** instead. So either the relationship step was never run
or it never took, and the interim renewable claim those accounts existed to capture has not landed in
July or August for any of these 7 QLD sites. That makes the deletion clean - there is no history to lose -
but it is also worth knowing on its own: **the FY27 QLD renewable claim for these sites is currently
missing, not merely mis-named.** STEP 1 of prompt 3 reads each account's relationship grid to settle which
of the two it was.

**2. Every new EngieAU account already holds Jul/Aug 2026 actual data - none is empty.** 30 rows, first
2026-07, last 2026-08, all Source Actual. This is consistent across every `900018xxx` account org-wide
(all show last data 31/08/2026), so it reads as normal Utilities Connector behaviour rather than a fault -
but it means the "new accounts start empty" assumption in the original prompt 3 was wrong. It has no
bearing on the move in prompt 1.

**3. Cards 4 and 6's `5000021_` accounts are already Closed, not open.** Both carry Replaced On 31 Mar
2026. All 11 `5000021_` accounts org-wide are Closed - full table below. This removes both from prompt 2's
close list, but the dates on exactly these two look wrong against how their nine siblings were dated (see
"Sibling dating" below) - flagged as a decision, not auto-corrected.

### Card-by-card

| Card | New acct: records? | Old acct(s): first/last month - Jul-26+? - Opened On - Replaced On | Certificate accounts at location | Clash | Odd |
| --- | --- | --- | --- | --- | --- |
| 1 RPQ Spray Seal (171230) | Y - 2026-07 to 2026-08, Actual | `1003072_3051770385` 2023-07 to 2026-08 - Y (accrued only, last actual Jun-26) - blank - blank | `LGCS_3051770385`, `LGCS_3120014382`, `LGCS_3120136120`, `1003072_3051770385_CERTS`, `1003070_3120014382_CERTS` | none | 3 LGCS rows (a third NMI, 3120136120, sits at this location outside our cards) + 2 CERTS |
| 2 RPQ Spray Seal (171230) | Y - 2026-07 to 2026-08, Actual | `1003070_3120014382` 2023-07 to 2026-08 - Y (accrued only, last actual Jun-26) - blank - blank | same 5 as card 1 | none | shares location with card 1 |
| 3 RPQ Swanbank (171505) | Y - 2026-07 to 2026-08, Actual | `1003071_3120070486` 2023-07 to 2026-08 - Y (accrued only, last actual Jun-26) - blank - blank | `LGCS_3120070486`, `1003071_3120070486_CERTS` | none | - |
| 4 Gympie (142) | Y - 2026-07 to 2026-08, Actual | `1003085_3120129028` 2026-04 to 2026-08 - Y (accrued only, last actual Jun-26) - 4 Jan 2026 - blank - Open. `5000021_3120129028` 2023-07 to 2026-05 - N - blank - 31 Mar 2026 (already Closed) | `LGCS_3120129028`, `1003085_3120129028_CERTS` | none | `5000021` already closed but holds a May-26 actual dated after its own close date; Apr-26 missing |
| 5 Bli Bli (408) | Y - 2026-07 to 2026-08, Actual | `1003079_3120103988` 2026-04 to 2026-08 - Y (accrued only, last actual Jun-26) - blank - blank. `5000021_3120103988` 2023-07 to 2026-03 - N - blank - 31 Mar 2026 (confirmed) | `LGCS_3120103988`, `1003079_3120103988_CERTS` | none | clean - data stops exactly at the close date |
| 6 Archerfield (406) | Y - 2026-07 to 2026-08, Actual | `1003081_QB05383854` 2026-04 to 2026-08 - Y (accrued only, last actual Jun-26) - 4 Jan 2026 - blank - Open. `5000021_QB05383854` 2023-07 to 2026-05 - N - blank - 31 Mar 2026 (already Closed) | `LGCS_QB05383854`, `1003081_QB05383854_CERTS` | none | identical to card 4 - May-26 actual after close date; Apr-26 missing |
| 7 SCUH (9078) | Y - 2026-07 to 2026-08, Actual | `1003075_3120143385` 2023-07 to 2026-08 - Y (accrued only, last actual Jun-26) - blank - blank | `1003075_3120143385_CERTS` only - no `LGCS_3120143385` exists anywhere | none | the one card with no LGCS row |

"Relates to" confirmed on-screen for every account. Account numbers matched character for character. On
every old CS Energy account, Jul-26+ means accrued only - the last **actual** reading on all seven is June
2026, which is exactly the handover pattern the earlier Engie batches showed and confirms 30 Jun 2026 as
the right close date for the seven main CS Energy accounts (prompt 2, unchanged).

### Sibling dating for the `5000021_` accounts

All 11 exist and all are Closed:

| Account | Location | Replaced On | Last actual data |
| --- | --- | --- | --- |
| `5000021_QB05383854` | Archerfield (406) | 31 Mar 2026 | 31 May 2026 <- mismatch |
| `5000021_3120103988` | Bli Bli (408) | 31 Mar 2026 | 31 Mar 2026 |
| `5000021_3120725958` | Brendale (423) | 31 Mar 2026 | 31 Mar 2026 |
| `5000021_3120129028` | Gympie | 31 Mar 2026 | 31 May 2026 <- mismatch |
| `5000021_QGGG000010` | Maryborough | 31 Mar 2026 | 31 Mar 2026 |
| `5000021_QGGG000320` | Maryborough | 31 Mar 2026 | 31 Mar 2026 |
| `5000021_QB06082220` | MT-Carrara | 31 May 2026 | 31 May 2026 |
| `5000021_QB06081428` | MT-Carrara | 31 Mar 2026 | 31 Mar 2026 |
| `5000021_3116600011` | Richlands | 30 Jun 2026 | 31 May 2026 |
| `5000021_3117134943` | Teneriffe | 31 May 2026 | 31 May 2026 |
| `5000021_3053253239` | Torbanlea | 31 Mar 2026 | 31 Mar 2026 |

The convention across the other nine is Replaced On = end of the last month holding actual data (Richlands
is the one existing exception, dated a month after its data). Cards 4 and 6's accounts don't fit it: both
were dated 31 Mar 2026 but subsequently picked up a May-2026 actual (Archerfield's is period 2-31 May,
ref `BE8734997`) with April missing entirely. On the sibling rule they should read 31 May 2026, not 31
Mar. This is a **date correction on an already-closed account**, not a close action, so it is broken out
as its own optional prompt (2b) rather than folded into prompt 2 - confirm before running it.

### Tooling note

Gympie's own per-location Accounts grid rendered only 3 of its 31 accounts even with "Show All Accounts"
on, and did not list `5000021_3120129028` despite it sitting at Gympie. Cross-checking through the
org-wide Accounts grid instead returned the complete list. Don't trust a per-location grid's row count for
the rest of this work without cross-checking org-wide.

---

## 0 · Survey (read-only) - RUN, 16 Sep 26

Nothing changes in this pass. It produced the readings above. Kept here for the record and in case any
card needs a re-read; no need to run it again unless something changes underneath the 7 cards.

```
You're helping me review some electricity accounts in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. THIS PASS IS READ-ONLY.
Do not click Edit, Save, Move, Close, Delete or Actions -> anything on any
account. If you land on a form that can save, back out.

Work through the 7 cards below ONE AT A TIME, in order. Each card has a NEW
account (currently at Unallocated Accounts) and one or two OLD accounts (the
CS Energy meter(s) it replaces). For each card:

=== READING A · The new account ===
Top-right search, dropdown "Accounts". Paste the new account number exactly.
Open it. Confirm the header shows exactly that number and "Relates to" reads
Unallocated Accounts. Review -> Monthly Data: record whether it holds any
records at all, and if so the first and last month with a value.

=== READING B · Each old CS Energy account ===
Same search. Paste the old account number. Confirm "Relates to" matches the
location I give you for this card. Review -> Monthly Data: record the first
and last month with a value, and whether any month from July 2026 on has a
value. Left panel: record Opened On and Replaced On (a blank Replaced On may
show as the Envizi null date 30 Dec 1899 - read that as blank).

=== READING C · The location's certificate accounts ===
From either account's Summary, Quick links -> Accounts -> "Show All
Accounts" (or search Accounts for the location name). List every account
whose Account Number starts with "LGCS_" or ends in "_CERTS" or "_CERT" at
this location, with its Account Number and Reference. I expect to find only
one "LGCS_<NMI>" row per card and nothing ending "_CERTS" - tell me
immediately if a real "_CERTS" account already exists, since that changes
prompt 3.

=== READING D · Name clash check ===
Whether any account at the location - open or closed - already carries
exactly "<new account>_CERTS" or "<new account>_closed". Record the clashing
number or "no clash".

=== OUTPUT ===
One row per card in a table: Card | New acct has records (Y/N, first/last
month) | Old acct(s): number, first/last month, has Jul-26+ (Y/N), Opened
On, Replaced On | Certificate accounts found at location | Name clash | 
Anything odd.

Do card 1, then stop and show me the table so I can check the readings
before you run the rest. Then continue to the end without stopping.

RULES
- Read-only. No edits of any kind, on any account or location.
- If a screen doesn't match what I've described, stop and describe what you see.
- Match account numbers character for character.

================================== THE 7 CARDS ==================================
Card 1 - Location: RPQ Spray Seal (Ref 171230)
  New: 900018189_3051770385
  Old: 1003072_3051770385

Card 2 - Location: RPQ Spray Seal (Ref 171230)
  New: 900018190_3120014382
  Old: 1003070_3120014382

Card 3 - Location: RPQ Swanbank (Ref 171505)
  New: 900018191_3120070486
  Old: 1003071_3120070486

Card 4 - Location: Gympie (Ref 142)
  New: 900018195_3120129028
  Old: 1003085_3120129028   AND   5000021_3120129028

Card 5 - Location: Asphalt Prod - Bli Bli (408)  (Ref 408)
  New: 900018196_3120103988
  Old: 1003079_3120103988   (5000021_3120103988 already shows Replaced On 31 Mar 2026 - read it anyway and confirm)

Card 6 - Location: Asphalt Prod - Archerfield (406)  (Ref 406)
  New: 900018197_QB05383854
  Old: 1003081_QB05383854   AND   5000021_QB05383854

Card 7 - Location: PPP - Sunshine Coast University Hospital (Ref 9078)
  New: 900018203_3120143385
  Old: 1003075_3120143385
==================================================================================
```

What was actually found is in "Survey results" above, not the expectations this prompt was originally
written against - see that section before running prompts 2 or 3.

---

## 1 · Allocate the 7 accounts to their locations

```
You're helping me move 7 electricity accounts onto their correct locations
in IBM Envizi (au001.envizi.com). I'm logged in on the Envizi tab. Work
through the list below ONE AT A TIME, in order.

=== STEP 1 · Find the account ===
Top-right search, dropdown "Accounts". Paste the account number exactly.
Open it. Confirm the header shows exactly that number and "Relates to" reads
Unallocated Accounts. If it already relates to some other location, stop and
tell me - someone has moved it since the survey.

=== STEP 2 · Move it ===
Go to the Unallocated Accounts location (it is the "Relates to" link), Quick
links -> Accounts -> "Show All Accounts". Tick the checkbox on the row for MY
account only. Blue "Actions" button -> "Move Account". That same Actions
menu holds "Delete Account(s)", "Close Account(s)" and "Virtual Account
Setup" - do not click any of those in this pass, ever. Screenshot the menu
and confirm before clicking.

In the move dialog, find the target location by the name I give you and
confirm its Location Ref matches the ref I give you before selecting it -
several locations share a name, the ref is what disambiguates. Save. Back on
the account Summary, "Relates to" should now read the target location.

=== STEP 3 · Check it ===
Open the target location's account list. Confirm my account is listed there
exactly once, and that the CS Energy account(s) on the same NMI I name are
still there too - I am not touching those in this prompt.

Report, per account: the number, the location it now relates to and its ref,
and confirmation the matching CS Energy account(s) are still present and
unedited.

Do the first account, then stop and show me. Once I've confirmed it, run the
rest without stopping.

RULES
- Never delete anything. Never use Close Account(s) or Virtual Account Setup
  in this pass.
- Never edit, move or close any account I have not named.
- If my exact target account isn't found, or the location ref doesn't match,
  stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.

================================ THE 7 ACCOUNTS ================================
900018189_3051770385   -> RPQ Spray Seal  (171230)
900018190_3120014382   -> RPQ Spray Seal  (171230)
900018191_3120070486   -> RPQ Swanbank  (171505)
900018195_3120129028   -> Gympie  (142)
900018196_3120103988   -> Asphalt Prod - Bli Bli (408)  (408)
900018197_QB05383854   -> Asphalt Prod - Archerfield (406)  (406)
900018203_3120143385   -> PPP - Sunshine Coast University Hospital  (9078)
==================================================================================
```

---

## 2 · Close the superseded CS Energy accounts

Only run this after prompt 1 has confirmed all 7 are allocated. The survey confirms 30 June 2026 for all
seven main CS Energy accounts - it is the last month each shows an **actual** reading before Jul/Aug turn
to accrued-only, the same handover pattern the LMC review used for the other Engie retailer-switch
close-outs. **The two `5000021_` duplicates at Gympie and Archerfield are NOT in this list** - the survey
found both already Closed (Replaced On 31 Mar 2026). Their date looks wrong against how the other nine
`5000021_` siblings were dated, which prompt 2b below addresses separately.

```
You're helping me close off electricity accounts that a new EngieAU account
has superseded, in IBM Envizi (au001.envizi.com). I'm logged in on the
Envizi tab. Work through the list below ONE AT A TIME, in order.

WHAT "CLOSE" MEANS HERE
Set Replaced On on the Edit Account form - the way the electricity close-offs
are always done in this workbook. NOT the Actions -> Close Account(s) menu
item, and NEVER Delete.

=== STEP 1 · Find the account ===
Top-right search, dropdown "Accounts". Paste the account number exactly.
Open it. Confirm "Relates to" shows the location I give you. If it already
has a Replaced On, stop and show me rather than overwrite it.

=== STEP 2 · Close it ===
Blue "Actions" (top right) -> "Edit Account". Not Capture Data. Set
"Replaced On" to the date I give you for that account. Change nothing else
on the form. Save. Back on the Summary the left panel should read "Replaced
On : <the date>".

=== STEP 3 · Check it ===
Confirm the location's account list still shows the new EngieAU account
(from prompt 1) as the live one on that NMI, and this account now reads
Replaced On.

Report, per account: the number, the date set, and confirmation the location
still shows exactly one live account on the NMI (the EngieAU one).

Do the first account, then stop and show me. Once I've confirmed it, run the
rest without stopping.

RULES
- Only Replaced On changes, and only on the accounts named below.
- Never edit, move, close or delete the EngieAU accounts, the LGCS_
  accounts, or any account I have not named.
- If an account already has a Replaced On, stop and tell me rather than
  changing it.
- If a screen doesn't match what I've described, stop and describe what you see.

================================ THE ACCOUNTS TO CLOSE ================================
1003072_3051770385   at RPQ Spray Seal (171230)                          -> Replaced On: 30 June 2026
1003070_3120014382   at RPQ Spray Seal (171230)                          -> Replaced On: 30 June 2026
1003071_3120070486   at RPQ Swanbank (171505)                            -> Replaced On: 30 June 2026
1003085_3120129028   at Gympie (142)                                     -> Replaced On: 30 June 2026
1003079_3120103988   at Asphalt Prod - Bli Bli (408) (408)               -> Replaced On: 30 June 2026
1003081_QB05383854   at Asphalt Prod - Archerfield (406) (406)           -> Replaced On: 30 June 2026
1003075_3120143385   at PPP - Sunshine Coast University Hospital (9078)  -> Replaced On: 30 June 2026
=========================================================================================
```

Note: `5000021_3120103988` (Bli Bli) and the two `5000021_` accounts at Gympie and Archerfield are NOT in
this list - all three are already Closed. Bli Bli's date checks out (31 Mar 2026, matching its own last
actual). Gympie's and Archerfield's dates don't - see prompt 2b.

---

## 2b · Fix the two mis-dated `5000021_` close-outs (optional - confirm first)

Not a close action - both accounts are already Closed. This only corrects the Replaced On date on two
accounts that were dated 31 Mar 2026 but kept recording an actual reading in May 2026 with April missing,
which breaks the "Replaced On = end of last month with actual data" convention every other `5000021_`
sibling follows (Richlands is the one pre-existing exception). **Confirm you want this before running it**
- changing a date on an already-closed account is a step above the plain close-outs elsewhere in this
dispatch, and it's possible the May reading is itself the anomaly (e.g. a late-arriving true-up bill) in
which case 31 Mar 2026 might be the one worth keeping. If in doubt, leave both as they are.

```
You're helping me correct the Replaced On date on two already-closed
electricity accounts in IBM Envizi (au001.envizi.com). I'm logged in on the
Envizi tab. Work ONE account at a time.

WHY
Both accounts were dated Replaced On 31 Mar 2026, but each has a real May
2026 actual reading on record (April is missing) - one month after their
own close date. Every other closed "5000021_" sibling in Envizi is dated to
the end of its own last actual month; these two are the exception.

=== PER ACCOUNT ===
STEP 1  Top-right search, dropdown "Accounts". Paste the account number.
        Open it. Confirm "Relates to" matches the location I give you and
        Replaced On currently reads 31 Mar 2026. Review -> Monthly Data:
        re-confirm the last actual row is May 2026 and April is genuinely
        missing (not just hidden). If either doesn't match, STOP and tell
        me rather than proceeding.

STEP 2  Actions -> Edit Account. Change ONLY Replaced On, from 31 Mar 2026
        to 31 May 2026. Nothing else on the form changes. Save.

STEP 3  Re-open the account, confirm Replaced On now reads 31 May 2026 and
        nothing else changed.

Report, per account: number, location, Replaced On before and after.

RULES
- Only Replaced On changes, only on the two accounts named below.
- Do not touch any other account, including the EngieAU or CS Energy
  accounts at these same locations.
- If a screen doesn't match what I've described, stop and describe what you see.

================================ THE TWO ================================
5000021_3120129028   at Gympie (142)                            -> Replaced On: 31 Mar 2026 -> 31 May 2026
5000021_QB05383854   at Asphalt Prod - Archerfield (406) (406)   -> Replaced On: 31 Mar 2026 -> 31 May 2026
===========================================================================
```

---

## 3 · Retire the temporary certificate accounts and rebuild against Engie

**Rewritten twice.** The original draft created accounts from scratch; the first rewrite repointed and
renamed them. Both were wrong. The 7 `_CERTS` accounts the survey found are the Section 3 **temporary**
accounts, and the documented route when the Engie account arrives is to delete the temporary account and
rebuild against the Engie source - see "Survey results" above for the quote and the reasoning. This prompt
follows that, and the rebuild half deliberately mirrors the field-by-field form in prompt 2 of
`../Large Market Certificates/Virtual Meter Guide/Claude_in_Chrome_prompts.md`, which is the proven one.

Only run this after prompt 1 has confirmed all 7 EngieAU accounts are allocated, and after prompt 2 has
closed the seven main CS Energy accounts. It does not depend on prompt 2b.

**Delete or close?** The guide says delete, and every one of the 7 holds zero records, so deleting loses
nothing and leaves the account list clean. If you would rather not delete in Envizi at all, the
conservative substitute is to set Replaced On = 30 Jun 2026 on the temporary account instead of deleting
it, and carry on to the rebuild - the new account is what does the work either way. STEP 2 below is
written for the delete; swap it for a close if that's the call. **Decide before running.**

```
You're helping me retire 7 temporary renewable-certificate accounts in IBM
Envizi (au001.envizi.com) and rebuild each against the EngieAU account that
has now arrived on its NMI. I'm logged in on the Envizi tab. Work ONE card
at a time, in order, and STOP after card 1 so I can check it before you
continue.

WHY
Each of these 7 QLD sites was contracted to Engie from 1 Jul 26 before its
Engie account existed in Envizi, so an interim certificate account was built
against the CS Energy account instead - named after that CS Energy account.
The Engie account has now arrived and been allocated, so the interim account
is deleted and rebuilt against Engie. Its name keys off its source, which is
why it is not simply renamed.

TWO THINGS AT EVERY LOCATION THAT ARE NOT IN SCOPE
- "LGCS_<NMI>" accounts: the pre-2026 historical record. Never touch one.
- The CS Energy accounts ("1003xxx_..." and, at Gympie and Archerfield,
  a closed "5000021_..."). Never delete, close, move or edit any of them in
  this pass - prompt 2 already dealt with them.

=== PER CARD ===
STEP 1 · READ FIRST, read-only
        Open the TEMPORARY account named below. Confirm it sits at the
        location I give you and that Review -> Monthly Data shows ZERO
        records. Then tick it in the location's account list, Actions ->
        "Virtual Account Setup", and read the relationship grid WITHOUT
        changing anything: does it read 0 Row, or 1 Row? If 1 Row, note the
        source account, the formula and the Effective From.
        Report both readings before going further. Then:
          - Zero records, whatever the grid reads -> continue to STEP 2.
          - ANY records at all -> STOP on this card and tell me. An account
            with history is not one I want deleted.

STEP 2 · Delete the temporary account
        In the location's account list, tick the checkbox on the TEMPORARY
        account's row ONLY. Screenshot the ticked row and the Actions menu
        and confirm the selection names the temporary account and nothing
        else BEFORE clicking. Then Actions -> "Delete Account(s)".
        This is the one pass in this dispatch where Delete is intended. It
        is intended for exactly the account named on the card and nothing
        else. If the confirmation dialog names any other account, or more
        than one, CANCEL and tell me.

STEP 3 · Create the replacement, empty
        In the same location's account list, click "Create New..." and set:
          Account style   Certificates - Location - kWh
          Account number  the NEW number on the card
          Account Ref     the NMI on the card - the NMI, NOT the account number
          Supplier        LGC Virtual Account
          Reader          leave blank
          Opened On       2026-07-01  (field displays as 7/1/2026)
        Leave Reader, Linked Meter, Replaced On and Sub Type blank. Account
        Style is a jqx DIV, not a native select - click it open and type into
        its internal Search box, then click the filtered result. The Opened
        On calendar opens on the current month, so page back to July 2026 and
        click 1. Save. Do NOT add any records, monthly data or capture data -
        an account can only become a virtual account while it holds none.

STEP 4 · Open Virtual Account Setup
        Back in the account list, tick the row for the account you just
        created, then Actions -> "Virtual Account Setup". Confirm the
        breadcrumb on the Virtual Account Relationships page names the NEW
        _CERTS account and the grid reads 0 Row. If it names anything else,
        stop. (The grid sometimes shows a second row pre-ticked - that is a
        display artifact.)

STEP 5 · Create the relationship
        Click "Create New...". Fill all three tabs BEFORE saving:
        - Select rule - Measure: Total Certificates. Data Rule: 100%
          Renewable Energy Certificates (subtitle "Kilowatt hours*Value
          Variable"). The Measure dropdown occasionally renders empty on
          first click; click it again.
        - Source data - expand "Kilowatt hours", then the location, then
          click the plus next to the SOURCE ACCOUNT on the card - the
          EngieAU "900018xxx_" one. Zoom in and match the full account
          number character for character. Add that one account and nothing
          else. Do NOT pick the CS Energy "1003xxx_" account or, at Gympie
          and Archerfield, the closed "5000021_" one - both are still listed
          and both are decoys here.
        - Condition (optional) - Effective From: July 2026 (the picker shows
          "2026 July"). Effective To: leave blank. This is what stops the
          account reaching back before the renewal, so it is not optional.
        SAVE. Confirm the grid reads 1 Row, Effective From 7/1/2026,
        Effective To blank.

STEP 6 · Check it
        Open the new account. Confirm Opened On reads 7/1/2026, Account Ref
        reads the NMI, and there is exactly one relationship. Then Review ->
        Monthly Data (the Summary chart tooltips don't render). Confirm:
          - Jul and Aug 2026 kWh EQUAL the EngieAU source account's own
            Jul/Aug actuals. The source already holds actual data for both
            months, so figures should appear immediately rather than waiting
            on a future bill.
          - There is NO June 2026 row. If June has a value, Effective From
            didn't take - stop and tell me.
          - The location's LGCS_<NMI> account, where there is one, is
            untouched.

Report, per card: the temporary account deleted (and that it had zero
records), the new account number, Account Ref, Opened On, the exact source
account selected, Effective From, and the Jun/Jul/Aug figures against the
source's own.

RULES
- Delete exactly the account named on the card, and only after STEP 1
  confirms it holds zero records. Never delete anything else, ever.
- Never touch an LGCS_ account, a CS Energy account, or a 5000021_ account.
- Never use a source other than the EngieAU account named on the card.
- If my target new account number already exists at the location, stop and
  tell me - do not edit or reuse it.
- If a screen doesn't match what I've described, stop and describe what you see.

===================== THE 7 CARDS · delete, then rebuild =====================
1. Location: RPQ Spray Seal - ref 171230
   Delete:  1003072_3051770385_CERTS
   Build:   900018189_3051770385_CERTS · ref 3051770385
   Source:  900018189_3051770385   (EngieAU)
   Leave alone here: LGCS_3051770385, LGCS_3120014382, LGCS_3120136120

2. Location: RPQ Spray Seal - ref 171230   (same location as card 1)
   Delete:  1003070_3120014382_CERTS
   Build:   900018190_3120014382_CERTS · ref 3120014382
   Source:  900018190_3120014382   (EngieAU)

3. Location: RPQ Swanbank - ref 171505
   Delete:  1003071_3120070486_CERTS
   Build:   900018191_3120070486_CERTS · ref 3120070486
   Source:  900018191_3120070486   (EngieAU)
   Leave alone here: LGCS_3120070486

4. Location: Gympie - ref 142
   Delete:  1003085_3120129028_CERTS
   Build:   900018195_3120129028_CERTS · ref 3120129028
   Source:  900018195_3120129028   (EngieAU)
   Leave alone here: LGCS_3120129028
   DECOY, never pick as source: 5000021_3120129028 (closed, still listed)
   NOTE: this location's own account grid rendered only 3 of its 31 accounts
   in the survey even with Show All on. Cross-check against the org-wide
   Accounts grid before trusting what you see here.

5. Location: Asphalt Prod - Bli Bli (408) - ref 408
   Delete:  1003079_3120103988_CERTS
   Build:   900018196_3120103988_CERTS · ref 3120103988
   Source:  900018196_3120103988   (EngieAU)
   Leave alone here: LGCS_3120103988

6. Location: Asphalt Prod - Archerfield (406) - ref 406
   Delete:  1003081_QB05383854_CERTS
   Build:   900018197_QB05383854_CERTS · ref QB05383854
   Source:  900018197_QB05383854   (EngieAU)
   Leave alone here: LGCS_QB05383854
   DECOY, never pick as source: 5000021_QB05383854 (closed, still listed)

7. Location: PPP - Sunshine Coast University Hospital - ref 9078
   Delete:  1003075_3120143385_CERTS
   Build:   900018203_3120143385_CERTS · ref 3120143385
   Source:  900018203_3120143385   (EngieAU)
   No LGCS_ account at this location.

NOT IN THIS PASS - the other two temporary accounts stay as they are, because
no Engie account has appeared on their NMI yet:
   1003084_3117134943_CERTS  at Teneriffe - Brisbane (QLD), ref 1020
   1003074_3116382269_CERTS  at PPP - Southbank TAFE (QLD), ref 9108
==============================================================================
```

Expected afterwards: the next accounts extract shows each of the 7 EngieAU accounts at its real location
with the old CS Energy meter replaced (30 Jun 2026), a `9000182xx_<NMI>_CERTS` account at each of the 7
locations mirroring its Engie source's Jul/Aug actuals with no June row, no `1003xxx_<NMI>_CERTS` left at
any of the 7, and the `LGCS_<NMI>` history untouched where it exists.

Then update the Large Market Certificates side, which this changes in three places:

- The **delete register** on the guide page: tick the 7 rows retired here. Only Teneriffe
  (`3117134943`) and Southbank TAFE (`3116382269`) should remain untickable, still waiting on an Engie
  account.
- **Section 3** in `Large Market Certificates/README.md`: it currently reads "9 temporary accounts, to be
  remade later". After this pass it is 2, and 7 have become permanent accounts.
- The **coverage count** (the 60 / 68 / 78 progression) and the certificate-account population count
  (163 as at 09 Sep 26, of which 69 real `_CERTS`): this pass is net-neutral on the total - 7 deleted, 7
  built - but it moves 7 rows from temporary to permanent.

One thing to raise separately, not fixed by this pass: all 7 temporary accounts held **zero records**,
where the build form expected them to mirror their CS Energy source's July and August accruals. So the
interim QLD renewable claim never actually landed for these sites. Once the rebuild is done these 7 are
correct from July onward against the Engie actuals, but if anyone has been reading an FY27 QLD renewable
figure that assumed the temporary accounts were crediting, it was overstated. Worth a check against
whatever the July reporting was built from, and it is the same class of problem as the Torbanlea `_CERT`
naming outlier - a certificate account that exists but is invisible to whatever reads it.

## What is deliberately not in these prompts

- No deletions. Closing a superseded account keeps its history at the location it belongs to.
- No touching the `LGCS_<NMI>` historical certificate accounts - they stay as the pre-2026 record.
- No emission-factor changes. The LMC review already tracks the 24-25 / 25-26 / 26-27 factor vintages
  separately; these 7 accounts pick up whatever factor is live once they start recording.
- No repointing or renaming of the temporary certificate accounts. The guide's route is delete and rebuild,
  because the account name keys off its source; prompt 3 follows that.
- Prompt 3 is the only pass where Delete is used, only on the 7 temporary accounts named on its cards, and
  only after each is confirmed to hold zero records.
- Teneriffe (`3117134943`) and Southbank TAFE (`3116382269`) are left alone - their Engie accounts have
  not appeared, so their temporary accounts still have a job to do.
- Prompt 2b is optional and needs a decision before running, not an automatic follow-on to prompt 2.
