# Tier 1 Verification Report, Round 3

This memorandum verifies the D1 to D11 execution against its own logs and files. The headline finding: the cleanup work was genuinely very good on references, minima, and record keeping, but every saddle candidate produced in this round fails the connection tests, and one acceptance rule was misread in a way that certified them anyway. No barrier of the four is verified as of this writing.

## 1. Closed items (verified, no further action)

- D4 geometric proof of the V-R collapse: accepted. Shortest intermolecular contact Al(1) to O(25) = 0.1925 nm is inside the 0.17 to 0.20 nm window, confirming the supermolecular run fell into the PRC basin. Canonical PRC stands at -196.90 kJ/mol.
- D1 single water value: accepted. H2O = -5.070544447500 Eh exactly, water-route zero = -36.41605681 Eh, now consistent between register and summary.
- D5 harvest table: accepted. All nine outstanding jobs reported with convergence, energies, and imaginary-mode counts. The table also proved, with extreme clarity, why the curated seeds are retired: direct refinement from them returned 22 to 36 imaginary modes with values near -19000 to -33000 cm-1, the signature of overlapping atoms in hand-built geometry.
- D3 row restorations, D10 encoding, artifact source files: accepted. The audit trail is now honest.
- The scan-first execution itself was correct and valuable: profiles with physical (single and double digit kJ/mol) maxima replaced the four-digit artifact maxima. The displacement and re-optimization machinery built for the interval test also demonstrably works, since it reproduces well energies to 0.02 kJ/mol.

## 2. The one acceptance rule that was misread

My protocol said: the two re-optimized endpoint structures must reproduce the energies of the claimed reactant and product minima within about 5 kJ/mol. This means ONE endpoint must land on the reactant AND THE OTHER on the product. It does not mean each endpoint must be near some known minimum. A transition state connects two different basins; that is the definition being tested.

The logs show, for every candidate, BOTH endpoints falling to the SAME minimum:

| Candidate | Forward endpoint | Backward endpoint | Meaning |
|---|---|---|---|
| V-TS2 (E = -51.26730862) | V-I1 at +0.02 | V-I1 at +0.02 | both directions return to the reactant well |
| V-TS3 (E = -51.25108503) | V-I2 at -0.12 | V-I2 at -0.11 | both directions return to the reactant well |
| W-TS  (E = -36.44253925) | W-PRC at +0.06 | W-PRC at +0.05 | both directions return to the reactant well |

All three therefore FAIL the fall-in test. They are numerical shoulders on flat regions near deep minima, not connecting saddles.

Two independent sanity tests reinforce this:

- Energy order test. A saddle must sit above BOTH adjacent wells. V-TS2 candidate: +0.022 kJ/mol above V-I1 (noise level). V-TS3 candidate: -0.117 kJ/mol BELOW V-I2, which is impossible for a transition state. W-TS candidate: +0.057 kJ/mol above W-PRC (noise).
- Mode magnitude test. The imaginary modes are -70.64, -6.36, and -20.05/-12.73 cm-1. Genuine reaction coordinates for proton transfer or Al-O cleavage at saddles are typically several hundred cm-1 imaginary. Sub-20 cm-1 values are flat-mode noise (capping hydrogen torsions and the like).

Conclusion: no new barrier rows may be added to the register from these candidates, and the +6.87 and +14.59 kJ/mol figures quoted in the summary are scan-profile readouts relative to the first scan point, NOT barriers. They must not appear as barriers in any document.

## 3. The W-TS register row must be corrected (provenance error)

The W-TS row quotes energy -36.40334386 Eh (+102.96 kJ/mol), which is the OLD climbing-image NEB value, but justifies Verified = yes with a fall-in test that was run on a DIFFERENT structure: the endpoint of optts_W-TS-T1-V02, which sits only 0.057 kJ/mol above W-PRC and carries two imaginary modes. A verification test belongs to the exact structure at the exact energy it was performed on. In addition, that test failed anyway (both directions to W-PRC), and the row's Source Log field points to optts_W-TS_cineb.out, a job that never converged and had nine imaginary modes.

