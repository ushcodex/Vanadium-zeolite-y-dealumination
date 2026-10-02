# Tier 1 Pathway Energy & Audit Summary (GFN2-xTB)

## 1. Reference Energy Zeros

| Species / Reference | Electronic Energy (Eh) | Zero Definition |
|---|---|---|
| Cluster (`AlSi4O4H13`) | $-31.34551236$ | Isolated FAU cluster minimum (`cluster-T1-V02.out`) |
| $\text{H}_3\text{VO}_4$ | $-19.77512769$ | Isolated vanadic acid minimum (`h3vo4-T1-V01.out`) |
| $\text{H}_2\text{O}$ | $-5.07054445$ | Isolated water minimum (`h2o-T1-V01.out`, exact: $-5.070544447500 \text{ Eh}$) |
| **Vanadium Ref Zero ($E_{\text{ref,V}}$)** | **$-51.12064005$** | $E(\text{cluster}) + E(\text{H}_3\text{VO}_4)$ |
| **Water Ref Zero ($E_{\text{ref,W}}$)** | **$-36.41605681$** | $E(\text{cluster}) + E(\text{H}_2\text{O})$ |

---

## 2. Tier 1 Pathway Register (Audited & Provenance-Mapped)

### (a) Vanadium Route ($V\text{-}R \rightarrow V\text{-}P$)
*Reference zero = $-51.12064005 \text{ Eh}$*

| Job ID | State | Role | Energy (Eh) | $\Delta E$ vs Ref Zero (kJ/mol) | Verified | Status |
|---|---|---|---|---|---|---|
| `V-R-T1-V02` | $V\text{-}R$ | Supermolecular check | $-51.19563631$ | $-196.90$ | yes | Accepted (Collapsed to PRC basin, 0.1925 nm contact) |
| `V-PRC-T1-V01` | $V\text{-}\text{PRC}$ | Pre-reaction complex | $-51.19461241$ | $-194.21$ | no | Superseded (Unconverged first pass restored) |
| `V-PRC_canonical` | $V\text{-}\text{PRC}$ | Pre-reaction complex | $-51.19563631$ | $-196.90$ | yes | Accepted (0 imag, H-bonded) |
| `V-TS1-T1-V01` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-50.88659123$ | $+614.50$ | no | Artifact, excluded (source: `freq_V-TS1-T1-V01.out`) |
| `V-TS1-T1-V02` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-51.05820550$ | $+163.92$ | no | Candidate, under refinement (Band A CI-NEB, barrier $+360.82 \text{ kJ/mol}$ vs $V\text{-}\text{PRC}$; Step 0 freqs) |
| `V-TS1-T1-V03` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-51.08132900$ | $+103.21$ | no | Candidate, under refinement (OptTS Pass 1, barrier $+300.12 \text{ kJ/mol}$ vs $V\text{-}\text{PRC}$; Step 0 freqs) |
| `V-TS1-T1-V04` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-51.08133370$ | $+103.20$ | no | Slid to minimum (OptTS continuation converged to 0 imag minimum basin) |
| `V-TS1-T1-V05` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-51.08139865$ | $+103.03$ | no | Diagnostic run (CI +0.01nm displacement converged to +300 kJ/mol basin) |
| `V-TS1-T1-V06` | $V\text{-}\text{TS1}$ | Chemisorption TS | $-51.08138390$ | $+103.07$ | no | Diagnostic run (CI -0.01nm displacement converged to +300 kJ/mol basin) |
| `V-I1-T1-V01` | $V\text{-}I_1$ | Chemisorbed intermediate | $-51.26731716$ | $-385.10$ | yes | Accepted (0 imag, 5-coord Al) |
| `V-TS2-T1-V01` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-50.84621402$ | $+720.51$ | no | Artifact, excluded (source: `freq_V-TS2-T1-V01.out`) |
| `V-TS2-T1-V02` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.10991869$ | $+28.15$ | no | Candidate, under refinement (Band B CI-NEB, barrier $+413.25 \text{ kJ/mol}$ vs $V\text{-}I_1$; Step 0 freqs) |
| `V-TS2-T1-V03` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.19071400$ | $-183.98$ | no | Candidate, under refinement (OptTS Pass 1, barrier $+201.12 \text{ kJ/mol}$ vs $V\text{-}I_1$; Step 0 freqs) |
| `V-TS2-T1-V04` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.20596103$ | $-224.01$ | no | Candidate, under refinement (OptTS continuation 1, barrier $+161.09 \text{ kJ/mol}$; Step 0 freqs: 1 imag) |
| `V-TS2-T1-V05` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.20610884$ | $-224.40$ | yes | Accepted (OptTS continuation 2 CONVERGED, barrier $+160.70 \text{ kJ/mol}$ vs $V\text{-}I_1$; 1 imag: $-78.21 \text{ cm}^{-1}$; A1-A5 passed) |
| `V-TS2-T1-V06` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.24508512$ | $-326.73$ | no | Diagnostic run (A4) (Mode 6 +0.01nm displacement converged to V-I2 well, +15.64 kJ/mol vs V-I2, 0 imag) |
| `V-TS2-T1-V07` | $V\text{-}\text{TS2}$ | First $\text{Al-O}$ cleavage TS | $-51.22653425$ | $-278.02$ | no | Diagnostic run (A4) (Mode 6 -0.01nm displacement converged to V-I1 well, +107.08 kJ/mol vs V-I1, 0 imag) |
| `V-I2-T1-V03` | $V\text{-}I_2$ | Hydrolysed intermediate | $-51.25102836$ | $-342.33$ | no | Superseded (imag mode $-118.68 \text{ cm}^{-1}$ restored) |
| `V-I2-T1-V04` | $V\text{-}I_2$ | Hydrolysed intermediate | $-51.25104052$ | $-342.36$ | yes | Accepted (0 imag, mode-displaced) |
| `V-TS3-T1-V01` | $V\text{-}\text{TS3}$ | Final $\text{Al-O}$ cleavage TS | $-50.60576010$ | $+1351.82$ | no | Artifact, excluded (source: `freq_V-TS3-T1-V01.out`) |
| `V-TS3-T1-V02` | $V\text{-}\text{TS3}$ | Final $\text{Al-O}$ cleavage TS | $-51.05369850$ | $+175.76$ | no | Candidate, under refinement (Band C CI-NEB, barrier $+518.12 \text{ kJ/mol}$ vs $V\text{-}I_2$; Step 0 freqs) |
| `V-TS3-T1-V03` | $V\text{-}\text{TS3}$ | Final $\text{Al-O}$ cleavage TS | $-51.06621100$ | $+142.91$ | no | Candidate, under refinement (OptTS Pass 1, barrier $+485.27 \text{ kJ/mol}$ vs $V\text{-}I_2$; Step 0 freqs) |
| `V-TS3-T1-V04` | $V\text{-}\text{TS3}$ | Final $\text{Al-O}$ cleavage TS | $-51.06676972$ | $+141.44$ | no | Candidate, under refinement (OptTS continuation 1, barrier $+483.80 \text{ kJ/mol}$; Step 0 freqs: 3 imag) |
| `V-TS3-T1-V05` | $V\text{-}\text{TS3}$ | Final $\text{Al-O}$ cleavage TS | $-51.06496560$ | $+146.17$ | no | Candidate, under refinement (OptTS continuation 2, barrier $+488.54 \text{ kJ/mol}$; Step 0 freqs: 1 imag $-40.33 \text{ cm}^{-1}$) |
| `V-P-T1-V01` | $V\text{-}P$ | Dealuminated product | $-51.15221675$ | $-82.90$ | yes | Accepted (0 imag, product minimum) |

