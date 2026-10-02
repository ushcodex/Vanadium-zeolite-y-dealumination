#!/usr/bin/env python3
"""gen_inputs.py - input generators for the Tier 2 / Tier 3 completion package.

Standard library only.  Run from the package root:

  python3 tools/gen_inputs.py --scope3
        Build PBE0-D3(BJ)/def2-TZVP single points for every relaxed geometry in
        results/geom/ (written by run_scope.sh after a successful Opt/OptTS).
        Output: jobs/scope3/pbe0_<state>.inp      Run them with: bash run_scope.sh 3

  python3 tools/gen_inputs.py --ghost-xyz
        FALLBACK for scope 2.  If ORCA refuses the %frag / GhostFrags route, this
        writes the same two calculations using the manual ghost-atom notation
        ("O :" in the coordinate list) which needs no special keywords.
        Output: xyz/relaxed/<cmplx>_ghost-<fragment>.xyz
                jobs/scope2_fallback/*.inp

  python3 tools/gen_inputs.py --displace RESULTS/out.out --geom results/geom/v-ts2.xyz \\
                              --tag v-ts2 [--mode 6] [--step 0.10]
        A4 test generator: reads the NORMAL MODES table of a finished frequency
        job, takes one mode (default: the imaginary one), and writes the two
        structures displaced +-step along it, with ready OPT inputs.
        --step is applied to the largest moving atom by default (--scale maxatom);
        use --scale norm to displace the whole 3N vector by that length instead.
        Output: results/diagnostics/<tag>_mode<N>_{plus,minus}.xyz
                jobs/diagnostics/<tag>_mode<N>_{plus,minus}_opt.inp
"""

import argparse
import os
import re
import sys

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASS = {"H": 1.008, "O": 15.999, "Si": 28.085, "Al": 26.982, "V": 50.942}
B3 = "! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF DefGrid3"
PBE = "! PBE0 D3BJ def2-TZVP RIJCOSX def2/J TightSCF DefGrid3"

# states that belong in scope 3 and the order they are reported in
ORDER = ["cluster", "h2o", "h3vo4", "v-prc", "w-prc", "v-i1", "v-i2", "v-p", "w-p",
         "v-ts2", "w-ts", "v-ts3", "v-ts1"]


def read_text(path):
    raw = open(path, "rb").read()
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16", errors="ignore")
    return raw.decode("utf-8", errors="ignore")


def read_xyz(path):
    lines = read_text(path).splitlines()
    n = int(lines[0].split()[0])
    atoms = []
    for line in lines[2:2 + n]:
        p = line.split()
        atoms.append((p[0], float(p[1]), float(p[2]), float(p[3])))
    return atoms


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="\n") as fh:
        fh.write(text)
    print("  wrote", os.path.relpath(path, PKG))


def block_kw(kind):
    """kind: 'freq' for a Hessian job, 'opt' for an optimisation"""
    return B3 + (" Opt TightOpt" if kind == "opt" else "")


# --------------------------------------------------------------------------
def scope3():
    geom_dir = os.path.join(PKG, "results", "geom")
    if not os.path.isdir(geom_dir):
        sys.exit("results/geom/ does not exist yet - run scope 1 and scope 4 first.")
    allxyz = [f[:-4] for f in os.listdir(geom_dir) if f.endswith(".xyz")]
    found = [s for s in allxyz if s in ORDER]
    unknown = [s for s in allxyz if s not in ORDER]
    if not found:
        sys.exit("results/geom/ holds no recognised state geometry yet "
                 "- run scope 1 and scope 4 first.")
    found.sort(key=ORDER.index)
    missing = [s for s in ORDER if s not in found]
    if unknown:
        print("  ignoring unrecognised files in results/geom/:", ", ".join(sorted(unknown)))
    for state in found:
        txt = (
            "# SCOPE 3  |  final-level single point on a RELAXED geometry\n"
            "# State: %s  |  register row: %s-PBE0<T2>\n"
            "# Why: second functional on the SAME relaxed geometry, so the B3LYP and PBE0\n"
            "#      columns of the level table differ only by the functional, not by the\n"
            "#      geometry. This is the cross-check that the old 24-slot single-point set\n"
            "#      could not provide (it used unrelaxed TIER 1 shapes).\n"
            "# Gate: TERMINATED NORMALLY and an SCF energy; no frequency is needed here.\n\n"
            % (state, state)
            + PBE + "\n\n%pal nprocs 4 end\n%maxcore 3000\n\n%scf\n  MaxIter 300\nend\n\n"
            + "* xyzfile 0 1 results/geom/%s.xyz\n" % state
        )
        write(os.path.join(PKG, "jobs", "scope3", "pbe0_%s.inp" % state), txt)
    print("\n  %d scope-3 input(s) written." % len(found))
    if missing:
        print("  not yet available (still to be relaxed):", ", ".join(missing))
    print("  run them with:  bash run_scope.sh 3")


