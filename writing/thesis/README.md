# B.Eng. THESIS MANUSCRIPT ARCHITECTURE
**Department of Chemical Engineering, Faculty of Engineering, Ahmadu Bello University, Zaria, Nigeria**

---

## 1. Overview and Structure

This directory (`writing/thesis/`) contains the complete, restructured, and rewritten undergraduate/postgraduate thesis manuscript titled:
> **"FIRST-PRINCIPLES INVESTIGATION OF VANADIC ACID-INDUCED DEALUMINATION IN ZEOLITE Y UNDER RESIDUE FLUID CATALYTIC CRACKING REGENERATION CONDITIONS"**

The entire work has been authored from the ground up to adhere to:
1. **Ahmadu Bello University (ABU) Guidelines for Project Reports, Theses, and Dissertations.**
2. **American Psychological Association (APA) 7th Edition Referencing Style** (in-text author-date citations and full alphabetical bibliography).
3. **Current Executed Methodology & Audited Results**: Strictly grounded in the 22-atom faujasite cluster active-site model ($AlSi_4O_4H_{13}$), multi-tier GFN2-xTB and hybrid DFT ($B3LYP\text{-}D3(BJ)/\text{def2-TZVP}$, $PBE0\text{-}D3(BJ)/\text{def2-TZVP}$) potential energy surfaces, and verified transition states.

---

## 2. Document Map and Table of Word Counts

| File Name | Section / Chapter Title | File Size | Description & Key Contents |
| :--- | :--- | :---: | :--- |
| [`00_preliminaries.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/00_preliminaries.md) | **Preliminary Pages** (pp. i–xii) | 20.4 KB | Title page, Declaration, Certification, Dedication, Acknowledgements, Structured Abstract (< 500 words), Table of Contents, List of Tables, List of Figures, List of Symbols & Abbreviations. |
| [`01_chapter_one.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/01_chapter_one.md) | **Chapter One: Introduction** | 27.8 KB | 1.1 Background (global & Nigerian RFCC context: Dangote, KRPC, WRPC, PHRC); 1.2 Problem Statement; 1.3 Aim & 7 Specific Objectives; 1.4 Research Questions; 1.5 Significance; 1.6 Scope & Delimitation; 1.7 Operational Definitions. |
| [`02_chapter_two.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/02_chapter_two.md) | **Chapter Two: Literature Review** | 58.1 KB | Deep technical review covering refining thermodynamics, residue metalloporphyrins, FCC/RFCC dynamics, Zeolite Y/USY/REY architecture, deactivation modes, volatile $H_3VO_4$ equilibria, critique of 4 experimental hypotheses (Wormsbecher, Pine, Occelli, Xu, Etim), metal traps & passivators (Adanenche et al., 2023), DFT foundations, and ABU Zaria catalysis heritage. |
| [`03_chapter_three.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/03_chapter_three.md) | **Chapter Three: Materials and Methods** | 25.2 KB | Research design, 22-atom FAU cluster model construction, gas-phase $H_3VO_4$ and $H_2O$ reactants, ORCA 6.1.1 setup on Azure HPC VM, multi-tier protocol (Tier 1 GFN2-xTB, Tier 2 B3LYP-D3(BJ), Tier 3 PBE0-D3(BJ)), 5-point formal saddle verification criteria (A1–A5), thermodynamic formulations for adsorption and activation barriers, and data provenance. |
| [`04_chapter_four.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/04_chapter_four.md) | **Chapter Four: Results and Discussion** | 37.5 KB | Pristine cluster structural validation; competitive adsorption thermodynamics ($-92.78$ vs. $-78.26$ kJ/mol, margin $-14.52$ kJ/mol); complete elementary pathway ($V\text{-PRC} \rightarrow V\text{-I1} \rightarrow V\text{-TS2} \rightarrow V\text{-I2} \rightarrow V\text{-P}$); verified rate-limiting barrier ($+160.70$ kJ/mol, $\nu_1 = -78.21\text{ cm}^{-1}$); steam baseline validation ($+118.42\text{ to }+120.87$ kJ/mol vs. periodic benchmark); coordination evolution of Al extraction; synthesis with experimental literature. |
| [`05_chapter_five.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/05_chapter_five.md) | **Chapter Five: Conclusions & Recommendations** | 14.8 KB | Summary of findings; explicit answers to each of the 7 research questions; distinct contributions to knowledge; actionable engineering recommendations for Nigerian refineries (temperature limits, stripping steam optimization, basic metal trap selection); recommendations for future research. |
| [`06_references.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/06_references.md) | **References** | 20.2 KB | Exhaustive, alphabetical bibliography formatted to APA 7th edition, cross-checking and validating all citations across Chapters 1–5, including all 15 source PDFs in `writing/Sources/`. |
| [`07_appendices.md`](file:///c:/Users/PC/Documents/thesis/writing/thesis/07_appendices.md) | **Appendices** | 24.9 KB | Appendix A: Audited GFN2-xTB PES register; Appendix B: Hybrid DFT calculation register; Appendix C: Representative ORCA 6.1.1 input scripts; Appendix D: Complete Cartesian coordinates ($\text{\AA}$) of 10 key stationary points. |

---

## 3. Formatting & Compilation Instructions

To compile the entire modular manuscript into a single unified Word document (`.docx`) or publication PDF (`.pdf`) using Pandoc:

### Unified Word Document (.docx)
```bash
pandoc -s -o complete_thesis.docx \
  00_preliminaries.md \
  01_chapter_one.md \
  02_chapter_two.md \
  03_chapter_three.md \
  04_chapter_four.md \
  05_chapter_five.md \
  06_references.md \
  07_appendices.md \
  --toc --number-sections
```

### Unified PDF via LaTeX Engine (XeLaTeX / pdfLaTeX)
```bash
pandoc -s -o complete_thesis.pdf \
  00_preliminaries.md \
  01_chapter_one.md \
  02_chapter_two.md \
  03_chapter_three.md \
  04_chapter_four.md \
  05_chapter_five.md \
  06_references.md \
  07_appendices.md \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=12pt \
  -V documentclass=report
```
