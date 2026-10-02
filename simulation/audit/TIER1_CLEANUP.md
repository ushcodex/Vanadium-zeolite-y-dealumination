# Tier 1 Cleanup and Verification Protocol

Scope: close out Tier 1 (GFN2-xTB, local laptop) so that every number admitted to the thesis is stationary-point proven, before any Tier 2 DFT work begins. This protocol has three phases: Phase A audits what exists, Phase B re-establishes the four saddle points properly, Phase C repairs the register and re-gates the project for Tier 2.

## 1. Why the first-pass saddle runs returned wrong values

The three vanadium-route NEB peak energies imply barriers of 808.7, 1105.6, and 1694.2 kJ/mol for steps whose chemistry is proton relay and Al-O bond cleavage. The same bond cleavage costs about 103 kJ/mol on the steam route, so these numbers are not chemistry; they are method output. Four root causes, in order of importance:

1. Endpoints that differ by too many events at once. Each NEB was run from one minimum all the way to the next reported minimum, but states such as V-I1 to V-P differ by vanadium migration plus two to three proton transfers plus framework bond cleavage. A single elastic band across such a transformation is not describing one elementary step; it is averaging several.
2. Linear interpolation in Cartesian coordinates. The default path construction places intermediate images on straight line segments between endpoint atom positions. When several bonds break and form, those straight lines pass through atom-overlap regions, so every interpolated image carries a large artificial energy. The highest image is an interpolation artifact, not a saddle point.
3. The curated seed saddles were never used as starting points. The structure set V-TS1, V-TS2, V-TS3 was prepared for exactly this purpose. A direct OptTS refinement from a good seed with an exact initial Hessian is the standard, cheapest, and most reliable way to converge a known saddle. It was skipped in favour of black-box endpoint NEB.
4. Register marked the NEB-TS jobs as Accepted with exactly one imaginary mode, while the run logs themselves show frequency checks on raw peak frames returning multiple small imaginary modes and OptTS refinements still descending at the end of those logs. The entry confused job completion with scientific acceptance. The steam-route saddle shares the weaker version of the same problem: its value comes from the NEB peak image, and its OptTS refinement was still drifting toward the product basin when the log ended.

So the answer to "was it because we gave guess structures" is no. The guess structures are the correct instrument; they were simply never deployed. The answer to "why not use a reactants-products method" is that NEB is precisely the reactants-products family, and we already used it: every automated endpoint method still has to guess the path between the endpoints, and that guess is what failed. There is no reliable black box that takes a reactant and a product and returns a trustworthy barrier. The reliable ladder, used throughout computational chemistry, is:

  seed geometry -> OptTS with exact initial Hessian -> exactly one imaginary mode
  -> IRC in both directions -> endpoint fall-in verification

with a relaxed surface scan as the way to manufacture a seed when none exists, and IDPP-interpolated NEB with the seed inserted as the fallback when direct refinement refuses to converge.

## 2. Phase A: ruthless audit of existing results (no new chemistry)

A1. Arithmetic re-verification. Every relative energy and barrier in the register was recomputed from the Hartree values with 1 Eh = 2625.50 kJ/mol. All twelve minimum and artifact rows reproduce exactly. The pathway step sums close exactly: -194.21 (adsorption) - 190.89 (chemisorption) + 42.77 (I1 to I2) + 259.43 (I2 to P) = -82.90 kJ/mol overall for the vanadium route; -69.59 + 3.74 = -65.85 kJ/mol for the steam route. The mathematics of the register is sound; the provenance of four rows is not.

A2. Automated output audit. Run the accompanying script against the whole Tier 1 tree:

  python verify_tier1.py 02_tier1

Expect: every minimum shows normal termination, a converged optimization, a frequency printout, and zero imaginary modes. Any row failing any condition goes back for re-optimization. Confirm in particular that each V02 restart job (V-R, W-PRC, V-P) reached "THE OPTIMIZATION HAS CONVERGED" and that its FREQ ran on the final converged geometry.

A3. V-R versus V-PRC identity check. The two adsorption energies differ by only 2.69 kJ/mol (-196.90 vs -194.21). A genuine supermolecule held apart at about 1 nm cannot carry -196.9 kJ/mol of interaction, so one of two things is true: the V-R optimization relaxed into the V-PRC basin, or the value is spurious. Measure it:

  python verify_tier1.py --dist V-R-T1-V02.xyz --fragA 1-22 --fragB 23-30

If the shortest cluster-to-acid contact is about 0.17 to 0.20 nm, V-R collapsed to the PRC basin; the rows describe one state, which is itself a result (the adsorption basin is unique and deep). Merge the rows accordingly in the register. If the contact exceeds about 0.5 nm, the V-R energy is inconsistent with its geometry and the job must be re-examined before Tier 2 reuses its references.

