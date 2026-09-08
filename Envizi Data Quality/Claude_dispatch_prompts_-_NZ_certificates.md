# Claude dispatch prompts - NZ certificate accounts, Sep-26

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
fix the 22 NZ renewable-certificate virtual accounts found in `findings.md` §2 and §7. Four prompts, run
in order: a **read-only survey** first, then the FY27 REC factor row, then the Hastings duplicate, then a
read-only check. Keep Envizi in front while it works - it only sees the active tab.

The 21 genuine relationships are **left as they are** - names and blank dates included. I had a pass
drafted to date them 2026-07-01 and drop the `Copy of ` prefix, copied from the Australian LGC set-up,
and pulled it after the survey: the AU date marks a contract start, but Ecotricity is a renewable retailer
and the credit runs for the whole supply period, which is exactly what a blank Effective From does. Dating
them would have wiped the FY24-FY26 credit. The `Copy of ` names are untidy but change nothing in the
numbers, so they stay too.

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
from the outside. So it is **prompt 1, then 2, then the check in 3**. The blank Effective From on the
relationships is not the cause and is not touched.

**The FY27 value.** The REC row has always been the sign-flip of the NZ grid factor the 22 source
accounts sit on: `RECs NZ` (-0.07289174) mirrored the grid figure in force for FY25 and `RECs NZ - 2026`
(-0.10111894) mirrors `Electricity used - 2024`, in force for FY26 and still applied to July and August
2026. The first run of prompt 1 (08 Sep 26) established that this grid factor is **Envizi-managed, not
custom**: no `Electricity used - 2024` exists under Custom - Downer (the custom NZ grid series stops at
`Electricity - New Zealand - 2014`), while the source account's July emissions divide by its kWh to
0.10111894 exactly. IBM maintains that row from the MfE guide, so it is not mine to close, clone or
override. That settles the value:

    RECs NZ - 2027   =   -0.10111894 kgCO2e/kWh   (1 Jul 2026 - 30 Jun 2027)

i.e. the mirror of what Envizi is actually applying, which is the only thing that nets the sites to zero.

**Watch item - the 2026 guide.** `emission_factors_2026_v2_long.csv` in the repo root (MfE *Measuring
emissions guide 2026*, long form) puts calendar 2025 purchased electricity at **0.078662** kgCO2e/kWh
(CO2 0.076133, CH4 0.002407, N2O 0.000123) and restates 2024 at 0.099360. When IBM loads that guide the
managed factor on the FY27 months will move, and `RECs NZ - 2027` has to be edited to the new mirror on
the same day or the sites stop netting to zero. The test is simple and is in prompt 3: source factor and
certificate factor on the same month must be equal and opposite. If the source ever reads 0.0787 and the
certificate still reads -0.1011, edit the certificate row. The T&D-loss figure in the guide (0.005956) is
not relevant: the NZ electricity accounts carry no scope 3 component (zero across all 1,214 export rows).

**Not a stray.** `RECs NZ` at -0.07289174 does not match any figure in the 2026 guide because that guide
restates earlier years; it is the FY25 mirror of the grid factor as published at the time and stays.

**Account display name.** The certificate account shows as `Copy of Eco_ICP_0000939570TUEC4` in the
account header; `…_CERTS` is on the account number, which is what the search matches. Prompts below say
which they mean.

## The pre-July credit stays

The relationships are undated, so the 21 genuine certificate accounts credit every month their source has
ever held. Ecotricity is a renewable retailer, so that is right in substance, and nothing here changes it.
The one thing worth a line from whoever signs off the NZ inventory is confirmation that the Ecotricity
supply was renewable across the whole period, since that is what the blank date asserts.

## The 22 accounts

| # | Location | Virtual account | Source account | Note |
| --- | --- | --- | --- | --- |
| 1 | Asphalt Prod - Auckland | Copy of Eco_ICP_1001126325LC57C_CERTS | Eco_ICP_1001126325LC57C | |
| 2 | Asphalt Prod - Dunedin | Copy of Eco_ICP_0000102308DEAD2_CERTS | Eco_ICP_0000102308DEAD2 | |
| 3 | Asphalt Prod - Hamilton | Copy of Eco_ICP_0000024050WE5E2_CERTS | Eco_ICP_0000024050WE5E2 | The real one - keep |
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
| 15 | Hastings Depot | Copy of Eco_ICP_0000024050WE5E2_CERTS | Eco_ICP_0000024050WE5E2 | **Duplicate - prompt 2 closes it** |
| 16 | Hawkins Construction Recharges | Copy of Eco_ICP_0141534532LCA70_CERTS | Eco_ICP_0141534532LCA70 | Source reads 0 kWh every month |
| 17 | Hawkins Construction Recharges | Copy of Eco_ICP_1002147325UN75B_CERTS | Eco_ICP_1002147325UN75B | Source stopped after May 26 |
| 18 | Nelson Depot | Copy of Eco_ICP_0000052034NT6A8_CERTS | Eco_ICP_0000052034NT6A8 | |
| 19 | Quarry - WOK | Copy of Eco_ICP_0005302992ENB6A_CERTS | Eco_ICP_0005302992ENB6A | |
| 20 | Tauranga Area Manager | Copy of Eco_ICP_1000522230PCA6E_CERTS | Eco_ICP_1000522230PCA6E | |
| 21 | Wellington Depot | Copy of Eco_ICP_1001151226CK008_CERTS | Eco_ICP_1001151226CK008 | |
| 22 | Wiri (130 Kerrs Rd) | Copy of Eco_ICP_1001240514LC3EB_CERTS | Eco_ICP_1001240514LC3EB | |

