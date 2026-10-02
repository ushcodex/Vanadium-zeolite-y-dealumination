# TIER1 VERIFICATION MEMO: ROUND 6 (OptTS Round 4 Results: Structural Deadlock Confirmed)

Prepared by the verifying agent, 2026-07-29. Scope: the agent's "Phase B Round 4 OptTS Refinement and Round 5 Verification Audit Report" (register/tier1_summary/provenance were not re-uploaded this round; audit therefore covers the pasted numbers, with files requested below). All energies re-derived independently from the raw Hartree values with 1 Eh = 2625.50 kJ/mol.

---

## 1. Arithmetic audit: PASSED

| Band | Final OptTS energy (Eh) | Barrier vs reactant, recomputed | Agent claim | Rel vs zero, recomputed | Agent claim | Descent from CI image |
|---|---|---|---|---|---|---|
| A (V-TS1-T1-V03) | -51.08132900 | +300.11 vs V-PRC | +300.12 | +103.21 | +103.21 | -60.71 kJ/mol |
| B (V-TS2-T1-V03) | -51.19071400 | +201.12 vs V-I1 | +201.12 | -183.98 | -183.98 | -212.13 kJ/mol |
| C (V-TS3-T1-V03) | -51.06621100 | +485.27 vs V-I2 | +485.27 | +142.90 | +142.91 | -32.85 kJ/mol |
| D (W-TS-T1-V03) | -36.43115234 | +29.95 vs W-PRC | +29.95 | -39.63 | -39.63 | -35.19 kJ/mol |

All within 0.01 kJ/mol. The new register rows (V03 series, candidates, Verified = no, CI rows untouched) follow the no-overwrite rule correctly. Requested for the next paste: energies to at least 8 decimals, the raw final VIBRATIONAL FREQUENCIES block lines from each optts output, and re-upload of calculation_register.csv, tier1_summary.md, provenance_map.md (the sub-20 restoration in tier1_summary.md was confirmed executed by the agent but I verify documents, not statements).

## 2. Acceptance verdicts: ALL FOUR REMAIN UNACCEPTED, and the reason changed in an important way

- A1 FAILS on all four bands: not one OptTS run converged; all hit MaxIter 300 with the energy still descending at cutoff. A non-converged structure is not a stationary point, so nothing else in the chain can even be tested.
- A2 still fails everywhere (mode counts 3, 9, 3, 6), and, critically, the spectra barely moved during 300 steps of descent. Band B's primary mode went from -267.22 to -267.20 cm-1 while the energy fell 212 kJ/mol. A spectrum that is frozen while the molecule slides is the signature of motion down a long trough on a flat surface, not of approach to a saddle.
- One anomaly to resolve verbatim: Band D's final frequency list is IDENTICAL to the earlier climbing-image audit to two decimals on all six modes, despite 300 geometry steps and a 35.19 kJ/mol energy drop. That coincidence is physically improbable. Paste the raw tail of the final frequency block from optts_bandD_ci.out so I can confirm the list belongs to the final structure and not to an earlier frame.

## 3. Scientific reading of the deadlock (stated plainly)

Three independent saddle-finding methods (endpoint bands, curated-seed refinement, scan-peak refinement, and now eigenvector-following from converged climbing images) have all stalled on the SAME physical object: a flat, multi-mode ridge region of the GFN2-xTB surface of a 30-atom cluster in which several coordinates (proton relays, vanadium motion, Al-O cleavage) reorganize without a single dominant curvature direction. The most probable root cause is methodological, not numeric: the steps PRC to I1, I1 to I2, and I2 to P as defined are not elementary. Each bundles two or more bond events, and between non-elementary endpoints a clean first-order saddle often does not exist; the surface instead holds a shoulder or plateau, which is exactly what every method keeps reporting (the "loop" you noticed is four different methods all describing the same plateau).

This is a known literature situation. The standard resolution is to subdivide each bundled step into elementary microsteps, each with one bond event and its own intermediate, then locate one saddle per microstep. That is more chemistry and more compute; see the decision gate in Section 5.

## 4. Escalation plan: two cheap attempts, then the gate

Step E1 (one continuation per band, one night each): continue each OptTS from its final frame (geometry = optts_bandX_ci.xyz) with MaxIter 300, exact Hessian rebuilt (Calc_Hess true), same keywords, template t1_xTb_optts_continue.inp provided. Watch the mode-count trajectory, not the energy: if the count drops (band B moving from 9 toward 1, band D from 6 toward 1), continue; if spectra freeze again, stop that band immediately and do not burn more nights on it.

Step E2 (one diagnostic run, band D only): repeat the band D OptTS with the peripheral capping hydrogen atoms frozen (%geom Constraints block; freeze only edge-cap H atoms, NEVER the reacting Al-OH proton or the water atoms; obtain cap indices from the canonical cluster file before launching). Template t1_xTb_optts_frozencaps.inp provided with the block skeleton. Interpretation: if the six modes collapse to approximately one, the noise is cap floppiness and we freeze caps in all four bands and finish; if nothing changes, the plateau is real and E1/E2 are done.

## 5. Decision gate (the user decides, with the deadline in hand)

If E1 and E2 fail, Tier 1 does not get cleaner saddles on this surface, and the two honest closures are:

Option 1 (rigorous, expensive): elementary microstepping. Split each V-route step into proton-relay and bond-capture substeps, locate the extra intermediates, run one band per microstep. Realistic cost on this laptop: weeks. Scientific quality: publishable inside an undergraduate thesis, but only if the calendar allows it.

Option 2 (rigorous and fast, recommended if the deadline is near): close Tier 1 with bracketed barriers. The converged bands give upper estimates (360.82 to 518.12 kJ/mol V route; 65.14 steam), the half-descended refinements show the saddles sit lower (300.12, 201.12, 485.27, 29.95 and still descending at cutoff), and the honest thesis statement becomes: single-imaginary-mode saddles could not be located at GFN2-xTB on this 30-atom flexible cluster for the bundled steps; barrier estimates are bracketed between the band climbing images and the refinement trajectories; subdivision into elementary steps and Tier 2 verification are defined as the continuation programme, not executed. The mechanistic conclusions of Chapter 4 (adsorption preference, exothermicity, benchmark-scale steam comparison) do not depend on exact barriers and remain fully supported.

Until the gate is taken, no V03 number enters the thesis; Table 4.4 continues to carry the converged band estimates labelled as candidates.

## 6. Thesis state after this round

Unchanged. No new accepted quantity exists; nothing was added, removed, or re-worded in the thesis this round.

End of memo.
