# Tier 1 Verification Report, Round 2

This memorandum verifies the executed cleanup against its own logs and files. It lists what stands, what does not, and the exact surviving actions required before Tier 2. Verdicts follow the evidence only.

## 1. What is verified and may stand

1.1 All nine minima (cluster, H3VO4, H2O, V-R, V-PRC, V-I1, V-I2, V-P, W-PRC, W-P) show converged optimizations, normal termination, frequency printouts, and zero imaginary modes. Every relative energy was re-derived from the Hartree values with 1 Eh = 2625.50 kJ/mol and reproduces exactly.

1.2 The canonical V-PRC decision is correct in direction: the supermolecular V-R run settled deeper (-196.90 kJ/mol) than the hand-docked PRC (-194.21 kJ/mol) and carried clean frequencies. Adsorption preference over water is therefore 127.31 kJ/mol. Chemisorption from the canonical PRC is -188.20 kJ/mol; the pathway still closes exactly (-196.90 - 188.20 + 42.74 + 259.46 = -82.90 kJ/mol).

1.3 The V-I2 mode-6 correction was real and well executed: a -118.68 cm-1 proton-orientation mode was displaced and re-optimized to a clean minimum at -51.25104052 Eh, an energy shift of only 0.03 kJ/mol. This catch also proves the earlier register's zero-imaginary claim for V-I2 was false; the audit trail must remain visible (see D3).

1.4 The artifact designation of the three vanadium-route saddle rows is correct, and the steam apparent value (102.97 kJ/mol) is correctly kept separate from verified numbers.

1.5 The corrected cluster metrics (Al-O(H) 1.916 Angstrom; Al-O 1.685 to 1.696; Si-O 1.607 to 1.666) remain inside the expected framework ordering.

## 2. What is not complete

The closing statement that all cleanup tasks are complete is premature. Phase B delivered zero of four verified saddles. The log itself shows: OptTS from the curated seeds failed; the IDPP bands with seeds inserted returned initial seed-image energies of +675, +720, and +1158 kJ/mol above the fragments (the seeds are energetically hot at the semi-empirical level, not merely the bands); three W-TS refinement jobs and four IDPP NEB-TS jobs were still running or unreported when the summary was written; and no IRC verification was run for anything. Phase B is open.

## 3. Deficiencies and required actions

D1. Water reference inconsistency. The register now gives H2O as -5.07054445 Eh (previous record -5.07054448) while the summary still quotes the water-route zero as -36.41605684, which is only consistent with the old value. Re-extract FINAL SINGLE POINT ENERGY from h2o-T1-V01.out once, state one true value, and propagate it (the difference is 0.008 kJ/mol; all two-decimal results are unaffected).

D2. W-TS row contradiction. Status "Apparent, benchmarked" cannot carry Verified = yes. Set Verified = no in the register and in tier1_summary.md until the acceptance chain in D6 is complete.

D3. Silent row replacement. The old V-PRC row (-51.19461241 Eh) and old V-I2 row (-51.25102836 Eh) were silently replaced. Restore both with Status "Superseded (see canonical rows)" and Verified = no. The no-silent-deletion rule exists so the failure history stays auditable; Chapter 4 references it.

D4. Missing geometric proof of the V-R collapse. Run and paste: python verify_tier1.py --dist V-R-T1-V02.xyz --fragA 1-22 --fragB 23-30, and additionally report the shortest heavy-atom contact. A contact around 0.17 to 0.20 nm confirms the collapse; anything far larger would invalidate the canonical PRC choice and must be investigated before Tier 2 reuses the fragment references.

D5. Unreported jobs. Report the outcomes of optts_W-TS-T1-V02 (scan peak, frame 67), optts_W-TS_cineb, and the four IDPP NEB-TS runs: convergence flags, final energies, imaginary-mode counts, and termination status. If any are still running, say so; do not fold them into a completion statement.

D6. No IRC exists yet. For each saddle that passes OptTS with exactly one correct imaginary mode, run t1_xTb_irc.inp, optimize both IRC endpoints, and require fall-in to the claimed minima within about 5 kJ/mol. Only then does Verified become yes.

D7. Saddle hunt, round 2 (supersedes seed insertion). The scan-first pattern that worked for steam is now the primary route for all four steps: clone scan_W-TS-T1-V02.inp per step and scan from the canonical minima, confirming atom indices against the canonical xyz files. Suggested coordinates: V-TS1, approach of the attacking hydroxyl oxygen to aluminium, about 0.26 to 0.17 nm; V-TS2, the Al-O bond being cleaved in V-I1, 0.175 to 0.305 nm; V-TS3, same coordinate in V-I2; W-TS scan already done. OptTS with Calc_Hess from each scan peak, then D6. If a scan shows two maxima, treat them as two elementary steps and refine each separately. The curated seeds are retired as direct starting points but remain canonical connectivity references for editing.

D8. Prohibited interpretation. The log line explaining away 800 to 1700 kJ/mol because the vanadium steps involve massive rearrangements is rejected. Multi-event transformations decompose into elementary saddles of at most a few hundred kJ/mol each; four-digit barriers are always artifacts at this chemistry. This framing must not enter any register note, summary, or thesis text. Chapter 4 Section 4.6 already states the correct position.

D9. Cores metadata. Earlier jobs ran with a three-core allocation; the cleanup jobs fell back to one core after MPI spawning was denied (error 5). The register must record each job's true allocation, which is per-job metadata, not a global value.

D10. Encoding hygiene. The register CSV contains a corrupted character in the V-R note (a mojibake replacement glyph from a non-ASCII dash). Save the CSV as UTF-8 and keep notes ASCII-only. Also record the source .out file for the artifact frequency counts (the register now says five imaginary modes; point to which .out produced that number).

D11. No action needed, for the record: one-core execution at the xTB level is acceptable; runtimes remained seconds to minutes. The MPI denial is a local sandbox restriction and irrelevant to the Tier 2 cloud plan.

## 4. Ordered next actions on the laptop

1. D4 distance proof; D1 single water value; D9, D10 register repairs; D3 row restorations; D2 flag fixes.
2. D5 harvest of the outstanding jobs (finish or kill; report either way).
3. D7 scans for V-TS1, V-TS2, V-TS3; OptTS from each peak; W-TS OptTS result evaluation from the existing scan-peak run.
4. D6 IRC verification for every accepted saddle.
5. Phase C close-out: register, tier1_summary.md, task.md, walkthrough.md, archive zip. Only then is the Tier 2 gate open.

## 5. Consequences already applied to the thesis

Chapter 4 now uses the audited numbers: V-PRC -196.90, chemisorption -188.20, V-I2 -342.36, adsorption preference 127.3 kJ/mol, and the V-I2 mode correction is documented in Section 4.3. Section 4.6 was rewritten to the true status: audit complete; seed-based refinement failed and seeds retired; scan-based hunt in progress; steam scan peak located. Figures 4.1 and 4.2 were regenerated to match.