# --------------------------------------------------------------------------
def ghost_xyz():
    """Fallback counterpoise route: 'X :' ghost atoms, no %frag block."""
    pairs = [("v-prc", 22, "h3vo4"), ("w-prc", 22, "h2o")]
    for state, nfrag1, frag2name in pairs:
        src = os.path.join(PKG, "xyz", "relaxed", "%s.xyz" % state)
        if not os.path.isfile(src):
            src = os.path.join(PKG, "xyz", "%s.xyz" % state)
        atoms = read_xyz(src)
        n = len(atoms)
        comment = "geometry for the %s counterpoise fallback" % state
        for ghost_frag, tag in ((1, "cluster"), (2, frag2name)):
            out = [str(n), "%s | ghosted fragment: %s" % (comment, tag)]
            for i, (el, x, y, z) in enumerate(atoms):
                in_frag1 = i < nfrag1
                ghost = (ghost_frag == 1 and in_frag1) or (ghost_frag == 2 and not in_frag1)
                out.append("  %-3s%s %18.10f %18.10f %18.10f"
                           % (el, " :" if ghost else "  ", x, y, z))
            xyz_path = os.path.join(PKG, "xyz", "relaxed",
                                    "%s_ghost-%s.xyz" % (state, tag))
            write(xyz_path, "\n".join(out) + "\n")
            txt = (
                "# SCOPE 2 FALLBACK  |  counterpoise via manual ghost atoms\n"
                "# Use only if ORCA rejects %%frag / GhostFrags. The ghosted fragment carries\n"
                "# basis functions but no electrons or nuclei (ORCA manual, Dummy/ghost atoms).\n"
                "# Everything else (level, geometry, interpretation) is identical to\n"
                "# jobs/scope2/%s_cp_ghost_%s.inp\n\n"
                % ("s2_01_vprc" if state == "v-prc" else "s2_02_wprc",
                   "cluster" if ghost_frag == 2 else frag2name)
                + PBE + "\n\n%pal nprocs 4 end\n%maxcore 3000\n\n%scf\n  MaxIter 300\nend\n\n"
                + "* xyzfile 0 1 xyz/relaxed/%s_ghost-%s.xyz\n" % (state, tag)
            )
            write(os.path.join(PKG, "jobs", "scope2_fallback",
                               "%s_cp_ghost-%s.inp" % (state, tag)), txt)


# --------------------------------------------------------------------------
def last_block(text, marker):
    """Index of the LAST occurrence of marker (OptTS outputs contain two blocks:
    the initial Calc_Hess one and the final FREQ one - always use the final)."""
    i = text.rfind(marker)
    if i < 0:
        sys.exit("no %r block in this output - was FREQ requested?" % marker)
    return i


def parse_normal_modes(text):
    """Return {mode_index: [3N floats]} from the LAST NORMAL MODES table."""
    i = last_block(text, "NORMAL MODES")
    lines = text[i:].splitlines()[1:]
    modes, current, vecs = [], None, {}
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if "IR SPECTRUM" in s or "THERMOCHEMISTRY" in s or "VIBRATIONAL" in s and not s[0].isdigit():
            break
        toks = s.split()
        if all(re.fullmatch(r"\d+", t) for t in toks) and "." not in s:
            current = [int(t) for t in toks]
            for m in current:
                vecs.setdefault(m, [])
            modes.extend(current)
            continue
        if current is None:
            continue
        try:
            row = int(toks[0])
            vals = [float(v) for v in toks[1:]]
        except ValueError:
            continue
        if len(vals) != len(current):
            continue
        for k, m in enumerate(current):
            vecs[m].append(vals[k])
    if not vecs:
        sys.exit("could not parse the NORMAL MODES table")
    return vecs


def imaginary_modes(text):
    """Imaginary modes of the LAST vibrational block (see last_block note)."""
    start = last_block(text, "VIBRATIONAL FREQUENCIES")
    end = text.find("NORMAL MODES", start)
    seg = text[start:end if end > 0 else len(text)]
    out = []
    for line in seg.splitlines():
        if "***imaginary mode***" in line:
            m = re.match(r"\s*(\d+):\s+(-?\d+\.\d+)", line)
            if m:
                out.append((int(m.group(1)), float(m.group(2))))
    return out