Row 15 is the only one of the 22 that is edited, in prompt 2. The other 21 are not opened.

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
  skip prompt 1 and look at the relationship before anything else.
- If B shows July data after all: the export was stale; nothing to fix.

---

## 1 · Add the FY27 NZ REC factor

One row. The grid factor it mirrors is Envizi-managed and is left alone (see the survey result); the
certificate row is Custom - Downer and is mine to add. Its first run on 08 Sep 26 stopped at the read step
on purpose, having found the grid factor was not custom - this is the rewritten version.

```
You're helping me add one emission-factor row in IBM Envizi (au001.envizi.com).
I'm logged in on the Envizi tab. ONE new row, nothing edited or deleted.

WHY
The NZ certificate credit "RECs NZ - 2026" ends on 30 June 2026 and nothing
covers July 2026 on, so the 22 NZ certificate accounts hold July and August
kWh with no emissions. The grid factor the credit mirrors is Envizi-managed
and is NOT to be touched; the successor credit row takes the same value the
grid factor is applying today, 0.10111894, with the sign flipped.

=== STEP 1 · Open the existing row ===
Emission Factors -> filter name "RECs" -> open "RECs NZ - 2026" read-only.
Confirm: region New Zealand, data type Certificates - Location [kWh],
Custom - Downer, value -0.10111894, Effective From 1 Jul 2025, Effective To
30 Jun 2026. Show me, then go on.

=== STEP 2 · Create the successor ===
Use the screen's copy / duplicate action if it has one; otherwise Add and
match every field of the 2026 row EXCEPT:
  Name:            RECs NZ - 2027
  Effective From:  01 Jul 2026
  Effective To:    30 Jun 2027
  Value:           -0.10111894
Region New Zealand, data type Certificates - Location [kWh], Custom - Downer,
unit kgCO2e per kWh. Sign NEGATIVE - it is a credit. Per-gas and source can
stay blank as they are on the 2026 row. Read the value back before saving -
tell me how many decimals the form kept. Save.

=== STEP 3 · Check the 2026 row is unchanged ===
Re-open "RECs NZ - 2026": value still -0.10111894, Effective To still
30 Jun 2026. If the copy action altered it, tell me before touching
anything else.

=== STEP 4 · Apply Factors ===
Saving does NOT recalculate anything. Back on the Custom Factors screen
there is an "Apply Factors" button that queues a job to push factor changes
through the accounts. Click it once. If it asks for a scope or date range,
choose everything / all dates - it must reach July and August 2026. Tell me
what it said (queued, running, done, job number). Do not click it twice.

=== STEP 5 · Spot-check one site (after the job has run) ===
Top-right search, dropdown "Accounts", paste
  Copy of Eco_ICP_0000939570TUEC4_CERTS
(the header may show the name without _CERTS - that is the same account;
confirm "Relates to" is Bitumen - Mt Maunganui). Review -> Monthly Data,
July and August 2026: the kWh were already there (114,834.3168 and
113,116.21); the Emission Factor should now read -0.1011 and Emissions
about -11,612 and -11,438 kg. June unchanged at -11,356.96. If the two
months are still blank, say so - the recalculation has not run yet and
prompt 3 picks it up.

Report back the three RECs NZ rows side by side, then the spot-check.
```

**Run on 08 Sep 26.** `RECs NZ - 2027` created by copy, 8 decimals kept, sign intact, 2026 row untouched.
Saving triggered nothing and the spot-check still showed July and August blank - that is how I learned
about Apply Factors, which was outside the brief as first written and is now Step 4. The 2027 row exists;
the recalculation is the outstanding piece.

---

## 2 · Close the Hastings copy of the Hamilton ICP

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

## 3 · Read-only check after prompts 1 and 2

```
Read-only in IBM Envizi (au001.envizi.com), I'm logged in on the tab. No
edits.

1. Search Accounts for "Copy of Eco_ICP_0000939570TUEC4_CERTS". Open it,
   confirm location Bitumen - Mt Maunganui, then Review -> Monthly
   Data (the header may show the name without _CERTS; "Relates to" must
   be Bitumen - Mt Maunganui). I want June, July and August 2026: kWh,
   Emission Factor and Emissions for each. June should still read -0.1011
   and -11,356.96. July
   and August already held the kWh (114,834.3168 and 113,116.21) before any
   of this; what changed should be the factor and emissions, which were
   blank and should now read -0.1011 and about -11,612 and -11,438 kg on
   the "RECs NZ - 2027" row. Then the source "Eco_ICP_0000939570TUEC4",
   same months: factor 0.1011, emissions 11,611.93 and 11,438.2 (positive),
   so the pair nets to zero. The factors MUST be equal and opposite - if
   the source has moved to a different figure (0.0787 would mean IBM has
   loaded the 2026 guide) and the certificate has not, tell me that first.
   If the certificate cells are still blank, tell
   me, then open the factor and read back its Effective From / To and data
   type - a mismatch there is the likeliest reason.
2. Search Accounts for "Eco_ICP_0000024050WE5E2". Two results. Confirm the
   Hastings Depot row shows a Replaced On and the Hamilton row does not.
   Then the same for "Copy of Eco_ICP_0000024050WE5E2_CERTS".
3. Search Accounts for "Copy of Eco_ICP" and tell me how many results there
   are. I expect 22, unchanged - none of them was renamed.
Show me all three.
```

After prompt 3 passes, the next data export should show the 21 NZ certificate accounts with July and
August rows on `RECs NZ - 2027`, about -203 t across the two months (2,008,386 kWh at 0.10111894), the
sources still on the managed `Electricity used - 2024` for the same months, and the Hastings pair closed.
Each later export gets the same equal-and-opposite check on the factors. Then
`findings.md` §2 and §7 can be closed off.
