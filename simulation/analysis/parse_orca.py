#!/usr/bin/env python3
"""Parse every ORCA output in the archive into one machine-checked register.

The repository mixes encodings (the laptop runs are UTF-16, the cloud runs are
UTF-8). The echoed input deck at the top of every ORCA log is stripped before
any status keyword is tested, otherwise strings quoted in the comments (for
example the acceptance gate text) are counted as real results.

Nothing is inferred: a field stays blank when ORCA did not print it.
"""
import csv, os, re

ROOT = "/home/user/Vanadium-zeolite-y-dealumination/simulation"
OUT = os.path.join(ROOT, "analysis", "orca_register.csv")

NUM = r"[-+]?\d*\.\d+(?:[EeDd][-+]?\d+)?"


def read(path):
    for enc in ("utf-8", "utf-16", "utf-16-le", "latin-1"):
        try:
            with open(path, "r", encoding=enc) as f:
                t = f.read()
            if "\x00" in t or len(t) < 200:
                continue
            return t
        except (UnicodeError, UnicodeDecodeError):
            continue
    return ""


def strip_input_echo(text):
    """Remove the INPUT FILE block ORCA prints at the top of the log."""
    m = re.search(r"\*{3,}END OF INPUT\*{3,}", text)
    if m:
        return text[m.end():]
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip().startswith("|") and ">" in ln:
            continue
        if i > 20 and "INPUT FILE" not in text[:len("\n".join(lines[:i]))]:
            pass
    return text


def last(pattern, text, group=1):
    v = re.findall(pattern, text)
    return v[-1] if v else ""


def parse(path):
    t = read(path)
    if not t:
        return None
    body = strip_input_echo(t)
    d = {"path": os.path.relpath(path, ROOT)}
    d["terminated"] = "yes" if "ORCA TERMINATED NORMALLY" in body else "no"
    d["converged"] = "yes" if "THE OPTIMIZATION HAS CONVERGED" in body else "no"
    d["error_term"] = "yes" if "ORCA finished by error termination" in body else "no"
    m = re.search(r"^\s*!\s*(.+)$", t, re.M)
    d["keywords"] = m.group(1).strip() if m else ""
    d["e_sp"] = last(r"FINAL SINGLE POINT ENERGY\s+(" + NUM + r")", t)
    d["natoms"] = last(r"Number of atoms\s*\.*\s*(\d+)", body)
    d["nbasis"] = last(r"Number of basis functions\s*\.*\s*(\d+)", body)
    # optimisation progress
    d["opt_cycles"] = len(re.findall(r"GEOMETRY OPTIMIZATION CYCLE\s+(\d+)", body))
    d["rms_grad"] = last(r"RMS gradient\s*\.*\s*(" + NUM + r")", body)
    # vibrational analysis: a log can hold several frequency blocks (the first
    # is often a restart checkpoint), so only the last one is reported.
    blocks = body.split("VIBRATIONAL FREQUENCIES")
    vib = blocks[-1] if len(blocks) > 1 else ""
    nfr = re.findall(r"Number of frequencies\s*\.*\s*(\d+)", body)
    d["nfreq"] = nfr[-1] if nfr else ""
    d["n_freq_blocks"] = len(blocks) - 1
    d["has_freq"] = "yes" if vib else "no"
    d["zpe"] = last(r"Zero point energy\s*\.*\s*(" + NUM + r")\s*Eh", vib)
    g = re.findall(r"G-E\(el\)\s*\.*\s*(" + NUM + r")\s*Eh", vib)
    d["g298_corr"] = g[0] if len(g) > 0 else ""
    d["g1003_corr"] = g[1] if len(g) > 1 else ""
    h = re.findall(r"Thermal Enthalpy correction\s*\.*\s*(" + NUM + r")\s*Eh", vib)
    d["h298_corr"] = h[0] if len(h) > 0 else ""
    d["h1003_corr"] = h[1] if len(h) > 1 else ""
    gf = re.findall(r"Final Gibbs free energy\s*\.*\s*(" + NUM + r")\s*Eh", vib)
    d["g298_abs"] = gf[0] if len(gf) > 0 else ""
    d["g1003_abs"] = gf[1] if len(gf) > 1 else ""
    im = re.findall(r"(" + NUM + r")\s*cm\*\*-1\s*\*{3}imaginary mode\*{3}", vib)
    d["n_imag"] = len(im)
    d["imag_cm"] = " ".join(im[:20])
    m = re.search(r"TOTAL RUN TIME[^:]*:\s*(\d+)\s*days\s*(\d+)\s*hours\s*(\d+)\s*minutes", body)
    d["hours"] = round(int(m.group(1)) * 24 + int(m.group(2)) + int(m.group(3)) / 60, 2) if m else ""
    d["orca_version"] = (re.search(r"Program Version (\S+)", t) or [None, ""])[1] if re.search(r"Program Version (\S+)", t) else ""
    return d


rows = []
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ("images", "text")]
    for fn in files:
        if fn.endswith(".out"):
            r = parse(os.path.join(base, fn))
            if r and r["e_sp"]:
                rows.append(r)

rows.sort(key=lambda r: r["path"])
cols = ["path", "natoms", "nbasis", "keywords", "orca_version", "terminated", "converged",
        "error_term", "opt_cycles", "rms_grad", "has_freq", "n_freq_blocks", "n_imag", "imag_cm",
        "e_sp", "zpe", "h298_corr", "h1003_corr", "g298_corr", "g1003_corr", "g298_abs", "g1003_abs", "hours"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("parsed", len(rows), "ORCA jobs ->", OUT)
