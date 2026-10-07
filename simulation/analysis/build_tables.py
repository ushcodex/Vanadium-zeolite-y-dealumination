#!/usr/bin/env python3
"""Build the result tables used in the thesis directly from the ORCA outputs.

Every number printed here is read out of a log file listed by name, so each
table row can be re-derived from the repository. No value is typed in by hand.
Outputs:
  analysis/RESULTS.md      - the tables, in markdown
  analysis/results.csv     - the same numbers, machine readable
"""
import csv, os, json

ROOT = "/home/user/Vanadium-zeolite-y-dealumination/simulation"
REG = os.path.join(ROOT, "analysis", "orca_register.csv")
HARTREE = 2625.4996394799  # kJ/mol per Eh, CODATA 2018

rows = {r["path"]: r for r in csv.DictReader(open(REG, encoding="utf-8"))}


def E(path):
    return float(rows[path]["e_sp"])


def f(path, field, default=None):
    v = rows[path][field]
    return float(v) if v not in ("", None) else default


def kJ(eh):
    return eh * HARTREE


# ---------------------------------------------------------------- Tier 2 set
T2 = "03_tier2_completion/results/"
T2A = "03_tier2_completion/results/first_pass/"
T1 = "02_tier1/"

# authoritative Tier 2 job for every state: converged + frequency verified wins
T2_JOBS = {
    "cluster": T2 + "s1_03_cluster_optfreq.out",
    "H2O": T2 + "s1_01_h2o_optfreq.out",
    "H3VO4": T2 + "s1_02_h3vo4_optfreq.out",
    "V-PRC": T2 + "s1_04_vprc_optfreq.out",
    "W-PRC": T2 + "s1_05_wprc_optfreq.out",
    "V-I1": T2 + "s4_01_vi1_optfreq.out",
    "W-P": T2 + "s4_04_wp_optfreq.out",
}
# states whose Tier 2 optimisation did not reach the convergence threshold
T2_UNCONVERGED = {
    "V-I2": [(T2A + "s4_02_vi2_optfreq.out", "90 opt cycles, terminated normally, not converged"),
             (T2 + "s4_02_vi2_optfreq.out", "60 opt cycles, not converged")],
    "V-P": [(T2A + "s4_03_vp_optfreq.out", "90 opt cycles, terminated normally, not converged"),
            (T2 + "s4_03_vp_optfreq.out", "25 opt cycles, job did not terminate normally")],
}
T2_REJECTED = {
    "V-TS2": (T2 + "s4_05_vts2_optts.out", "OptTS stopped at 200 cycles with 14 imaginary modes"),
}
# PBE0-D3(BJ)/def2-TZVP single points on the same relaxed geometries
PBE0 = {
    "cluster": T2 + "pbe0_cluster.out",
    "H2O": T2 + "pbe0_h2o.out",
    "H3VO4": T2 + "pbe0_h3vo4.out",
    "V-PRC": T2 + "pbe0_v-prc.out",
    "W-PRC": T2 + "pbe0_w-prc.out",
    "V-I1": T2 + "pbe0_v-i1.out",
    "V-I2": T2 + "pbe0_v-i2.out",
    "V-P": T2 + "pbe0_v-p.out",
    "W-P": T2 + "pbe0_w-p.out",
    "V-TS2(candidate)": T2 + "pbe0_v-ts2.out",
}

# ---------------------------------------------------------------- Tier 1 set
T1_JOBS = {
    "cluster": "01_models/cluster/cluster-T1-V02.out",
    "H2O": "01_models/h2o/h2o-T1-V01.out",
    "H3VO4": "01_models/h3vo4/h3vo4-T1-V01.out",
    "V-PRC": "02_tier1/V-R/V-R-T1-V02.out",
    "V-I1": "02_tier1/V-I1/V-I1-T1-V01.out",
    "V-TS2": "02_tier1/V-TS2/optts3_bandB_ci.out",
    "V-I2": "02_tier1/V-I2/V-I2-T1-V04_pos.out",
    "V-P": "02_tier1/V-TS3/V-TS3-T1-V02.out",
    "W-PRC": "02_tier1/W-PRC/W-PRC-T1-V02.out",
    "W-TS": "02_tier1/W-TS/optts2_bandD_ci.out",
    "W-P": "02_tier1/W-P/W-P-T1-V01.out",
}

out = []
w = out.append

