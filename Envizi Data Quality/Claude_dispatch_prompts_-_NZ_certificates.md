# Claude dispatch prompts - NZ certificate accounts, Sep-26

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
fix the 22 NZ renewable-certificate virtual accounts found in `findings.md` §2 and §7. Four prompts, run
in order: a **read-only survey** first, then three action passes built on what it brings back. Keep Envizi
in front while it works - it only sees the active tab.

## Position as of the 07 Sep 26 exports

- 22 NZ certificate accounts, all named `Copy of Eco_ICP_<icp>_CERTS`, each a virtual meter of the
  matching `Eco_ICP_<icp>` Ecotricity account at 100%. All 22 relationships have a **blank Effective
  From**, so they credit every month the source has ever held. The 69 Australian ones are dated
  2026-07-01.
- They credited -395.8 tCO2e across Mar-Jun 26 on the factor `RECs NZ - 2026` (-0.101 kg/kWh), about
  -99 t a month. The sources go back to late 2023.
- **None of the 22 has a July or August 2026 row in the export**, while 20 of the sources recorded
  2,008,386 kWh in those two months. The Australian certificate accounts do have July and August rows, so
  it is not the export. My working assumption was the factor: `RECs NZ - 2026` is the only NZ certificate
  factor and looks to have an Effective To of 30 Jun 2026 with nothing after it. The survey (below)
  confirmed it.
- One of the 22 is a duplicate. `Eco_ICP_0000024050WE5E2` (a Waikato ICP) exists as a live account at
  **both** Asphalt Prod - Hamilton (link 6223426, Dec 2023) and Hastings Depot (link 6391000, Nov 2025),
  each with its own `Copy of …_CERTS`. The Hastings pair is accrual-only and double counts ~24 t; it gets
  closed, not dated.

## Survey result - prompt 0 run 08 Sep 26

**A - the factor.** Two rows, both region New Zealand / `Certificates - Location [kWh]` / Custom - Downer:

| Name | Value (kgCO2e/kWh) | Effective From | Effective To |
| --- | --- | --- | --- |
| `RECs NZ` | -0.07289174 | 1 Jul 2024 | 30 Jun 2025 |
| `RECs NZ - 2026` | -0.10111894 | 1 Jul 2025 | 30 Jun 2026 |

No `( Copy of … )` variant. **Nothing covers 1 July 2026 onwards.** The naming convention is the FY end
year, so the successor is `RECs NZ - 2027`, not the `2026-27` I had pencilled in below - prompt 1 now says
so.

**B - the certificate account** (`Copy of Eco_ICP_0000939570TUEC4_CERTS`). Envizi's Monthly Data holds
July 2026 (114,834.3168 kWh) and August 2026 (113,116.21 kWh), both with 31 days, but the Emission Factor
and Emissions columns are blank on both. June carries the -0.1011 factor and -11,356.96 kg. The relationship
reads source `Eco_ICP_0000939570TUEC4`, 100%, rule `100% Renewable Energy Certificates`, Effective From and
Effective To both blank.

**C - the source account.** June 112,312.914, July 114,834.3168, August 113,116.21 kWh, all Automatically
Accrued. Same figures the export shows.

**What that settles.** The relationship is working - it mirrored the kWh into July and August the moment
the source accrued. The gap is the factor alone: with no row covering July, Envizi carries the kWh but
writes no emissions, and the data export drops months with no CO2e, which is why the 22 looked "silent"
from the outside. So it is **prompt 1, then prompt 2, then 3, then 4**, in that order. Prompt 2 still
runs - the blank Effective From is a separate tidy-up, not the cause of the gap.

**The FY27 value.** I no longer need to look this up. The 2026 row is an exact sign-flip of the NZ grid
factor the 22 source accounts sit on - `Electricity used - 2024`, 0.10111894 kgCO2e/kWh, sourced from the
MfE *Measuring emissions guide 2025* - and the FY25 row (-0.07289174) is the same treatment against the
prior guide. The sources are **still on that 2024 grid factor in July and August 2026**, so the value that
makes the certificate credit net each site to zero for FY27 is:

    RECs NZ - 2027   =   -0.10111894 kgCO2e/kWh   (1 Jul 2026 - 30 Jun 2027)

Caution: this only holds while the NZ scope 2 grid factor is 0.10111894. If someone loads the
*Measuring emissions guide 2026* grid figure against the electricity accounts for FY27, the REC row has to
move to match it or the sites will no longer net to zero. I have not seen a 2026-guide row in the export;
if one appears, re-run survey A before changing anything.

