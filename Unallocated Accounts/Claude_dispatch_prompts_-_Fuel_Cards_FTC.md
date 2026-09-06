# Claude dispatch prompts - Fuel Cards (FTC), Sep-26 cycle

What I paste into Claude (browser dispatch) with Envizi (`au001.envizi.com`) open in the active tab, to
work Section `2 - Fuel Cards FTC` of `Unallocated_Accounts_FY27_Sep26.xlsx`. Two prompts, run in order:
a **read-only survey** first, then the **action pass** built on what the survey brings back. Keep Envizi
in front while it works - it only sees the active tab.

## Position as of the 05 Sep 26 accounts extract

- 91 FTC accounts still sit at `Unallocated Accounts`, unchanged from 03 Sep. No new FTC accounts have
  appeared. None has a Replaced On (the 75 that read `30 Dec 1899` are Envizi's null date).
- All 91 were created on 02, 15 or 23 Apr 2026 by the FTC Finance Report load. None has an Opened On.
- 89 of the 91 job numbers resolve to exactly one live location in the 26 Aug location extract. The two
  that do not are listed under *Handle separately* below.
- **Every FTC account is `Event Data`** - all 2,713 of them across Envizi, not just these 91. FTC accounts
  cannot accrue, so unlike the electricity close-offs there is no accrual leaking into the numbers while
  these sit unallocated or dormant. Closing is hygiene, not a reporting fix, and the bar for closing
  stays high.
- **The double-count risk is the supplier feeds.** Direct Viva / WEX / Ampol fuel card accounts were built
  at job level from late Mar 2026 (2,468 accounts, numbered `<job>_<full style name>`), and on 02 Apr 2026
  902 FTC accounts were closed with Replaced On 28 Feb 2026 - the FTC feed was cut over to the supplier
  feeds at the end of Feb 2026. On 19 Aug 2026 a further 40 `<job>_Diesel` FTC accounts were closed at PAS /
  Spotless locations that carry supplier feeds. 90 of our 91 proposed locations already hold a Viva, WEX
  or Ampol account, and 86 hold one for the *same fuel* as the FTC account. If an FTC account here has
  records after Feb 2026, moving it in doubles up that fuel against the supplier feed - the survey checks
  this before anything moves.
- 13 of the 91 sit at a job whose `<job>_Diesel` FTC account was already closed on 19 Aug 26 (list below).
  That is the strongest signal that the FTC feed at that job is finished, but it is a signal, not a
  decision - the survey still reads the records.

## My rules for closing a fuel card account

Fuel cards go quiet and come back. Dormancy on its own is never a reason to close. An account is closed
**only when all three hold**:

1. Its records stop at Feb 2026 or earlier (or it has no records at all) - i.e. it has had nothing since the
   FTC cut-over.
2. The same fuel at the same job is now recorded by a Viva / WEX / Ampol account at the location, with
   records from Mar 2026 on. The supplier feed has taken over, so the FTC account has nowhere to go.
3. Either the job's `<job>_Diesel` FTC sibling was already closed on 19 Aug 26, or the account holds no
   records at all.

Anything that fails one of the three is **moved and left open**. When an account is closed it is also
renamed with the suffix `_closed` (`16012399_Petrol` becomes `16012399_Petrol_closed`), so if a future FTC
file carries that job again the load lands in a fresh `16012399_Petrol` at `Unallocated Accounts` instead of
failing against a closed account. Envizi's older convention for this is `_OLD` (241 FTC accounts from the
2023 tidy-up carry it); I am using `_closed` for this cycle so the two waves stay distinguishable.

Close = set Replaced On on the Edit Account form, the way the electricity close-offs were done. Not the
Actions -> Close Account(s) menu item, and never Delete.

---

## 1 · Survey (read-only)

Nothing changes in this pass. It produces the table the action pass keys off.

