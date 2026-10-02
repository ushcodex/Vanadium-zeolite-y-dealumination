# TIER 1 VERIFICATION MEMO: ROUND 9

**Project**: DFT Investigation of the Mechanism of Zeolite Y Deactivation by Vanadium in RFCC Units (Final-Year Thesis, ABU Zaria)
**Date**: 2026-07-29
**Auditor**: Verification desk (Arena)
**Scope of this round**: Band B A4 two-sided fall-in test with pre-declared geometry discriminators; Band B A2 mode-animation evidence; register closeout relabels; document audit of the re-uploaded tracking files; thesis regeneration at Round 9 closeout.
**Documents audited**: `calculation_register.csv` (37 data rows), `tier1_summary.md`, `provenance_map.md` (all re-uploaded 2026-07-29).
**Conversion used throughout**: 1 Eh = 2625.50 kJ/mol.

---

## 1. Executive Verdict

**V-TS2-T1-V05 is ACCEPTED as the first verified transition state of the study, with an explicitly recorded A4 qualification.** Verified Tier 1 barrier for the first framework Al-O cleavage: **+160.70 kJ/mol above canonical V-I1** (rel -224.40 vs the vanadium fragment zero), from a converged saddle carrying exactly one imaginary mode at -78.21 cm-1.

The qualification, stated plainly: the two-sided fall-in test proved connectivity by chemistry (pre-declared geometry discriminators, decisive) but not by well energies. Neither displaced optimization landed within the 5 kJ/mol tolerance of a canonical well (+15.64 vs V-I2 on the positive side; +107.08 vs V-I1 on the negative side), and the negative-side minimum differs from canonical V-I1 in the composition of its coordination shell. On a surface this flat, that outcome is documented behavior, not disqualifying behavior; but it must travel with the number wherever the number appears. It now does: register notes (amendments prescribed in Section 4), memo, and thesis Sections 4.3, 4.6, 4.7, and 4.8.

| Band | Outcome this round | Status |
|---|---|---|
| B (V-I1 to V-I2) | A1 to A3, A5 PASS; A4 chemistry PASS with formal tolerance breach recorded | **ACCEPTED (qualified); barrier +160.70** |
| A (V-PRC to V-I1) | (Round 8) non-elementarity sealed | Closed; no elementary saddle |
| C (V-I2 to V-P) | (Round 8) protocol stop | Bracketed +483.80 to +488.54 |
| D (W-PRC to W-P) | (Round 8) A4 fail, degenerate shuttle | Steam barrier remains apparent CI +65.14 |

---

## 2. Independent Arithmetic Re-Derivation

| # | Quantity | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 | POS minimum vs V-I2 | +15.64 | +15.64 | MATCH |
| 2 | POS minimum vs V-I1 | +58.37 | +58.37 | MATCH |
| 3 | POS minimum rel zero | -326.73 | -326.73 | MATCH |
| 4 | NEG minimum vs V-I1 | +107.08 | +107.08 | MATCH |
| 5 | NEG minimum vs V-I2 | (reported) +64.34 | +64.34 | MATCH |
| 6 | NEG minimum rel zero | -278.02 | -278.03 | CONSISTENT (0.01 truncation remainder) |
| 7 | Saddle vs V-I1 | +160.70 | +160.70 | MATCH |
| 8 | Saddle vs V-I2 | +117.96 | +117.97 | CONSISTENT (truncation remainder, unchanged from Round 8 note) |
| 9 | Saddle below band B CI estimate | (derived) 252.55 kJ/mol | -51.10991869 vs -51.20610884 | Confirms refined saddle sits far below the CI guess |
| 10 | CI to refined overshoot factor | (derived) 2.57 | 413.25 / 160.70 | About 2.6 |

Register Rel Energy column: 37 rows, 0 mismatches beyond rounding.

---

## 3. Acceptance-Chain Adjudication for V-TS2-T1-V05

