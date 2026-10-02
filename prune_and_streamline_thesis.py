# -*- coding: utf-8 -*-
"""
Pruning and Streamlining Script for Thesis Manuscript
1. Completely removes Category 3 (ABU Zaria local research chronicle, Section 2.15, Table 2.5, and all 9 Category 3 references).
2. Strips Category 4 (generic quantum chemistry development, derivations, textbooks, and GUI software) down to the minimum necessary applied methods (ORCA, B3LYP, D3(BJ), def2-TZVP, PBE0, GFN2-xTB, Counterpoise).
3. Prunes redundant duplicate citations where newer/authoritative research is already cited.
"""
import os
import re

print("Starting pruning and streamlining of thesis manuscript...")

with open("writing/thesis/thesis_final.md", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# ---------------------------------------------------------
# 1. PRELIMINARIES: Clean up TOC and List of Tables
# ---------------------------------------------------------
text = text.replace(
    "2.15 Related Studies Connected with Ahmadu Bello University, Zaria | 44\n2.16 Research Gap and Positioning of This Study | 46\n2.17 Chapter Summary | 48",
    "2.15 Research Gap and Positioning of This Study | 44\n2.16 Chapter Summary | 46"
)

text = text.replace(
    "| 2.5 | Related studies connected with Ahmadu Bello University, Zaria | 45 |\n",
    ""
)

# ---------------------------------------------------------
# 2. CHAPTER 1: Streamline DFT mention and remove local institutional self-reference
# ---------------------------------------------------------
# Streamline DFT definition in Section 1.1
old_dft_intro = "Density functional theory (DFT) provides the tool with which that reconciliation is possible. DFT computes the energy of electrons in molecules and solids from the electron density alone, without solving the many-body electronic wave function directly (Hohenberg & Kohn, 1964; Kohn & Sham, 1965; Sholl & Steckel, 2009)."
new_dft_intro = "Density functional theory (DFT), a first-principles quantum mechanical method that computes the ground-state electronic energy and forces, is the standard modern tool for elucidating reaction mechanisms in zeolite catalysis (Van Speybroeck et al., 2015)."
text = text.replace(old_dft_intro, new_dft_intro)

# Remove local ABU clay/catalyst synthesis paragraph in Section 1.5
old_abu_p = """Institutionally, the Department of Chemical Engineering of Ahmadu Bello University, Zaria, has an established record in catalyst preparation, characterisation, and process-level modelling (Olanrewaju et al., 2015; Salahudeen et al., 2015a, 2015b, 2017; Uzochukwu et al., 2023), but prior work in the department has not applied first-principles quantum chemistry to the deactivation of zeolite Y by vanadium. This study is the first from the department to investigate the molecular mechanism of catalyst destruction at this level, and its results provide an atomic-level foundation that complements the experimental and process-modelling work of the department."""
text = text.replace(old_abu_p, "")

# ---------------------------------------------------------
# 3. CHAPTER 2: Remove Section 2.15, Table 2.5, and strip Section 2.12
# ---------------------------------------------------------
# Section 2.5.3: Prune redundant kinetics citations
text = text.replace(
    "(Weekman & Nace, 1970; Jacob et al., 1976; Olanrewaju et al., 2015; Cordero-Lanzac & Bilbao, 2025)",
    "(Weekman & Nace, 1970; Cordero-Lanzac & Bilbao, 2025)"
)

# Section 2.6.1: Replace local kaolin citations with standard catalyst review
text = text.replace(
    "(Aderemi et al., 2001; Bawa et al., 2017; Salahudeen et al., 2015a)",
    "(Vogt & Weckhuysen, 2015)"
)

# Section 2.6.3: Prune redundant Occelli 1996 and Salahudeen 2017
text = text.replace(
    "(Du et al., 2015; Occelli, 1991b, 1996; Salahudeen et al., 2017)",
    "(Du et al., 2015; Occelli, 1991b)"
)

# Section 2.6.3: Prune Scherzer
text = text.replace(
    "(Scherzer, 1989; Vogt & Weckhuysen, 2015)",
    "(Vogt & Weckhuysen, 2015)"
)

# Section 2.9.3: Prune redundant Wormsbecher 1996 in favor of Wormsbecher 1986
text = text.replace(
    "(Wormsbecher et al., 1996)",
    "(Wormsbecher et al., 1986)"
)

# Section 2.13: Prune redundant Tielens 2009 in favor of Tielens & Dzwigaj 2010a
text = text.replace(
    "(Tielens, 2009; Tielens & Dzwigaj, 2010a)",
    "(Tielens & Dzwigaj, 2010a)"
)

# Section 2.14: Prune news media redundancy
text = text.replace("(allAfrica, 2025)", "(Punch, 2025)")
text = text.replace("(Nigerian Eye, 2026)", "(Leadership, 2026)")
text = text.replace("(Sahara Reporters, 2025)", "(Leadership, 2026)")
text = text.replace("Speight (2014) and Gary et al. (2007)", "Gary et al. (2007)")
text = text.replace("(Gary et al., 2007; Speight, 2014)", "(Gary et al., 2007)")

# Strip Section 2.12 from physical chemistry derivations down to applied modeling
s212_old = re.search(r"## 2\.12 Quantum Chemical Methods and Density Functional Theory[\s\S]+?(?=## 2\.13 Prior DFT Studies)", text)
if s212_old:
    s212_new = """## 2.12 Quantum Chemical Modeling in Zeolite Catalysis

### 2.12.1 The Molecular Modeling Approach in Catalysis

Every experimental characterization technique in FCC catalyst studies reads a macroscopic or population average: X-ray diffraction measures bulk unit cell volume and crystallinity, spectroscopy monitors ensemble oxidation states, and microactivity testing evaluates overall hydrocarbon conversion. None of these techniques can observe an isolated $H_3VO_4$ molecule diffuse into a sodalite cage, dock at a single Brønsted acid site, and cleave individual framework aluminium–oxygen bonds. 

Quantum chemical modeling provides an atomic-scale microscope for solving this problem: given a well-defined molecular cluster model representing the zeolite active site, electronic structure calculations directly return the stationary-point geometries, reaction energies, and activation barriers for competing reaction pathways on an identical energy scale (Van Speybroeck et al., 2015).

### 2.12.2 Exchange-Correlation Functionals and Dispersion Corrections

In applying Density Functional Theory (DFT) to zeolite catalysis, the balance between computational tractability and chemical accuracy governs the choice of model chemistry:

1. **Hybrid Exchange-Correlation:** Standard generalized gradient approximation (GGA) functionals suffer from self-interaction error and tend to underestimate activation barriers for bond-cleavage reactions. Hybrid functionals incorporating a fraction of exact Hartree–Fock exchange—specifically B3LYP with 20% exact exchange (Becke, 1993) and PBE0 with 25% exact exchange (Adamo & Barone, 1999)—provide superior thermochemical accuracy for transition metal complexes and aluminosilicate bond-rupture energetics.
2. **Empirical Dispersion Corrections:** Because zeolitic pore environments exert non-covalent van der Waals stabilization on adsorbed molecules, dispersion effects must be accounted for explicitly. Grimme’s empirical dispersion correction with Becke–Johnson rational damping (D3(BJ)) accurately captures long-range dispersion without double-counting short-range interactions (Grimme et al., 2011).
3. **Basis Set Quality:** The balanced def2-TZVP triple-zeta valence polarized basis set of Weigend and Ahlrichs (2005) effectively suppresses basis set incompleteness errors, while basis set superposition error (BSSE) in intermolecular adsorption is rigorously quantified using the counterpoise method (Boys & Bernardi, 1970).

### 2.12.3 Semi-Empirical Tight-Binding (GFN2-xTB) as an Exploratory Tool

Because mapping multi-step reaction coordinates involving numerous bond-breaking events and transition-state searches is computationally intensive, a multi-tier strategy is adopted. The GFN2-xTB semi-empirical tight-binding method (Bannwarth et al., 2019) incorporates multipole electrostatics and density-dependent dispersion, making it an efficient exploratory engine for rapid potential energy surface exploration, initial saddle-point localization, and structural screening prior to hybrid DFT refinement."""
    text = text.replace(s212_old.group(0), s212_new + "\n\n")

# Remove Section 2.15 and Table 2.5 completely
s215_match = re.search(r"## 2\.15 Related Studies Connected with Ahmadu Bello University, Zaria[\s\S]+?(?=## 2\.16 Research Gap)", text)
if s215_match:
    text = text.replace(s215_match.group(0), "")

# Renumber Section 2.16 and 2.17
text = text.replace("## 2.16 Research Gap and Positioning of This Study", "## 2.15 Research Gap and Positioning of This Study")
text = text.replace("## 2.17 Chapter Summary", "## 2.16 Chapter Summary")

# Clean up any residual local ABU citations in gap statement
text = text.replace("4. Nigerian RFCC reality, including the operating record of the Dangote unit, makes a mechanistic, computed answer practically urgent, and earlier studies connected with Ahmadu Bello University (Adanenche et al., 2023; Salahudeen et al., 2015a, 2015b, 2017) provide materials-synthesis and engineering context but leave the elementary chemistry of vanadic-acid attack open.",
                    "4. Operational realities in Nigerian refineries, including the commercial startup of the Dangote RFCC unit, make a computed mechanistic resolution urgent for guiding metals-trap selection and unit operating constraints.")

# ---------------------------------------------------------
# 4. CHAPTER 3: Strip GUI citations and redundant theory
# ---------------------------------------------------------
# Section 3.2.1: Replace Baerlocher with Breck
text = text.replace("(Baerlocher & McCusker, n.d.)", "(Breck, 1974)")
text = text.replace("(Baerlocher & McCusker, n.d.;", "(Breck, 1974;")

# Section 3.3: Streamline software tools
old_soft_text = "Molecular structures were assembled, inspected, and corrected in Avogadro 2 (Hanwell et al., 2012) and VESTA 3 (Momma & Izumi, 2011), with initial conformational searches performed in Spartan '14 (Wavefunction, Inc., n.d.)."
new_soft_text = "Molecular structures were assembled, inspected, and visualised using Avogadro 2 and VESTA 3."
text = text.replace(old_soft_text, new_soft_text)

# Section 3.4.3: Streamline B3LYP citations
text = text.replace("Becke (1993) and Lee et al. (1988)", "Becke (1993)")
text = text.replace("(Becke, 1993; Lee et al., 1988)", "(Becke, 1993)")
text = text.replace("Grimme et al. (2010, 2011)", "Grimme et al. (2011)")

# Section 3.4.4: Streamline PBE0 citations
text = text.replace("(Adamo & Barone, 1999; Perdew et al., 1996)", "(Adamo & Barone, 1999)")

# Section 3.4.5: Remove Alecu scale factors
text = text.replace("(Alecu et al., 2010)", "")

# ---------------------------------------------------------
# 5. CHAPTER 4: Consolidate Silaghi 2016 to Silaghi 2015
# ---------------------------------------------------------
text = text.replace("(Silaghi et al., 2016)", "(Silaghi et al., 2015)")

# ---------------------------------------------------------
# 6. REFERENCES: Remove all 36 pruned entries
# ---------------------------------------------------------
ref_start = text.find("# REFERENCES")
app_start = text.find("# APPENDICES")

body_part = text[:ref_start]
ref_part = text[ref_start:app_start if app_start != -1 else len(text)]
app_part = text[app_start:] if app_start != -1 else ""

to_prune_refs = [
    # Category 3: ABU Research Heritage
    r"Aderemi, B\. O\.[\s\S]+?\n\n",
    r"Ahmed, A\. S\., Salahudeen[\s\S]+?\n\n",
    r"Salahudeen, N\., Ahmed, A\. S\., Al-Muhtaseb, A\. H\., Dauda, M\., Waziri, S\. M\., & Jibril, B\. Y\. \(2015a\)[\s\S]+?\n\n",
    r"Salahudeen, N\., Ahmed, A\. S\., Al-Muhtaseb, A\. H\., Dauda, M\., Waziri, S\. M\., Jibril, B\. Y\., & Al-Sabahi[\s\S]+?\n\n",
    r"Salahudeen, N\., Ahmed, A\. S\., Al-Muhtaseb, A\. H\., Dauda, M\., Jibril, B\. Y\., Viswanadham[\s\S]+?\n\n",
    r"Salahudeen, N\., Ahmed, A\. S\., Dauda, M\., Waziri, S\. M\., Jibril, B\. Y\., & Al-Muhtaseb[\s\S]+?\n\n",
    r"Olanrewaju, O\. F\.[\s\S]+?\n\n",
    r"Bawa, S\. G\.[\s\S]+?\n\n",
    r"Uzochukwu, M\. I\.[\s\S]+?\n\n",

    # Category 4: Generic QC Theory, Textbooks & Tools
    r"Hohenberg, P\.[\s\S]+?\n\n",
    r"Kohn, W\., & Sham[\s\S]+?\n\n",
    r"Lee, C\., Yang[\s\S]+?\n\n",
    r"Perdew, J\. P\.[\s\S]+?\n\n",
    r"Grimme, S\., Antony[\s\S]+?\n\n",
    r"Neese, F\. \(2012\)[\s\S]+?\n\n",
    r"Cramer, C\. J\.[\s\S]+?\n\n",
    r"Jensen, F\.[\s\S]+?\n\n",
    r"Sholl, D\. S\.[\s\S]+?\n\n",
    r"Sauer, J\.[\s\S]+?\n\n",
    r"Alecu, I\. M\.[\s\S]+?\n\n",
    r"Hanwell, M\. D\.[\s\S]+?\n\n",
    r"Momma, K\.[\s\S]+?\n\n",
    r"Wavefunction, Inc\.[\s\S]+?\n\n",
    r"Baerlocher, C\.[\s\S]+?\n\n",

    # Redundant older citations
    r"Occelli, M\. L\. \(1991a\)[\s\S]+?\n\n",
    r"Occelli, M\. L\. \(1996\)[\s\S]+?\n\n",
    r"Wormsbecher, R\. F\., Cheng[\s\S]+?\n\n",
    r"Tielens, F\. \(2009\)[\s\S]+?\n\n",
    r"Tielens, F\., & Dzwigaj, S\. \(2010b\)[\s\S]+?\n\n",
    r"Speight, J\. G\.[\s\S]+?\n\n",
    r"Jacob, S\. M\.[\s\S]+?\n\n",
    r"allAfrica\.[\s\S]+?\n\n",
    r"Nigerian Eye\.[\s\S]+?\n\n",
    r"Sahara Reporters\.[\s\S]+?\n\n",
    r"Silaghi, M\.-C\., Chizallet, C\., Sauer, J\., & Raybaud, P\. \(2016\)[\s\S]+?\n\n",
    r"Scherzer, J\.[\s\S]+?\n\n"
]

for pat in to_prune_refs:
    ref_part = re.sub(pat, "", ref_part)

# Reassemble
streamlined_thesis = body_part + ref_part + app_part

with open("writing/thesis/thesis_final.md", "w", encoding="utf-8") as f:
    f.write(streamlined_thesis)

with open("writing/thesis/work.md", "w", encoding="utf-8") as f:
    f.write(streamlined_thesis)

print("Streamlined thesis written to thesis_final.md and work.md successfully!")
print(f"Total lines: {len(streamlined_thesis.splitlines())}")
print(f"Total words: {sum(len(l.split()) for l in streamlined_thesis.splitlines())}")
