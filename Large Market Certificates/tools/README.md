# tools

The generators behind everything in the folder above. Run them from anywhere; paths are absolute.

| Script | Reads | Writes |
| --- | --- | --- |
| `build_lmcerts.py` | Site register, Jun–Aug 26 summary, `FY27/Extract_for_Accounts 05 Sep 26.csv`, `FY27/Extract_for_Locations 26 Aug 26.csv` | `Account_Setup_and_Data_Load_-_PM&C_LMCERTSJUL26_Setup.xlsx` |
| `build_guide_data.py` | The workbook above, the Jun–Aug 26 energy export taken after the first Claude in Chrome batches (`Electricity download after the first Claude in Chrome batches.xlsx`, repo root), the accounts extract | `guide_data.json` |
| `build_register_map.py` | The pristine budget summary, the accounts extract, `guide_data.json` | `..._with_Envizi_accounts.xlsx` |
| `build_rts_check.py` | `Electricity Data as of 060926.xlsx` (repo root) | `RTS_Market_Based_Check_Jul26.xlsx` — standalone; recalc after building |
| `guide_template.html` + `guide_data.json` | — | `Virtual Meter Guide/Large_Market_Virtual_Meters.html` (replace `/*__DATA__*/null` with the JSON) |

Order: `build_lmcerts.py` → recalc the workbook (LibreOffice, `recalc.py` from the xlsx skill) →
`build_guide_data.py` → build the page → `build_register_map.py`.

**On a new accounts extract:** drop it in `FY27/`, change the filename and `EXTRACT_DAY` in all three
scripts, and rerun the chain. The page reads "built" from the extract, so accounts created in Envizi
show as done once an extract that contains them goes through.

**On a new energy export:** drop it in the repo root, change `EXPORT` and `verify_date` in
`build_guide_data.py`, and rerun from that step. The month chips and the section 1 surplus come from the
export; "built" does not, because an export only lists accounts that hold data — a certificate account
that has been created but not yet linked is invisible in it. Cross-check the two before trusting either:
an account in the extract with no export rows is unlinked, and an account in the export but not the extract
means the extract is stale.

Two rules the scripts encode that are easy to lose:

- A **future `Replaced On` is still open**. Envizi lets you set a close date ahead of time; the account
  keeps accruing until then. `_still_open()` in each script handles it.
- **Meters are not accounts.** The energy export lists NEMMCO interval meters as bare-NMI rows with
  supplier EnergyAction. They are excluded (`Item Type == "Account"`); counting them doubles the site.
