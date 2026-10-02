# TIER1 VERIFICATION MEMO: ROUND 5 (Band Completion Report)

Prepared by the verifying agent, 2026-07-29. Scope: the agent's "Phase B Round 3 Final Harvest and Completion Report" and the three uploaded files: calculation_register.csv, tier1_summary.md, provenance_map.md. All energies re-derived independently from the raw Hartree values with 1 Eh = 2625.50 kJ/mol. Acceptance judged only by the fixed A1-A5 chain, never by appearance or expectation.

---

## 1. Arithmetic audit: PASSED, every number reproduces

| Quantity | Agent claim | Independent recomputation | Verdict |
|---|---|---|---|
| Band A barrier vs V-PRC (-51.19563631 Eh) | +360.82 | (-51.05820550 + 51.19563631) x 2625.50 = +360.82 | MATCH |
| Band A vs V-I1 well (-51.26731716 Eh) | (not quoted) | +549.02 (above, A3 passes) | computed |
| Band A rel E_ref,V (-51.12064005 Eh) | +163.92 | +163.92 | MATCH |
| Band B barrier vs V-I1 | +413.25 | (-51.10991869 + 51.26731716) x 2625.50 = +413.25 | MATCH |
| Band B vs V-I2 well (-51.25104052 Eh) | (not quoted) | +370.52 (above, A3 passes) | computed |
| Band B rel E_ref,V | +28.15 | +28.15 | MATCH |
| Band C barrier vs V-I2 | +518.12 | (-51.05369850 + 51.25104052) x 2625.50 = +518.12 | MATCH |
| Band C vs V-P well (-51.15221675 Eh) | (not quoted) | +258.66 (above, A3 passes) | computed |
| Band C rel E_ref,V | +175.76 | +175.76 | MATCH |
| Band D barrier vs W-PRC (-36.44256091 Eh) | +65.14 | (-36.41774965 + 36.44256091) x 2625.50 = +65.14 | MATCH |
| Band D vs W-P well (-36.44113826 Eh) | (earlier round: +61.40) | +61.41 | MATCH |
| Band D rel E_ref,W (-36.41605681 Eh) | -4.44 | -4.44 | MATCH |

Frequency spectra were transcribed without numerical distortion: Band A (-188.09, -27.29, -14.27), Band B (-267.22 plus eight weaker modes to -28.29), Band C (-256.99, -94.59, -34.28), Band D (-162.72 plus five weaker modes to -22.88). The register rows, the tier1_summary.md tables, and the provenance_map.md entries are numerically identical one-to-one; A5 (one structure, one energy, one log per row) is satisfied. No silent deletions: the three V-TS artifact rows, both superseded minimum rows, and W-TS-T1-V01 (superseded old CI-NEB) are all retained with correct labels.

## 2. Acceptance verdicts under the fixed chain: ALL FOUR CANDIDATES REMAIN UNACCEPTED

| Test | Band A (V-TS1-T1-V02) | Band B (V-TS2-T1-V02) | Band C (V-TS3-T1-V02) | Band D (W-TS-T1-V02) |
|---|---|---|---|---|
| A1 converged OptTS refinement | NOT RUN (queued) | NOT RUN (queued) | NOT RUN (queued) | PENDING (running, unreported) |
| A2 exactly one reactive imaginary mode | FAIL: two genuine modes (-188.09, -27.29); -14.27 below the 20 cm-1 flat threshold | FAIL: nine modes | FAIL: three modes | FAIL: six modes |
| A3 above both wells by > 1 kJ/mol | PASS (+360.82 / +549.02) | PASS (+413.25 / +370.52) | PASS (+518.12 / +258.66) | PASS (+65.14 / +61.41) |
| A4 two-sided fall-in, two different minima | NOT RUN | NOT RUN | NOT RUN | PASS (displacement test from Round 4; endpoints resolved as two distinct wells) |
| A5 row provenance | PASS | PASS | PASS | PASS |

Consequence: these are pre-refinement climbing-image estimates. The multiple imaginary modes are expected at this stage: NEB convergence eliminates forces along the path but does not remove the second-order curvature carried by the interpolation and spring coordinates. That is precisely why A1 (eigenvector-following OptTS with an exact initial Hessian) exists. No candidate may be reported as a barrier anywhere. The thesis quotes only the steam candidate as an apparent, provisional benchmark cross-check and carries all four in the new Table 4.4 labelled as candidates; the vanadium-route candidate energies are not used for any mechanistic statement.

## 3. Document discrepancy found in tier1_summary.md: FIX REQUIRED