A4. Cluster geometry re-check. Confirm the optimized cluster still shows the expected metric ordering: Al-O(H) longest at 0.192 nm, remaining Al-O at 0.169 to 0.170 nm, Si-O at 0.161 to 0.167 nm. Any capping-hydrogen torsion under about 40 cm-1 with zero imaginary modes is acceptable; anything imaginary under the framework modes is not.

A5. Metadata repair. The register records Cores = 1 for jobs whose logs show a three-core parallel allocation. Align the metadata with reality. Add a Verified column to the register distinguishing arithmetic-valid from stationary-point-proven.

## 3. Phase B: re-establish the four saddle points

Run these in the order listed; each is minutes of laptop time at the xTB level. Templates are in orca_templates/.

B1. V-TS1 (chemisorption plus proton transfer, endpoints V-PRC and V-I1). Run t1_xTb_optts_from_seed.inp from xyz_seeds/V-TS1_start.xyz. Acceptance: converged OptTS, exactly one imaginary mode, mode animation shows the transferring proton and the forming Al-O(V) bond. Then run t1_xTb_irc.inp from the converged saddle; optimize both IRC endpoints; they must reproduce V-PRC and V-I1 within about 5 kJ/mol. Only then does the barrier enter the register with Verified = yes.

B2. V-TS2 (first Al-O cleavage with proton relay, endpoints V-I1 and V-I2). Same procedure from V-TS2_start.xyz.

B3. V-TS3 (final Al-O cleavage, endpoints V-I2 and V-P). Same procedure from V-TS3_start.xyz.

B4. W-TS (steam hydrolysis, endpoints W-PRC and W-P). This one has no curated seed, so manufacture it first: run t1_xTb_relaxed_scan.inp stretching the Al-O(H) bond (about 0.175 to 0.305 nm in 14 steps) from the W-PRC geometry, identify the scan maximum, then OptTS plus FREQ from that maximum, then IRC verification as above. Replace the present apparent value with the verified one; only then may the comparison with the 76 to 125 kJ/mol literature range be stated as a numerical result rather than a method-level cross-check.

B5. Fallback rule. If any OptTS-from-seed fails on two genuine attempts (does not converge, or converges to the wrong mode), switch to t1_xTb_nebts_idpp.inp for that step: IDPP interpolation with the curated seed inserted into the path (ORCA 6.1 keyword TS "V-TSn_start.xyz" inside %neb), then finish with the same OptTS, FREQ, and IRC acceptance tests. Under no circumstances does a raw NEB peak image enter the record as a barrier again.

B6. Known semi-empirical biases to carry forward. The deep chemisorption well (-385.10 kJ/mol) and the chelated product (-82.90 kJ/mol) depend on five-coordinate aluminium and V-O-Al bonding, motifs that GFN2-xTB can overbind. These remain Tier 1 reports as stated; Tier 2 will re-evaluate them, and thesis Chapter 4 Section 4.7 already flags the qualification. Record the bias note in the register so the Tier 2 job list explicitly includes V-I1, V-I2, and V-P.

## 4. Phase C: register repair and the Tier 2 gate

C1. Re-label the four current saddle rows (V-TS1, V-TS2, V-TS3, W-TS) as "Artifact, excluded" (vanadium rows) and "Apparent, superseded" (steam row). Do not delete them; they document the failure mode and are referenced by Chapter 4 Section 4.6.

C2. Enter the new verified saddles as rows V-TSn-T1-V03 / W-TS-T1-V03 with energy, one-imaginary-mode confirmation, IRC endpoint confirmation, and Verified = yes.

C3. Regenerate tier1_summary.md from the repaired register, re-zip the Tier 1 archive, and note the cleanup in walkthrough.md.

C4. Tier 2 gate: Tier 2 begins only when (a) every minimum in Phase A is audit-clean, (b) all four barriers in Phase B are verified with IRC fall-in, and (c) the register carries no Accepted row whose provenance the logs contradict.

C5. Thesis update after cleanup: Chapter 4 Table 4.3 and Figure 4.2(a) receive the verified barriers, Section 4.6 is rewritten as resolved with the new values, Table 3.6 status marks the saddle stage completed, and Section 4.8 and Chapter 5 text are updated accordingly.

## 5. Acceptance criteria reference

Minimum (reactant, intermediate, product): normal termination; converged optimization; zero imaginary frequencies; geometry metrics inside sanity ranges.
Saddle: converged OptTS; exactly one imaginary frequency; the mode animates along the reacting bonds; IRC endpoints re-optimize to the claimed reactant and product within about 5 kJ/mol; only then may the barrier be quoted.
Any result failing a criterion keeps its register row but is excluded from interpretation, per the no-silent-deletion rule.
