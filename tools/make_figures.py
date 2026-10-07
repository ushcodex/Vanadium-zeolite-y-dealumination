#!/usr/bin/env python3
"""
make_figures.py

Draws every "own work" figure in the thesis with matplotlib, reading the numbers
straight out of writing/markdown/_results.json (produced by
tools/build_results_table.py, which in turn reads the ORCA .out files).

No figure in this thesis was produced by an image generator.  Every curve and
bar below traces back to a number in the repository, and the molecular pictures
are rendered from the optimised Cartesian coordinates in
simulation/03_tier2_completion/results/geom/.

Run:  python3 tools/make_figures.py
"""

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "figures")
GEOM = os.path.join(ROOT, "simulation", "03_tier2_completion", "results", "geom")
DATA = os.path.join(ROOT, "writing", "markdown", "_results.json")

os.makedirs(FIG, exist_ok=True)
with open(DATA, encoding="utf-8") as f:
    R = json.load(f)

# ---------------------------------------------------------------- styling
plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 11,
    "axes.linewidth": 1.0,
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#111111",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

C = {
    "V": "#B3312C",      # vanadic acid route
    "W": "#1F5C99",      # steam route
    "V2": "#E08B86",
    "W2": "#8FB6DC",
    "grey": "#6B6B6B",
    "light": "#D9D9D9",
    "ok": "#2E7D32",
    "bad": "#C62828",
    "warn": "#EF8C00",
}

ACCEPTED = ["V-PRC", "V-I1", "W-PRC", "W-P"]
NOT_ACCEPTED = ["V-TS2", "V-I2", "V-P"]


def save(fig, name):
    p = os.path.join(FIG, name)
    fig.savefig(p)
    plt.close(fig)
    print("  wrote", name)


# ================================================================ molecules
COV = {"H": 0.31, "O": 0.66, "Al": 1.21, "Si": 1.11, "V": 1.53}
COL = {"H": "#E8E8E8", "O": "#D94F4F", "Al": "#7FA8D9",
       "Si": "#C9A227", "V": "#5B8C5A"}
RAD = {"H": 0.30, "O": 0.42, "Al": 0.60, "Si": 0.62, "V": 0.68}


def read_xyz(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    n = int(lines[0].split()[0])
    atoms = []
    for ln in lines[2:2 + n]:
        p = ln.split()
        if len(p) < 4:
            break
        atoms.append((p[0], float(p[1]), float(p[2]), float(p[3])))
    return atoms


def bonds(atoms, tol=1.28):
    b = []
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            ai, aj = atoms[i][0], atoms[j][0]
            if ai == "H" and aj == "H":
                continue
            d = np.linalg.norm(np.array(atoms[i][1:]) - np.array(atoms[j][1:]))
            if d < (COV[ai] + COV[aj]) * tol:
                b.append((i, j, d))
    return b


def sphere(ax, c, r, col, alpha=1.0, n=14):
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    x = c[0] + r * np.outer(np.cos(u), np.sin(v))
    y = c[1] + r * np.outer(np.sin(u), np.sin(v))
    z = c[2] + r * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color=col, alpha=alpha, linewidth=0,
                    antialiased=True, shade=True)


def draw_mol(ax, atoms, scale=1.0, hbond=None, title=""):
    pts = np.array([a[1:] for a in atoms])
    ctr = pts.mean(axis=0)
    pts = (pts - ctr) * scale
    bs = bonds(atoms)
    for i, j, d in bs:
        p, q = pts[i], pts[j]
        ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]],
                color="#8A8A8A", linewidth=2.4, solid_capstyle="round", zorder=1)
    if hbond:
        for i, j in hbond:
            p, q = pts[i], pts[j]
            ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]],
                    color="#2E7D32", linewidth=1.4, linestyle=(0, (5, 3)), zorder=1)
    for k, a in enumerate(atoms):
        sphere(ax, pts[k], RAD[a[0]] * scale, COL.get(a[0], "#999999"))
    # equal aspect
    rng = np.abs(pts).max() + 1.0
    for s, lim in (("x", 0), ("y", 1), ("z", 2)):
        getattr(ax, "set_%slim" % s)(-rng, rng)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    ax.view_init(elev=18, azim=-58)
    if title:
        ax.set_title(title, fontsize=11, pad=2)