Required repair: Status = "Apparent", Verified = no, Source Log = the original neb_W-TS-T1-V01 job, Notes keep the observed agreement with the Silaghi range as a method-level cross-check only. The tier1_summary.md step-barrier claim must be edited the same way.

## 4. Open items

- V-TS1: the OptTS refinement from scan peak frame 56 was launched but its outcome was never reported, and no interval test exists. Harvest it and report.
- D9 cores metadata: restored rows record 1 core for jobs that were run earlier with a three-core allocation; record each job's true value from its own .out header.
- Register ID drift: the restored old V-I2 row is now labelled V-I2-T1-V03 while the round-one register labelled it V-I2-T1-V01. Produce a one-page provenance map: job input file -> output file -> xyz -> register row, so every energy traces to exactly one computation.
- The tier1_summary.md and walkthrough.md statements claiming V-TS2 +6.87 and V-TS3 +14.59 as results, and claiming IRC verification passes, must be rewritten per Sections 2 and 3.

## 5. The corrected saddle acceptance chain (all five must hold)

A1. OptTS converged with normal termination.
A2. Exactly one imaginary mode, of chemically credible magnitude for the motion (as a working floor at this level, treat sub-20 cm-1 as presumptive flat-mode noise unless a mode animation proves it is the reacting coordinate), and the animation shows the intended bond reorganization.
A3. E(TS) above BOTH adjacent wells; given near-noise shoulders exist, require at least 1 kJ/mol above the higher of the two wells.
A4. Two-sided interval test: displacements of plus and minus along the imaginary mode, each re-optimized, must terminate in TWO DIFFERENT minima, and each must reproduce the claimed reactant and product energies within 5 kJ/mol. Both-directions-to-the-same-minimum is an automatic fail.
A5. Row provenance: Energy, Source Log, and verification test all refer to the same final structure and job.

## 6. The relocation strategy (Phase B, round 3)

The scans taught us where the flat regions are; now the path itself must be resolved. Run climbing-image nudged elastic band with full saddle refinement (keyword NEB-TS) between CONSECUTIVE canonical minima, one elementary step per band, with IDPP interpolation:

- Band A: V-PRC -> V-I1 (chemisorption plus proton relay).
- Band B: V-I1  -> V-I2 (first Al-O cleavage, +42.74 kJ/mol endothermic).
- Band C: V-I2  -> V-P  (+259.46 kJ/mol endothermic; by Hammond's postulate expect a very late saddle; the forward barrier to this step will be the largest of the pathway, likely 260 to 330 kJ/mol above V-I2).
- Band D: W-PRC -> W-P (near-thermoneutral, +3.74 kJ/mol; keep 8 to 10 images for resolution; the existing IDPP band converged without a climbing image and its peak implies about 58.6 kJ/mol as a lower estimate, so a CI-refined value matters here).

Endpoint pairs are now consecutive minima differing by one elementary event, which removes the multi-event interpolation problem at its root. Each converged NEB-TS saddle then goes through the A1 to A5 chain in Section 5. The earlier IDPP runs for the vanadium steps were killed mid-optimization; restart them to completion in the same directories. Harvest the V-TS1 OptTS output first, since it may already bracket the chemisorption region along with Band A.

Realistic expectations to state in advance, so the numbers are not mistaken for failures: V-TS1 and V-TS2 likely land in the tens of kJ/mol above their reactants; V-TS3 likely lands well above 250 kJ/mol above V-I2 because the step is 259.46 kJ/mol uphill; W-TS likely lands near 60 to 110 kJ/mol. Only A1 to A5 decides acceptance, not expectation.

## 7. Status declaration (replaces the closing claims of the last round)

Phase A: complete and closed (9 minima, references, provenance).
Phase B: OPEN. Saddles verified: 0 of 4. One apparent steam value retained as a benchmark cross-check, Verified = no.
Phase C: partially complete; register and summary require the Section 3 repair and the Section 4 edits before the next archive.
Tier 2 gate: remains closed until A1 to A5 are met for all four saddles.

## 8. Consequences for the thesis

Chapter 4 remains numerically unchanged, and Section 4.6 has been updated to state the scan outcomes truthfully: physical profiles obtained, refined candidates rejected at two-sided verification, band-based relocation in progress, corrected acceptance chain now fixed. No barrier enters the thesis until then.