| Criterion | Evidence | Verdict |
|---|---|---|
| A1 converged refinement | Verbatim paste on the record: "THE OPTIMIZATION HAS CONVERGED"; FINAL SINGLE POINT ENERGY -51.206108843940; end-of-job VIBRATIONAL FREQUENCIES block printed | PASS. The Round 8 primary-evidence caveat is now closed |
| A2 one credible reactive mode | Exactly one imaginary mode at -78.21 cm-1; next modes +17.20, +23.10; the 20 to 50 animation clause is not engaged | PASS |
| A2 animation content | Mode 6 vector: relay proton H27 \|dr\| = 0.315 A; reactive centres Al 0.141, V 0.122, vanadate O23/O25/O26 0.164 to 0.195, framework proton H21 0.168; framework O2 0.075. Content = Al-O2 extension with coupled proton relays: one elementary event. Capping H components up to 0.52 A are flat-surface soft-mode contamination, not a second reacting bond | PASS |
| A3 above both wells | +160.70 vs V-I1, +117.97 vs V-I2 | PASS, wide margin |
| A4 two-sided fall-in | POS: 0-imag minimum, Al 4-coordinate (O1, O3, O4, O24), Al-O2 absent below 2.30 A, framework silanol O3-H21 = 0.9575 A: hydrolysed family. NEG: 0-imag minimum, Al 5-coordinate (O1, O3, O4, O24, O25), vanadate hydroxyl O24-H27 = 0.9557 A retained: chemisorbed family. Two chemically different wells reached in opposite directions, as a connecting first-order saddle must return. Formal tolerance NOT met: +15.64 vs V-I2, +107.08 vs V-I1; NEG-side shell composition (two vanadate contacts, Al-O2 beyond 2.30 A) is off-canonical | **CHEMISTRY PASS, FORMAL FAIL; accepted with recorded qualification** |
| A5 provenance | Rows V-TS2-T1-V05 (saddle), V06 (POS), V07 (NEG); one structure, log, energy per row; provenance map carries all three | PASS |

Rationale for accepting despite the formal tolerance breach: the 5 kJ/mol clause exists to confirm the identity of the two wells. Here the wells stand 42.73 kJ/mol apart and the identity question is answered decisively by geometry: one side hydrolysed, one side chemisorbed, matching the pre-declared discriminators published in the Round 8 execution list before the jobs ran. Landing tens of kJ/mol above the canonical well inside the correct family is the documented signature of this surface (the Round 8 displacements did not reach the exact canonical W-PRC minimum either, stopping +1.35 above it). The alternative reading, that the saddle connects two accidental conformers unrelated to the intended chemistry, is excluded by the discriminators. The residual risk, that a lower saddle connects the canonical wells through subdivided microsteps, is inherent to Tier 1 flatness and is assigned to Tier 2 arbitration; the thesis records this in Section 4.7.

What would not have been acceptable: adopting "+160.70" while letting the register note read "A1-A5 passed" without the breach. Section 4 prescribes the exact note text.

---

## 4. Errata and Prescribed Register Amendments (Apply Verbatim, Keep All Rows)

Errata found in this round's report, with proof:

1. **Mode 6 vector table, atom H27**: printed dy = +2.372150 is a transcription slip. Self-consistency check: with dx = -0.165027, dz = +0.126295 and claimed \|dr\| = 0.315365, dy must be +0.237215 (since (-0.165027)^2 + (0.237215)^2 + (0.126295)^2 = 0.099455 = (0.315365)^2). With dy = +2.372150 the magnitude would be 2.381235, impossible for a normalized mode. Physics unchanged: H27 remains the largest reactive displacement. Correct the walkthrough.
2. **Mid-run sign slip**: the walkthrough once reported the POS displacement as "-15.61 kJ/mol vs V-I2"; the value is +15.64 (the minimum lies above the V-I2 well). Final register note is correct.
3. **Mode 6 norm line** from the parser print was not carried into the report; include it in the walkthrough for completeness.
4. **V-system atom index map**: the discriminator tables reference indices (H14, H19, H24, O24 to O27 etc.) whose V-system ordering differs visibly from the W-system convention. Paste the element-index list of the V-system xyz (30 lines) so every discriminator is auditable.

Prescribed register note amendments:

| Row | Prescribed Notes text |
|---|---|
| V-TS2-T1-V05 | "OptTS continuation 2 CONVERGED (+160.70 kJ/mol vs V-I1); 1 imag (-78.21 cm-1); A1-A3 and A5 passed; A4 chemistry-passed via pre-declared discriminators with recorded tolerance breach (endpoints +15.64 vs V-I2, +107.08 vs V-I1)" |
| V-TS2-T1-V06 | "Mode 6 +0.01nm displacement converged to an I2-family minimum (Al 4-coordinate, Al-O2 broken, framework silanol formed); +15.64 above canonical V-I2, 0 imag; A4 tolerance 5 not met, identity by geometry" |
| V-TS2-T1-V07 | "Mode 6 -0.01nm displacement converged to a chemisorbed-family minimum (Al 5-coordinate via two vanadate contacts, Al-O2 beyond 2.30 A); +107.08 above canonical V-I1, 0 imag; A4 tolerance 5 not met, identity by geometry" |