def figure_models():
    fig = plt.figure(figsize=(9.4, 3.5))
    specs = [("cluster.xyz", "Zeolite Y cluster\nAlSi$_4$O$_4$H$_{13}$"),
             ("h3vo4.xyz", "Vanadic acid\nH$_3$VO$_4$"),
             ("h2o.xyz", "Water\nH$_2$O")]
    for k, (fn, ttl) in enumerate(specs):
        ax = fig.add_subplot(1, 3, k + 1, projection="3d")
        atoms = read_xyz(os.path.join(GEOM, fn))
        draw_mol(ax, atoms, scale=1.0 if k else 0.85, title=ttl)
    fig.suptitle("Reference species optimised at B3LYP-D3(BJ)/def2-TZVP",
                 fontsize=11, y=0.99)
    fig.tight_layout()
    save(fig, "fig3_2_cluster.png")

    # adsorbed complexes
    fig = plt.figure(figsize=(9.4, 4.0))
    for k, (fn, ttl) in enumerate([("v-prc.xyz", "V-PRC: H$_3$VO$_4$ on the acid site"),
                                   ("w-prc.xyz", "W-PRC: H$_2$O on the acid site")]):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        atoms = read_xyz(os.path.join(GEOM, fn))
        draw_mol(ax, atoms, scale=0.72, title=ttl)
    fig.suptitle("Pre-reaction complexes (B3LYP-D3(BJ)/def2-TZVP optimised geometries)",
                 fontsize=11, y=0.99)
    fig.tight_layout()
    save(fig, "fig4_1_complexes.png")


# ================================================================ Chapter 2
def figure_dispute():
    """The three competing explanations for Y destruction, side by side."""
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 52)
    ax.axis("off")

    cols = [(1.5, 33.5, C["W2"], "A. Steam-only hydrolysis",
             "Framework Al-O bonds are hydrolysed\nby steam alone. Vanadium is a\nspectator or a minor accelerant.",
             "Malola et al. (2012);\nSilaghi et al. (2016)"),
            (35.0, 65.0, C["V2"], "B. Vanadic acid catalysis",
             "V2O5 + steam gives volatile H3VO4,\na strong acid that catalyses the\nhydrolysis of framework Al.",
             "Wormsbecher et al. (1986);\nTrujillo et al. (1997)"),
            (66.5, 98.5, "#E6C79C", "C. Sodium / NaOH route",
             "Steam plus Na gives a surface\nNa+OH- that attacks Si-O.\nVanadium only releases the Na.",
             "Pine (1990);\nXu, Liu and Madon (2002)")]

    for x0, x1, col, head, body, cite in cols:
        ax.add_patch(FancyBboxPatch((x0, 6), x1 - x0, 34, boxstyle="round,pad=0.4",
                                    facecolor=col, edgecolor="#444444",
                                    linewidth=1.0, alpha=0.85))
        ax.text((x0 + x1) / 2, 36.2, head, ha="center", va="center",
                fontsize=11.5, fontweight="bold")
        ax.text((x0 + x1) / 2, 25.5, body, ha="center", va="center", fontsize=9.6,
                linespacing=1.5)
        ax.text((x0 + x1) / 2, 10.2, cite, ha="center", va="center",
                fontsize=9, style="italic", color="#333333")

    ax.text(50, 47.5, "The unresolved question this project tests:\n"
                      "does H$_3$VO$_4$ bind the Bronsted acid site strongly enough\nto matter against 20 vol% steam?",
            ha="center", va="center", fontsize=11.5, fontweight="bold")
    ax.annotate("", xy=(50, 42.5), xytext=(50, 46.0),
                arrowprops=dict(arrowstyle="->", lw=1.4, color="#333333"))
    ax.text(50, 1.6, "Figure compiled by the author from the cited sources",
            ha="center", fontsize=8.5, style="italic", color="#666666")
    fig.tight_layout()
    save(fig, "fig2_1_dispute.png")