def displace(args):
    text = read_text(args.disp_out)
    vecs = parse_normal_modes(text)
    if args.mode is None:
        im = imaginary_modes(text)
        if not im:
            sys.exit("no imaginary mode found; pass --mode explicitly if you meant a real one.")
        mode = im[0][0]
        print("  imaginary modes found:", im)
    else:
        mode = args.mode
    if mode not in vecs or len(vecs[mode]) % 3:
        sys.exit("mode %s not found (available: %s)" % (mode, sorted(vecs)))
    v = vecs[mode]
    atoms = read_xyz(args.geom)
    if len(atoms) * 3 != len(v):
        sys.exit("mode has %d components but %s has %d atoms"
                 % (len(v), args.geom, len(atoms)))

    # ORCA prints mass-weighted vectors: undo the weighting to get Cartesian directions
    cart = []
    for i, (el, *_rest) in enumerate(atoms):
        m = MASS.get(el, 1.0)
        cart.extend([v[3 * i + c] / (m ** 0.5) for c in range(3)])
    norm = sum(x * x for x in cart) ** 0.5
    cart = [x / norm for x in cart]
    if args.scale == "maxatom":
        biggest = max((cart[3 * i] ** 2 + cart[3 * i + 1] ** 2
                       + cart[3 * i + 2] ** 2) ** 0.5 for i in range(len(atoms)))
        scale, how = args.step / biggest, "largest single-atom displacement"
    else:
        scale, how = args.step, "overall vector norm"
    cart = [x * scale for x in cart]
    print("  mode %d: %d components; %s set to %.3f Angstrom"
          % (mode, len(v), how, args.step))
    print("     (moving atoms: %s)"
          % ", ".join(sorted({atoms[i][0] + str(i + 1) for i in range(len(atoms))
                              if (cart[3 * i] ** 2 + cart[3 * i + 1] ** 2
                                  + cart[3 * i + 2] ** 2) ** 0.5 > 0.2 * args.step})))

    base = args.tag or os.path.splitext(os.path.basename(args.disp_out))[0]
    for sign, word in ((1, "plus"), (-1, "minus")):
        out = [str(len(atoms)),
               "%s | mode %d | displacement %+0.3f A along the mode (A4 test)"
               % (base, mode, sign * args.step)]
        for i, (el, x, y, z) in enumerate(atoms):
            out.append("  %-3s %18.10f %18.10f %18.10f"
                       % (el, x + sign * cart[3 * i],
                          y + sign * cart[3 * i + 1],
                          z + sign * cart[3 * i + 2]))
        xyz_path = os.path.join(PKG, "results", "diagnostics",
                                "%s_mode%d_%s.xyz" % (base, mode, word))
        write(xyz_path, "\n".join(out) + "\n")

        txt = (
            "# A4 TWO-SIDED TEST  |  %s, mode %d, %s displacement\n"
            "# Purpose: prove which two minima the saddle at %s actually connects.\n"
            "# Expected: one direction relaxes to the state BEFORE the step, the other to\n"
            "#      the state AFTER it, each within ~5 kJ/mol of the accepted minimum\n"
            "#      (use the B3LYP energies from the scope 4 outputs).\n"
            "# If either direction lands somewhere else, the saddle is NOT the saddle of\n"
            "#      that step and the barrier must not be reported as verified.\n\n"
            % (base, mode, word, base)
            + B3 + " Opt TightOpt\n\n%pal nprocs 4 end\n%maxcore 3000\n\n"
            + "%scf\n  MaxIter 300\nend\n\n%geom\n  MaxIter 200\nend\n\n"
            + "* xyzfile 0 1 results/diagnostics/%s_mode%d_%s.xyz\n"
            % (base, mode, word)
        )
        write(os.path.join(PKG, "jobs", "diagnostics",
                           "%s_mode%d_%s_opt.inp" % (base, mode, word)), txt)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--scope3", action="store_true")
    g.add_argument("--ghost-xyz", action="store_true")
    g.add_argument("--displace", action="store_true")
    ap.add_argument("--disp-out", help="finished ORCA .out of the frequency job")
    ap.add_argument("--geom", help="relaxed geometry .xyz of the same structure")
    ap.add_argument("--tag", help="label for the outputs (e.g. v-ts2)")
    ap.add_argument("--mode", type=int, default=None, help="mode index (default: imaginary)")
    ap.add_argument("--step", type=float, default=0.10, help="displacement in Angstrom")
    ap.add_argument("--scale", choices=["maxatom", "norm"], default="maxatom",
                    help="what --step refers to (default: the largest moving atom)")
    args = ap.parse_args()
    if args.displace and not (args.disp_out and args.geom):
        ap.error("--displace needs --disp-out and --geom")
    if args.scope3:
        scope3()
    elif args.ghost_xyz:
        ghost_xyz()
    else:
        displace(args)


if __name__ == "__main__":
    main()