```
You're helping me review fuel card accounts in IBM Envizi (au001.envizi.com).
I'm logged in on the Envizi tab. THIS PASS IS READ-ONLY. Do not click Edit,
Save, Move, Close or Delete on anything. If you find yourself on a form that
can save, back out.

Work through the accounts listed at the bottom ONE AT A TIME, in order. For
each one I need two readings.

=== READING A · The unallocated FTC account ===
Top-right search, dropdown "Accounts". Paste the full account number, open it.
Confirm the header shows exactly my account number and "Relates to" reads
Unallocated Accounts. Then Review -> Monthly Data in the account nav (the
Summary chart tooltips don't render). Record:
  - first month with a value, last month with a value
  - number of months with a value, and the total litres
  - whether any month from Mar 2026 onwards has a value (YES / NO)
If the account has no records at all, record "no records".

=== READING B · The proposed location ===
Top-right search, dropdown "Locations". Search the location name I give you.
Several locations share a name - open the one whose Location Ref on the
Summary page matches the ref I give you. If no location matches the ref, or
more than one does, record that and move on. From the location Summary:
Quick links -> Accounts -> "Show All Accounts". Record:
  - every account whose Account Number starts with the same job number, with
    its Supplier and Account Style (there will be VIVA / WEX / AMPOL rows -
    those are expected, do not touch them)
  - for the supplier account whose Account Style matches my FTC account's
    fuel (Petrol -> "Petrol (Gasoline) Transport post 2004", E10 Petrol ->
    "Petrol Gasoline (E10) Transport post 2004", Diesel -> "Diesel Transport
    post 2004", Oil & Lubes -> "Petroleum based oils (lubricants)"), open it
    and read Review -> Monthly Data: first month with a value, and whether it
    has values from Mar 2026 on
  - whether a "<job>_Diesel" FTC row is present with a Replaced On date, and
    the date
  - NAME CLASH CHECK: whether any account at the location - open or closed -
    already carries EXACTLY my account number, or my account number with
    "_closed" on the end. A location cannot hold two accounts with the same
    number, so a clash here blocks the move until the existing one is renamed.
    Record the clashing number and its Replaced On, or "no clash".

=== OUTPUT ===
Give me one row per account in a table with these columns, in this order:
  Account | Location found (Y/N, name, ref) | FTC first month | FTC last month |
  FTC months | FTC litres | FTC has Mar-26+ (Y/N) | Same-fuel supplier acct
  (number) | Supplier first month | Supplier has Mar-26+ (Y/N) | Closed
  _Diesel sibling (number + date, or none) | Name clash (number + Replaced
  On, or none) | Anything odd

Do the first 3 accounts, then stop and show me the table so I can check the
readings before you run the rest. Then continue to the end without stopping.

RULES
- Read-only. No edits of any kind, on any account or location.
- If a screen doesn't match what I've described, stop and describe what you see.
- Match account numbers character for character. "16017764_Petrol" and
  "16017764_E10 Petrol" are different accounts.

================================ THE ACCOUNTS ================================
Format: account -> location name (Ref_No). The Location Ref to confirm on the
location Summary page is the job number, i.e. the digits before the underscore.

  1. 13000907_Oil & Lubes     -> Skilltech Management  (L9.S.13000907)
  2. 14000945_Petrol          -> SA Schools Roma Mitchell Overhead  (L9.S.14000945)   - sibling 14000945_Diesel closed 19 Aug 26
  3. 14001923_E10 Petrol      -> EMOS Transition  (L9.S.14001923)   - sibling 14001923_Diesel closed 19 Aug 26
  4. 16011405_Petrol          -> Townsville North Land  (L9.S.16011405)
  5. 16011491_Petrol          -> Shoalhaven  Range & Training  (L9.S.16011491)
  6. 16011520_Petrol          -> Kapooka Military Land  (L9.S.16011520)
  7. 16012000_Petrol          -> Melbourne City Council East ServDel  (L9.S.16012000)
  8. 16012018_Petrol          -> City of Yarra Streets Serv Del  (L9.S.16012018)
  9. 16012225_Petrol          -> Southbank Grounds Serv Del  (L9.S.16012225)
 10. 16012376_Petrol          -> NSW Sch#1 Ironbark Rdg PS Maint  (L9.S.16012376)
 11. 16012378_Petrol          -> NSW Sch#1 Woongarrah PS Maintenance  (L9.S.16012378)
 12. 16012382_Petrol          -> NSW Sch#1 JohnEdm HS Maintenance  (L9.S.16012382)
 13. 16012385_Petrol          -> NSW Sch#2 Warnervale PS Maintenance  (L9.S.16012385)
 14. 16012387_E10 Petrol      -> NSW Sch#2 RopesCross PS Maintenance  (L9.S.16012387)
 15. 16012391_Petrol          -> NSW Sch#2 Tullimbar PS Maintenance  (L9.S.16012391)
 16. 16012393_Petrol          -> NSW Sch#2 Elderslie PS Maintenance  (L9.S.16012393)
 17. 16012397_Petrol          -> NSW Sch#2 Rouse Hill HS Maintenance  (L9.S.16012397)
 18. 16012399_Petrol          -> NSW Sch#2 Kelso HS Maintenance  (L9.S.16012399)   - sibling 16012399_Diesel closed 19 Aug 26
 19. 16012401_Petrol          -> NSW Sch#2 Ashtonfield PS Maint  (L9.S.16012401)   - sibling 16012401_Diesel closed 19 Aug 26
 20. 16012403_Petrol          -> NSW Sch#2 Halinda SSP Maintenance  (L9.S.16012403)
 21. 16012405_Petrol          -> NSW Sch#2 Kariong Mtns HS Maint  (L9.S.16012405)
 22. 16013532_Petrol          -> VIC Sch Mernda Central P-6 Grounds  (L9.S.16013532)
 23. 16013781_Petrol          -> ANU - Maintenance SD  (L9.S.16013781)
 24. 16016051_Petrol          -> HCMT Train Pakenham East Depot  (L9.S.16016051)
 25. 16017764_E10 Petrol      -> PAS Brisbane EU- Prevent  (L9.S.16017764)
 26. 16017764_Petrol          -> PAS Brisbane EU- Prevent  (L9.S.16017764)
 27. 16017768_Petrol          -> PAS Brisbane Overhead  (L9.S.16017768)
 28. 16017770_Petrol          -> PAS Canungra EU- Prevent  (L9.S.16017770)
 29. 16017771_Petrol          -> PAS Canungra Land  (L9.S.16017771)   - sibling 16017771_Diesel closed 19 Aug 26; no Petrol feed at this location (AMPOL only)
 30. 16017785_E10 Petrol      -> PAS Amberley EU- Prevent  (L9.S.16017785)
 31. 16017785_Petrol          -> PAS Amberley EU- Prevent  (L9.S.16017785)
 32. 16017791_E10 Petrol      -> PAS Darling Downs EU- Prevent  (L9.S.16017791)
 33. 16017791_Petrol          -> PAS Darling Downs EU- Prevent  (L9.S.16017791)
 34. 16017806_E10 Petrol      -> PAS BSC - Cairns EU- Prevent  (L9.S.16017806)
 35. 16017806_Petrol          -> PAS BSC - Cairns EU- Prevent  (L9.S.16017806)
 36. 16017810_E10 Petrol      -> PAS BSC - Cairns Overhead  (L9.S.16017810)
 37. 16017812_Petrol          -> PAS BSC - Towns N EU- Prevent  (L9.S.16017812)
 38. 16017816_E10 Petrol      -> PAS BSC - Towns N Overhead  (L9.S.16017816)
 39. 16017816_Petrol          -> PAS BSC - Towns N Overhead  (L9.S.16017816)
 40. 16017827_E10 Petrol      -> PAS BSC - TWS Sth EU- Prevent  (L9.S.16017827)
 41. 16017827_Petrol          -> PAS BSC - TWS Sth EU- Prevent  (L9.S.16017827)
 42. 16017842_Petrol          -> PAS QLD Management Ov  (L9.S.16017842)
 43. 16017863_Petrol          -> PAS Canberra Trng Bases Overhead  (L9.S.16017863)
 44. 16017882_Petrol          -> PAS Kapooka MA EU- Prevent  (L9.S.16017882)
 45. 16017886_Petrol          -> PAS Kapooka MA Overhead  (L9.S.16017886)
 46. 16017902_E10 Petrol      -> PAS Williamtown EU-Correc  (L9.S.16017902)   - sibling 16017902_Diesel closed 19 Aug 26
 47. 16017902_Oil & Lubes     -> PAS Williamtown EU-Correc  (L9.S.16017902)   - sibling 16017902_Diesel closed 19 Aug 26
 48. 16017902_Petrol          -> PAS Williamtown EU-Correc  (L9.S.16017902)   - sibling 16017902_Diesel closed 19 Aug 26
 49. 16017903_E10 Petrol      -> PAS Williamtown EU-Prevent  (L9.S.16017903)
 50. 16017903_Petrol          -> PAS Williamtown EU-Prevent  (L9.S.16017903)
 51. 16017906_E10 Petrol      -> PAS Williamtown Overhead  (L9.S.16017906)
 52. 16017908_E10 Petrol      -> PAS Singleton EU- Prevent  (L9.S.16017908)
 53. 16017909_Petrol          -> PAS Singleton Land  (L9.S.16017909)   - sibling 16017909_Diesel closed 19 Aug 26
 54. 16017922_E10 Petrol      -> PAS Sydney & Metro Army EU-Prevent  (L9.S.16017922)
 55. 16017922_Petrol          -> PAS Sydney & Metro Army EU-Prevent  (L9.S.16017922)
 56. 16017932_E10 Petrol      -> PAS Fleet Base Estab Overhead  (L9.S.16017932)   - sibling 16017932_Diesel closed 19 Aug 26
 57. 16017932_Petrol          -> PAS Fleet Base Estab Overhead  (L9.S.16017932)   - sibling 16017932_Diesel closed 19 Aug 26
 58. 16017943_E10 Petrol      -> PAS Liverpool Mil Area EU- Prevent  (L9.S.16017943)
 59. 16017943_Petrol          -> PAS Liverpool Mil Area EU- Prevent  (L9.S.16017943)
 60. 16017947_E10 Petrol      -> PAS Liverpool Mil Area Overhead  (L9.S.16017947)   - sibling 16017947_Diesel closed 19 Aug 26
 61. 16017947_Petrol          -> PAS Liverpool Mil Area Overhead  (L9.S.16017947)   - sibling 16017947_Diesel closed 19 Aug 26
 62. 16017951_Diesel          -> PAS RAAF Richmond EU- Correc  (L9.S.16017951)
 63. 16017952_Petrol          -> PAS RAAF Richmond EU- Prevent  (L9.S.16017952)
 64. 16017953_Diesel          -> PAS RAAF Richmond Land  (L9.S.16017953)
 65. 16017962_Diesel          -> PAS Shoalhaven Land  (L9.S.16017962)
 66. 16017962_Petrol          -> PAS Shoalhaven Land  (L9.S.16017962)
 67. 16017964_Diesel          -> PAS Shoalhaven Aero  (L9.S.16017964)
 68. 16017965_Petrol          -> PAS Shoalhaven Overhead  (L9.S.16017965)
 69. 16017976_E10 Petrol      -> PAS NSW Management  (L9.S.16017976)
 70. 16017976_Petrol          -> PAS NSW Management  (L9.S.16017976)
 71. 16017981_Diesel          -> PAS BSC - RCK TARM  (L9.S.16017981)
 72. 16018034_Diesel          -> Special Frces Training Fac-Holswrthy  (L9.S.16018034)
 73. 170353_Oil & Lubes       -> Vic Civil Works  (L9.J.170353)
 74. 170770_Diesel            -> Townsville Spray Services  (L9.J.170770)
 75. 170772_Diesel            -> Mackay Asp Laying  (L9.J.170772)
 76. 170772_Oil & Lubes       -> Mackay Asp Laying  (L9.J.170772)
 77. 170777_Diesel            -> Metro Spray Services  (L9.J.170777)
 78. 170778_Diesel            -> Dalby Spray Services  (L9.J.170778)
 79. 170779_Diesel            -> Sunshine Coast Spray  (L9.J.170779)
 80. 170782_Diesel            -> Grafton Spray Services  (L9.J.170782)
 81. 170803_Oil & Lubes       -> SPO-SI&CS  (L9.J.170803)
 82. 170967_Diesel            -> Thin Surfacing BU Mgt  (L9.J.170967)
 83. 241104_Petrol            -> Utilities Facility Nth Syd  (L9.J.241104)   - no Petrol feed at this location (VIVA/WEX only)
 84. 241301_Petrol            -> RPS - Finance  (L9.J.241301)
 85. 241745_Oil & Lubes       -> GSC Derrimut Support  (L9.J.241745)
 86. 372003_Petrol            -> Plant West - DEP  (L9.J.372003)   - no Petrol feed at this location (AMPOL only)
 87. 37740142_Petrol          -> TLER Replacement  (L9.J.37740142)
 88. 38225143_Diesel          -> Vales Pt Elec Contract 2026  (L9.J.38225143)
 89. 8000050_Petrol           -> SSV General  (L9.J.8000050)   - no Petrol feed at this location (VIVA only)

--- Read these two too, but they get no action in the next pass ---

 90. 16017960_Diesel          -> TWO locations share Location Ref 16017960:
                                 "PAS Shoalhaven EU- Correc" and "PAS Shoalhaven
                                 EU- Prevent" (both L9.S.16017960). Do Reading B
                                 on both and tell me which, if either, carries a
                                 Diesel supplier account.
 91. 170944_Petrol            -> _CLOSED_REV_Binders and Circular Technology
                                 (L9.J.170944, Location Ref BCT). Reading A only.
==============================================================================
```