# ================================================================ Chapter 3
def figure_workflow():
    fig, ax = plt.subplots(figsize=(9.0, 6.4))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    def box(x, y, w, h, txt, fc, fs=9.6, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5",
                                    facecolor=fc, edgecolor="#333333", linewidth=1.1))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center",
                fontsize=fs, fontweight="bold" if bold else "normal",
                linespacing=1.45)

    def arrow(x1, y1, x2, y2, label=""):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=14, linewidth=1.3,
                                     color="#333333"))
        if label:
            ax.text((x1 + x2) / 2 + 1.5, (y1 + y2) / 2, label, fontsize=8.6,
                    color="#333333")

    ax.text(50, 96, "Two-tier computational workflow", ha="center",
            fontsize=12.5, fontweight="bold")

    box(6, 78, 40, 12, "Build the 4T cluster\nAlSi$_4$O$_4$H$_{13}$ and the\n"
                       "adsorbates H$_3$VO$_4$, H$_2$O", "#EDEDED", bold=True)
    box(56, 78, 38, 12, "Spartan / Avogadro for\nediting; XYZ files carry the\n"
                        "atom order into ORCA", "#F7F7F7")

    ax.add_patch(Rectangle((3, 40), 88, 33, facecolor="#FBF3F3",
                           edgecolor=C["V"], linewidth=1.4, ls="--"))
    ax.text(5, 70.5, "TIER 1  -  Dell Latitude E6430, 16 GB RAM, SSD, ORCA 6.1, 1 core",
            fontsize=9.4, fontweight="bold", color=C["V"])
    box(6, 43, 25, 22, "GFN2-xTB\noptimisations\nof reactants,\ncomplexes",
        "#F5D8D6")
    box(34, 43, 25, 22, "Nudged elastic\nband scans for\ncandidate\nsaddles",
        "#F5D8D6")
    box(62, 43, 26, 22, "OptTS + mode\ndisplacement\ntests (A1-A5\nrules)",
        "#F5D8D6")
    arrow(31, 54, 34, 54)
    arrow(59, 54, 62, 54)

    arrow(47, 40, 47, 35, "accepted geometries")

    ax.add_patch(Rectangle((3, 2), 88, 31, facecolor="#EEF3FA",
                           edgecolor=C["W"], linewidth=1.4, ls="--"))
    ax.text(5, 30.0, "TIER 2  -  cloud virtual machine, ORCA 6.1, 4 MPI ranks",
            fontsize=9.4, fontweight="bold", color=C["W"])
    box(6, 5, 25, 20, "B3LYP-D3(BJ)\ndef2-TZVP\nopt + frequency",
        "#D8E4F2")
    box(34, 5, 25, 20, "PBE0-D3(BJ)\ndef2-TZVP\nsingle points",
        "#D8E4F2")
    box(62, 5, 26, 20, "Thermochemistry\n298.15 K and\n1003.15 K",
        "#D8E4F2")
    arrow(31, 15, 34, 15)
    arrow(59, 15, 62, 15)
    fig.tight_layout()
    save(fig, "fig3_1_workflow.png")


# ================================================================ Chapter 4
def figure_energy_profile():
    b3 = R["levels"]["B3LYP"]
    fig, ax = plt.subplots(figsize=(9.2, 5.0))

    # vanadium route
    xs = [0, 1, 2, 3, 4, 5]
    labs = ["Reactants\nclusters + H$_3$VO$_4$", "V-PRC", "V-I1",
            "V-TS2\n(not accepted)", "V-I2\n(not accepted)", "V-P\n(not accepted)"]
    ys = [0.0, b3["V-PRC"]["dE"], b3["V-I1"]["dE"], b3["V-TS2"]["dE"],
          b3["V-I2"]["dE"], b3["V-P"]["dE"]]
    acc = [True, True, True, False, False, False]

    ax.plot(xs[:3], ys[:3], "-o", color=C["V"], lw=2.2, ms=8, zorder=3)
    ax.plot(xs[2:6], ys[2:6], "--o", color=C["V"], lw=1.6, ms=8, mfc="white",
            zorder=3, alpha=0.85)
    for i, (x, y, a) in enumerate(zip(xs, ys, acc)):
        ax.annotate("%+.1f" % y, (x, y), textcoords="offset points",
                    xytext=(0, 11 if y > 0 else -17), ha="center",
                    fontsize=9.5, color=C["V"], fontweight="bold")

    # steam route, drawn on the same axis using an offset baseline label
    xs2 = [0, 1.0]
    ys2 = [0.0, b3["W-PRC"]["dE"]]
    ax.plot([0, 1, 2.0], [0.0, b3["W-PRC"]["dE"], b3["W-P"]["dE"]], "-s",
            color=C["W"], lw=2.2, ms=7, zorder=3)
    ax.annotate("%+.1f" % b3["W-PRC"]["dE"], (1, b3["W-PRC"]["dE"]),
                textcoords="offset points", xytext=(0, -17), ha="center",
                fontsize=9.5, color=C["W"], fontweight="bold")
    ax.annotate("%+.1f" % b3["W-P"]["dE"], (2.0, b3["W-P"]["dE"]),
                textcoords="offset points", xytext=(0, 11), ha="center",
                fontsize=9.5, color=C["W"], fontweight="bold")

    ax.axhline(0, color="#999999", lw=1.0)
    ax.set_xticks(xs)
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Relative electronic energy, $\\Delta E$ (kJ mol$^{-1}$)")
    ax.set_title("Stationary points at B3LYP-D3(BJ)/def2-TZVP, relative to the "
                 "separated reactants", fontsize=10.5)
    ax.grid(axis="y", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)

    handles = [plt.Line2D([], [], color=C["V"], lw=2.2, marker="o",
                          label="Vanadic acid route (H$_3$VO$_4$)"),
               plt.Line2D([], [], color=C["W"], lw=2.2, marker="s",
                          label="Steam route (H$_2$O)"),
               plt.Line2D([], [], color="#555555", lw=1.6, ls="--", marker="o",
                          mfc="white", label="Not accepted: geometry failed the "
                                             "stationary-point tests")]
    ax.legend(handles=handles, loc="upper left", fontsize=9, framealpha=0.95)
    ax.text(0.02, 0.03, "V-P and W-P use different reference zeros; the two routes "
                        "are not on a common scale.",
            transform=ax.transAxes, fontsize=8.2, style="italic", color="#555555")
    fig.tight_layout()
    save(fig, "fig4_2_energy_profile.png")


