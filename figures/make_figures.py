#!/usr/bin/env python3
"""Draw every original figure in the thesis with matplotlib.

All of the data plotted here is read from simulation/analysis/RESULTS.md values
that are reproduced in the DATA block below, which were themselves taken from
simulation/analysis/orca_register.csv. Re-run this file after re-running
simulation/analysis/build_tables.py if the numbers change.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.lines import Line2D

OUT = "/home/user/Vanadium-zeolite-y-dealumination/figures"
GEOM = "/home/user/Vanadium-zeolite-y-dealumination/simulation/03_tier2_completion/results/geom"
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ---------------------------------------------------------------- data block
# B3LYP-D3(BJ)/def2-TZVP, ORCA 6.1.1, from build_tables.py
ADS = {
    "label": ["electronic", "with ZPE", "H, 298 K", "G, 298 K", "G, 1003 K"],
    "H3VO4": [-93.01, -81.75, -95.48, -17.05, 133.39],
    "H2O": [-78.32, -66.94, -80.80, -28.87, 67.03],
}
PBE0 = {"H3VO4": -93.07, "H2O": -78.62}

# GFN2-xTB, ORCA 6.1.0, kJ/mol relative to the separated reactants
T1 = {
    "V-PRC": -196.90, "V-I1": -385.10, "V-TS2": -224.40,
    "V-I2": -342.37, "V-P": -82.90,
}
T1W = {"W-PRC": -69.59, "W-TS": -40.29, "W-P": -65.85}
BARR = {"V": 160.70, "W": 29.29}
IMAG = {"V": -78.21, "W": -226.10}

# ---------------------------------------------------------- helper: geometry
def read_xyz(path):
    L = open(path, encoding="utf-8", errors="replace").read().split("\n")
    n = int(L[0].split()[0])
    el, xyz = [], []
    for line in L[2:2 + n]:
        p = line.split()
        el.append(p[0])
        xyz.append([float(p[1]), float(p[2]), float(p[3])])
    return el, np.array(xyz)


COV = {"Al": 1.21, "Si": 1.11, "O": 0.66, "H": 0.31, "V": 1.34}
COL = {"Al": "#7b5ea7", "Si": "#d9a53b", "O": "#d64545", "H": "#e8e8e8",
       "V": "#2e8b8b"}
RAD = {"Al": 0.42, "Si": 0.40, "O": 0.34, "H": 0.22, "V": 0.48}


def draw_mol(ax, el, xyz, elems=None, elev=18, azim=35, scale=1.0, title=""):
    """Ball and stick drawing with a cheap depth sort."""
    cov = np.array([COV.get(e, 1.0) for e in el])
    d = np.linalg.norm(xyz[:, None, :] - xyz[None, :, :], axis=-1)
    rng = (cov[:, None] + cov[None, :]) * 1.30
    # rotate
    a = np.radians(elev)
    b = np.radians(azim)
    Rz = np.array([[np.cos(b), -np.sin(b), 0], [np.sin(b), np.cos(b), 0], [0, 0, 1]])
    Rx = np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])
    P = (Rx @ Rz @ xyz.T).T
    z = P[:, 2]
    order = np.argsort(z)
    for i, j in zip(*np.where((d < rng) & (d > 0.1))):
        if i >= j:
            continue
        zi = (z[i] + z[j]) / 2
        ax.plot([P[i, 0], P[j, 0]], [P[i, 1], P[j, 1]], "-", color="#606060",
                lw=2.4, solid_capstyle="round", zorder=zi)
    for k in order:
        e = el[k]
        if elems and e not in elems:
            continue
        c = plt.Circle((P[k, 0], P[k, 1]), RAD.get(e, 0.35) * scale,
                       color=COL.get(e, "#888888"),
                       ec="black" if e == "H" else "#202020", lw=0.7, zorder=z[k] + 0.5)
        ax.add_patch(c)
        if e != "H":
            ax.text(P[k, 0], P[k, 1], e, ha="center", va="center", fontsize=8,
                    color="white", weight="bold", zorder=z[k] + 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.margins(0.12)
    if title:
        ax.set_title(title, fontsize=11)


# ------------------------------------------------- Figure 3.1: cluster model
def fig_cluster():
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
    elC, xC = read_xyz(os.path.join(GEOM, "cluster.xyz"))
    elP, xP = read_xyz(os.path.join(GEOM, "v-prc.xyz"))
    elW, xW = read_xyz(os.path.join(GEOM, "w-prc.xyz"))
    draw_mol(axes[0], elC, xC, title="(a) bare acid site, AlSi\u2084O\u2084H\u2081\u2083")
    draw_mol(axes[1], elW, xW, title="(b) water complex, W-PRC")
    draw_mol(axes[2], elP, xP, title="(c) vanadic acid complex, V-PRC")
    handles = [Line2D([], [], marker="o", ls="", color=COL[k], markersize=9,
                      markeredgecolor="#202020", label=k) for k in ["Al", "Si", "O", "V", "H"]]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, fontsize=10)
    fig.suptitle("Faujasite cluster models used in this work "
                 "(B3LYP-D3(BJ)/def2-TZVP geometries)", fontsize=12, y=1.0)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig(os.path.join(OUT, "fig3_1_cluster_models.png"))
    plt.close(fig)


# ------------------------------------------------- Figure 3.2: workflow
def fig_workflow():
    fig, ax = plt.subplots(figsize=(9.2, 6.4))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

    def box(x, y, w, h, text, fc, fs=10, tc="black"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.6",
                                    fc=fc, ec="#333333", lw=1.1, zorder=2))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
                zorder=3, color=tc)

    def arrow(x1, y1, x2, y2, label="", style="-|>"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                     mutation_scale=16, lw=1.4, color="#333333", zorder=1))
        if label:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 2.2, label, ha="center", fontsize=9,
                    style="italic", color="#444444", zorder=4)

    ax.text(50, 96, "Two-level computational workflow", ha="center", fontsize=13,
            weight="bold")
    box(6, 80, 88, 10, "Build the 4T faujasite cluster, AlSi\u2084O\u2084H\u2081\u2083, "
        "with one Br\u00f8nsted acid site", "#eef3fa", fs=10)
    arrow(50, 80, 50, 71)
    box(6, 58, 42, 13, "Level 1  GFN2-xTB\nscan the whole path, locate\nstarting "
        "shapes for every state", "#e3f0e6", fs=9.5)
    box(52, 58, 42, 13, "Level 2  B3LYP-D3(BJ)/def2-TZVP\nre-optimise and compute\n"
        "frequencies", "#fdeede", fs=9.5)
    arrow(27, 58, 27, 49)
    arrow(73, 58, 73, 49)
    box(6, 35, 42, 14, "Accept a state only if\noptimisation converged\nand the "
        "frequency run is clean", "#e3f0e6", fs=9.5)
    box(52, 35, 42, 14, "Accept a saddle only if\nexactly one imaginary mode\n"
        "and both displacements match", "#fdeede", fs=9.5)
    arrow(27, 35, 27, 27)
    arrow(73, 35, 73, 27)
    arrow(27, 27, 48, 27, "geometries")
    arrow(73, 27, 52, 27)
    box(30, 14, 40, 13, "PBE0-D3(BJ)/def2-TZVP\nsingle-point cross-check",
        "#f5e9f7", fs=10)
    arrow(50, 14, 50, 6)
    box(6, 0.5, 88, 6, "Report: what is established, what is not, and why",
        "#f2f2f2", fs=10)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig3_2_workflow.png"))
    plt.close(fig)


# ------------------------------------------------- Figure 4.1: tier 1 profile
def fig_tier1_profile():
    fig, ax = plt.subplots(figsize=(9.4, 5.0))
    steps = ["V-PRC", "V-I1", "V-TS2", "V-I2", "V-P"]
    y = [T1[s] for s in steps]
    xlab = ["adsorption\ncomplex", "chemisorbed\nintermediate", "first Al-O\ncleavage "
            "saddle", "opened\nintermediate", "dealuminated\nproduct"]
    ax.plot(range(5), y, "o-", color="#2e8b8b", lw=2.2, ms=8, label="vanadic acid route")
    # reference line
    ax.axhline(0, color="#999999", lw=1.0, ls="--")
    ax.text(4.1, 8, "separated cluster + H\u2083VO\u2084", fontsize=9, color="#666666",
            ha="right")
    # barrier annotation
    ax.annotate("", xy=(2, T1["V-TS2"]), xytext=(1, T1["V-I1"]),
                arrowprops=dict(arrowstyle="<->", color="#2e8b8b", lw=1.3))
    ax.text(1.5, (T1["V-TS2"] + T1["V-I1"]) / 2, "161 kJ/mol", fontsize=9.5,
            color="#2e8b8b", ha="center", va="bottom")

    xs = [0, 1, 2]
    ys = [T1W["W-PRC"], T1W["W-TS"], T1W["W-P"]]
    ax.plot(xs, ys, "s--", color="#b5651d", lw=2.0, ms=7, label="steam route")
    ax.annotate("", xy=(1, T1W["W-TS"]), xytext=(0, T1W["W-PRC"]),
                arrowprops=dict(arrowstyle="<->", color="#b5651d", lw=1.3))
    ax.text(0.55, (T1W["W-TS"] + T1W["W-PRC"]) / 2, "29 kJ/mol", fontsize=9.5,
            color="#b5651d", ha="center", va="bottom")
    ax.set_xticks(range(5))
    ax.set_xticklabels(xlab, fontsize=10)
    ax.set_ylabel("energy relative to the separated reactants, kJ/mol", fontsize=11)
    ax.set_title("Level 1 profile, GFN2-xTB (saddle points: one imaginary mode at "
                 "-78 and -226 cm\u207b\u00b9)", fontsize=11)
    ax.legend(frameon=False, loc="lower left")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4_1_tier1_profile.png"))
    plt.close(fig)


# ------------------------------------------------- Figure 4.2: adsorption
def fig_adsorption():
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.6))
    ax = axes[0]
    x = np.arange(len(ADS["label"]))
    w = 0.38
    ax.bar(x - w / 2, ADS["H3VO4"], w, color="#2e8b8b", label="vanadic acid, H\u2083VO\u2084")
    ax.bar(x + w / 2, ADS["H2O"], w, color="#b5651d", label="steam, H\u2082O")
    ax.axhline(0, color="black", lw=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(ADS["label"], fontsize=10)
    ax.set_ylabel("energy of adsorption, kJ/mol", fontsize=11)
    ax.set_title("(a) B3LYP-D3(BJ)/def2-TZVP", fontsize=11)
    ax.legend(frameon=False, fontsize=9.5)
    ax.grid(axis="y", alpha=0.25)

    ax = axes[1]
    names = ["B3LYP-D3(BJ)", "PBE0-D3(BJ)"]
    v = [ADS["H3VO4"][0], PBE0["H3VO4"]]
    wv = [ADS["H2O"][0], PBE0["H2O"]]
    x = np.arange(2)
    ax.bar(x - 0.19, v, 0.38, color="#2e8b8b", label="vanadic acid")
    ax.bar(x + 0.19, wv, 0.38, color="#b5651d", label="steam")
    for i in range(2):
        ax.text(i, min(v[i], wv[i]) - 4, "gap %.1f" % (v[i] - wv[i]), ha="center",
                fontsize=9.5)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.set_ylabel("electronic adsorption energy, kJ/mol", fontsize=11)
    ax.set_title("(b) two functionals, same geometries", fontsize=11)
    ax.set_ylim(min(v + wv) * 1.35, 0)
    ax.legend(frameon=False, fontsize=9.5)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4_2_adsorption.png"))
    plt.close(fig)


# ------------------------------------------------- Figure 4.3: Gibbs vs T
def fig_gibbs():
    # dG(T) = dH - T dS, with dH and dS fitted from the two computed points
    T1_, T2_ = 298.15, 1003.15
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    T = np.linspace(298.15, 1003.15, 200)
    for lab, g1, g2, c in [("vanadic acid, H\u2083VO\u2084", ADS["H3VO4"][3],
                            ADS["H3VO4"][4], "#2e8b8b"),
                           ("steam, H\u2082O", ADS["H2O"][3], ADS["H2O"][4], "#b5651d")]:
        dS = -(g2 - g1) / (T2_ - T1_)          # kJ/mol/K
        dH = g1 + T1_ * dS
        ax.plot(T, dH - T * dS, "-", color=c, lw=2.2, label=lab)
        ax.plot([T1_, T2_], [g1, g2], "o", color=c, ms=7)
    ax.axhline(0, color="#666666", lw=1.0, ls="--")
    ax.set_xlabel("temperature, K", fontsize=11)
    ax.set_ylabel("Gibbs energy of adsorption, kJ/mol", fontsize=11)
    ax.set_title("Standard-state (1 bar) adsorption free energy against temperature\n"
                 "filled markers are the computed points; the line assumes the "
                 "enthalpy and entropy of adsorption are constant between them",
                 fontsize=10.5)
    ax.legend(frameon=False, fontsize=10)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4_3_gibbs_temperature.png"))
    plt.close(fig)


# ------------------------------------------------- Figure 4.4: level 2 ladder
def fig_tier2_ladder():
    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    names = ["V-PRC", "V-I1", "V-I2\n(not converged)", "V-P\n(not converged)",
             "V-TS2\n(rejected)"]
    vals = [-93.01, -115.38, -122.12, 419.69, 323.63]
    ok = ["yes", "yes", "no", "no", "no"]
    cols = ["#2e8b8b" if o == "yes" else "#b0b0b0" for o in ok]
    bars = ax.bar(names, vals, color=cols, edgecolor="#333333", lw=0.8)
    ax.axhline(0, color="black", lw=0.9)
    ax.set_ylabel("electronic energy relative to\ncluster + H\u2083VO\u2084, kJ/mol",
                  fontsize=11)
    ax.set_title("Level 2 ladder: what the DFT runs actually settled", fontsize=11.5)
    for b, v in zip(bars, vals):
        off = -18 if v > 0 else 6
        ax.text(b.get_x() + b.get_width() / 2, v + off, "%.0f" % v, ha="center",
                fontsize=10)
    ax.grid(axis="y", alpha=0.25)
    ax.set_ylim(-180, 500)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4_4_tier2_ladder.png"))
    plt.close(fig)


for fn in (fig_cluster, fig_workflow, fig_tier1_profile, fig_adsorption,
           fig_gibbs, fig_tier2_ladder):
    fn()
    print("wrote", fn.__name__)