Expected: most rows read FTC last month = Feb 2026 or earlier with the supplier account picking up from
Mar 2026. Any row where the FTC account has Mar-26+ values *and* the supplier account also does is the
one to look at hard - that is a live double count and neither this prompt nor the next decides it.

---

## 2 · Action pass

Built from the survey table. Before pasting, fill the three lists at the bottom from the survey: **MOVE**
(rows that fail any of my three closing rules), **MOVE + CLOSE** (rows that meet all three), and
**HOLD** (anything odd, plus the two special rows). Give the CLOSE rows the Replaced On date to use: the
last day of the FTC account's last month with a value, or 28 Feb 2026 if it has no records.

```
You're helping me tidy fuel card accounts in IBM Envizi (au001.envizi.com).
I'm logged in on the Envizi tab. Work through the accounts listed at the
bottom ONE AT A TIME, in order. Each account is in exactly one list: MOVE,
MOVE + CLOSE, or HOLD. HOLD accounts get no action at all.

=== STEP 1 · Find the account ===
Top-right search, dropdown "Accounts". Paste the full account number, open it.
Confirm the header shows exactly my account number and "Relates to" reads
Unallocated Accounts. If it already relates to some other location, stop and
tell me - someone has moved it since.

=== STEP 2 · Move it ===
Before moving, the survey confirmed no account at the target location already
carries this account number. If the move dialog or a save error says the
number already exists at the location, do NOT rename anything - stop and
tell me which account it collided with.

Go to the Unallocated Accounts location (it is the "Relates to" link), Quick
links -> Accounts -> "Show All Accounts". Tick the checkbox on the row for MY
account only. Blue "Actions" button -> "Move Account".

That same Actions menu holds "Delete Account(s)", "Close Account(s)" and
"Virtual Account Setup". Do not click any of those, ever. Screenshot the menu
and confirm before clicking.

In the move dialog, find the target location by the name I give you and
confirm its Location Ref matches the ref I give you before selecting it -
several locations share a name, the ref is what disambiguates. Save. Back on
the account Summary, "Relates to" should now read the target location.

=== STEP 3 · Close it (MOVE + CLOSE list only) ===
On the account Summary, blue "Actions" (top right) -> "Edit Account". Not
Capture Data. Set "Replaced On" to the date I give you. Change nothing else
yet. Save. Back on the Summary the left panel should read "Replaced On : <the
date>". If the account already has a Replaced On, stop and show me.

=== STEP 4 · Rename it (MOVE + CLOSE list only, after step 3) ===
Actions -> "Edit Account" again. In "Account Number", append "_closed" to the
existing value - so "16012399_Petrol" becomes "16012399_Petrol_closed".
Nothing else on the form changes. Save. Confirm the header now shows the new
number and Replaced On still reads the date from step 3.

=== STEP 5 · Check it ===
Open the target location's account list. Confirm my account is listed there
exactly once, under its (new) number, with the Replaced On column reading the
date for CLOSE rows and blank for MOVE rows. Confirm the VIVA / WEX / AMPOL
rows at the location are untouched.

Report, per account: the number (old and new if renamed), the location it now
relates to and its ref, Replaced On before and after, and that Opened On is
still blank.

Do the first account, then stop and show me. Once I've confirmed it, run the
rest without stopping.

RULES
- Never delete anything. Never use Close Account(s) or Virtual Account Setup.
- Never edit, move or close a VIVA, WEX, AMPOL or Ampol account, or any account
  I have not named.
- Replaced On and Account Number are the only fields that change, and only on
  MOVE + CLOSE rows. On MOVE rows nothing on the form changes.
- If my exact target account isn't found, or the location ref doesn't match,
  stop and tell me.
- If a screen doesn't match what I've described, stop and describe what you see.

================================== MOVE ==================================
(account -> location name, Location Ref)
<paste from survey>

============================== MOVE + CLOSE ==============================
(account -> location name, Location Ref, Replaced On date to set)
<paste from survey>

================================== HOLD ==================================
16017960_Diesel   - two locations share ref 16017960; waiting on Nathan
170944_Petrol     - location is _CLOSED_REV_; waiting on a successor location
<plus anything the survey flagged as odd>
==========================================================================
```

