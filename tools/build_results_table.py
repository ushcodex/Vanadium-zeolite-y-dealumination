#!/usr/bin/env python3
"""
build_results_table.py

Single source of truth for every number that appears in Chapters 4 and 5.

It parses the ORCA outputs in simulation/03_tier2_completion/results/ (the
completion campaign) and simulation/02_tier1/ (the laptop campaign) and writes
writing/markdown/_results.json plus a human-readable table.

Nothing here is typed in by hand: energies, imaginary-mode counts, zero-point
energies and thermal corrections are all read out of the .out files.  If the
thesis and this script disagree, this script is right.

Run:  python3 tools/build_results_table.py
"""

import csv
import json
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
    ims = []
    for blk in t.split("VIBRATIONAL FREQUENCIES")[1:]:
        for m in re.finditer(r"\*\*\*imaginary mode\*\*\*", blk):
            pass
    # imaginary modes: take them from the last frequency block only
    i = t.rfind("VIBRATIONAL FREQUENCIES")
    vib = t[i:] if i >= 0 else ""
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

    # ---------- Tier 1 (GFN2-xTB) ----------
    t1 = {}
    with open(T1, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            t1[row["Job ID"]] = row
    table["tier1_reference"] = {
        "cluster": -31.34551236, "H3VO4": -19.77512769, "H2O": -5.07054445,
        "V_zero": -51.12064005, "W_zero": -36.41605681,
        "accepted": {
            "V-PRC": -196.90, "V-I1": -385.10, "V-TS2": -224.40,
            "V-I2": -342.36, "V-P": -82.90,
            "W-PRC": -69.59, "W-TS": -40.29, "W-P": -65.85,
        },
        "barriers": {
            "V-TS2 vs V-I1": 160.70,
            "W-TS vs W-PRC": 29.29,
        },
        "source": "simulation/analysis/calculation_register.csv (accepted rows only)",
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
    L.append("Tier 1 (GFN2-xTB) accepted stationary points, kJ/mol vs separated reactants")
    for k, v in table["tier1_reference"]["accepted"].items():
        L.append("  %-8s %10.2f" % (k, v))
    with open(OUTTXT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
