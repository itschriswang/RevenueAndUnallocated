# Claude dispatch prompts - EngieAU electricity accounts, Sep16 grid_data extract

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
work the 7 EngieAU electricity accounts sitting at `Unallocated Accounts` in
`grid_data_2026Sep16_16h5m10s.csv`. Run in order: a **read-only survey** (done, 16 Sep 26 - see "Survey
results" below), then **1** allocate each account and close the CS Energy meter it supersedes, site by
site (done, 18 Sep 26 - see "Run record"); **2b** delete two duplicated May records the survey turned up;
and **3** retire the 7 Section 3 temporary certificate accounts the survey found and rebuild them against
the Engie source. Keep Envizi in front while it works - it only sees the active tab.

**Both remaining passes delete things, and the 18 Sep run showed this platform firing writes nobody
clicked** - a frozen dialog replayed a postback and closed an account fourteen seconds after a click aimed
somewhere else. Read "Operating notes" before running either. Neither should run until sessions stop
expiring.

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
duplicates at Gympie and Archerfield are already closed. The action passes below are rewritten to match
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
this dispatch was built on, and the action passes below are rewritten around them.

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
2026. All 11 `5000021_` accounts org-wide are Closed - full table below. This removes both from prompt 1's
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
the right close date for the seven main CS Energy accounts (prompt 1, unchanged).

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
is the one existing exception, dated a month after its data). Cards 4 and 6's accounts look like they
don't fit it: both are dated 31 Mar 2026 but hold a May-2026 actual (Archerfield's is period 2-31 May,
ref `BE8734997`) with April missing entirely.

**Checked against the 6 Sep 26 electricity export, and the date is not the problem - the May record is.**
The May figures on the closed accounts are identical, to the cent, to the May figures on the live
successor account on the same NMI:

| NMI | Closed `5000021_` May 2026 | Live `1003xxx_` May 2026 |
| --- | --- | --- |
| `QB05383854` (Archerfield) | 64,727.16 kWh / 43.37 t | 64,727.16 kWh / 43.37 t |
| `3120129028` (Gympie) | 10,717.9 kWh / 7.18 t | 10,717.9 kWh / 7.18 t |

Both actual, both the same month, both on the same NMI - a duplicated record, not a late true-up bill.
March is genuinely each account's own last month (Gympie 15,268.8 kWh, Archerfield 65,241.67 kWh, neither
matching the successor's April figure), and April hands over cleanly - no April row on the `5000021_`
account, the `1003xxx_` account starting there. **So Replaced On 31 Mar 2026 is correct on both** and
moving it to 31 May would have blessed the double count instead of removing it.