## What I am not deciding here

Whether the pre-July credit stays. Ecotricity is a renewable retailer, so the FY24-FY26 credit may be
right in substance even though the relationships are undated. Dating them 2026-07-01 removes it going
forward only; nothing here deletes history. That call sits with whoever signs off the NZ inventory.

## The 22 accounts

| # | Location | Virtual account | Source account | Note |
| --- | --- | --- | --- | --- |
| 1 | Asphalt Prod - Auckland | Copy of Eco_ICP_1001126325LC57C_CERTS | Eco_ICP_1001126325LC57C | |
| 2 | Asphalt Prod - Dunedin | Copy of Eco_ICP_0000102308DEAD2_CERTS | Eco_ICP_0000102308DEAD2 | |
| 3 | Asphalt Prod - Hamilton | Copy of Eco_ICP_0000024050WE5E2_CERTS | Eco_ICP_0000024050WE5E2 | The real one - keep, date it |
| 4 | Asphalt Prod - Invercargill | Copy of Eco_ICP_0000734355NVC9C_CERTS | Eco_ICP_0000734355NVC9C | |
| 5 | Asphalt Prod - Wellington | Copy of Eco_ICP_1001113152UNBF4_CERTS | Eco_ICP_1001113152UNBF4 | |
| 6 | Asphalt Prod - Whangarei | Copy of Eco_ICP_0000519132NR7B9_CERTS | Eco_ICP_0000519132NR7B9 | |
| 7 | Bitumen - Bluff | Copy of Eco_ICP_0000931749NV418_CERTS | Eco_ICP_0000931749NV418 | |
| 8 | Bitumen - Lyttleton | Copy of Eco_ICP_0006863450RN0A4_CERTS | Eco_ICP_0006863450RN0A4 | |
| 9 | Bitumen - Lyttleton | Copy of Eco_ICP_0007202058RN859_CERTS | Eco_ICP_0007202058RN859 | |
| 10 | Bitumen - Mt Maunganui | Copy of Eco_ICP_0000939570TUEC4_CERTS | Eco_ICP_0000939570TUEC4 | Largest, ~-13 t/month |
| 11 | Bitumen - Taranaki | Copy of Eco_ICP_0001510110PCCA2_CERTS | Eco_ICP_0001510110PCCA2 | |
| 12 | BOP Omanawa - 345 Matakokiri Drive, Tauranga | Copy of Eco_ICP_1000610486PC18D_CERTS | Eco_ICP_1000610486PC18D | |
| 13 | Hamilton Depot | Copy of Eco_ICP_0000031643WEA48_CERTS | Eco_ICP_0000031643WEA48 | |
| 14 | Hastings Depot | Copy of Eco_ICP_0000015023HBABD_CERTS | Eco_ICP_0000015023HBABD | |
| 15 | Hastings Depot | Copy of Eco_ICP_0000024050WE5E2_CERTS | Eco_ICP_0000024050WE5E2 | **Duplicate - prompt 3 closes it, do not date it** |
| 16 | Hawkins Construction Recharges | Copy of Eco_ICP_0141534532LCA70_CERTS | Eco_ICP_0141534532LCA70 | Source reads 0 kWh every month |
| 17 | Hawkins Construction Recharges | Copy of Eco_ICP_1002147325UN75B_CERTS | Eco_ICP_1002147325UN75B | Source stopped after May 26 |
| 18 | Nelson Depot | Copy of Eco_ICP_0000052034NT6A8_CERTS | Eco_ICP_0000052034NT6A8 | |
| 19 | Quarry - WOK | Copy of Eco_ICP_0005302992ENB6A_CERTS | Eco_ICP_0005302992ENB6A | |
| 20 | Tauranga Area Manager | Copy of Eco_ICP_1000522230PCA6E_CERTS | Eco_ICP_1000522230PCA6E | |
| 21 | Wellington Depot | Copy of Eco_ICP_1001151226CK008_CERTS | Eco_ICP_1001151226CK008 | |
| 22 | Wiri (130 Kerrs Rd) | Copy of Eco_ICP_1001240514LC3EB_CERTS | Eco_ICP_1001240514LC3EB | |

Row 15 is excluded from prompt 2 and handled in prompt 3. That leaves **21** to date and rename.

---

## 0 · Read-only survey - run first, then stop

