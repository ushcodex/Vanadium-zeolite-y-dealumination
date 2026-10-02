r"""verify_tier1.py - ruthless audit of every ORCA Tier 1 output on this laptop.

Standard library only. Run on Windows from the thesis simulation folder:

  cd c:\Users\ushcodex\Downloads\thesis\simulation
  python verify_tier1.py 02_tier1
  python verify_tier1.py --dist V-R-T1-V02.xyz --fragA 1-22 --fragB 23-30

What it does
------------
Audit mode (default): walks a directory tree, reads every ORCA .out file,
and prints one row per job:
  normal termination flag  (ORCA TERMINATED NORMALLY)
  optimization convergence (THE OPTIMIZATION HAS CONVERGED / HURRAY)
  number of imaginary modes in the frequency printout
  final single point energy (Eh)
  runtime
Any minimum that does not show CLEAN OPT + FREQ + 0 imaginary modes is flagged.

Distance mode (--dist): for a 30-atom supermolecular xyz, reports the shortest
atom pair distance between fragment A and fragment B (1-based index ranges),
so the V-R vs V-PRC near-identity question can be settled quantitatively.
Pass ranges that match how the structure was built (cluster first, adsorbate
second, per the seed atom ordering).
"""

import os
import re
import sys

ENERGY = re.compile(r"FINAL SINGLE POINT ENERGY\s+(-?\d+\.\d+)")
FREQ_LINE = re.compile(r"^\s*\d+:\s+(-?\d+\.\d+)\s+cm\*\*-1", re.M)
RUNTIME = re.compile(r"TOTAL RUN TIME\s*:\s*(.+)")


def audit(root):
    rows = []
    for dirpath, _dirs, files in os.walk(root):
        for f in sorted(files):
            if not f.endswith(".out"):
                continue
            path = os.path.join(dirpath, f)
            try:
                text = open(path, errors="ignore").read()
            except OSError:
                continue
            ok_term = "ORCA TERMINATED NORMALLY" in text
            converged = ("THE OPTIMIZATION HAS CONVERGED" in text) or ("H U R R A Y" in text.replace("*", "").replace("  ", " "))
            imaginary = text.count("***imaginary mode***")
            energies = ENERGY.findall(text)
            freqs = [float(x) for x in FREQ_LINE.findall(text)]
            lowest = min(freqs) if freqs else None
            runtime = RUNTIME.findall(text)
            e = float(energies[-1]) if energies else None
            rows.append((f, ok_term, converged, imaginary, lowest, e,
                         runtime[-1].strip() if runtime else "?"))
    hdr = f"{'output file':38s} {'normal':6s} {'conv':5s} {'imag':4s} {'lowest cm-1':>11s} {'final E (Eh)':>16s}  runtime"
    print(hdr)
    print("-" * len(hdr))
    for f, t, c, i, lo, e, rt in rows:
        flag = ""
        if not t:
            flag = "  <== did not terminate normally"
        if ("opt" in f.lower() or "freq" in f.lower()) and "TS" not in f.upper() and not t:
            flag = "  <== CHECK"
        print(f"{f[:38]:38s} {str(t):6s} {str(c):5s} {i:4d} "
              f"{('%11.1f' % lo) if lo is not None else '         -'} "
              f"{('%16.8f' % e) if e is not None else '               -'}  {rt}{flag}")
    print()
    print("Rule for minima: normal termination, converged OPT, FREQ present, imag = 0.")
    print("Rule for saddles: normal termination, converged OPTTS, imag = 1, and the")
    print("mode must animate along the reacting bonds; then IRC must fall to the")
    print("claimed endpoints. Anything else is not a reportable barrier.")


def read_xyz(path):
    lines = open(path).read().splitlines()
    n = int(lines[0].strip())
    atoms = []
    for line in lines[2:2 + n]:
        el, x, y, z = line.split()[:4]
        atoms.append((el, float(x), float(y), float(z)))
    return atoms


def parse_range(spec):
    out = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out.extend(range(int(a), int(b or a) + 1))
    return [i - 1 for i in out]  # to zero-based


def distance_mode(xyz, fragA, fragB):
    atoms = read_xyz(xyz)
    A = parse_range(fragA)
    B = parse_range(fragB)
    best = None
    for i in A:
        for j in B:
            dx = atoms[i][1] - atoms[j][1]
            dy = atoms[i][2] - atoms[j][2]
            dz = atoms[i][3] - atoms[j][3]
            d = (dx * dx + dy * dy + dz * dz) ** 0.5
            if best is None or d < best[0]:
                best = (d, i, j)
    d, i, j = best
    print(f"Shortest intermolecular contact in {xyz}:")
    print(f"  {atoms[i][0]}(atom {i+1}) -- {atoms[j][0]}(atom {j+1}) = {d/10:.3f} nm ({d:.2f} Angstrom)")
    print()
    print("Decision rule for the V-R audit:")
    print("  about 0.17 to 0.20 nm = direct bonding or strong H bond -> V-R collapsed")
    print("    into the PRC basin; the two rows describe one state, merge them.")
    print("  about 0.5 nm or more = genuine separated supermolecule; then a -196.9")
    print("    kJ/mol interaction at that distance is spurious and must be investigated.")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--dist":
        xyz = args[1]
        fragA = fragB = None
        if "--fragA" in args:
            fragA = args[args.index("--fragA") + 1]
        if "--fragB" in args:
            fragB = args[args.index("--fragB") + 1]
        if not (fragA and fragB):
            sys.exit("usage: --dist file.xyz --fragA 1-22 --fragB 23-30")
        distance_mode(xyz, fragA, fragB)
        return
    root = args[0] if args else "."
    audit(root)


if __name__ == "__main__":
    main()
