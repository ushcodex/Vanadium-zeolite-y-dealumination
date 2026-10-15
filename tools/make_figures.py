#!/usr/bin/env python3
"""
make_figures.py

Draws author-produced explanatory figures and molecular structures used in the
thesis. The molecular pictures are rendered from the optimised Cartesian
coordinates in simulation/03_tier2_completion/results/geom/.

Run:  python3 tools/make_figures.py
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "figures")
GEOM = os.path.join(ROOT, "simulation", "03_tier2_completion", "results", "geom")
os.makedirs(FIG, exist_ok=True)

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
}


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

    box(6, 78, 40, 12, "Build a local Zeolite Y cluster\nAlSi$_4$O$_4$H$_{13}$ and the\n"
                       "adsorbates H$_3$VO$_4$, H$_2$O", "#EDEDED", bold=True)
    box(56, 78, 38, 12, "Spartan / Avogadro for\nediting; XYZ files carry the\n"
                        "atom order into ORCA", "#F7F7F7")

    ax.add_patch(Rectangle((3, 40), 88, 33, facecolor="#FBF3F3",
                           edgecolor=C["V"], linewidth=1.4, ls="--"))
    ax.text(5, 70.5, "TIER 1  -  Dell Latitude E6430, 16 GB RAM, SSD, ORCA 6.1.0, 1 core",
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
    ax.text(5, 30.0, "TIER 2  -  cloud virtual machine, ORCA 6.1.1, 4 MPI ranks",
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


if __name__ == "__main__":
    print("building figures")
    figure_models()
    figure_dispute()
    figure_workflow()