```
You're helping me check some renewable-certificate set-up in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. This whole prompt is
READ-ONLY. Do not click Save, Edit, Delete or Actions anywhere. If a page
offers to save changes, choose Cancel and tell me.

Three things to read, in order. After each one, write down exactly what the
screen says. When all three are done, stop and show me the lot.

=== A · The NZ certificate factor ===
Open the emission factors area (Admin / Setup -> Emission Factors, or the
factors library - find it from the left menu, don't guess a URL). Search the
factor list for "RECs NZ". List every row whose name contains "RECs NZ" or
"REC NZ": full name, region, factor value and unit, Effective From, Effective
To. If there is a "( Copy of ... )" variant, list it too. I expect to see one
row named "RECs NZ - 2026"; I want its Effective To date in particular, and
whether any row covers 1 July 2026 onwards.

=== B · One certificate account's monthly data ===
Top-right search, dropdown "Accounts". Paste exactly:
  Copy of Eco_ICP_0000939570TUEC4_CERTS
Open it (it sits at Bitumen - Mt Maunganui). Review -> Monthly Data. Tell me
the LAST month that holds a kWh figure and what it is, and whether any month
after June 2026 shows anything at all (a value, a zero, or no row). Then go to
the account's virtual meter / relationship settings (Actions is fine to OPEN
the menu, but choose only a view - if the only options edit, come back and
tell me) and read the source account, the apportionment %, the rule name and
the Effective From / Effective To on the relationship.

=== C · The source account for the same site ===
Same search, paste exactly:
  Eco_ICP_0000939570TUEC4
Open it, Review -> Monthly Data. Tell me the kWh for June, July and August
2026 and whether each is actual or accrued.

Then STOP. I'll decide from A whether the factor needs a new row, and from B
and C whether the missing July/August is the factor or the relationship.
```

What I do with the answer:

- If A shows `RECs NZ - 2026` ends 30 Jun 2026 and nothing covers July on: **prompt 1**.
- If A shows a factor covering July but B still has no July row: the relationship is the problem -
  skip prompt 1, run prompt 2 and re-check with prompt 4.
- If B shows July data after all: the export was stale; run prompt 2 only.

---

## 1 · Extend the NZ REC factor into FY27

The survey confirmed the factor stops at 30 Jun 2026, so this runs next. The value is -0.10111894, the
same as the 2026 row, because the source accounts are still on the 0.10111894 grid factor for FY27 (see
the survey result above). The name follows the existing convention, `RECs NZ` then `RECs NZ - 2026`, so
the new row is `RECs NZ - 2027`.

```
You're helping me add one emission-factor row in IBM Envizi (au001.envizi.com).
I'm logged in on the Envizi tab. ONE new row, nothing edited or deleted.

WHY
The NZ renewable-certificate factor "RECs NZ - 2026" ends on 30 June 2026 and
there is nothing after it, so the 22 NZ certificate accounts have produced no
July or August 2026 figures. A dated successor row fixes that.

=== STEP 1 · Open the existing row ===
Emission Factors -> search "RECs NZ - 2026" -> open it read-only first. Note
every field: name, region, category / data type it applies to, unit, value,
Effective From, Effective To, source text. Show me before going on.

=== STEP 2 · Create the successor ===
Use the screen's copy / duplicate action if it has one (it keeps the
category and unit mapping); otherwise "Add" and fill each field to match the
2026 row EXCEPT:
  Name:            RECs NZ - 2027
  Effective From:  01 Jul 2026
  Effective To:    30 Jun 2027
  Value:           -0.10111894
Region stays New Zealand. Data type stays Certificates - Location [kWh].
Sign stays NEGATIVE - it is a credit. Unit stays kgCO2e per kWh. If the form
rounds the value when you read it back, tell me how many decimals it kept.

=== STEP 3 · Check the 2026 row is unchanged ===
Re-open "RECs NZ - 2026" and confirm its Effective To still reads 30 Jun 2026
and its value is unchanged. If the copy action altered it, tell me before
touching anything else.

=== STEP 4 · Recalculate if offered ===
If saving prompts a recalculation of dependent accounts, accept it. If it
doesn't, tell me - I'll trigger it from the account side in prompt 4.

=== STEP 5 · Spot-check one account ===
Search Accounts for "Copy of Eco_ICP_0000939570TUEC4_CERTS" (Bitumen - Mt
Maunganui), Review -> Monthly Data. July and August 2026 already show
114,834.3168 and 113,116.21 kWh; what I want to know is whether the Emission
Factor and Emissions columns have now filled in on those two months (I expect
-0.1011 and roughly -11,612 and -11,438 kg). If they are still blank, say so -
the recalculation has not run yet and prompt 4 picks it up.

Report back the three factor rows side by side, then the spot-check.
```