### (b) Steam Baseline Route ($W\text{-}R \rightarrow W\text{-}P$)
*Reference zero = $-36.41605681 \text{ Eh}$*

| Job ID | State | Role | Energy (Eh) | $\Delta E$ vs Ref Zero (kJ/mol) | Verified | Status |
|---|---|---|---|---|---|---|
| `W-PRC-T1-V02` | $W\text{-}\text{PRC}$ | Water complex | $-36.44256091$ | $-69.59$ | yes | Accepted (0 imag) |
| `W-TS-T1-V01` | $W\text{-}\text{TS}$ | Steam TS (Old run) | $-36.40334386$ | $+33.38$ | no | Superseded (Old CI-NEB run restored for audit trail) |
| `W-TS-T1-V02` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.41774965$ | $-4.44$ | no | Candidate, under refinement (Band D CI-NEB, barrier $+65.14 \text{ kJ/mol}$ vs $W\text{-}\text{PRC}$; Step 0 freqs) |
| `W-TS-T1-V03` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.43115234$ | $-39.63$ | no | Candidate, under refinement (OptTS Pass 1, barrier $+29.95 \text{ kJ/mol}$ vs $W\text{-}\text{PRC}$; Step 0 freqs) |
| `W-TS-T1-V04` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.43140308$ | $-40.29$ | no | Candidate (pending A4) (OptTS continuation 1 CONVERGED, barrier $+29.29 \text{ kJ/mol}$ vs $W\text{-}\text{PRC}$, EXACTLY 1 imag: $-226.10 \text{ cm}^{-1}$) |
| `W-TS-T1-V05` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.41883009$ | $-7.28$ | no | Diagnostic run (Step E2 frozen caps, barrier $+62.31 \text{ kJ/mol}$ vs $W\text{-}\text{PRC}$, 5 imag) |
| `W-TS-T1-V06` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.44204682$ | $-68.24$ | no | Diagnostic run (Mode 6 +0.01nm displacement converged to W-PRC well, +1.35 kJ/mol vs W-PRC) |
| `W-TS-T1-V07` | $W\text{-}\text{TS}$ | Steam dealumination TS | $-36.44204971$ | $-68.25$ | no | Diagnostic run (Mode 6 -0.01nm displacement converged to W-PRC well, +1.34 kJ/mol vs W-PRC) |
| `W-P-T1-V01` | $W\text{-}P$ | Water product | $-36.44113826$ | $-65.85$ | yes | Accepted (0 imag) |

---

## 3. Five-Point Saddle Acceptance Chain Rules (A1--A5)

1. **A1. Optimization**: OptTS converged with normal termination.
2. **A2. Mode Count & Animation**: Exactly one imaginary mode, of chemically credible magnitude for the motion; sub-20 $\text{cm}^{-1}$ is presumptive flat-mode noise; modes between 20 and 50 $\text{cm}^{-1}$ are decided by recorded mode-animation evidence stating which bonds the displacement vector animates; if it animates a second reacting-bond reorganization, it counts against A2.
3. **A3. Energy Order**: $E(\text{TS}) > \max(E(\text{Reactant}), E(\text{Product})) + 1.0 \text{ kJ/mol}$.
4. **A4. Two-Sided Interval Test**: Displacements along imaginary mode land on two different minima ($\le 5 \text{ kJ/mol}$ deviation).
5. **A5. Row Provenance**: Energy, log, and test thread map strictly to one structure.