Expected afterwards: the next accounts extract shows the MOVE rows at their job's location with no
Replaced On, the CLOSE rows there with the date and the `_closed` suffix, and only the HOLD rows still at
`Unallocated Accounts`. Section 2 of the tracker then gets Status / Date Actioned / Notes filled from the
report, and the closed rows carry "closed - renamed _closed" in Notes so the next refresh knows not to
treat a fresh `<job>_<fuel>` at Unallocated as the same account.

---

## Handle separately

**16017960_Diesel.** The location extract has two locations on Location Ref 16017960 - `PAS Shoalhaven
EU- Correc` and `PAS Shoalhaven EU- Prevent`, both Ref_No `L9.S.16017960`. Neither is closed. The tracker's
col H picks whichever comes first, which is not a decision. One of the two refs is presumably wrong on
the location side; flag to Nathan with the survey's Reading B for both and hold the account until one is
corrected.

**170944_Petrol.** Job 170944 resolves only to `_CLOSED_REV_Binders and Circular Technology` (Ref_No
`L9.J.170944`, Location Ref BCT) - a closed revenue location, and the only Medium-confidence row from the
Aug-26 review. No live successor location carries the job. Do not move it into a `_CLOSED_` location; if
the survey shows records, ask Nathan where Binders / Circular Technology fuel is now booked. If the survey
shows no records this one is the likeliest candidate for closing without a move, but it still waits on
the answer.

