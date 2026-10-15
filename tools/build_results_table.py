#!/usr/bin/env python3
"""
build_results_table.py

Auditable source for the reported electronic and harmonic thermochemical data.

It parses the ORCA outputs in simulation/03_tier2_completion/results/ (the
completion campaign) and combines them with the audited Tier 1 register at
simulation/analysis/calculation_register.csv, which records the laptop ORCA
logs and acceptance status. It writes writing/markdown/_results.json plus a
human-readable table. It also derives a
conditional single-site occupation estimate from the harmonic Gibbs energies
and stated regenerator partial pressures. Geometry distances are taken from the
saved optimised XYZ structures and are listed separately in the thesis.

Energies, imaginary-mode counts, zero-point energies and thermal corrections
are read from the .out files. If the thesis and this script disagree on those
values, the script output should be checked against the named ORCA logs.

Run:  python3 tools/build_results_table.py
"""

import csv
import json
import math
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T2 = os.path.join(ROOT, "simulation", "03_tier2_completion", "results")
T1 = os.path.join(ROOT, "simulation", "analysis", "calculation_register.csv")
OUTJSON = os.path.join(ROOT, "writing", "markdown", "_results.json")
OUTTXT = os.path.join(ROOT, "writing", "markdown", "_results_table.txt")

EH = 2625.499638  # kJ/mol per Hartree


