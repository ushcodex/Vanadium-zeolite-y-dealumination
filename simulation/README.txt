SIMULATION PACKAGE - FILE GUIDE
================================

molfiles/
  The six curated structures with strict covalent connectivity, split from the
  original molfiles.txt. Use these for building, editing, and visual checking
  in Spartan and Avogadro. The bond tables in these files are the canonical
  statement of intended connectivity for every state.

xyz_seeds/
  Coordinate-only files generated directly from the same structures, plus
  cluster, H3VO4, and H2O seeds. Coordinates and atom order are identical to
  the molfiles. Use these strictly as ORCA and xTB inputs (* xyzfile 0 1).

Why both formats exist:
  XYZ contains no bond information, so viewers GUESS bonds from distances and
  may draw wrong ones (transferring protons, five-coordinate Al, V-O bonds).
  This is a display artifact only. ORCA and xTB energies depend solely on atom
  positions, charge, and multiplicity; the bond table is neither read nor
  needed by the quantum chemistry. Connectivity matters only when hand-editing
  or visually checking in a GUI, which is what the molfiles are for.

Rules:
  1. Never judge a calculation input by the bonds a viewer draws on an XYZ.
  2. Never regenerate XYZs by hand; derive them from the molfiles so atom
     order stays identical (required for NEB endpoints).
  3. If a new structure is drawn in the GUI, save BOTH the .mol and export
     the .xyz from the same session.

orca_templates/
  Ready ORCA input files for Tiers 1-3. Atom numbering inside %geom blocks is
  ZERO-based; adjust to match the actual input file before every run.

WAY_FORWARD.md / RFCC_DFT_Simulation_Way_Forward.docx
  The execution protocol: stages, commands, quality gates, register format,
  and Chapter Four feed-stock.

TIER1_CLEANUP.md / TIER1_CLEANUP.docx
  The Tier 1 audit and saddle-point re-establishment protocol. Required
  reading before any Tier 2 job is started. Explains why the first-pass NEB
  barriers are artifacts, audits every existing result, and fixes the four
  saddles via OptTS from the curated seeds plus IRC verification.

03_tier2_completion/
  The completion package for the cloud DFT work: the four agreed scopes
  (frequencies, counterpoise, PBE0 single points on relaxed geometries, and
  optimisations for the eight states the Tier 2 plan never ran).

    README_RUNBOOK.md   what to run, in what order, with what budget, and the
                        decision rules written down BEFORE each job
    AUDIT_FINDINGS.md   what the repository actually contains, with the
                        arithmetic behind every corrected number
    run_scope.sh        resumable runner (skips finished jobs, records a
                        manifest per scope, stops cleanly on a budget or a
                        results/STOP file, never overwrites a result)
    xyz/                the 13 input geometries, atom order identical to Tier 1
    jobs/               ORCA inputs, split by scope
    tools/              gen_inputs.py (scope 3, ghost fallback, A4
                        displacements), audit_tier2.py (audit + level tables +
                        counterpoise), pull_results.sh
    plan/JOB_PLAN.csv   the 30 planned jobs with purposes, cost brackets, gates

  Nothing may be judged from the raw XYZ bond perception; see the rules above.

verify_tier1.py
  Standard-library audit script for ORCA outputs on the laptop:
    python verify_tier1.py 02_tier1
  lists termination, convergence, imaginary-mode count, and final energy for
  every .out file under the Tier 1 tree. Its --dist mode measures the shortest
  fragment separation in a supermolecular xyz (for the V-R vs V-PRC identity
  check). Tier 2 may not start until Phase A and Phase B are clean.