## The 13 with a Diesel sibling already closed on 19 Aug 26

These are the rows where someone has already judged the job's FTC feed finished. They are the likeliest
MOVE + CLOSE rows, subject to the survey.

```
  14000945_Petrol          at SA Schools Roma Mitchell Overhead  (closed sibling: 14000945_Diesel)
  14001923_E10 Petrol      at EMOS Transition  (closed sibling: 14001923_Diesel)
  16012399_Petrol          at NSW Sch#2 Kelso HS Maintenance  (closed sibling: 16012399_Diesel)
  16012401_Petrol          at NSW Sch#2 Ashtonfield PS Maint  (closed sibling: 16012401_Diesel)
  16017771_Petrol          at PAS Canungra Land  (closed sibling: 16017771_Diesel)
  16017902_E10 Petrol      at PAS Williamtown EU-Correc  (closed sibling: 16017902_Diesel)
  16017902_Oil & Lubes     at PAS Williamtown EU-Correc  (closed sibling: 16017902_Diesel)
  16017902_Petrol          at PAS Williamtown EU-Correc  (closed sibling: 16017902_Diesel)
  16017909_Petrol          at PAS Singleton Land  (closed sibling: 16017909_Diesel)
  16017932_E10 Petrol      at PAS Fleet Base Estab Overhead  (closed sibling: 16017932_Diesel)
  16017932_Petrol          at PAS Fleet Base Estab Overhead  (closed sibling: 16017932_Diesel)
  16017947_E10 Petrol      at PAS Liverpool Mil Area Overhead  (closed sibling: 16017947_Diesel)
  16017947_Petrol          at PAS Liverpool Mil Area Overhead  (closed sibling: 16017947_Diesel)
```