Also apply the Round 8 relabels that remain pending (W-TS-T1-V04 rejected for connectivity; V-TS1-T1-V02 and V03 superseded by sealed non-elementarity; V-TS3-T1-V05 bracketed closure), if not already applied.

---

## 5. Document Audit

| Check | Result |
|---|---|
| Register data rows | 37 (two added: V-TS2-T1-V06, V07) |
| Duplicate Job IDs | NONE |
| Rel Energy column vs route zeros | 0 mismatches beyond 0.01 truncation |
| No-silent-deletion rule | Honored |
| A2 rule text in tier1_summary.md | Verbatim intact (sub-20 plus 20 to 50 animation clause) |
| Provenance map | V06/V07 rows present, job-level mapping one to one |
| tier1_summary energy tables | Mirror register |
| Archive | Rebuilt, 212.07 MB |

One audit request stands: the register notes for V05, V06, V07 currently overstate ("A1-A5 passed"; "converged to V-I2 well"; "converged to V-I1 well"). Replace with the Section 4 texts.

---

## 6. Thesis Regeneration Executed at This Closeout

Applied under the standing prepared-diffs plan plus this round's qualification language:

- **Table 4.3**: V-TS2 row inserted (rel -224.40; barrier +160.70; marked "verified; A4 qualified"); source line now records which states are verified, which have no elementary saddle, and that W-TS remains the apparent climbing-image estimate.
- **Section 4.4**: reports the degenerate proton-shuttle saddle (+29.29) and its physical interpretation (proton mobility cheap, Al-O cleavage organization is the bottleneck); benchmark judgment deferred to Tier 2.
- **Section 4.5**: the verified +160.70 barrier is integrated into the kinetic argument on Research Question 2.
- **Figure 4.2**: verified V-TS2 level added at -224.40 with footnotes recording its qualified status and the degenerate steam saddle; caption source line updated.
- **Section 4.6**: rewritten to the closeout audit; **Table 4.4** retitled "Saddle-search audit at Tier 1 closeout" with the four final outcomes (sealed non-elementary; accepted with qualification; bracketed; rejected for connectivity with apparent estimate retained).
- **Section 4.7**: flat-surface conformer qualification added.
- **Section 4.8**: chapter summary rewritten to the verified state and the Tier 2 agenda.
- **List of Tables**: Table 4.4 title updated.

Build validation passed: 14 media objects, 17 tables, zero en/em dashes, all new-value probes present. The thesis file is the deliverable `DFT_Investigation_ZeoliteY_Deactivation_Vanadium_RFCC_Nigerian_Refineries_Chapters1-4.docx`.

---

## 7. Round 10 Execution List (for the compute agent)

Constraints unchanged: one job at a time; `cmd /c "D:\ORCA_6.1.0\orca.exe job.inp > job.out"`; `%pal nprocs 1 end`.

1. Apply the Section 4 note amendments and Round 8 relabels verbatim to `calculation_register.csv`; mirror in `tier1_summary.md`; correct the walkthrough H27 dy value and the POS sign slip; add the mode 6 norm line.
2. Paste the V-system element-index map (xyz atom list, 30 lines) and full discriminator tables: Al-O distances to 3.0 A and all O-H pairs below 1.05 A for `V-I1_canonical.xyz`, `V-I2_canonical.xyz`, `V-TS2_ts_pos_disp.xyz`, `V-TS2_ts_neg_disp.xyz`.
3. Rebuild the archive; re-upload the three tracking documents.
4. Optional rigor upgrade (only if the user authorizes the compute time): an IRC descent from optts3_bandB_ci.xyz in both directions at GFN2-xTB to close the A4 formal tolerance question at primary-evidence level. Cost estimate on the present hardware: tens of hours. Not required for acceptance; the qualification is already recorded.

---

## 8. Decision Gate (Still Open)

The user's four decisions remain unanswered and now scope only the final Chapter 4 polish, not the verified result:

1. Submission window (decides whether microstepping bands A or D is worth attempting at all).
2. Band A and D closure: bracketed documented status (current thesis state) vs microstepping campaign.
3. Band C: accept bracket (current thesis state) vs one final continuation.
4. Any objection to the Round 9 thesis regeneration as executed; none was raised before the build.

---

*Verification desk note: the barrier now quoted in the thesis, +160.70 kJ/mol for the first framework Al-O cleavage on the vanadium route, is the first number of this campaign to carry a complete, documented evidentiary chain: converged refinement on the record, one animated imaginary mode on the record, energy order on the record, chemistry-grounded two-sided connectivity on the record, and one qualification on the same record. That is what "verified" means in this thesis.*
