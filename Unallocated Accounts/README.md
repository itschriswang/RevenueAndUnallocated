# Unallocated Accounts

Accounts sitting against the `Unallocated Accounts` location in Envizi, and the tracker used to
work them back onto real locations.

## Files

| File | What it is |
| --- | --- |
| `Unallocated_Accounts_FY27_Sep26.xlsx` | **The working file.** Current cycle, refreshed on the 03 Sep 2026 accounts extract in `../FY27/`. |
| `Unallocated_Accounts_FY27_Aug26.xlsx` | The Aug-26 cycle, built on the 25 Aug 2026 extracts. Superseded — its 32 electricity accounts are all allocated. |
| `Unallocated_Accounts_FY26_May26.xlsx` | The May 2026 cycle. This is the template the later files follow. |
| `Claude_dispatch_prompts_-_Fuel_Cards_FTC.md` | The two Claude dispatch prompts for working Section 2 in Envizi - a read-only survey of each FTC account's records against the supplier feed at its job, then the move / move-and-close pass. Carries the closing rules and the `_closed` rename convention. |
| `Unallocated Accounts - Proposed Location Links.csv` / `.xlsx` | The flat review that fed the Aug-26 tracker — 136 accounts with match basis and confidence each. Superseded as a working document; kept as the evidence trail behind the tracker's Notes columns. |

## Tracker layout

| Tab | Rows (Sep-26) | Contents |
| --- | --- | --- |
| `1 - Electricity Gas NMI` | 5 | Electricity / natural gas accounts, matched by NMI to an account already allocated to a location. |
| `1a - Closed Sep-26` | 32 | The Aug-26 NMI accounts, now allocated. Where each landed, plus its Aug-26 note. |
| `2 - Fuel Cards FTC` | 91 | Fuel card accounts, matched by job / cost-centre number to a location reference. |
| `3 - BOC Viva` | 13 | BOC and Viva stationary fuel and gas, matched by invoice delivery address. |
| `How to Refresh` | — | The six-step refresh procedure, plus what changed from the May-26 and Aug-26 files. |
| `MDS Extract`, `Location Extract`, `Accounts Extract` | — | Paste targets the working tabs look up against. |
| `BOC_*`, `VIVA_*` | — | Ten supplier invoice files, carried over from the May-26 tracker. |

Formula columns are live and read from the three extract tabs. Yellow columns are manual.
Status (Section 1 col L, Section 2 col M, Section 3 col W) and Section 3's Match Result (col T)
are data validation lists. Section 1 rows shade themselves: green once Status is `Done`, amber
where no meter matches and a manual Envizi search is needed. On `3 - BOC Viva` the row shades
itself from the Match Result in col T (BU Approved / Management Approved / Higher Confidence /
Low Confidence / TBA).

## Refreshing for a new cycle

Follow the `How to Refresh` tab. In short: export the MDS, Accounts Extract and Location Extract
from Envizi; paste each into its tab starting at row 3; fill the helper columns down
(Accounts Extract AJ–AM, Location Extract AC–AD); then review the working tabs for accounts that
have been allocated since (move to the closed tab) and any that have newly appeared (classify into
a section).

## Sep-26 refresh — what the new extract showed

Refreshed on `../FY27/Extract_for_Accounts 03 Sep 26.csv` (59,205 rows). Accounts at
`Unallocated Accounts` fell from 137 to 109.

- **All 32 electricity accounts from the Aug-26 cycle are allocated.** Every one of them was
  actioned on 03 Sep 2026 between 15:58 and 17:36 and now sits at a real location — including
  Synergy `8001014340`, the one row the Aug-26 build left amber for a manual Envizi search. They
  are on `1a - Closed Sep-26`.