def read(p):
    raw = open(p, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", errors="ignore")
    return raw.decode("utf-8", errors="ignore")


def parse(path):
    t = read(path)
    d = {"file": os.path.basename(path)}
    d["terminated"] = "ORCA TERMINATED NORMALLY" in t
    d["converged"] = "THE OPTIMIZATION HAS CONVERGED" in t
    e = re.findall(r"FINAL SINGLE POINT ENERGY\s+(-?\d+\.\d+)", t)
    d["E"] = float(e[-1]) if e else None
    # Imaginary modes: take them from the last frequency block only
    i = t.rfind("VIBRATIONAL FREQUENCIES")
    vib = t[i:] if i >= 0 else ""
    ims = []
    for line in vib.splitlines():
        if "imaginary mode" in line:
            m = re.match(r"\s*\d+:\s+(-?\d+\.\d+)", line)
            if m:
                ims.append(float(m.group(1)))
    d["imag"] = ims
    rt = re.findall(r"TOTAL RUN TIME\s*:\s*(.+)", t)
    d["runtime"] = rt[-1].strip() if rt else "?"

    d["thermo"] = {}
    for ch in t.split("THERMOCHEMISTRY AT ")[1:]:
        m = re.match(r"(-?\d+\.?\d*)K", ch)
        if not m:
            continue
        T = float(m.group(1))
        ent = {}
        z = re.search(r"Zero point energy\s+\.\.\.\s+(-?\d+\.\d+)\s*Eh", ch)
        if z:
            ent["zpe"] = float(z.group(1))
        g = re.search(r"G-E\(el\)\s+\.\.\.\s+(-?\d+\.\d+)\s*Eh", ch)
        if g:
            ent["Gcorr"] = float(g.group(1))
        h = re.search(r"Total thermal energy\s+\.\.\.\s+(-?\d+\.\d+)\s*Eh", ch)
        if h:
            ent["Etherm"] = float(h.group(1))
        d["thermo"][T] = ent
    return d


def main():
    res = {}
    for f in sorted(os.listdir(T2)):
        if f.endswith(".out"):
            res[f[:-4]] = parse(os.path.join(T2, f))

    # ---------- B3LYP level tables ----------
    clu = res["s1_03_cluster_optfreq"]["E"]
    h2o = res["s1_01_h2o_optfreq"]["E"]
    van = res["s1_02_h3vo4_optfreq"]["E"]
    p_clu = res["pbe0_cluster"]["E"]
    p_h2o = res["pbe0_h2o"]["E"]
    p_van = res["pbe0_h3vo4"]["E"]

    b3 = {
        "V-PRC": res["s1_04_vprc_optfreq"],
        "V-I1": res["s4_01_vi1_optfreq"],
        "V-TS2": res["s4_05_vts2_optts"],
        "V-I2": res["s4_02_vi2_optfreq"],
        "V-P": res["s4_03_vp_optfreq"],
        "W-PRC": res["s1_05_wprc_optfreq"],
        "W-P": res["s4_04_wp_optfreq"],
    }
    pbe0 = {
        "V-PRC": res["pbe0_v-prc"],
        "V-I1": res["pbe0_v-i1"],
        "V-TS2": res["pbe0_v-ts2"],
        "V-I2": res["pbe0_v-i2"],
        "V-P": res["pbe0_v-p"],
        "W-PRC": res["pbe0_w-prc"],
        "W-P": res["pbe0_w-p"],
    }

    v_states = ["V-PRC", "V-I1", "V-TS2", "V-I2", "V-P"]
    w_states = ["W-PRC", "W-P"]

    table = {"levels": {}, "states": {}, "refs": {}}
    table["refs"] = {
        "B3LYP": {"cluster": clu, "H2O": h2o, "H3VO4": van,
                  "V_zero": clu + van, "W_zero": clu + h2o},
        "PBE0": {"cluster": p_clu, "H2O": p_h2o, "H3VO4": p_van,
                 "V_zero": p_clu + p_van, "W_zero": p_clu + p_h2o},
    }

    for lvl, src, refs in (("B3LYP", b3, table["refs"]["B3LYP"]),
                           ("PBE0", pbe0, table["refs"]["PBE0"])):
        table["levels"][lvl] = {}
        for st in v_states + w_states:
            r = src[st]
            zero = refs["V_zero"] if st.startswith("V") else refs["W_zero"]
            row = {
                "E": r["E"],
                "terminated": r["terminated"],
                "converged": r["converged"],
                "n_imag": len(r["imag"]),
                "imag": r["imag"],
                "runtime": r["runtime"],
                "dE": (r["E"] - zero) * EH if r["E"] is not None else None,
                "route": "V" if st.startswith("V") else "W",
            }
            # Gibbs at the two temperatures, from the state's own FREQ and the
            # two reference species at the same level
            for T in (298.15, 1003.15):
                stt = r["thermo"].get(T)
                ct = res["s1_03_cluster_optfreq"]["thermo"].get(T)
                if st.startswith("V"):
                    at = res["s1_02_h3vo4_optfreq"]["thermo"].get(T)
                else:
                    at = res["s1_01_h2o_optfreq"]["thermo"].get(T)
                if stt and ct and at and "Gcorr" in stt and "Gcorr" in ct and "Gcorr" in at:
                    dG = ((r["E"] + stt["Gcorr"]) - (refs["cluster"] + ct["Gcorr"])
                          - ((refs["H3VO4"] if st.startswith("V") else refs["H2O"]) + at["Gcorr"]))
                    row["dG_%g" % T] = dG * EH
                else:
                    row["dG_%g" % T] = None
            table["levels"][lvl][st] = row

    # ---------- Conditional competitive-site estimate ----------------------
    # This is a formal ideal-gas, single-site calculation using the harmonic
    # Gibbs energies and RFCC partial pressures discussed by Wormsbecher et al.
    # (1986). It is not a pore-aware prediction of experimental coverage.
    site_T = 1003.15
    gas_R = 0.00831446261815324  # kJ mol-1 K-1
    p_standard_atm = 1.0
    p_h2o_atm = 0.4
    p_h3vo4_range_atm = (2.0e-6, 2.0e-5)
    dg_v = table["levels"]["B3LYP"]["V-PRC"]["dG_1003.15"]
    dg_w = table["levels"]["B3LYP"]["W-PRC"]["dG_1003.15"]
    k_v = math.exp(-dg_v / (gas_R * site_T))
    k_w = math.exp(-dg_w / (gas_R * site_T))
    site_rows = []
    for p_v in p_h3vo4_range_atm:
        q_v = k_v * (p_v / p_standard_atm)
        q_w = k_w * (p_h2o_atm / p_standard_atm)
        denominator = 1.0 + q_v + q_w
        theta_v = q_v / denominator
        theta_w = q_w / denominator
        site_rows.append({
            "p_H3VO4_atm": p_v,
            "Kp_H3VO4": q_v,
            "Kp_H2O": q_w,
            "theta_H3VO4": theta_v,
            "theta_H2O": theta_w,
            "theta_H2O_over_H3VO4": theta_w / theta_v,
        })
    table["site_occupation"] = {
        "temperature_K": site_T,
        "standard_pressure_atm": p_standard_atm,
        "gas_constant_kJ_mol_K": gas_R,
        "partial_pressure_atm": {
            "H2O": p_h2o_atm,
            "H3VO4_range": list(p_h3vo4_range_atm),
        },
        "dG_1003.15_kJ_mol": {"H3VO4": dg_v, "H2O": dg_w},
        "K_standard_dimensionless": {"H3VO4": k_v, "H2O": k_w},
        "site_fraction_ranges": {
            "H3VO4": [site_rows[0]["theta_H3VO4"], site_rows[1]["theta_H3VO4"]],
            "H2O": [min(row["theta_H2O"] for row in site_rows),
                    max(row["theta_H2O"] for row in site_rows)],
        },
        "water_to_vanadic_acid_occupation_ratio": [
            site_rows[1]["theta_H2O_over_H3VO4"],
            site_rows[0]["theta_H2O_over_H3VO4"],
        ],
        "pressure_source": "Wormsbecher et al. (1986), 20% steam at 2 atm total pressure and 1-10 ppm H3VO4",
        "assumptions": [
            "ideal-gas standard states at 1 atm",
            "one equivalent adsorption site",
            "no interactions between adsorbed molecules",
            "harmonic Gibbs energies used as a conditional model input",
        ],
        "calculation_rows": site_rows,
    }

    # ---------- Tier 1 (GFN2-xTB) ----------
    with open(T1, newline="", encoding="utf-8") as f:
        t1_rows = list(csv.DictReader(f))
    t1 = {row["Job ID"]: row for row in t1_rows}

    def t1_energy(job_id):
        return float(t1[job_id]["Energy (Eh)"])

    def t1_relative(job_id, reference):
        registered = t1[job_id].get("Rel Energy (kJ/mol)", "")
        if registered not in ("", "-"):
            return float(registered)
        return (t1_energy(job_id) - reference) * EH

    cluster_t1 = t1_energy("cluster-T1-V02")
    h3vo4_t1 = t1_energy("h3vo4-T1-V01")
    h2o_t1 = t1_energy("h2o-T1-V01")
    v_zero_t1 = cluster_t1 + h3vo4_t1
    w_zero_t1 = cluster_t1 + h2o_t1

    minima_ids = {
        "V-PRC": "V-PRC_canonical",
        "V-I1": "V-I1-T1-V01",
        "V-I2": "V-I2-T1-V04",
        "V-P": "V-P-T1-V01",
        "W-PRC": "W-PRC-T1-V02",
        "W-P": "W-P-T1-V01",
    }
    minima = {}
    for state, job_id in minima_ids.items():
        row = t1[job_id]
        if row["Status"] != "Accepted" or row["Verified"].lower() != "yes":
            raise ValueError(f"Tier 1 minimum {job_id} is not marked accepted and verified")
        reference = v_zero_t1 if state.startswith("V") else w_zero_t1
        minima[state] = {
            "job_id": job_id,
            "energy_Eh": t1_energy(job_id),
            "relative_to_separated_kJ_mol": t1_relative(job_id, reference),
            "status": row["Status"],
            "verified": row["Verified"],
        }

    v_ts_id = "V-TS2-T1-V05"
    v_ts_row = t1[v_ts_id]
    if v_ts_row["Status"] != "Accepted" or v_ts_row["Verified"].lower() != "yes":
        raise ValueError("Tier 1 vanadic-acid saddle-point candidate is not marked accepted")
    v_ts_mode = re.search(r"\((-?\d+\.\d+)\s*cm-1\)", v_ts_row["Notes"])
    if not v_ts_mode:
        raise ValueError("Could not read the accepted V-TS2 imaginary-mode frequency")
    v_ts_barrier = (t1_energy(v_ts_id) - t1_energy("V-I1-T1-V01")) * EH

    w_ts_id = "W-TS-T1-V04"
    w_ts_row = t1[w_ts_id]
    w_ts_mode = re.search(r"\((-?\d+\.\d+)\s*cm-1\)", w_ts_row["Notes"])
    if not w_ts_mode:
        raise ValueError("Could not read the water-path candidate imaginary-mode frequency")
    w_ts_barrier = (t1_energy(w_ts_id) - t1_energy("W-PRC-T1-V02")) * EH
    w_displacements = [
        row["Notes"] for row in t1_rows
        if row["State"] == "W-TS" and row["Status"] == "Diagnostic run"
        and "Mode 6" in row["Notes"]
    ]
    if len(w_displacements) != 2 or not all("W-PRC well" in note for note in w_displacements):
        raise ValueError("Water-path transition-state displacement checks did not both return to W-PRC")

    table["tier1_reference"] = {
        "reference_energies_Eh": {"V": v_zero_t1, "W": w_zero_t1},
        "accepted_minima": minima,
        "accepted_saddle_point_candidate": {
            "state": "V-TS2",
            "job_id": v_ts_id,
            "energy_Eh": t1_energy(v_ts_id),
            "relative_to_separated_kJ_mol": t1_relative(v_ts_id, v_zero_t1),
            "barrier_from_V-I1_kJ_mol": v_ts_barrier,
            "imaginary_mode_cm-1": float(v_ts_mode.group(1)),
            "status": v_ts_row["Status"],
            "verified": v_ts_row["Verified"],
            "notes": v_ts_row["Notes"],
        },
        "water_path_candidate_not_accepted": {
            "state": "W-TS",
            "job_id": w_ts_id,
            "energy_Eh": t1_energy(w_ts_id),
            "relative_to_separated_kJ_mol": t1_relative(w_ts_id, w_zero_t1),
            "barrier_from_W-PRC_kJ_mol": w_ts_barrier,
            "imaginary_mode_cm-1": float(w_ts_mode.group(1)),
            "status": w_ts_row["Status"],
            "verified": w_ts_row["Verified"],
            "displacement_checks": w_displacements,
        },
        "source": "simulation/analysis/calculation_register.csv (job IDs and status) and named ORCA logs",
    }

    os.makedirs(os.path.dirname(OUTJSON), exist_ok=True)
    with open(OUTJSON, "w", encoding="utf-8") as f:
        json.dump(table, f, indent=2)

    # ---------- readable table ----------
    L = []
    L.append("RESULTS TABLE generated from ORCA outputs")
    L.append("=" * 96)
    L.append("Reference energies (Eh)")
    for lvl, r in table["refs"].items():
        L.append("  %-6s cluster=%.8f  H2O=%.8f  H3VO4=%.8f" %
                 (lvl, r["cluster"], r["H2O"], r["H3VO4"]))
    for lvl in ("B3LYP", "PBE0"):
        L.append("")
        L.append("Level: %s-D3(BJ)/def2-TZVP   (kJ/mol relative to separated reactants)" % lvl)
        L.append("  %-8s %6s %6s %6s %18s %10s %10s %10s %10s" %
                 ("state", "term", "conv", "nimag", "E(Eh)", "dE",
                  "dG(298K)", "dG(1003K)", "runtime"))
        for st in v_states + w_states:
            r = table["levels"][lvl][st]
            f2 = lambda x: ("%10.1f" % x) if x is not None else "         -"
            L.append("  %-8s %6s %6s %6d %18.8f %10.1f %s %s %10s" %
                     (st, r["terminated"], r["converged"], r["n_imag"], r["E"],
                      r["dE"], f2(r.get("dG_298.15")), f2(r.get("dG_1003.15")),
                      r["runtime"].split("  ")[0][:10]))
    L.append("")
    L.append("Conditional single-site occupation estimate at %.2f K" % site_T)
    L.append("  standard pressure: %.1f atm; p(H2O)=%.3g atm; p(H3VO4)=%.3g to %.3g atm" %
             (p_standard_atm, p_h2o_atm, p_h3vo4_range_atm[0], p_h3vo4_range_atm[1]))
    L.append("  K°(H3VO4)=%.3g; K°(H2O)=%.3g" % (k_v, k_w))
    for row in site_rows:
        L.append("  p(H3VO4)=%.3g atm: theta(H3VO4)=%.3g; theta(H2O)=%.3g; theta(H2O)/theta(H3VO4)=%.3g" %
                 (row["p_H3VO4_atm"], row["theta_H3VO4"], row["theta_H2O"],
                  row["theta_H2O_over_H3VO4"]))
    L.append("  Assumptions: ideal-gas harmonic thermochemistry, one equivalent site, no adsorbate interactions.")
    L.append("  This is a conditional model estimate, not a pore-aware experimental coverage prediction.")
    L.append("")
    t1_summary = table["tier1_reference"]
    L.append("Tier 1 (GFN2-xTB) accepted minima, kJ/mol vs separated reactants")
    for state, row in t1_summary["accepted_minima"].items():
        L.append("  %-8s %10.2f" % (state, row["relative_to_separated_kJ_mol"]))
    v_ts = t1_summary["accepted_saddle_point_candidate"]
    L.append("Accepted GFN2-xTB saddle-point candidate: V-TS2")
    L.append("  barrier above V-I1: %.2f kJ/mol; one imaginary mode at %.2f cm-1" %
             (v_ts["barrier_from_V-I1_kJ_mol"], v_ts["imaginary_mode_cm-1"]))
    w_ts = t1_summary["water_path_candidate_not_accepted"]
    L.append("Water-path candidate W-TS was not accepted")
    L.append("  barrier above W-PRC: %.2f kJ/mol; one imaginary mode at %.2f cm-1" %
             (w_ts["barrier_from_W-PRC_kJ_mol"], w_ts["imaginary_mode_cm-1"]))
    L.append("  both two-sided displacement checks returned to W-PRC")
    with open(OUTTXT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
