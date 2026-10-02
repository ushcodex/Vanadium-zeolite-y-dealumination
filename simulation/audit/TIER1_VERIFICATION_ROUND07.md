# TIER1 VERIFICATION MEMO: ROUND 7 (E1/E2 Executed; Band D at the Gate)

Prepared by the verifying agent, 2026-07-29. Scope: the agent's "Round 6 Audit and Step E1/E2 Execution Report" plus the three uploaded files (calculation_register.csv, tier1_summary.md, provenance_map.md). All energies re-derived independently from raw Hartree values with 1 Eh = 2625.50 kJ/mol.

---

## 1. Arithmetic audit: PASSED in full

| Claim | Agent value | Recomputed | Verdict |
|---|---|---|---|
| W-TS-T1-V04 barrier vs W-PRC | +29.29 | +29.29 | MATCH |
| W-TS-T1-V04 vs W-P (A3 check) | +25.56 | +25.56 | MATCH |
| W-TS-T1-V04 rel zero | -40.29 | -40.29 | MATCH |
| V-TS2-T1-V04 barrier vs V-I1 | +161.09 | +161.09 | MATCH |
| V-TS2-T1-V04 rel zero | -224.01 | -224.01 | MATCH |
| V-TS1-T1-V04 vs V-PRC | +300.10 | +300.10 | MATCH |
| V-TS3-T1-V04 vs V-I2 | +483.80 | +483.80 | MATCH |
| W-TS-T1-V05 (frozencaps) vs W-PRC | +62.31 | +62.31 | MATCH |

Register: 29 rows, no duplicate IDs, no overwrites, no silent deletions, honest statuses ("Candidate (pending A4)", "Slid to minimum", "Diagnostic run"), Verified = no throughout the TS family, and the A2 sub-20 formulation is still intact in tier1_summary.md. Provenance map one-to-one. Document hygiene: clean pass.

## 2. The frequency-block anomaly: RESOLVED, with one record correction

The agent's explanation is correct and I confirm it: with Calc_Hess true, ORCA computes and prints the Hessian frequencies at step 0 only; on a MaxIter stop there is no end-of-job frequency block, while on convergence the final FREQ block is printed. Consequence for the record, stated plainly: the imaginary-mode counts quoted in Round 6 for the V03 rows (3, 9, 3, 6) were counts on the CLIMBING-IMAGE structures, not on the V03 geometries. My Round 6 statement that "spectra are frozen during descent" was therefore based on frequency blocks belonging to the wrong structures and is hereby corrected: the true frame-300 Hessians (revealed at step 0 of the continuation runs) show the descent changed the spectra substantially (Band B: 9 to 1; Band A: to 0; Band C: to 3 low modes; Band D: 6 to 3, then to 1 on convergence). The register notes now carry "Step 0 freqs reported" on V03 rows, which is the right way to keep the audit honest. This correction changes no verdict from Round 6; it changes the diagnosis: the OptTS pass 1 was nearer the goal than it looked.

## 3. Acceptance verdicts after E1

**Band D (W-TS-T1-V04): A1 PASS, A2 PASS, A3 PASS. A4 PENDING. Do not celebrate yet.**
- A1: converged with normal termination (195 iterations).
- A2: exactly one imaginary mode at -226.10 cm-1, cleanly separated from the next mode at +4.89 cm-1; magnitude chemically credible for Al-O cleavage with proton relay. The animation sub-clause still requires evidence: paste the displacement vector of mode 6 from the NORMAL MODES section (or a rendered frame) so we can see that the moving coordinate breaks the framework Al-O bond and shuttles the proton through the water molecule. If mode 6 animates something else, A2 fails on the sub-clause.
- A3: above both wells (+29.29 vs W-PRC, +25.56 vs W-P), margins far above the 1 kJ/mol floor.
- A4 (the gatekeeper, and it must be done with geometry checks because the wells are only 3.74 kJ/mol apart): displace the converged structure plus and minus about 0.01 nm along mode 6, optimize both with ! XTB2 OPT FREQ, and report for each direction: final energy (must be within 5 kJ/mol of the intended canonical well: W-PRC at -36.44256091 or W-P at -36.44113826) AND a geometry discriminator that can tell the two wells apart (intact versus broken framework Al-O distance, and which oxygen hosts the migrated proton: water O22 versus the framework hydroxyl O). Energy alone cannot distinguish these wells; do not report A4 without the geometry line.
- Expectation discipline: the two displaced structures may both slide downward W-P-side on this flat surface; if so, report it as it falls and we interpret.