This is already a known finding. `../Envizi Data Quality/findings.md` §5 ("Data recorded after Replaced
On") lists both accounts, puts the pair at "a genuine May double count", and prescribes the fix: *delete
the May records on the two `5000021_` accounts*. Row 3 and row 4 of
`../Envizi Data Quality/csv/08_data_after_replaced_on.csv` are these two. Prompt 2b below is rewritten to
do that - 75,445 kWh / 50.55 tCO2e of duplicated May electricity - and leaves Replaced On alone.

### Tooling note

Gympie's own per-location Accounts grid rendered only 3 of its 31 accounts even with "Show All Accounts"
on, and did not list `5000021_3120129028` despite it sitting at Gympie. Cross-checking through the
org-wide Accounts grid instead returned the complete list. Don't trust a per-location grid's row count for
the rest of this work without cross-checking org-wide.

---

## Run record - prompt 1, 18 Sep 26

**Prompt 1 is done. All 7 accounts are allocated and all 7 CS Energy meters are closed at 30 Jun 2026.**
It took two sessions, and they overlapped, which is worth reading before the remaining passes are run.

| Card | Moved to | CS Energy closed |
| --- | --- | --- |
| 1 | `900018189_3051770385` -> RPQ Spray Seal (171230) | `1003072_3051770385` 30 Jun 2026 |
| 2 | `900018190_3120014382` -> RPQ Spray Seal (171230) | `1003070_3120014382` 30 Jun 2026 |
| 3 | `900018191_3120070486` -> RPQ Swanbank (171505) | `1003071_3120070486` 30 Jun 2026 |
| 4 | `900018195_3120129028` -> Gympie (142) | `1003085_3120129028` 30 Jun 2026 |
| 5 | `900018196_3120103988` -> Asphalt Prod - Bli Bli (408) | `1003079_3120103988` 30 Jun 2026 |
| 6 | `900018197_QB05383854` -> Asphalt Prod - Archerfield (406) | `1003081_QB05383854` 30 Jun 2026 |
| 7 | `900018203_3120143385` -> PPP - Sunshine Coast Univ Hospital (9078) | `1003075_3120143385` 30 Jun 2026 |

Unallocated Accounts holds no `900018…` accounts. All three `5000021_` accounts still carry their own
31 Mar 2026, verified individually. Every `LGCS_` and `_CERTS` account is present and unchanged. Opened On
was never altered - `1003085_3120129028` and `1003081_QB05383854` both still read 4 Jan 2026.

### The two sessions overlapped - that explains the "pre-existing" moves

Session one ran inside the maintenance window and got cards 1, 2 and 3 moved before it hung. Session two
started fresh afterwards, found cards 1 and 3 already at their target locations, and correctly flagged
that it had not made those moves. Nothing else has been touching this handover - it is the first session's
work seen from the second. Both reached the same end state, and the second verified every card.

### The unintended close on `1003072_3051770385` - no rollback needed

During session one, while a Move dialog was open on a different account, a JS `SyntaxError` fired and
fourteen seconds later `1003072_3051770385` was closed with Replaced On 30 Jun 2026 (audit stamp Chris
Wang, 18/09/2026 21:50:35). Close Account(s) was never opened. The likeliest reading is a postback replayed
against stale server state as the session expired.

That session was running the old move-only prompt, where the CS Energy accounts were explicitly
do-not-touch, so it correctly reported it as damage. **Against the merged prompt it is not**: closing
`1003072_3051770385` at 30 Jun 2026 is exactly what card 1 prescribes. The write was uncontrolled; the
value it landed on was the intended one.

The data it removed is also exactly right, checked against the 6 Sep 26 electricity export:

| `1003072_3051770385` | Actual | Accrued |
| --- | --- | --- |
| Mar-Jun 2026 | 11,479 / 18,467 / 15,461 / 15,213 | 0 |
| Jul 2026 | 0 | 15,721 |
| Aug 2026 | 0 | 17,432 |

15,721 + 17,432 = **33,153 kWh**, and the account's 12-month total moved 200,469 -> 167,316, a drop of
33,153. So what disappeared was the July and August **accruals** and nothing else - no actual reading was
lost, which is why Actual% went 83.46 -> 100. Removing those accruals is the point of the close: they were
double counting against the Engie account's July and August actuals. **Do not reopen it.**

One thing it does leave open. The write did not come from a form anyone filled in, and in the same run a
stale `Supplier` value bled into an Edit Account form on a different account (below), so it is worth
confirming that nothing except Replaced On changed on `1003072_3051770385` - Supplier should still read
`CSEnergy`, Opened On should still be blank, Account Ref unchanged. That is a read, not a fix.

---

## Operating notes - how Envizi behaved on 18 Sep 26

Learned the hard way across the two prompt 1 sessions. These apply to every remaining pass and are the
reason prompt 3 is held (see below).

**A hung dialog can still write.** This is the one that matters. Sessions expired roughly four times in an
hour, and the failure mode is not a clean error - it is a frozen dialog whose postback may still land,
against stale server state, seconds later. That is how `1003072_3051770385` was closed by a click aimed at
a different account. Retrying inside a frozen dialog never worked; only a full page reload and redo did.

**So: no deletes while the platform is doing this.** A replayed close happened to land on the value we
wanted. A replayed *delete* has no such luck available. Prompt 3 deletes accounts and prompt 2b deletes
records; both wait for a session that is not expiring. Check the maintenance banner before starting.

**The maintenance window ate writes.** *Scheduled Platform Maintenance, Fri 8:00PM Sep 18 - Sat 4:00AM
Sep 19 EDT.* Inside it, every first save failed - frozen dialogs with disabled buttons, one explicit
`Error: No Data to extract metadata`, one full session timeout. After it closed, every save landed first
try. Do not run these passes inside a maintenance window.

**The Edit Account form carries stale state between accounts.** On one attempt the form for CS Energy
account `1003070_3120014382` loaded with Supplier reading **EngieAU** - bled in from the account viewed
just before. It was cancelled rather than saved, which was the right call: saving would have changed a
field other than Replaced On. **Reload the page before every Edit Account, and read Supplier back before
saving.** On a CS Energy account it must say `CSEnergy`.

**The Move dialog lies.** It showed a red *"The given key was not present in the dictionary"* and blanked
the location field on a move that had already succeeded. Never judge a move from the dialog - verify on
the account's own Summary page.

**The grids serve stale and partial data.** Gympie rendered 3 of 31 rows with Show All on; RPQ Spray Seal
reported "29 Rows" and rendered 6; the org-wide grid did not list a just-moved account until re-queried.
So the under-render is not a Gympie quirk, it is general. Verify through the org-wide Accounts grid, and
treat search as more current than any grid. A short list is never evidence of absence.

**`getselectedrowindexes` returns a self-referencing array** - it reports 2 selections when there is 1.
Count checked checkboxes in the DOM instead. This matters most where a pass acts on a selection, which is
every delete in prompt 3.

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
written against - see that section before running any of the action passes.

---

## 1 · Allocate and close, site by site - RUN, 18 Sep 26

**Merged from what were prompts 1 and 2.** They were originally two passes, with the close waiting on the
move. They don't actually depend on each other - they act on different accounts, and the CS Energy account
is already sitting at the target location whether or not the Engie account has arrived. The only thing the
old prompt 2 needed from prompt 1 was its final check ("is the Engie account now the live one here"), and
doing both at one site in one visit makes that check better, not worse: the account list is read once, with
both accounts in their final state.

Two reasons to prefer it merged:

- **One visit per location instead of two.** RPQ Spray Seal carries two of the seven, so it is six
  locations, not fourteen visits.
- **It shortens the double count.** Right now each of these NMIs has the Engie account holding July and
  August actuals while the CS Energy account accrues the same two months. Closing at 30 Jun 2026 in the
  same breath as the move closes that overlap per site rather than leaving all seven overlapping until a
  second pass runs.

The close date is 30 June 2026 for all seven - the last month each CS Energy account shows an **actual**
reading before July and August turn accrued-only, and the same date the LMC review used for the other
Engie retailer-switch close-outs. **The `5000021_` accounts are not touched here**: all three are already
closed and correctly dated 31 Mar 2026. Gympie's and Archerfield's carry a duplicated May record past
that, which is prompt 2b's job, not this one's.

What stays separate, and why: **2b** deletes records rather than editing a field, on accounts this pass
never opens. **3** deletes and rebuilds the certificate accounts, and its safety rests on an unhurried
zero-records check per account - folding account deletion into the same pass as account moves invites
exactly the confusion the card format is there to prevent. Run those on their own.

```
You're helping me hand seven electricity meters over from CS Energy to
EngieAU in IBM Envizi (au001.envizi.com). I'm logged in on the Envizi tab.
Work through the cards below ONE CARD AT A TIME, in order.

Each card is one NMI at one location and has TWO accounts, each with its own
action. They are easy to tell apart - the one being MOVED starts "900018",
the one being CLOSED starts "1003". Read both numbers off the card before
touching anything.

  MOVE  the EngieAU account (900018...) from Unallocated Accounts to the
        location on the card. Nothing else about it changes - no dates, no
        fields.
  CLOSE the CS Energy account (1003...) that is already at that location, by
        setting Replaced On to 30 June 2026. Nothing else about it changes.

WHAT "CLOSE" MEANS HERE
Set Replaced On on the Edit Account form - the way the electricity close-offs
are always done in this workbook. NOT the Actions -> Close Account(s) menu
item, and NEVER Delete.

=== STEP 1 · Find the account to move ===
Top-right search, dropdown "Accounts". Paste the 900018... number exactly.
Open it. Confirm the header shows exactly that number and "Relates to" reads
Unallocated Accounts. If it already relates to some other location, stop and
tell me - someone has moved it since the survey.

=== STEP 2 · Move it ===
Go to the Unallocated Accounts location (it is the "Relates to" link), Quick
links -> Accounts -> "Show All Accounts". Tick the checkbox on the row for MY
900018... account only. Blue "Actions" button -> "Move Account". That same
Actions menu holds "Delete Account(s)", "Close Account(s)" and "Virtual
Account Setup" - do not click any of those in this pass, ever. Screenshot the
menu and confirm before clicking.

In the move dialog, find the target location by the name on the card and
confirm its Location Ref matches the ref on the card before selecting it -
several locations share a name, the ref is what disambiguates. Save. Back on
the account Summary, "Relates to" should now read the target location.

=== STEP 3 · Open the account to close ===
Top-right search, dropdown "Accounts". Paste the 1003... number from the same
card exactly. Open it. Before changing anything, confirm all three:
  - the header shows exactly that number, character for character
  - "Relates to" reads the same location you just moved the other account to
  - Replaced On is blank (it may display as the Envizi null date 30 Dec 1899
    - read that as blank)
If it already carries a real Replaced On, STOP on this card and show me
rather than overwriting it.

=== STEP 4 · Close it ===
Blue "Actions" (top right) -> "Edit Account". Not Capture Data. Set
"Replaced On" to 30 June 2026. The field shows m/d/yyyy, so read it back as
6/30/2026, not 30/6/2026. Change nothing else on the form. Save. Back on the
Summary the left panel should read "Replaced On : 30 Jun 2026".

=== STEP 5 · Check the site ===
Open the location's account list and confirm, for this NMI:
  - the 900018... account is there exactly once, with no Replaced On
  - the 1003... account is there with Replaced On 30 Jun 2026
  - where the card names a closed 5000021... account, it is still listed and
    still carries its own original Replaced On - untouched by you
  - any LGCS_ or _CERTS accounts at the location are untouched

A caution on that list: at Gympie the per-location account grid rendered only
3 of its 31 accounts last time, even with "Show All Accounts" on, and left
out an account that is definitely there. If the list looks short, don't
conclude anything from it - cross-check through the org-wide Accounts grid
(Manage -> Accounts, Show All on, filter the Account Number) and tell me.

Report, per card: the account moved and where it now relates to (with ref),
the account closed and its Replaced On read back, and confirmation the
5000021... account and any LGCS_ / _CERTS accounts at that location are
unchanged.

Do CARD 1 completely - move AND close - then stop and show me. Once I've
confirmed it, run the rest without stopping.

RULES
- Never move the 1003... account and never close the 900018... account. One
  is moved, the other is closed, and they are not interchangeable.
- The only field that changes anywhere in this pass is Replaced On, on the
  1003... accounts only. Opened On is never touched.
- Never delete anything. Never use Close Account(s) or Virtual Account Setup.
- Never edit, move or close a 5000021... account, an LGCS_ account, a _CERTS
  account, or anything else I have not named.
- If my exact target account isn't found, or the location ref doesn't match,
  stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.

===================================== THE 7 CARDS =====================================
CARD 1 - RPQ Spray Seal, Location Ref 171230 - NMI 3051770385
  MOVE  900018189_3051770385  ->  RPQ Spray Seal (171230)
  CLOSE 1003072_3051770385    ->  Replaced On 30 June 2026
  Leave alone at this location: LGCS_3051770385, LGCS_3120014382,
    LGCS_3120136120, 1003072_3051770385_CERTS, 1003070_3120014382_CERTS

CARD 2 - RPQ Spray Seal, Location Ref 171230 - NMI 3120014382
  SAME LOCATION AS CARD 1, different NMI. Match the full account numbers.
  MOVE  900018190_3120014382  ->  RPQ Spray Seal (171230)
  CLOSE 1003070_3120014382    ->  Replaced On 30 June 2026
  Leave alone: as card 1

CARD 3 - RPQ Swanbank, Location Ref 171505 - NMI 3120070486
  MOVE  900018191_3120070486  ->  RPQ Swanbank (171505)
  CLOSE 1003071_3120070486    ->  Replaced On 30 June 2026
  Leave alone: LGCS_3120070486, 1003071_3120070486_CERTS

CARD 4 - Gympie, Location Ref 142 - NMI 3120129028
  MOVE  900018195_3120129028  ->  Gympie (142)
  CLOSE 1003085_3120129028    ->  Replaced On 30 June 2026
  Leave alone: 5000021_3120129028 (already closed 31 Mar 2026),
    LGCS_3120129028, 1003085_3120129028_CERTS
  NOTE: this is the location whose account grid under-renders. Cross-check.

CARD 5 - Asphalt Prod - Bli Bli (408), Location Ref 408 - NMI 3120103988
  MOVE  900018196_3120103988  ->  Asphalt Prod - Bli Bli (408)  (408)
  CLOSE 1003079_3120103988    ->  Replaced On 30 June 2026
  Leave alone: 5000021_3120103988 (already closed 31 Mar 2026),
    LGCS_3120103988, 1003079_3120103988_CERTS

CARD 6 - Asphalt Prod - Archerfield (406), Location Ref 406 - NMI QB05383854
  MOVE  900018197_QB05383854  ->  Asphalt Prod - Archerfield (406)  (406)
  CLOSE 1003081_QB05383854    ->  Replaced On 30 June 2026
  Leave alone: 5000021_QB05383854 (already closed 31 Mar 2026),
    LGCS_QB05383854, 1003081_QB05383854_CERTS

CARD 7 - PPP - Sunshine Coast University Hospital, Location Ref 9078 - NMI 3120143385
  MOVE  900018203_3120143385  ->  PPP - Sunshine Coast University Hospital (9078)
  CLOSE 1003075_3120143385    ->  Replaced On 30 June 2026
  Leave alone: 1003075_3120143385_CERTS
  (No LGCS_ account at this location - that is expected, not a problem.)
========================================================================================
```

Expected afterwards: each of the seven NMIs has exactly one live electricity account, the EngieAU one, at
its real location, with the CS Energy account beside it reading Replaced On 30 Jun 2026 and the July and
August accruals it was carrying no longer live. The `_CERTS` accounts are still there, still named after
the CS Energy account, still holding nothing - prompt 3 deals with those.

---

## 2b · Delete the duplicated May records on the two `5000021_` accounts

**Rewritten.** The first draft moved Replaced On from 31 Mar to 31 May 2026 to match the sibling
convention. Checking the 6 Sep 26 export showed that would have been the wrong fix: the May record on each
of these closed accounts is a cent-for-cent duplicate of the same month on the live successor account on
the same NMI, so the close date is right and the record is what's wrong. See "Sibling dating" above for
the figures. This is `../Envizi Data Quality/findings.md` §5's own prescribed action, not a new idea:
delete the May records, leave Replaced On at 31 Mar 2026.

Worth **75,445 kWh / 50.55 tCO2e** of double-counted May electricity across the two. Independent of
prompts 1 and 3 - it can run before or after them, and nothing in this dispatch depends on it.

This one deletes records rather than editing a field, so it wants a careful read step first. **Do not run
it during a maintenance window or in a session that has been expiring** - see "Operating notes". A
replayed write on a delete has no safe value to land on.

```
You're helping me remove two duplicated monthly records in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Two accounts, one at a
time, read step first on each.

WHY
Each of these two accounts is closed (Replaced On 31 Mar 2026) but holds a
May 2026 actual record. That May record is an exact duplicate of the May
record on the live account on the same NMI at the same location - same kWh,
same CO2e - so the site's May electricity is counted twice. The close date
is correct and stays as it is. Only the duplicate May record comes off.

=== PER ACCOUNT · STEP 1 · READ, then stop ===
Top-right search, dropdown "Accounts". Paste the closed account number.
Open it. Confirm "Relates to" matches the location I give you and that
Replaced On reads 31 Mar 2026. Then Review -> Monthly Data and record every
month it holds from Jan 2026 on, with the kWh.
Then open the LIVE account I name for the same NMI and read ITS May 2026
kWh.
Show me both before deleting anything. I expect:
  - the closed account to hold March and May 2026 and NOT April
  - its May kWh to equal the live account's May kWh exactly
If the two May figures are NOT identical, STOP - that would mean it is a
real separate reading, not a duplicate, and I need to look at it myself.

=== PER ACCOUNT · STEP 2 · Delete the May record ===
On the closed account, Review -> Records (not Monthly Data - Records is the
list of individual records). Find the record whose period is May 2026 - for
Archerfield it is period 2-31 May 2026, ref BE8734997. Confirm before
deleting that the row you have selected is:
  - on the CLOSED account (the 5000021_ one), not the live one
  - the May 2026 period, not March
Then delete that one record. Delete nothing else. If the screen offers to
delete more than the one record, or the confirmation names a different
period or account, CANCEL and tell me.

=== PER ACCOUNT · STEP 3 · Check it ===
Re-open the closed account, Review -> Monthly Data. Confirm May 2026 is now
gone, March 2026 is still there with its original kWh, and Replaced On
still reads 31 Mar 2026. Then re-open the LIVE account and confirm its May
2026 record is untouched - that is the one that should survive.

Report, per account: the months held before and after, the May kWh deleted,
the live account's May kWh (unchanged), and Replaced On before and after.

RULES
- Delete exactly one record per account: the May 2026 one on the closed
  5000021_ account. Never delete a record on the live account.
- Never change Replaced On on either account in this pass. 31 Mar 2026 is
  correct and stays.
- Never touch the March 2026 record - it is that account's own genuine last
  reading.
- If the closed and live May figures don't match exactly, stop before
  deleting.
- If a screen doesn't match what I've described, stop and describe what you see.

==================================== THE TWO ====================================
1. Location: Gympie (142)
   Delete the May 2026 record on: 5000021_3120129028   (closed, Replaced On 31 Mar 2026)
   Expect May 10,717.9 kWh / 7.18 t
   Live account to leave alone, and to check the figure against: 1003085_3120129028
   That account's own March figure, which stays: 15,268.8 kWh

2. Location: Asphalt Prod - Archerfield (406)  (406)
   Delete the May 2026 record on: 5000021_QB05383854   (closed, Replaced On 31 Mar 2026)
   Expect May 64,727.16 kWh / 43.37 t · period 2-31 May 2026 · ref BE8734997
   Live account to leave alone, and to check the figure against: 1003081_QB05383854
   That account's own March figure, which stays: 65,241.67 kWh
===================================================================================
```

Once this runs, rows 3 and 4 of `../Envizi Data Quality/csv/08_data_after_replaced_on.csv` are cleared and
findings §5's remaining item is the Mackay one (`A-11525536_3053135053`), which is a different fix - its
Replaced On is wrong, not its data - and is not in scope here.

---

## 3 · Retire the temporary certificate accounts and rebuild against Engie

**Rewritten twice.** The original draft created accounts from scratch; the first rewrite repointed and
renamed them. Both were wrong. The 7 `_CERTS` accounts the survey found are the Section 3 **temporary**
accounts, and the documented route when the Engie account arrives is to delete the temporary account and
rebuild against the Engie source - see "Survey results" above for the quote and the reasoning. This prompt
follows that, and the rebuild half deliberately mirrors the field-by-field form in prompt 2 of
`../Large Market Certificates/Virtual Meter Guide/Claude_in_Chrome_prompts.md`, which is the proven one.

Prompt 1 is done (18 Sep 26), so its precondition is met. It does not depend on prompt 2b.

**Hold this pass until the platform is stable.** It is the heaviest in the dispatch - it deletes seven
accounts and creates seven more - and the 18 Sep run showed frozen dialogs replaying writes against stale
state, a selection API that miscounts, grids that under-render, and stale field values bleeding between
Edit Account forms. A replayed close landed on the right value by luck; a replayed delete has no such luck
available. Before starting: check the maintenance banner, and reload the page between every account. Read
"Operating notes" first.

**Delete - decided.** The guide's route, and every one of the 7 holds zero records, so deletion loses no
history and leaves the account list clean rather than carrying seven dead `1003xxx_<NMI>_CERTS` rows
alongside their replacements. STEP 2 below deletes. The zero-records check in STEP 1 is the guard: it is
what makes the deletion safe, so it is not optional, and any account that turns out to hold records stops
there instead.

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
  this pass - prompt 1 already dealt with them.

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
        Reload the page first. This platform bleeds stale state between
        forms and has replayed a postback from a frozen dialog against the
        wrong account, so start this step on a freshly loaded page.
        In the location's account list, tick the checkbox on the TEMPORARY
        account's row ONLY. Do NOT trust getselectedrowindexes - it returns
        a self-referencing array and reports 2 selections where there is 1.
        Count the checked checkboxes in the DOM instead, and confirm the
        count is exactly 1. Screenshot the ticked row and the Actions menu
        and confirm the selection names the temporary account and nothing
        else BEFORE clicking. Then Actions -> "Delete Account(s)".
        If the dialog freezes or errors, do NOT retry inside it - retrying
        in a frozen dialog never works and the original click may still
        land. Reload the page, re-read the account list, and tell me what
        state you find before touching anything again.
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

- No deletion of anything holding history. A superseded electricity account is closed, never deleted, so
  its record stays at the location it belongs to. The two passes that do delete (3, and 2b) only ever
  touch something confirmed empty or confirmed duplicated first.
- No touching the `LGCS_<NMI>` historical certificate accounts - they stay as the pre-2026 record.
- No emission-factor changes. The LMC review already tracks the 24-25 / 25-26 / 26-27 factor vintages
  separately; these 7 accounts pick up whatever factor is live once they start recording.
- No repointing or renaming of the temporary certificate accounts. The guide's route is delete and rebuild,
  because the account name keys off its source; prompt 3 follows that.
- Prompt 3 is the only pass where Delete is used, only on the 7 temporary accounts named on its cards, and
  only after each is confirmed to hold zero records.
- Teneriffe (`3117134943`) and Southbank TAFE (`3116382269`) are left alone - their Engie accounts have
  not appeared, so their temporary accounts still have a job to do.
- No change to Replaced On on the two `5000021_` accounts. 31 Mar 2026 is correct on both; prompt 2b
  removes the duplicated May record instead, which is what `../Envizi Data Quality/findings.md` §5 asks
  for.
- Prompt 2b is the only pass that deletes a record, and only the one May record per account, only after
  its figure is confirmed identical to the live account's.
- Not in scope: findings §5's other account, Mackay `A-11525536_3053135053`. Its Replaced On is the thing
  that's wrong there, not its data, and it is nothing to do with these 7 sites.