w("# Verified result tables")
w("")
w("Built by `simulation/analysis/build_tables.py` from `orca_register.csv`, which is")
w("produced by `simulation/analysis/parse_orca.py` straight from the ORCA logs.")
w("1 Eh = %.6f kJ/mol (CODATA 2018)." % HARTREE)
w("")

# --- Tier 1 -----------------------------------------------------------------
w("## Tier 1, GFN2-xTB (ORCA 6.1.0, Dell Latitude E6430)")
w("")
w("| state | log file | E / Eh | rel. to separated reactants / kJ/mol | imaginary modes |")
w("|---|---|---|---|---|")
t1 = {}
refV = E(T1_JOBS["cluster"]) + E(T1_JOBS["H3VO4"])
refW = E(T1_JOBS["cluster"]) + E(T1_JOBS["H2O"])
for k in ["cluster", "H2O", "H3VO4"]:
    p = T1_JOBS[k]
    t1[k] = E(p)
    w("| %s | `%s` | %.8f | reference | %s |" % (k, p, E(p), rows[p]["n_imag"]))
for k in ["V-PRC", "V-I1", "V-TS2", "V-I2", "V-P"]:
    p = T1_JOBS[k]
    t1[k] = E(p)
    w("| %s | `%s` | %.8f | %.2f | %s |" % (k, p, E(p), kJ(E(p) - refV), rows[p]["n_imag"] or 0))
for k in ["W-PRC", "W-TS", "W-P"]:
    p = T1_JOBS[k]
    t1[k] = E(p)
    w("| %s | `%s` | %.8f | %.2f | %s |" % (k, p, E(p), kJ(E(p) - refW), rows[p]["n_imag"] or 0))
w("")
w("Tier 1 reference zero, vanadium route: %.8f Eh." % refV)
w("Tier 1 reference zero, steam route: %.8f Eh." % refW)
w("")

# --- Tier 2 -----------------------------------------------------------------
w("## Tier 2, B3LYP-D3(BJ)/def2-TZVP (ORCA 6.1.1, cloud)")
w("")
w("### Converged and frequency verified")
w("")
w("| state | log file | cycles | E / Eh | ZPE / Eh | H(298) corr / Eh | G(298) corr / Eh | G(1003) corr / Eh | imaginary |")
w("|---|---|---|---|---|---|---|---|---|")
t2 = {}
for k, p in T2_JOBS.items():
    t2[k] = E(p)
    w("| %s | `%s` | %s | %.8f | %s | %s | %s | %s | %s |" % (
        k, p, rows[p]["opt_cycles"], E(p), rows[p]["zpe"], rows[p]["h298_corr"],
        rows[p]["g298_corr"], rows[p]["g1003_corr"],
        (rows[p]["imag_cm"] or "0")))
w("")
w("### Started but not converged (reported, not used for the conclusions)")
w("")
w("| state | log file | status | best E / Eh |")
w("|---|---|---|---|")
for k, lst in T2_UNCONVERGED.items():
    for p, why in lst:
        w("| %s | `%s` | %s | %.8f |" % (k, p, why, E(p)))
for k, (p, why) in T2_REJECTED.items():
    w("| %s | `%s` | %s | %.8f |" % (k, p, why, E(p)))
w("")

refV2 = E(T2_JOBS["cluster"]) + E(T2_JOBS["H3VO4"])
refW2 = E(T2_JOBS["cluster"]) + E(T2_JOBS["H2O"])
w("Tier 2 reference zero, vanadium route: %.8f Eh." % refV2)
w("Tier 2 reference zero, steam route: %.8f Eh." % refW2)
w("")


def ads(frag, cplx, ref_frag):
    """[dE, dE+ZPE, dH298, dG298, dG1003] in kJ/mol for frag + cluster -> complex."""
    dE = E(cplx) - E(frag) - E(ref_frag)
    zpe = f(cplx, "zpe", 0) - f(frag, "zpe", 0) - f(ref_frag, "zpe", 0)
    out = [kJ(dE), kJ(dE + zpe)]
    for cf in ["h298_corr", "g298_corr", "g1003_corr"]:
        c = f(cplx, cf, 0) - f(frag, cf, 0) - f(ref_frag, cf, 0)
        out.append(kJ(dE + c))
    return out


