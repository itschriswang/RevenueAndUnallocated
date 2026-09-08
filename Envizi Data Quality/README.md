# Envizi Data Quality

The September 2026 data-quality review of the Envizi account set-up, built from the four exports in the
repo root (`Setup_Virtual_Account_Relationships.csv`, `Accounts_Incomplete_Data.csv`,
`Extract_for_Accounts (1).csv`, `All Envizi data.xlsx`). The exports are read, never written.

- **`findings.md`** — start here. Executive summary ranked by materiality, then a section per issue with
  what it is, which accounts, the months, the tonnes where they can be derived, and the action.
- **`Claude_dispatch_prompts_-_NZ_certificates.md`** — the browser-dispatch prompts that fix findings §2 and §7: survey,
  FY27 REC factor, close the Hastings duplicate, read-only check. The 21 genuine relationships are left
  as they are (names and blank dates) and the NZ grid factor is Envizi-managed and left to IBM - the
  reasoning for both is at the top of the file.
  The survey result of 08 Sep 26 is recorded at the top. `../emission_factors_2026_v2_long.csv` (MfE
  guide 2026) is the watch item: when IBM loads it the REC row has to move to match.
- **`csv/`** — the account-level detail each section points to (19 files).
- **`tools/analyse.py`** — regenerates every CSV from the four exports. Run it again when a fresh set is
  dropped in the root; the filenames are in the header of the script.
