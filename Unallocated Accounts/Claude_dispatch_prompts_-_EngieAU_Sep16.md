# Claude dispatch prompts - EngieAU electricity accounts, Sep16 grid_data extract

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
work the 7 EngieAU electricity accounts sitting at `Unallocated Accounts` in
`grid_data_2026Sep16_16h5m10s.csv`. Four prompts, run in order: a **read-only survey** first, then three
action passes built on what it brings back - allocate, close the superseded meter, create the virtual
certificate meter. Keep Envizi in front while it works - it only sees the active tab.

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
(`Large Market Certificates/README.md`, "Section 1 - 14 accounts to close off"). All seven locations are
in scope for a large-market-certificate virtual meter and none has a real `_CERTS` account yet - only the
historical `LGCS_<NMI>` account, which is left alone.

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

## 0 · Survey (read-only)

Nothing changes in this pass. It produces the readings the three action passes key off.

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

Expected: each new account has no records yet (Small Market accounts built by the Utilities Connector
start empty and fill in on the next bill), each old CS Energy account has been carrying the electricity
and should show nothing from July 2026 if Engie has already taken over the billing, and Reading C should
turn up exactly one `LGCS_<NMI>` row per card and no `_CERTS` account anywhere. Anything that reads
differently is worth a pause before the action passes run.

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

Only run this after prompt 1 has confirmed all 7 are allocated. Fill in the Replaced On dates from the
survey before pasting: 30 June 2026 for the main CS Energy meter at each of the 7 (the same date the LMC
review used for the other Engie retailer-switch close-outs), and for the two `5000021_` duplicates at
Gympie and Archerfield, whatever date the survey's Reading B shows matches how their nine already-closed
siblings were dated (31 Mar, 31 May or 30 Jun 2026) rather than assuming 30 Jun.

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
5000021_3120129028   at Gympie (142)                                     -> Replaced On: <from survey - match its 9 closed siblings>
1003079_3120103988   at Asphalt Prod - Bli Bli (408) (408)               -> Replaced On: 30 June 2026
1003081_QB05383854   at Asphalt Prod - Archerfield (406) (406)           -> Replaced On: 30 June 2026
5000021_QB05383854   at Asphalt Prod - Archerfield (406) (406)           -> Replaced On: <from survey - match its 9 closed siblings>
1003075_3120143385   at PPP - Sunshine Coast University Hospital (9078)  -> Replaced On: 30 June 2026
=========================================================================================
```

Note: `5000021_3120103988` at Bli Bli is NOT in this list - the survey should confirm it already carries
Replaced On 31 Mar 2026 from an earlier cycle. If the survey found otherwise, add it to the list above
with the same 31 Mar 2026 date before running.

---

## 3 · Create the virtual certificate meter for each new account

Only run this after prompt 2 confirms the old meters are closed. This follows the exact recipe
`Large Market Certificates/README.md` uses for every other Engie / large-market certificate account:
create the account empty, then set it up as a virtual meter with the new EngieAU account as its 100%
source. **A virtual meter has to be empty - the account is built by hand, never loaded with a record
first.**

```
You're helping me build 7 renewable-certificate virtual accounts in IBM
Envizi (au001.envizi.com), one for each EngieAU electricity account
allocated and switched over in the last two prompts. I'm logged in on the
Envizi tab. Work ONE account at a time, in order, and stop after the first
one so I can check it before you continue.

WHY
Each of these 7 locations already has a historical "LGCS_<NMI>" certificate
account, but none has ever had a live certificate account tracking the
current Engie supply - the LGCS_ account stays exactly as it is, untouched,
as the historical record. The new account sits alongside it.

=== PER ACCOUNT ===
STEP 1  Confirm the source account (the EngieAU one) is at its target
        location and has no Replaced On - it should be the live meter now.

STEP 2  Create a new account at the SAME location with these fields exactly:
          Account Number / Name : <source account>_CERTS
          Account Style         : Certificates - Location - kWh
          Account Reference     : the NMI (the text after the last
                                   underscore in the source account number)
          Supplier               : LGC Virtual Account
          Reader                 : blank
          Opened On              : 01 Jul 2026 (2026-07-01)
        Do not add any records or data to it - it must stay empty to be
        turned into a virtual meter. Save.

