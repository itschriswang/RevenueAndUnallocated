# Envizi Data Quality

The September 2026 data-quality review of the Envizi account set-up, built from the four exports in the
repo root (`Setup_Virtual_Account_Relationships.csv`, `Accounts_Incomplete_Data.csv`,
`Extract_for_Accounts (1).csv`, `All Envizi data.xlsx`). The exports are read, never written.

- **`findings.md`** — start here. Executive summary ranked by materiality, then a section per issue with
  what it is, which accounts, the months, the tonnes where they can be derived, and the action.
- **`csv/`** — the account-level detail each section points to (19 files).
- **`tools/analyse.py`** — regenerates every CSV from the four exports. Run it again when a fresh set is
  dropped in the root; the filenames are in the header of the script.
