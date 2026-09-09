# Monthly-Revenue-Uploads

Monthly revenue actuals and the account setup / data load workbooks built from them, organised by fiscal year (July–June).

## Layout

```
FY26/                        Jul 2025 – Jun 2026
FY27/                        Jul 2026 – Jun 2027          see FY27/README.md
Unallocated Accounts/        Unallocated-account trackers, by MDS cycle
Large Market Certificates/   Renewable certificate virtual accounts for the large market sites
Envizi Data Quality/         Sep-26 review of the four Envizi exports — findings.md and the CSVs behind it
```

Each fiscal year folder contains:

- **`Actual Revenue <Mon> <YY> -unlinked.xlsx`** — the raw monthly actuals extract (one file per month, links removed).
- **`Account_Setup_and_Data_Load_-_PM&C_REV<start>to<end>_Setup.xlsx`** — the setup and data-load workbook covering that month range, built from the monthly actuals. Interim versions from earlier in the year are kept alongside the latest (e.g. FY26 has `...toAPR26`, `...toMAY26`, and the final `...toJUN26`).
- **`Account_Setup_and_Data_Load_-_PM&C_JVREV...`** — the JV revenue exclusion counterpart workbook, where one has been produced.
- **`JV Revenue MDS.xlsx` / `all Revenue MDS.xlsx`** — MDS reference extracts used when building the FY26 workbooks.

## Monthly process

1. Add the new month's `Actual Revenue <Mon> <YY> -unlinked.xlsx` to the fiscal year folder.
2. Extend the year's `Account_Setup_and_Data_Load` workbook to cover the new month (the filename range moves, e.g. `REVJUL26toJUL26` → `REVJUL26toAUG26`).
3. Verify before relying on it: recalculate all formulas (zero errors), and confirm the month's check sheets tie out — every line item OK and the monthly total matching between the revenue sheet and the data load.

## New revenue locations

The setup workbook maps each revenue line to a location named `REV_` & UD1 Name/Sub-LOB. When a
month introduces a Sub-LOB that has no such location, its rows have to ride on a stand-in until the
location is created. Two bulk-upload templates in `FY27/` cover that — `Setup_locations_TEMPLATE.xlsx`
for the locations, then `Setup_Direct_Location_Group_Memberships.xlsx` for the groups, which are
unassigned until it is loaded.

Copy the region and weather-station block from an equivalent location rather than deriving it, and
give each new location both memberships its peers carry: Classification `Operational Control` >
division, and Portfolio `Revenue`. See [`FY27/README.md`](FY27/README.md) for the conventions in
full and for the Jul-26 files built this way.

## Unallocated accounts

Accounts sitting against the `Unallocated Accounts` location in Envizi are worked in a tracker built
on the May-26 template. The workbooks and the full write-up live in **`Unallocated Accounts/`** — see
[`Unallocated Accounts/README.md`](Unallocated%20Accounts/README.md) for the tab layout, the refresh
procedure and the open items on the current cycle.

The current cycle is `Unallocated_Accounts_FY27_Sep26.xlsx`, refreshed on
`FY27/Extract_for_Accounts 03 Sep 26.csv`. The Aug-26 electricity accounts are all allocated; five
new ones have appeared since and are listed with a proposed location each.

## Large market certificate accounts

The FY26–28 renewal agreement sites are matched by NMI to their Envizi accounts, checked for an existing
offset (an `LGCS_` certificate account at the location, or green kWh already recorded on the account's
own green component), and a `Certificates - Location - kWh` virtual account is set up as a virtual meter
of each **large market** electricity account — modelled on the Ecotricity `_CERTS` accounts. Sites whose
Envizi account is styled small market are not under the renewal and are out of scope. The existing
`LGCS_` accounts hold 2025-and-earlier data, so they stay as history and the new accounts sit beside them.
The file to keep in the work folder is **`Large Market Certificates/LGC_Account_Creation_FY27.xlsx`** —
the contract spreadsheet cut down to the 69 accounts to create, the 14 to close off and the 12 rows with
no action, with dropdown status columns to work through. The working guide is
**`Large Market Certificates/Virtual Meter Guide/Large_Market_Virtual_Meters.html`**; the review workbook
and write-up are in **`Large Market Certificates/`** — see
[`Large Market Certificates/README.md`](Large%20Market%20Certificates/README.md).