## Name clashes at the target location

A location cannot hold two accounts with the same account number, closed or not, so an existing account
with the same number has to be renamed before the unallocated one can move in. Against the 05 Sep extract
**none of the 91 collides** - the closed FTC accounts already at these locations are all `<job>_Diesel`,
and the unallocated Diesel accounts sit at jobs with no FTC account at all. The survey's Reading B checks
this live anyway, and the action pass stops rather than renaming if Envizi reports a collision.

This is also the second reason for the `_closed` rename. Without it, a future FTC file recreating
`16012399_Petrol` at `Unallocated Accounts` could never be moved onto Kelso HS while the closed
`16012399_Petrol` sits there. The 40 `<job>_Diesel` accounts closed on 19 Aug 26 were not renamed, so if
the FTC feed ever carries Diesel for those jobs again, the new account will collide - worth a follow-up
rename pass on those 40 if that happens.

## What is deliberately not in these prompts

- No deletions. A closed, renamed account keeps its history at the job it belongs to.
- No touching the supplier feed accounts. They are the live record from Mar 2026 and the reason the FTC
  accounts can be closed at all.
- No use of the tracker's MDS columns (E and L) - the MDS Extract tab is still empty this cycle, so the
  survey reads first / last month straight from Envizi instead. When an MDS export is pasted in, cols E
  and L should agree with the survey table.