STEP 3  Confirm the account was created with no records (Review -> Monthly
        Data should be blank). If it isn't empty, STOP - it can't become a
        virtual meter until it's empty, and I need to know before you try.

STEP 4  Open the new account, Actions -> Account Settings (or wherever the
        virtual meter / relationship setup lives - it's the same screen used
        for the other _CERTS accounts). Set it up as a virtual meter with
        ONE source: the EngieAU account from prompt 1, at 100%. Leave
        Effective From blank unless the screen requires one, in which case
        use 01 Jul 2026 to match Opened On. Save.

STEP 5  Re-open the new account, Review -> Monthly Data. It should now show
        kWh equal to the source account for any month the source already
        has data (there may be none yet, since these accounts were only
        allocated moments ago). Confirm the location's LGCS_<NMI> account is
        unchanged - still there, still holding only its historical data.

Report, per account, in a table: new account number, location, NMI, source
account, Opened On, virtual meter source and %, and whatever Monthly Data
shows.

RULES
- Never touch the LGCS_<NMI> account at any of these locations.
- Never load a record onto the new account before it is set up as a virtual
  meter - it must stay empty until STEP 4 is done.
- Never use a source other than the one EngieAU account named for that card.
- If a name clash is reported (an account already called "<source>_CERTS"
  exists), stop and tell me - do not create a second one.
- If a screen doesn't match what I've described, stop and describe what you see.

============================== THE 7 NEW CERTIFICATE ACCOUNTS ==============================
1. Location: RPQ Spray Seal (171230)
   Source (100% virtual meter feed): 900018189_3051770385
   New account: 900018189_3051770385_CERTS   |  Ref: 3051770385

2. Location: RPQ Spray Seal (171230)
   Source: 900018190_3120014382
   New account: 900018190_3120014382_CERTS   |  Ref: 3120014382

3. Location: RPQ Swanbank (171505)
   Source: 900018191_3120070486
   New account: 900018191_3120070486_CERTS   |  Ref: 3120070486

4. Location: Gympie (142)
   Source: 900018195_3120129028
   New account: 900018195_3120129028_CERTS   |  Ref: 3120129028

5. Location: Asphalt Prod - Bli Bli (408)  (408)
   Source: 900018196_3120103988
   New account: 900018196_3120103988_CERTS   |  Ref: 3120103988

6. Location: Asphalt Prod - Archerfield (406)  (406)
   Source: 900018197_QB05383854
   New account: 900018197_QB05383854_CERTS   |  Ref: QB05383854

7. Location: PPP - Sunshine Coast University Hospital (9078)
   Source: 900018203_3120143385
   New account: 900018203_3120143385_CERTS   |  Ref: 3120143385
==============================================================================================
```

Expected afterwards: the next accounts extract shows each of the 7 EngieAU accounts at its real location
with the old CS Energy meter(s) replaced (30 Jun 2026 or the matched sibling date), and each location
carrying a new `_CERTS` account mirroring the EngieAU kWh from whatever month it starts recording,
alongside its untouched `LGCS_<NMI>` history. `Large Market Certificates/README.md`'s "Section 1" and
coverage counts should both be updated once this runs - two of the fourteen close-offs it lists
(the `5000021_` duplicates at Gympie and Archerfield) are done here, and the register's coverage moves by
however many of these 7 sites are green rows not already counted in the 60/68/78 progression.

## What is deliberately not in these prompts

- No deletions. Closing a superseded account keeps its history at the location it belongs to.
- No touching the `LGCS_<NMI>` historical certificate accounts - they stay as the pre-2026 record.
- No emission-factor changes. The LMC review already tracks the 24-25 / 25-26 / 26-27 factor vintages
  separately; these 7 accounts pick up whatever factor is live once they start recording.
- Card 5's `5000021_3120103988` sibling is deliberately left out of prompt 2's close list because it
  already carries a Replaced On - only re-add it if the survey shows otherwise.