**Band B (V-TS2-T1-V04): ON TRAJECTORY, one or two continuations left.**
Mode count collapsed 9 to 1 at the frame-300 Hessian; the continuation then descended another 40 kJ/mol and hit MaxIter again, unconverged, at +161.09 above V-I1. Run ONE further continuation from optts2_bandB_ci.xyz (same template). Watch the end-of-job behavior: on convergence the printed FREQ must show exactly one imaginary mode. If it converges with one mode, it enters the A2 sub-clause + A3 + A4 sequence identically to Band D. If it hits MaxIter again, run ONE more; after two further continuations without convergence, stop and report as bracketed.

**Band A (V-TS1-T1-V04): SLID OFF THE RIDGE; evidence of non-elementarity.**
The continuation converged in 101 iterations to a genuine 0-imaginary-mode minimum only 0.01 kJ/mol below the pass-1 end point: a shallow basin sitting +300 kJ/mol above V-PRC and +488 above V-I1. Pass 1 had already left the saddle ridge. No first-order saddle exists near the band A climbing-image region at this level, which is the expected signature of a step that bundles two bond events (capture plus proton relay). Before spending anything more, run the cheap diagnostic: displace the ORIGINAL band A CI image (neb_ts_bandA_NEB-CI_converged.xyz) plus and minus about 0.01 nm along its primary mode (-188.09 cm-1), optimize both, and report both energies and geometries. If both directions fall into the same well, the diagnosis is sealed and Band A goes to the microstepping gate, not to more refinement attempts.

**Band C (V-TS3-T1-V04): marginal progress, one more continuation.**
Three low modes remain at frame 300 (-60.64, -38.37, -18.11; the last is sub-20 noise), energy nearly stationary. Run ONE more continuation from optts2_bandC_ci.xyz. If it does not converge, stop and report as bracketed.

## 4. E2 diagnostic interpretation, for the record

Frozen caps made it worse, not better (5 imaginary modes at a higher energy, -36.41883009). Conclusion: the multi-mode noise was never capping-hydrogen floppiness; full relaxation was the right path. The frozencaps row stands in the register as a documented diagnostic; no constraint scheme is to be reused on any band.

## 5. Consequence for the thesis (no edits yet, and a hard warning to internalize now)

If Band D passes A4, the Tier 1 steam barrier becomes the refined 29.29 kJ/mol, not 65.14, and Section 4.4 must be rewritten AGAIN, this time against us on the surface: the refined GFN2-xTB value sits far below the Silaghi periodic DFT window of 76 to 125 kJ/mol. The honest framing, prepared in advance: at the semi-empirical level on a 30-atom cluster, proton-transfer barriers carry documented errors of tens of kJ/mol; Tier 1 therefore supports the qualitative statement that steam hydrolysis faces a moderate barrier, while the quantitative benchmark comparison is deferred to the Tier 2 hybrid DFT refinement defined in Chapter Three. The thesis's core mechanistic claims (adsorption preference of 127.3 kJ/mol, exothermic vanadium pathway) do not move at all. If A4 fails, the thesis stays exactly as it is, with 65.14 as the apparent band estimate. Under no circumstance is 29.29 to appear anywhere in the thesis before A4 closes.

## 6. Execution list (one job at a time, cmd launcher only)

1. Band D: two displaced OPT FREQ runs (plus/minus 0.01 nm along mode 6 of optts2_bandD_ci), with energies AND geometry discriminators, plus the mode-6 displacement vector for A2.
2. Band A: plus/minus displacement diagnostic from the band A CI image along -188.09 cm-1, both optimized, energies and well assignments reported.
3. Band B: third OptTS (continuation 2) from optts2_bandB_ci.xyz.
4. Band C: second OptTS continuation from optts2_bandC_ci.xyz.
Register: new rows only (V06 onward as needed), Notes must state plainly which structure each frequency count belongs to (step-0 Hessian of the starting frame versus end-of-job FREQ of the converged structure).

Time: items 1 and 2 are small jobs (hours total); items 3 and 4 are overnight each. Upload register, tier1_summary.md, provenance_map.md with each report paste.

End of memo.