---

## 2 · Date and rename the 21 relationships

The Australian certificate accounts show what right looks like: name `<source>_CERTS`, relationship
Effective From 2026-07-01, no Effective To. This makes the 21 NZ ones match. Row 15 in the table
above (the Hastings copy of the Hamilton ICP) is **not** in this list - prompt 3 closes it.

```
You're helping me tidy 21 virtual-meter relationships in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Work ONE account at a
time, in the order listed, and after the FIRST one stop and show me before
continuing with the rest.

WHAT CHANGES, PER ACCOUNT - two things only
  1. The relationship's Effective From becomes 01 Jul 2026 (2026-07-01).
     Effective To stays blank.
  2. The account's name / number loses the leading "Copy of " so
     "Copy of Eco_ICP_1001126325LC57C_CERTS" becomes
     "Eco_ICP_1001126325LC57C_CERTS".
Nothing else moves. Source account stays the same, apportionment stays 100%,
rule stays "100% Renewable Energy Certificates", location stays, Opened On /
Replaced On untouched, no records deleted.

THIS BATCH HAS A DECOY
"Copy of Eco_ICP_0000024050WE5E2_CERTS" exists at TWO locations. The one at
Asphalt Prod - Hamilton is in this list. The one at Hastings Depot is NOT -
never open it in this prompt. Always confirm "Relates to" shows the location
I give you before you edit anything.

=== PER ACCOUNT ===
STEP 1  Top-right search, dropdown "Accounts", paste the full name including
        "Copy of ". Open it. Confirm the header name matches character for
        character and "Relates to" is the location I give. If two results
        appear, pick by location.
STEP 2  Open the virtual meter / relationship settings for the account
        (Actions -> Account Settings, then the virtual meter or relationship
        tab; if the screen calls it "Source Accounts" or "Apportionment", that
        is it). You should see one source row: the Eco_ICP account, 100%.
        If you see anything other than exactly one source at 100%, stop and
        show me.
STEP 3  Set that relationship's Effective From to 01 Jul 2026. Use the
        calendar or type it and tab out, then read it back - the field shows
        m/d/yyyy, so it must read 7/1/2026, not 1/7/2026. Leave Effective To
        blank. Save.
STEP 4  Back on the account, Actions -> Edit Account. In the account name /
        number field delete the leading "Copy of " (and the space after it).
        Change nothing else on the form. Save.
STEP 5  Re-open the account and read back: name, location, relationship
        Effective From. Move to the next one.

If a save is refused because the new name already exists, STOP and tell me
which one - do not pick a different name.

=== THE 21, in order (name -> location) ===
Copy of Eco_ICP_1001126325LC57C_CERTS -> Asphalt Prod - Auckland
Copy of Eco_ICP_0000102308DEAD2_CERTS -> Asphalt Prod - Dunedin
Copy of Eco_ICP_0000024050WE5E2_CERTS -> Asphalt Prod - Hamilton   (NOT Hastings)
Copy of Eco_ICP_0000734355NVC9C_CERTS -> Asphalt Prod - Invercargill
Copy of Eco_ICP_1001113152UNBF4_CERTS -> Asphalt Prod - Wellington
Copy of Eco_ICP_0000519132NR7B9_CERTS -> Asphalt Prod - Whangarei
Copy of Eco_ICP_0000931749NV418_CERTS -> Bitumen - Bluff
Copy of Eco_ICP_0006863450RN0A4_CERTS -> Bitumen - Lyttleton
Copy of Eco_ICP_0007202058RN859_CERTS -> Bitumen - Lyttleton
Copy of Eco_ICP_0000939570TUEC4_CERTS -> Bitumen - Mt Maunganui
Copy of Eco_ICP_0001510110PCCA2_CERTS -> Bitumen - Taranaki
Copy of Eco_ICP_1000610486PC18D_CERTS -> BOP Omanawa - 345 Matakokiri Drive, Tauranga
Copy of Eco_ICP_0000031643WEA48_CERTS -> Hamilton Depot
Copy of Eco_ICP_0000015023HBABD_CERTS -> Hastings Depot
Copy of Eco_ICP_0141534532LCA70_CERTS -> Hawkins Construction Recharges
Copy of Eco_ICP_1002147325UN75B_CERTS -> Hawkins Construction Recharges
Copy of Eco_ICP_0000052034NT6A8_CERTS -> Nelson Depot
Copy of Eco_ICP_0005302992ENB6A_CERTS -> Quarry - WOK
Copy of Eco_ICP_1000522230PCA6E_CERTS -> Tauranga Area Manager
Copy of Eco_ICP_1001151226CK008_CERTS -> Wellington Depot
Copy of Eco_ICP_1001240514LC3EB_CERTS -> Wiri (130 Kerrs Rd)

When all 21 are done, give me a table: old name, new name, location,
relationship Effective From as read back.
```