def figure_adsorption():
    b3, pbe = R["levels"]["B3LYP"], R["levels"]["PBE0"]
    t1 = R["tier1_reference"]["accepted"]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.9))

    # panel a: three levels of theory
    ax = axes[0]
    labels = ["GFN2-xTB\n(Tier 1)", "B3LYP-D3(BJ)\n(Tier 2)", "PBE0-D3(BJ)\n(single point)"]
    v = [t1["V-PRC"], b3["V-PRC"]["dE"], pbe["V-PRC"]["dE"]]
    w = [t1["W-PRC"], b3["W-PRC"]["dE"], pbe["W-PRC"]["dE"]]
    x = np.arange(3)
    ax.bar(x - 0.19, v, 0.38, color=C["V"], label="H$_3$VO$_4$")
    ax.bar(x + 0.19, w, 0.38, color=C["W"], label="H$_2$O")
    for xi, vv in zip(x - 0.19, v):
        ax.text(xi, vv - 8, "%0.1f" % vv, ha="center", fontsize=9, color="white",
                fontweight="bold")
    for xi, ww in zip(x + 0.19, w):
        ax.text(xi, ww - 8, "%0.1f" % ww, ha="center", fontsize=9, color="white",
                fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.8)
    ax.set_ylabel("Adsorption energy, $\\Delta E$ (kJ mol$^{-1}$)")
    ax.set_title("(a) Adsorption at three levels of theory", fontsize=10.5)
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)

    # panel b: the margin between the two adsorbates
    ax = axes[1]
    marg = [t1["V-PRC"] - t1["W-PRC"],
            b3["V-PRC"]["dE"] - b3["W-PRC"]["dE"],
            pbe["V-PRC"]["dE"] - pbe["W-PRC"]["dE"]]
    bars = ax.bar(x, marg, 0.45, color=["#B0B0B0", C["V"], "#7A9E7A"])
    for xi, m in zip(x, marg):
        ax.text(xi, m - 6, "%0.1f" % m, ha="center", fontsize=9.5, color="white",
                fontweight="bold")
    kt = 8.314 * 1003.15 / 1000.0
    ax.axhline(-kt, color=C["warn"], ls=":", lw=1.4)
    ax.text(2.42, -kt + 3, "$k_BT$ at 1003 K = %.1f kJ mol$^{-1}$" % kt,
            fontsize=8.4, color=C["warn"], ha="right")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.8)
    ax.set_ylabel("$\\Delta\\Delta E$ (H$_3$VO$_4$ minus H$_2$O), kJ mol$^{-1}$")
    ax.set_title("(b) How much stronger does vanadic acid bind?", fontsize=10.5)
    ax.grid(axis="y", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig4_3_adsorption.png")


def figure_gibbs():
    b3 = R["levels"]["B3LYP"]
    labels = ["V-PRC", "V-I1", "W-PRC", "W-P"]
    g298 = [b3[k]["dG_298.15"] for k in labels]
    g1003 = [b3[k]["dG_1003.15"] for k in labels]
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(8.4, 4.1))
    ax.bar(x - 0.19, g298, 0.38, color=C["W2"], label="298.15 K (25 $^\\circ$C)")
    ax.bar(x + 0.19, g1003, 0.38, color=C["V2"], label="1003.15 K (730 $^\\circ$C)")
    for xi, a in zip(x - 0.19, g298):
        ax.text(xi, a + (5 if a > 0 else -12), "%+.1f" % a, ha="center",
                fontsize=9, fontweight="bold", color=C["W"])
    for xi, a in zip(x + 0.19, g1003):
        ax.text(xi, a + 5, "%+.1f" % a, ha="center", fontsize=9,
                fontweight="bold", color=C["V"])
    ax.axhline(0, color="#444444", lw=1.1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Gibbs free energy relative to separated\\nreactants, "
                  "$\\Delta G$ (kJ mol$^{-1}$)")
    ax.set_title("Thermochemistry of the accepted minima at "
                 "B3LYP-D3(BJ)/def2-TZVP", fontsize=10.5)
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig4_4_gibbs.png")