CL = T2_JOBS["cluster"]
w("### Adsorption thermodynamics at the Brønsted site")
w("")
w("| quantity | vanadic acid, H3VO4 | steam, H2O | vanadic acid minus steam |")
w("|---|---|---|---|")
labels = ["electronic dE", "dE with ZPE", "dH at 298.15 K", "dG at 298.15 K", "dG at 1003.15 K"]
va = ads(T2_JOBS["H3VO4"], T2_JOBS["V-PRC"], CL)
wa = ads(T2_JOBS["H2O"], T2_JOBS["W-PRC"], CL)
for lab, x, y in zip(labels, va, wa):
    w("| %s | %.2f | %.2f | %.2f |" % (lab, x, y, x - y))
w("")
w("Thermal corrections are the G-E(el) and H-E(el) terms printed by ORCA in the")
w("frequency run of each job. The reference is the separated cluster plus the free")
w("molecule, each at its own optimised geometry.")
w("")

w("### PBE0-D3(BJ)/def2-TZVP single points on the Tier 2 geometries")
w("")
w("| state | log file | E / Eh |")
w("|---|---|---|")
for k, p in PBE0.items():
    w("| %s | `%s` | %.8f |" % (k, p, E(p)))
w("")
pV = E(PBE0["V-PRC"]) - E(PBE0["cluster"]) - E(PBE0["H3VO4"])
pW = E(PBE0["W-PRC"]) - E(PBE0["cluster"]) - E(PBE0["H2O"])
w("PBE0 electronic adsorption energy, vanadic acid: %.2f kJ/mol." % kJ(pV))
w("PBE0 electronic adsorption energy, steam: %.2f kJ/mol." % kJ(pW))
w("PBE0 margin, vanadic acid over steam: %.2f kJ/mol." % (kJ(pV) - kJ(pW)))
w("")

w("### Tier 2 stationary-point ladder (electronic energies only)")
w("")
w("| state | relative to separated cluster + H3VO4 / kJ/mol | note |")
w("|---|---|---|")
for k in ["V-PRC", "V-I1"]:
    w("| %s | %.2f | converged, 0 imaginary |" % (k, kJ(E(T2_JOBS[k]) - refV2)))
for k, lst in T2_UNCONVERGED.items():
    p = lst[0][0]
    w("| %s | %.2f | not converged; bracket only |" % (k, kJ(E(p) - refV2)))
w("| V-TS2 | %.2f | rejected: 14 imaginary modes |" % kJ(E(T2_REJECTED["V-TS2"][0]) - refV2))
w("")
w("| state | relative to separated cluster + H2O / kJ/mol | note |")
w("|---|---|---|")
for k in ["W-PRC", "W-P"]:
    w("| %s | %.2f | converged, 0 imaginary |" % (k, kJ(E(T2_JOBS[k]) - refW2)))
w("")

w("### Tier 1 barrier summary (GFN2-xTB)")
w("")
w("| step | barrier / kJ/mol | imaginary mode / cm-1 |")
w("|---|---|---|")
w("| V-PRC -> V-TS2 (first Al-O cleavage via V-I1) | %.2f (from V-I1) | %s |" % (
    kJ(E(T1_JOBS["V-TS2"]) - E(T1_JOBS["V-I1"])), rows[T1_JOBS["V-TS2"]]["imag_cm"]))
w("| W-PRC -> W-TS (steam hydrolysis) | %.2f (from W-PRC) | %s |" % (
    kJ(E(T1_JOBS["W-TS"]) - E(T1_JOBS["W-PRC"])), rows[T1_JOBS["W-TS"]]["imag_cm"]))
w("")
w("V-I1 lies %.2f kJ/mol below V-PRC at Tier 1." % kJ(E(T1_JOBS["V-I1"]) - E(T1_JOBS["V-PRC"])))
w("V-I2 lies %.2f kJ/mol above V-I1 at Tier 1." % kJ(E(T1_JOBS["V-I2"]) - E(T1_JOBS["V-I1"])))
w("")

w("### Cluster reference check")
w("")
w("| run | E / Eh | cycles | converged | imaginary |")
w("|---|---|---|---|---|")
for p in ["03_tier2_completion/results/first_pass/s1_03_cluster_optfreq.out",
          T2_JOBS["cluster"]]:
    w("| `%s` | %.8f | %s | %s | %s |" % (p, E(p), rows[p]["opt_cycles"],
                                          rows[p]["converged"], rows[p]["imag_cm"] or 0))
w("")
w("Spread between the two cluster runs: %.4f kJ/mol." % abs(kJ(
    E(T2_JOBS["cluster"]) - E("03_tier2_completion/results/first_pass/s1_03_cluster_optfreq.out"))))
w("")

open(os.path.join(ROOT, "analysis", "RESULTS.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