---

## 3 · Close the Hastings copy of the Hamilton ICP

`Eco_ICP_0000024050WE5E2` is a Waikato ICP (the `WE` network code). Its live account belongs at Asphalt
Prod - Hamilton. The copy at Hastings Depot was created in Nov 2025, holds only accruals that alternate
between two fixed values, and has its own certificate account. Both Hastings accounts get closed off.
I close rather than delete so the history stays visible; the records themselves are a separate decision.

```
You're helping me close off two accounts at ONE location in IBM Envizi
(au001.envizi.com). I'm logged in on the Envizi tab. Two accounts, one at a
time, read step first.

WHAT "CLOSE" MEANS HERE
Set Replaced On. Nothing else. Do NOT delete, move or merge, and do NOT touch
Opened On.

THE DECOY IS THE POINT
Both account numbers below ALSO exist at Asphalt Prod - Hamilton. Those are
the real ones and must not be touched. Everything in this prompt happens at
Hastings Depot only. Before any edit, "Relates to" must read Hastings Depot.

=== STEP A · Read, then stop ===
Top-right search, dropdown "Accounts", paste
  Eco_ICP_0000024050WE5E2
Two results should appear. Open the HASTINGS DEPOT one. Review -> Monthly
Data: tell me the first and last months holding data, and whether the rows
are actual or accrued. Left panel: Opened On, Replaced On, Supplier. Then do
the same for
  Copy of Eco_ICP_0000024050WE5E2_CERTS
at Hastings Depot. Show me both and stop. I'll give you the Replaced On date
(I expect 30 Jun 2026, the day before the FY27 contract, but I'll confirm).

=== STEP 1 · The certificate account first ===
Open "Copy of Eco_ICP_0000024050WE5E2_CERTS" at Hastings Depot. Confirm the
location. Actions -> Edit Account -> Replaced On -> the date I gave you ->
read it back in m/d/yyyy -> Save. Re-open and confirm the left panel shows
the Replaced On.

=== STEP 2 · Then the source ===
Open "Eco_ICP_0000024050WE5E2" at Hastings Depot. Same steps, same date.

=== STEP 3 · Confirm Hamilton is untouched ===
Open both accounts at Asphalt Prod - Hamilton and confirm each still reads
"Replaced On : -". Report back.
```

---

## 4 · Read-only check after prompts 1-3

```
Read-only in IBM Envizi (au001.envizi.com), I'm logged in on the tab. No
edits.

1. Search Accounts for "Eco_ICP_0000939570TUEC4_CERTS" (no "Copy of").
   Open it, confirm location Bitumen - Mt Maunganui, then Review -> Monthly
   Data. I want June, July and August 2026: kWh, Emission Factor and
   Emissions for each. June should still read -0.1011 and -11,356.96. July
   and August already held the kWh (114,834.3168 and 113,116.21) before any
   of this; what changed should be the factor and emissions, which were
   blank and should now read -0.1011 and about -11,612 and -11,438 kg on the
   "RECs NZ - 2027" row. If they are still blank, tell me, then open the
   factor and read back its Effective From / To and data type - a mismatch
   there is the likeliest reason.
2. Search Accounts for "Copy of Eco_ICP". Tell me how many results remain and
   list them. I expect exactly one: the Hastings Depot one, now closed.
3. Search Accounts for "Eco_ICP_0000024050WE5E2" and confirm the Hastings
   row shows a Replaced On and the Hamilton row does not.
Show me all three.
```

After prompt 4 passes, the next data export should show the 21 NZ certificate accounts with July and
August rows on `RECs NZ - 2027`, about -203 t across the two months, and no `Copy of` names, and
`findings.md` §2 and §7 can be closed off.