def figure_imag():
    im = R["levels"]["B3LYP"]["V-TS2"]["imag"]
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    y = np.arange(len(im))
    ax.barh(y, im, color=[C["bad"] if abs(v) > 50 else C["warn"] for v in im])
    ax.set_yticks(y)
    ax.set_yticklabels(["%d" % (i + 7) for i in range(len(im))], fontsize=8)
    ax.set_xlabel("Imaginary frequency (cm$^{-1}$)")
    ax.set_ylabel("Vibrational mode number")
    ax.set_title("V-TS2 carries %d imaginary modes; a true first-order saddle "
                 "carries exactly one" % len(im), fontsize=10.5)
    ax.grid(axis="x", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig4_5_imaginary.png")


def figure_competition():
    """Langmuir two-site competition between steam and vanadic acid."""
    b3 = R["levels"]["B3LYP"]
    ddE = b3["V-PRC"]["dE"] - b3["W-PRC"]["dE"]          # kJ/mol, negative
    Rg = 8.314e-3                                         # kJ/mol/K
    T = np.array([1003.15])
    K = np.exp(-ddE / (Rg * T))[0]                        # > 1, favours H3VO4
    pW = 0.20 * 2.0                                       # atm, 20% steam at 2 atm
    ppm = np.logspace(-3, 3, 400)                         # ppm(v) H3VO4
    pV = ppm * 1e-6 * 2.0
    theta = K * pV / (pW + K * pV)                        # fraction of sites
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    ax.semilogx(ppm, theta * 100, color=C["V"], lw=2.2)
    for xv, lab, col in ((1.7, "Trujillo et al. (1997)\n1.7 ppm", "#444444"),
                         (10.0, "Wormsbecher et al. (1986)\n1-10 ppm", C["W"])):
        ax.axvline(xv, color=col, ls="--", lw=1.3)
        ax.annotate(lab, (xv, 0.55), fontsize=8.6, color=col,
                    rotation=90, va="bottom", ha="right")
    ax.annotate("at 10 ppm: %.3f%% of sites" % (np.interp(10, ppm, theta * 100)),
                (10, np.interp(10, ppm, theta * 100)),
                textcoords="offset points", xytext=(-140, 40), fontsize=9.5,
                color=C["V"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=C["V"], lw=1.2))
    ax.set_xlabel("Vanadic acid in the regenerator gas (ppm by volume)")
    ax.set_ylabel("Brønsted sites held by H$_3$VO$_4$ (%)")
    ax.set_title("Two-site Langmuir competition at 1003 K, 20 vol%% steam, 2 atm\n"
                 "(binding-constant ratio $K_V/K_W$ = %.1f from this work)" % K,
                 fontsize=10)
    ax.grid(alpha=0.28, lw=0.7)
    ax.set_ylim(0, 1.0)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig4_6_competition.png")


def figure_method_gap():
    t1 = R["tier1_reference"]["accepted"]
    b3 = R["levels"]["B3LYP"]
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    labels = ["GFN2-xTB\n(Tier 1)", "B3LYP-D3(BJ)\n(Tier 2)"]
    vals = [t1["V-PRC"] - t1["W-PRC"], b3["V-PRC"]["dE"] - b3["W-PRC"]["dE"]]
    bars = ax.bar(labels, vals, 0.42, color=["#B0B0B0", C["V"]])
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v - 4, "%.1f" % v, ha="center",
                fontsize=11, color="white", fontweight="bold")
    ax.set_ylabel("$\\Delta\\Delta E$ (H$_3$VO$_4$ minus H$_2$O), kJ mol$^{-1}$")
    ax.set_title("The semi-empirical screen exaggerates the gap between the two "
                 "adsorbates by about nine times", fontsize=10)
    ax.grid(axis="y", alpha=0.28, lw=0.7)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "fig4_7_method_gap.png")


if __name__ == "__main__":
    print("building figures")
    figure_models()
    figure_dispute()
    figure_workflow()
    figure_energy_profile()
    figure_adsorption()
    figure_gibbs()
    figure_imag()
    figure_competition()
    figure_method_gap()
