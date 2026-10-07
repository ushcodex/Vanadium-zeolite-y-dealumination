import matplotlib.pyplot as plt
import numpy as np
import os

# Create figures directory if it doesn't exist
os.makedirs("figures", exist_ok=True)

# 1. Adsorption Comparison
labels = ['H3VO4 (vanadic acid)', 'H2O (steam)']
b3lyp_energies = [-93.0, -78.3]
pbe0_energies = [-93.1, -78.6]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width/2, b3lyp_energies, width, label='B3LYP-D3(BJ)/def2-TZVP', color='#1f77b4')
rects2 = ax.bar(x + width/2, pbe0_energies, width, label='PBE0-D3(BJ)/def2-TZVP', color='#d62728')

ax.set_ylabel('Adsorption Energy, ΔE (kJ/mol)', fontsize=12)
ax.set_title('Adsorption Energy of H3VO4 and H2O on the FAU Cluster Model', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -20),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color='white', fontweight='bold')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig("figures/fig4_1_adsorption.png", dpi=300)
plt.close()

# 2. Energy Profile
states_v = ['Reference', 'V-PRC', 'V-I1', 'V-TS2', 'V-I2', 'V-P']
energies_v = [0.0, -93.0, -115.3, 323.6, -122.1, 419.7]

states_w = ['Reference', 'W-PRC', 'W-P']
energies_w = [0.0, -78.3, -24.0]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(range(len(states_v)), energies_v, marker='o', linestyle='-', color='#d62728', label='Vanadic Acid Pathway', linewidth=2)
ax.plot(range(len(states_w)), energies_w, marker='s', linestyle='--', color='#1f77b4', label='Steam Baseline Pathway', linewidth=2)

for i, txt in enumerate(energies_v):
    ax.annotate(f'{txt}', (i, energies_v[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(energies_w):
    ax.annotate(f'{txt}', (i, energies_w[i]), textcoords="offset points", xytext=(0,-15), ha='center')

ax.set_xticks(range(len(states_v)))
ax.set_xticklabels(states_v)
ax.set_ylabel('Relative Electronic Energy, ΔE (kJ/mol)', fontsize=12)
ax.set_title('Electronic Reaction Profile at B3LYP-D3(BJ)/def2-TZVP', fontsize=14)
ax.axhline(0, color='black', linewidth=1)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend()

plt.tight_layout()
plt.savefig("figures/fig4_2_energy_profile.png", dpi=300)
plt.close()

# 3. Gibbs Free Energy
labels = ['V-PRC', 'V-I1', 'W-PRC', 'W-P']
g_298 = [-17.0, -35.7, -28.9, 30.8]
g_1003 = [133.4, 108.4, 67.0, 132.7]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 6))
rects1 = ax.bar(x - width/2, g_298, width, label='298 K (25 °C)', color='#2ca02c')
rects2 = ax.bar(x + width/2, g_1003, width, label='1003 K (730 °C)', color='#ff7f0e')

ax.set_ylabel('Gibbs Free Energy, ΔG (kJ/mol)', fontsize=12)
ax.set_title('Gibbs Free Energy of Adsorption and Reaction', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

for rect in rects1:
    height = rect.get_height()
    ypos = height + 5 if height > 0 else height - 15
    ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, ypos),
                ha='center', va='bottom' if height > 0 else 'top')

for rect in rects2:
    height = rect.get_height()
    ypos = height + 5 if height > 0 else height - 15
    ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, ypos),
                ha='center', va='bottom' if height > 0 else 'top')

plt.tight_layout()
plt.savefig("figures/fig4_3_gibbs.png", dpi=300)
plt.close()

print("Figures successfully generated in figures/ directory.")