The A2 rule in the uploaded tier1_summary.md now reads "sub-30 cm-1 treated as presumptive flat-mode noise". The chain fixed in Round 3 and recorded in my memos states: sub-20 cm-1 is presumptive flat-mode noise. Thresholds do not get relaxed mid-project. Restore the sub-20 formulation, with this completing clause (which was always part of the rule): modes between 20 and 50 cm-1 are decided by recorded mode-animation evidence stating which bonds the displacement vector animates; if it animates a second reacting-bond reorganization, it counts against A2. Note that under EITHER threshold all four current candidates fail A2, so nothing is rescued by the relaxation; the rule still has to be corrected for the record and for the final decisions ahead.

## 4. Ruthless scientific assessment of the candidate scales

Band D (+65.14 kJ/mol) is a chemically sane scale for a water-assisted Al-O cleavage and sits about 11 kJ/mol below the published periodic DFT window of 76 to 125 kJ/mol (Silaghi et al., 2015). The thesis text has been rewritten to say exactly that; the earlier draft's language "falls inside the benchmark range" applied to the superseded first-pass value and is now corrected everywhere (Table 4.3, Figure 4.1, Sections 4.4, 4.5, 4.6, 4.8). The benchmark cross-check is now framed honestly: same order, approximately 11 kJ/mol under the window, same-magnitude agreement expected from a 30-atom semi-empirical cluster, definitive judgment after refinement.

Bands A, B, C (+360.82 to +518.12 kJ/mol) are, in my assessment, upper-scale estimates, not final barriers:

1. The wells involved are 200 to 385 kJ/mol deep; climbing out of a deep chemisorption well along interpolation coordinates on a floppy 30-atom cluster commonly inflates the climbing image. OptTS along the true reaction eigenvector typically lands far below the CI estimate on such systems.
2. Band B connects wells only 42.74 kJ/mol apart. A 413 kJ/mol saddle between two minima that close would imply an extraordinary rearrangement; treat it as a CI-scale artifact candidate until OptTS proves otherwise.
3. If OptTS on band B slides back into a well, or lands implausibly low, run the guard already agreed: Kabsch RMSD atom-order comparison between V-I1_canonical.xyz and V-I2_canonical.xyz. A silent atom permutation between endpoint files forces the band over a steric wall and produces exactly this signature.

Do not speculate further in writing until the refined structures exist.

## 5. Phase B Round 4 execution instructions (final Tier 1 step)

Order: Band D first (benchmark value for Section 4.4), then Band B (the suspicious one), then A, then C. One job at a time.

For each band X in {A, B, C, D}:

1. Copy the template t1_xTb_optts_from_ci.inp (in the orca_templates folder) to the band directory and set its geometry line to the harvested file neb_ts_bandX_NEB-CI_converged.xyz. The template uses ! XTB2 OPTTS FREQ with %geom Calc_Hess true MaxIter 300 end and %pal nprocs 1 end.
2. Launch only via cmd: cmd /c "D:\ORCA_6.1.0\orca.exe optts_bandX_ci.inp > optts_bandX_ci.out" (never PowerShell redirection: it writes UTF-16 and breaks the parsers).
3. On ORCA TERMINATED NORMALLY, read the FREQ block in the same output. Apply A2: exactly one genuine reactive imaginary mode; sub-20 cm-1 modes are presumptive flat noise; 20 to 50 cm-1 modes decided by animation evidence recorded in the register notes.
4. Two-sided fall-in test: displace the refined saddle plus and minus along its single imaginary mode (about 0.01 nm), optimize both displaced structures with ! XTB2 OPT FREQ, and confirm the two directions land in the two intended canonical minima (energy within 5 kJ/mol). For Band D, endpoints must ALSO be confirmed by geometry, because W-PRC and W-P differ by only 3.74 kJ/mol and energy alone cannot distinguish them.
5. Register rules: add a NEW row per refined structure (W-TS-T1-V03 etc.); never overwrite the CI candidate rows; Verified = yes only if A1 through A5 all pass; Status wording must state "Accepted saddle" or the specific failing test.
6. Report back: for each band, the pasted FREQ list, the FINAL SINGLE POINT ENERGY, the fall-in displacement energies for both directions, and the updated register. Paste raw numbers; I re-derive everything.

Time estimate on the laptop: hours per band at nprocs 1, so this is an overnight-per-band schedule. Do not run two ORCA processes concurrently; they share the same core allocation and the memory margin is thin.

## 6. Thesis state after this round

Table 4.3 steam row now reads -4.44 relative, apparent barrier +65.14. Figure 4.1 shows the band D candidate. Section 4.4 frames the benchmark honestly, including the 11 kJ/mol shortfall against the published window. Section 4.6 now contains Table 4.4 with all four candidate estimates, their mode counts, and their candidate status, plus the statement that refinement is the open step. Section 4.8 mirrors the corrected summary. No numbers derived from unaccepted candidates appear anywhere as results.

End of memo.
