#!/usr/bin/env python3
"""audit_tier2.py - ruthless audit of the Tier 2 / Tier 3 completion outputs.

Standard library only.  Run from the package root (or point it at any directory):

    python3 tools/audit_tier2.py results
    python3 tools/audit_tier2.py results --table        # level tables only
    python3 tools/audit_tier2.py results --cp           # counterpoise analysis
    python3 tools/audit_tier2.py results --csv summary.csv

WHAT IT REPORTS
  1. One row per ORCA .out: normal termination, optimisation convergence,
     imaginary-mode count and values, final single point energy, runtime.
     (Both UTF-8 and the UTF-16 output written by ORCA on Windows are read.)
  2. --table : the energy tables, per level of theory, relative to the two
     reference zeros, with ZPE and Gibbs corrections where a FREQ job exists:
        vanadium route zero = E(cluster) + E(H3VO4)
        steam route zero    = E(cluster) + E(H2O)
  3. --cp : the counterpoise analysis for V-PRC and W-PRC, using the two
     ghost-fragment jobs, with the formulas written out.

RULES IT ENFORCES (printed at the end)
     minimum : terminated, converged, 0 imaginary modes
     saddle  : terminated, converged, exactly 1 imaginary mode, then A4
"""

import argparse
import os
import re
import sys

EH = 2625.499638  # kJ/mol per Hartree

# the same job-base -> state map as run_scope.sh
STATE_MAP = {
    "s1_01_h2o_optfreq": "h2o", "s1_02_h3vo4_optfreq": "h3vo4",
    "s1_03_cluster_optfreq": "cluster", "s1_04_vprc_optfreq": "v-prc",
    "s1_05_wprc_optfreq": "w-prc",
    "s4_01_vi1_optfreq": "v-i1", "s4_02_vi2_optfreq": "v-i2",
    "s4_03_vp_optfreq": "v-p", "s4_04_wp_optfreq": "w-p",
    "s4_05_vts2_optts": "v-ts2", "s4_06_vts3_optts": "v-ts3",
    "s4_07_wts_optts": "w-ts", "s4_08_vts1_optfreq": "v-ts1",
}
V_STATES = ["v-prc", "v-i1", "v-ts2", "v-i2", "v-ts3", "v-p", "v-ts1"]
W_STATES = ["w-prc", "w-ts", "w-p"]
LABELS = {"v-prc": "V-PRC", "v-i1": "V-I1", "v-ts1": "V-TS1", "v-ts2": "V-TS2",
          "v-i2": "V-I2", "v-ts3": "V-TS3", "v-p": "V-P", "w-prc": "W-PRC",
          "w-ts": "W-TS", "w-p": "W-P", "cluster": "cluster", "h2o": "H2O",
          "h3vo4": "H3VO4"}