- **Five electricity accounts have appeared since and are not yet allocated.** All five resolve to
  exactly one active meter on the same NMI, so each proposal is High confidence:

  | Item Number | Supplier | NMI | Proposed location | Location ref |
  | --- | --- | --- | --- | --- |
  | `900018198_QB06081428` | EngieAU | QB06081428 | MT-Carrara | MT-39510068 |
  | `900018199_3120725958` | EngieAU | 3120725958 | Asphalt Prod - Brendale (423) | 423 |
  | `900018200_QGGG000010` | EngieAU | QGGG000010 | Maryborough | 3011 |
  | `900018201_3053253239` | EngieAU | 3053253239 | Torbanlea - QTMP | L9.J.70700018 |
  | `DEDI01_088_8000326927` | ShellEnergyAU | 8000326927 | Asphalt Prod - Mowbray (360) | 360 |

  The four Engie accounts were created on 02 Sep 2026 and fill the gaps in the 900018192–900018219
  series worked in the Aug-26 cycle. Each sits on an NMI where a CS Energy account is still live —
  the same CS Energy → Engie handover the Aug-26 batch went through, where the CS Energy account
  was closed 30 Jun 2026. So the close-out step in col K applies to `1003080`, `1003078`, `1003077`
  and `1003571` respectively.

  The Shell account was created 26 Aug 2026, the day after the 25 Aug extract the Aug-26 cycle was
  built from, so it fell outside that cycle's 136. It shares NMI `8000326927` with Aug-26 row 1,
  which was allocated to Asphalt Prod - Mowbray (360) on 03 Sep.
- **Sections 2 and 3 are unchanged.** All 91 FTC and all 13 BOC / Viva accounts are still
  unallocated. Checked again on the 05 Sep extract: still 91, no new FTC accounts, no Replaced On on any.

### Section 2 - what the FTC accounts turned out to be

- Every FTC account in Envizi (2,713) is `Event Data`, so none of these can accrue. There is no accrual
  leak from leaving them unallocated or dormant; closing them is hygiene.
- The FTC feed was cut over to direct Viva / WEX / Ampol fuel card accounts at the end of Feb 2026: 902
  FTC accounts were closed on 02 Apr 2026 with Replaced On 28 Feb 2026, the same day these 91 were
  created, and 40 more `<job>_Diesel` accounts were closed on 19 Aug 2026. 90 of the 91 proposed locations
  already hold a supplier feed account, 86 for the same fuel. The risk in allocating is double counting
  from Mar 2026 on, not a missing allocation - so each account's records are read in Envizi before it
  moves. The prompts and the closing rules are in `Claude_dispatch_prompts_-_Fuel_Cards_FTC.md`.
- Two rows cannot be actioned from the extract: `16017960_Diesel` (two locations share Location Ref
  16017960) and `170944_Petrol` (resolves only to a `_CLOSED_REV_` location). Both go to Nathan.

### Template defects fixed this cycle

1. **New Accounts Extract helper col AM, `_NMI_Active_Meter`.** Same as AL but blank for
   `Certificates - Location [kWh]` accounts; Section 1 cols H and J now look up against it.
   Against the Aug-26 extract, col H was returning the LGC certificate account (`LGCS_<NMI>`)
   rather than the electricity meter on 21 of the 32 rows, which pointed STEP 3 at the wrong
   account to close. Col J is unaffected — it resolved to the same location either way.
2. **Envizi's null date is now read as blank.** An empty `Replaced On` comes out of the export as
   the Excel zero-date `30 Dec 1899` (362 rows in this extract). Those were loading as a real date,
   so helper col AK and the Section 3 col U status counted the account as replaced when it is
   active.

## Open items

- **MDS columns read "Not found" / 0 until an MDS export is pasted in.** Section 1 cols E/I,
  Section 2 cols E/L and Section 3 cols O/P/Q/V. No MDS extract for this cycle is in the repo.
  This is a step in the documented refresh, not a fault.
- **No new Location Extract for this cycle.** The `Location Extract` tab still holds the
  26 Aug 2026 data, so re-export before relying on Section 2's job-number lookups.
- **`1006152_Acetylene` has a conflict.** May matched it to Linton Operations on the delivery
  address; the Aug review matched it to Palmerston North Depot on an existing Envizi allocation of
  the same BOC account. May's value is left in cols R/S and the conflict is flagged in Notes —
  needs a decision before loading.
- **Three BOC / Viva rows have no invoice file.** `100017373`, `100480339` and Viva `2489625` are
  not in any carried-over invoice tab, so their `Source Invoice File` cell is blank and cols J–M
  read "Not in file". They need a newer invoice file per `How to Refresh` STEP 6.
