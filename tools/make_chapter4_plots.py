#!/usr/bin/env python3
"""Create Chapter Four plots from the machine-readable calculation results."""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
RESULTS = json.loads((ROOT / "writing" / "markdown" / "_results.json").read_text())
P_TOTAL_ATM = 2.0  # regenerator pressure used to express acid pressure as ppm

BLUE = "#1F5C99"
RED = "#B3312C"
plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 10,
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


def gibbs_temperature_plot():
    temperatures = [298.15, 1003.15]
    b3lyp = RESULTS["levels"]["B3LYP"]
    series = [
        ("V-PRC", RED, "-", [b3lyp["V-PRC"]["dG_298.15"], b3lyp["V-PRC"]["dG_1003.15"]]),
        ("V-I1", RED, "--", [b3lyp["V-I1"]["dG_298.15"], b3lyp["V-I1"]["dG_1003.15"]]),
        ("W-PRC", BLUE, "-", [b3lyp["W-PRC"]["dG_298.15"], b3lyp["W-PRC"]["dG_1003.15"]]),
        ("W-P", BLUE, "--", [b3lyp["W-P"]["dG_298.15"], b3lyp["W-P"]["dG_1003.15"]]),
    ]
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    x = np.arange(len(temperatures))
    label_offsets = {
        "V-PRC": [(0, 10), (0, 11)],
        "V-I1": [(0, -16), (0, 10)],
        "W-PRC": [(0, 10), (0, 10)],
        "W-P": [(0, 10), (0, -16)],
    }
    for name, colour, linestyle, values in series:
        ax.plot(x, values, color=colour, linestyle=linestyle, marker="o",
                linewidth=1.8, markersize=6, label=name, zorder=3)
        for index, value in enumerate(values):
            dx, dy = label_offsets[name][index]
            ax.annotate(f"{value:+.1f}", (x[index], value),
                        xytext=(dx, dy), textcoords="offset points",
                        ha="center", va="center", fontsize=8.5,
                        color=colour)
    ax.axhline(0, color="#555555", linestyle=":", linewidth=1.1, zorder=1)
    ax.set_xticks(x, [f"{temperature:.2f}" for temperature in temperatures])
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel(r"Standard Gibbs energy of adsorption, $\Delta G^{\circ}_{\mathrm{ads}}$ (kJ mol$^{-1}$)")
    ax.set_ylim(-60, 165)
    ax.set_xlim(-0.18, 1.18)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    ax.legend(ncol=2, frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "fig4_2_gibbs_temperature.png")
    plt.close(fig)


def site_occupation_plot():
    site_data = RESULTS["site_occupation"]
    rows = site_data["calculation_rows"]
    pressure = [row["p_H3VO4_atm"] for row in rows]
    water = [row["theta_H2O"] for row in rows]
    acid = [row["theta_H3VO4"] for row in rows]
    x = np.arange(len(rows))
    labels = [f"{p / P_TOTAL_ATM * 1e6:g} ppm H₃VO₄" for p in pressure]

    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    ax.plot(x, water, color=BLUE, marker="o", linewidth=2.0, markersize=7,
            label=r"Water, $p_{\mathrm{H_2O}}=0.4$ atm", zorder=3)
    ax.plot(x, acid, color=RED, marker="s", linewidth=2.0, markersize=7,
            label=r"Vanadic acid, $p_{\mathrm{H_3VO_4}}$ varied", zorder=3)
    ax.annotate(f"{water[0]:.2e}", (x[0], water[0]), xytext=(0, 12),
                textcoords="offset points", ha="center", color=BLUE, fontsize=9)
    for index, value in enumerate(acid):
        ax.annotate(f"{value:.2e}", (x[index], value), xytext=(0, -18),
                    textcoords="offset points", ha="center", color=RED,
                    fontsize=9)
    ax.set_yscale("log")
    ax.set_ylim(1e-14, 1e-3)
    ax.set_xlim(-0.22, len(rows) - 0.78)
    ax.set_xticks(x, labels)
    ax.set_xlabel("Vanadic-acid concentration at 2 atm total pressure")
    ax.set_ylabel(r"Conditional site fraction, $\theta_i$ (log scale)")
    ax.grid(axis="y", which="both", color="#D9D9D9", linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="center right")
    fig.tight_layout()
    fig.savefig(FIGURES / "fig4_3_site_occupation.png")
    plt.close(fig)


if __name__ == "__main__":
    gibbs_temperature_plot()
    site_occupation_plot()
    print("Wrote figures/fig4_2_gibbs_temperature.png and figures/fig4_3_site_occupation.png")