def read_text(path):
    raw = open(path, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", errors="ignore")
    return raw.decode("utf-8", errors="ignore")


def last_vib_block(text):
    i = text.rfind("VIBRATIONAL FREQUENCIES")
    if i < 0:
        return ""
    j = text.find("NORMAL MODES", i)
    return text[i:j if j > i else i + 20000]


def parse_out(path):
    t = read_text(path)
    d = {"file": os.path.basename(path)}
    d["terminated"] = "ORCA TERMINATED NORMALLY" in t
    d["converged"] = ("THE OPTIMIZATION HAS CONVERGED" in t)
    conv = d["converged"]
    d["opt_type"] = "SP"
    vib = last_vib_block(t)
    ims = []
    for line in vib.splitlines():
        if "***imaginary mode***" in line:
            m = re.match(r"\s*(\d+):\s+(-?\d+\.\d+)", line)
            if m:
                ims.append(float(m.group(2)))
    d["imag"] = ims
    if d["converged"]:
        d["kind"] = ("MIN" if len(ims) == 0 else
                     ("TS?" if len(ims) == 1 else "check"))
    else:
        d["kind"] = "SP" if not ims else "freq"
    e = re.findall(r"FINAL SINGLE POINT ENERGY\s+(-?\d+\.\d+)", t)
    d["energy"] = float(e[-1]) if e else None
    rt = re.findall(r"TOTAL RUN TIME\s*:\s*(.+)", t)
    d["runtime"] = rt[-1].strip() if rt else "?"

    # thermochemistry, one entry per temperature
    d["thermo"] = {}
    chunks = t.split("THERMOCHEMISTRY AT ")
    for ch in chunks[1:]:
        m = re.match(r"(-?\d+\.?\d*)K", ch)
        if not m:
            continue
        temp = float(m.group(1))
        zpe = re.search(r"Zero point energy\s+\.\.\.\s+(-?\d+\.\d+)\s*Eh", ch)
        g = re.findall(r"G-E\(el\)\s+\.\.\.\s+(-?\d+\.\d+)\s*Eh", ch)
        entry = {}
        if zpe:
            entry["zpe"] = float(zpe.group(1))
        if g:
            entry["G-E"] = float(g[-1])
        d["thermo"][temp] = entry

    # counterpoise bookkeeping
    d["ghosted_frag"] = None
    m = re.search(r"GhostFrags\s*\{([^}]*)\}", t)
    if m:
        d["ghosted_frag"] = m.group(1).strip()
    return d


def classify(base):
    if base.startswith("pbe0_"):
        return "PBE0", base[5:]
    if base in STATE_MAP:
        return "B3LYP", STATE_MAP[base]
    if "_cp_ghost" in base:
        return "PBE0", base
    return None, base


def cell(x, fmt="%.4f"):
    return "-" if x is None else fmt % x


def rel(energy, ref):
    """energy difference in kJ/mol, or None if either number is missing"""
    if energy is None or ref is None:
        return None
    return (energy - ref) * EH


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="results")
    ap.add_argument("--csv")
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--cp", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    rows = []
    for dirpath, _dirs, files in os.walk(args.root):
        for f in sorted(files):
            if f.endswith(".out"):
                rows.append(parse_out(os.path.join(dirpath, f)))
    if not rows:
        sys.exit("no .out files under %s" % args.root)

    if not args.quiet:
        hdr = ("%-34s %-4s %-5s %-6s %-28s %16s  %s"
               % ("output", "term", "conv", "type", "imaginary modes (cm-1)",
                  "final E (Eh)", "runtime"))
        print(hdr)
        print("-" * len(hdr))
        for r in rows:
            print("%-34s %-4s %-5s %-6s %-28s %16s  %s"
                  % (r["file"][:34], "yes" if r["terminated"] else "NO",
                     "yes" if r["converged"] else "-", r["kind"],
                     (", ".join("%.2f" % x for x in r["imag"]) or "-")[:28],
                     cell(r["energy"], "%.8f"), r["runtime"]))
        print("\nrule for minima : terminated + converged + 0 imaginary modes")
        print("rule for saddles: terminated + converged + exactly 1 imaginary mode,")
        print("                  then the A4 two-sided test (tools/gen_inputs.py --displace)\n")

    # collect the best record per (level, state)
    REC, THERMO = {}, {}
    for r in rows:
        level, state = classify(r["file"][:-4])
        if level is None or r["energy"] is None:
            continue
        REC[(level, state)] = r
        if r["thermo"]:
            THERMO[(level, state)] = r["thermo"]

    def get(level, state, what):
        r = REC.get((level, state))
        if r is None:
            return None
        if what == "E":
            return r["energy"]
        if what == "imag":
            return len(r["imag"])
        th = r["thermo"]
        if not th:
            return None
        t0 = min(th)
        return th[t0].get(what)

    def getT(level, state, temp, what="G-E"):
        th = THERMO.get((level, state))
        if not th:
            return None
        for T, v in th.items():
            if abs(T - temp) < 0.01:
                return v.get(what)
        return None

    def level_table(level, zero_states, states):
        if not all((level, s) in REC for s in zero_states):
            return
        zero = sum(REC[(level, s)]["energy"] for s in zero_states)
        zpe0 = [get(level, s, "zpe") for s in zero_states]
        zpe0 = sum(zpe0) if None not in zpe0 else None
        print("  %s   zero = %s" % (level, " + ".join(LABELS[s] for s in zero_states)))
        print("  %-8s %5s %18s %9s %9s %10s %10s"
              % ("state", "imag", "E (Eh)", "dE", "dE+ZPE", "dG(298K)", "dG(1003K)"))
        for s in states:
            if (level, s) not in REC:
                print("  %-8s %5s %18s %9s %9s %10s %10s"
                      % (LABELS[s], "-", "not run", "-", "-", "-", "-"))
                continue
            e = get(level, s, "E")
            n = get(level, s, "imag")
            de = rel(e, zero)
            z = get(level, s, "zpe")
            dz = rel(z, zpe0) if (z is not None and zpe0 is not None) else None
            out = [LABELS[s], "-" if n is None else str(n), "%.8f" % e,
                   cell(de, "%.1f"), cell((de + dz) if (de is not None and dz is not None) else None, "%.1f")]
            for T in (298.15, 1003.15):
                gs = getT(level, s, T)
                g0 = [getT(level, z_, T) for z_ in zero_states]
                g0 = sum(g0) if None not in g0 else None
                out.append(cell((rel(e + gs, zero + g0) if (gs is not None and g0 is not None) else None), "%.1f"))
            print("  %-8s %5s %18s %9s %9s %10s %10s" % tuple(out))
        print()

    if args.table or not args.quiet:
        for level in ("B3LYP", "PBE0"):
            if not any(k[0] == level for k in REC):
                continue
            print("=" * 86)
            print("  LEVEL TABLE - %s / def2-TZVP   (kJ/mol relative to the reference zero)" % level)
            print("  dE = electronic only; dE+ZPE, dG(298K), dG(1003K) need FREQ data for")
            print("  every state in the row, including both reference species.")
            print("=" * 86)
            level_table(level, ["cluster", "h3vo4"], V_STATES)
            level_table(level, ["cluster", "h2o"], W_STATES)
            print("  reference: E(cluster) = %.8f Eh\n" % REC[(level, "cluster")]["energy"])

    if args.cp:
        print("=" * 86)
        print("  COUNTERPOISE - Boys-Bernardi, single geometry, PBE0-D3(BJ)/def2-TZVP")
        print("=" * 86)
        print("  All four energies must come from the same level and the same geometry:")
        print("    E(complex)              <- pbe0_<complex>            (scope 3)")
        print("    E(cluster, full basis)  <- ..._cp_ghost_frag2        (scope 2)")
        print("    E(adsorbate, full basis)<- ..._cp_ghost_frag1        (scope 2)")
        print("    E(isolated monomers)    <- pbe0_cluster, pbe0_h3vo4 / pbe0_h2o (scope 3)")
        print()
        ghost = {}
        for r in rows:
            b = r["file"][:-4]
            if "cp_ghost" not in b and "cp-ghost" not in b:
                continue
            key = "v-prc" if ("vprc" in b or "v-prc" in b) else "w-prc"
            role = "e_cluster_full" if ("frag2" in b or "ghost-cluster" in b) else "e_ads_full"
            ghost.setdefault(key, {})[role] = r["energy"]

        for cplx, ads in (("v-prc", "h3vo4"), ("w-prc", "h2o")):
            g = ghost.get(cplx, {})
            print("  " + LABELS[cplx])
            if len(g) < 2:
                print("    ghost jobs not found yet (%d of 2) - run: bash run_scope.sh 2\n"
                      % len(g))
                continue
            e_cplx = get("PBE0", cplx, "E")
            e_clu = get("PBE0", "cluster", "E")
            e_ads = get("PBE0", ads, "E")
            e_ads_full = g["e_ads_full"]
            e_clu_full = g["e_cluster_full"]
            print("    E(complex, full basis)        = %.8f Eh%s"
                  % (e_cplx, "" if e_cplx is not None else "   <- run scope 3 first"))
            print("    E(cluster, full basis)        = %.8f Eh" % e_clu_full)
            print("    E(%s, full basis)        = %.8f Eh" % (LABELS[ads], e_ads_full))
            if e_cplx is not None:
                print("    CP-corrected interaction      = %+.2f kJ/mol"
                      % ((e_cplx - e_clu_full - e_ads_full) * EH))
            if e_cplx is not None and e_clu is not None and e_ads is not None:
                print("    uncorrected interaction       = %+.2f kJ/mol"
                      % ((e_cplx - e_clu - e_ads) * EH))
                bsse = (e_clu_full + e_ads_full - e_clu - e_ads) * EH
                print("    BSSE (fragments stabilised by the partner basis) = %.2f kJ/mol"
                      % (-bsse))
                print("      -> the CP correction weakens the interaction by that amount")
            print()
        print("  The number to quote is the CP-corrected interaction energy. It is the")
        print("  standard single-geometry correction: BSSE is removed at fixed geometry,")
        print("  so the difference from the uncorrected value is the basis-set part only.")
        print("  ORCA 6.1 manual eq. 2.21 additionally separates a deformation term,")
        print("  which needs two extra monomer-geometry jobs - do that only if asked.")
        print()

    if args.csv:
        with open(args.csv, "w", newline="\n") as fh:
            fh.write("file,terminated,converged,type,imag_count,imag_cm-1,energy_Eh,runtime\n")
            for r in rows:
                fh.write("%s,%s,%s,%s,%d,\"%s\",%s,%s\n"
                         % (r["file"], r["terminated"], r["converged"], r["kind"],
                            len(r["imag"]), " ".join("%.2f" % x for x in r["imag"]),
                            "" if r["energy"] is None else "%.10f" % r["energy"],
                            r["runtime"]))
        print("csv written:", args.csv)


if __name__ == "__main__":
    main()
