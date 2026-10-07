# CHAPTER THREE

# MATERIALS AND METHODS

## 3.1 Overview of the Approach

This chapter describes how the calculations were set up and how the results were judged. The work is a computational study, so there are no reagents and no apparatus in the usual chemical engineering sense. The materials are the geometric models, and the apparatus is a quantum chemistry program running on two computers. Everything that a reader would need in order to repeat the work is stated here: the composition and construction of the model, the exact keywords passed to the program, the hardware, the sequence in which the calculations were run, and the criteria by which a computed structure was accepted or rejected.

The strategy is a two level treatment. A fast semi-empirical method is used to explore the potential energy surface and to generate candidate structures, and a slower density functional treatment is used to refine and judge them. Figure 3.1 illustrates the sequence.

![Figure 3.1: The two level computational workflow used in this study.](figures/fig3_2_workflow.png)

## 3.2 The Cluster Model

### 3.2.1 Choice of model type

The zeolite framework can be represented either as a periodic crystal or as a finite cluster cut from the crystal and terminated with hydrogen atoms. The periodic representation is the more faithful one because it retains the confinement of the pore and the mechanical constraint of the surrounding lattice. It is also far more expensive, and a hybrid functional calculation on a periodic cell of zeolite Y with a transition state search is beyond the computing resources available to this project.

A cluster model was therefore adopted. The consequence of that choice is stated in Section 1.8 and repeated here for emphasis: a finite cluster is more flexible than the real framework, so the barriers computed on it should be read as lower bounds and the adsorption energies as upper bounds. Because the vanadic acid and water routes were computed on exactly the same cluster with exactly the same methods, the systematic part of that error cancels in the difference between them, and the difference is the quantity on which the conclusions of this work rest.

### 3.2.2 Composition and construction

The model represents one Brønsted acid site within a faujasite framework. It was cut from the faujasite structure so that the central aluminium atom retains its four framework oxygen neighbours and each of the four surrounding silicon atoms retains four oxygen neighbours. Dangling bonds at the periphery were saturated with hydrogen atoms placed along the direction of the bond that was cut, at a bond length of approximately 0.98 Å.

The resulting composition is AlSi₄O₄H₁₃. It contains twenty two atoms, one aluminium, four silicon, four framework oxygen atoms that coordinate the aluminium, nine further oxygen atoms completing the silicon coordination spheres, and thirteen hydrogen atoms comprising the single Brønsted proton and twelve terminating protons. The formula unit is shown schematically below, with the Brønsted proton marked.

```
         H
         |
   Si - O - Al - O - Si
        |    |    |
       Si    O    Si
```

The charge of the cluster is zero and the spin multiplicity is one, and these were set as the charge and multiplicity in all calculations. The Brønsted proton sits on the bridging oxygen between the aluminium and one silicon, which is the configuration that gives the cluster its acidity.

### 3.2.3 Reference state

For either adsorbate, the reference state is the separated cluster plus the free adsorbate molecule, each at its own optimised geometry. The reference energy for the vanadic acid route is therefore

E_ref,V = E(cluster) + E(H₃VO₄)                        (3.1)

and for the steam route

E_ref,W = E(cluster) + E(H₂O)                          (3.2)

Every relative energy reported in Chapter Four is referred to the appropriate zero.

The isolated water molecule and the isolated vanadic acid molecule were each optimised and their frequencies computed separately using a three atom and an eight atom model respectively. The optimised bond lengths were 0.965 Å for the two oxygen hydrogen bonds of water and 1.918 Å for the hydrogen bond angle, in agreement with the accepted experimental geometry to within the accuracy of the method.

The composition of the cluster and the two adsorbates is summarised in Table 3.1.

| System | Formula | Atoms | Charge | Multiplicity | Role |
|---|---|---|---|---|---|
| Cluster | AlSi₄O₄H₁₃ | 22 | 0 | 1 | Reference framework |
| Water | H₂O | 3 | 0 | 1 | Steam baseline adsorbate |
| Vanadic acid | H₃VO₄ | 8 | 0 | 1 | Vanadium route adsorbate |
| Vanadium route complex | AlSi₄O₄H₁₃·H₃VO₄ | 30 | 0 | 1 | Adsorption and reaction states |
| Steam route complex | AlSi₄O₄H₁₃·H₂O | 25 | 0 | 1 | Comparison states |

Table 3.1: Composition of the model systems used in this study.

## 3.3 Computational Methods

### 3.3.1 Software

All calculations were performed with the ORCA quantum chemistry program package (Neese et al., 2020). Two builds were used: version 6.1.0 for the semi-empirical and initial density functional work, and version 6.1.1 for the later density functional work. Both builds used the libint2 and libxc integral and functional libraries, which is recorded here because the numerical output of a functional evaluation depends on the library version that implements it.

ORCA reads a plain text input file and writes a plain text output file. The input file contains a keyword line beginning with an exclamation mark, followed by blocks introduced by a percent sign that set the resources and the technical parameters, and finally the molecular geometry in Cartesian coordinates. A representative input file from this work is reproduced in Table 3.2.

```
! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF DefGrid3 Opt Freq TightOpt

%pal nprocs 4 end
%maxcore 3000

%scf
  MaxIter 300
end

%freq
  Temp 298.15, 1003.15
end

* xyzfile 0 1 v-prc.xyz
```

Table 3.2: Input file for the geometry optimisation and frequency analysis of the vanadic acid adsorption complex at the B3LYP-D3(BJ)/def2-TZVP level.

The keywords in Table 3.2 have the following meanings. B3LYP selects the exchange and correlation functional. D3BJ applies Grimme's third generation empirical dispersion correction with Becke-Johnson damping. def2-TZVP selects the triple zeta valence polarised basis set. RIJCOSX and def2/J accelerate the evaluation of the exact exchange and the Coulomb terms by approximations that are standard for hybrid functionals on systems of this size. TightSCF tightens the self-consistent field convergence criterion. DefGrid3 sets the numerical integration grid. Opt requests geometry optimisation, Freq requests a frequency calculation, and TightOpt tightens the convergence thresholds for the geometry.

### 3.3.2 Semi-empirical level: GFN2-xTB

The exploratory calculations used the GFN2-xTB method (Bannwarth et al., 2019). This is a self-consistent tight binding method rather than a full quantum chemical treatment: it solves an approximate electronic structure problem in a minimal atomic orbital basis, with multipole electrostatics expanded to quadrupole order and a charge dependent dispersion correction included self consistently. The method is parameterised for elements up to radon and requires no system specific parameters, so it can be applied to a vanadium containing model without additional fitting.

The justification for using it is cost. A geometry optimisation and frequency analysis of a thirty atom cluster at the GFN2-xTB level completes in minutes on a laptop, whereas the same job at the B3LYP level requires days on a multi-processor node. The method was therefore used to generate starting geometries for every state on both reaction routes, to locate candidate saddle points, and to provide a first estimate of the energy profile. Its results are reported as such in Chapter Four and are not used as the basis of any conclusion that the density functional results do not also support.

### 3.3.3 Density functional level: B3LYP-D3(BJ)/def2-TZVP

The principal density functional treatment used the B3LYP functional with the D3 dispersion correction and Becke-Johnson damping (Becke, 1993; Lee et al., 1988; Grimme et al., 2011) and the def2-TZVP basis set (Weigend & Ahlrichs, 2005). This combination is the most widely used hybrid level for zeolite and organic reaction energetics, and the dispersion correction is essential when the interaction being studied is partly non-covalent, as the adsorption of a molecule on a framework site is.

Geometry optimisation was carried out with the TightOpt convergence option, and each optimised structure was then subjected to a frequency calculation at the same level. The frequency calculation serves two purposes. It confirms that the structure is a genuine minimum by showing that all of its vibrational modes have real frequencies, and it supplies the zero point energy, the thermal enthalpy correction and the Gibbs energy correction that convert an electronic energy into a quantity comparable with experiment.

### 3.3.4 Second functional: PBE0-D3(BJ)/def2-TZVP

To test whether a computed result is a property of the chemistry or an artefact of one functional, single point energies were computed with the PBE0 functional (Adamo & Barone, 1999) using the same basis set and dispersion correction. These calculations used the geometries obtained at the B3LYP level, so they probe the electronic energy only and not the shape of the potential energy surface. The comparison is therefore a test of the functional and not of the geometry.

### 3.3.5 Technical settings

All calculations used the resolution of identity approximation for the Coulomb integrals with the def2/J auxiliary basis set, and the chain of spheres approximation for the exact exchange, which is the standard efficient scheme for hybrid functionals. The numerical integration grid was DefGrid3 throughout, so that the comparison between states was not contaminated by a change of grid. The self-consistent field procedure was allowed up to three hundred iterations. Resources were set to four parallel processes with three gigabytes of memory each.

## 3.4 Computing Hardware and Execution

The semi-empirical calculations and the initial density functional calculations were run on a Dell Latitude E6430 laptop with sixteen gigabytes of random access memory and a solid state drive, running the ORCA 6.1.0 build. Output files from these runs were written in UTF-16 encoding, which is the Windows default for the program's output stream, and this has a practical consequence that is recorded in Section 3.7: a plain text search of those files returns nothing, and a parser must know the encoding.

The later density functional calculations were run on a virtual machine provisioned for the purpose, using the ORCA 6.1.1 build and writing UTF-8 output. Jobs were submitted with four parallel processes. Table 3.3 records the measured wall clock time for the principal jobs, taken from the run time line that ORCA prints at the end of every output.

| Job | System size | Level | Wall clock time |
|---|---|---|---|
| Water optimisation and frequency | 3 atoms | GFN2-xTB | 35 seconds |
| Vanadic acid optimisation and frequency | 8 atoms | GFN2-xTB | 147 seconds |
| Cluster geometry optimisation | 22 atoms | B3LYP-D3(BJ) | 30 minutes |
| Vanadic acid adsorption complex | 30 atoms | B3LYP-D3(BJ) | 5 hours 28 minutes |
| Water adsorption complex | 25 atoms | B3LYP-D3(BJ) | 3 hours 34 minutes |
| Chemisorbed intermediate | 30 atoms | B3LYP-D3(BJ) | 27 hours |
| Second intermediate | 30 atoms | B3LYP-D3(BJ) | 11 hours 12 minutes (not converged) |
| Reaction product | 30 atoms | B3LYP-D3(BJ) | 5 hours (not converged) |
| Saddle point attempt, first bond cleavage | 30 atoms | B3LYP-D3(BJ) | 1 day 4 hours (rejected) |
| Single point energies, ten states | up to 30 atoms | PBE0-D3(BJ) | 3 seconds to 11 minutes each |

Table 3.3: Measured wall clock times for the principal calculations.

The table carries an important engineering message that is often left out of computational reports. The cost of a hybrid density functional calculation does not rise gently with system size. Increasing the cluster from twenty two to thirty atoms, a change of thirty six per cent in atom count, raised the cost of a converged optimisation and frequency analysis from thirty minutes to more than five hours, a tenfold increase. Adding a transition state search with a computed initial Hessian multiplied it again. This is why the reaction profile reported in Chapter Four is complete at the semi-empirical level and partial at the density functional level: the two levels differ in cost by roughly two orders of magnitude, and the available computing budget was fixed.

## 3.5 Calculation Sequence

### 3.5.1 Reference species

Each of the two adsorbates and the bare cluster were optimised and their frequencies computed. For water this was straightforward. For vanadic acid, twenty six optimisation cycles were required before the convergence criteria were met, which indicates a flexible potential energy surface with several shallow minima. The isolated vanadic acid minimum obtained from this procedure was used as the reference for the vanadium route.

### 3.5.2 Adsorption complexes

Starting geometries for the adsorption complexes were built by placing the adsorbate above the Brønsted acid site at a separation of approximately 0.2 nanometres, with the acidic proton of the adsorbate directed towards the framework oxygen and the vanadium atom oriented so that it could approach the aluminium. Both complexes were then optimised without constraint. The vanadic acid complex required forty optimisation cycles and the water complex sixty three, both converging normally.

### 3.5.3 Stationary points along the vanadium route

The intended route for the vanadium series, with the atom economy of each step noted, is set out below.

Adsorption: AlSi₄O₄H₁₃ + H₃VO₄ → AlSi₄O₄H₁₃·H₃VO₄   (3.3)

Chemisorption: AlSi₄O₄H₁₃·H₃VO₄ → [AlSi₄O₄H₁₂]·(VO(OH)₃)·H₂O + H⁺   (3.4)

First aluminium oxygen cleavage: ≡Si–O–Al≡ + H₃VO₄ → ≡Si–OH + ≡Al(OH)(H₃VO₄)   (3.5)

Second cleavage: ≡Al(OH)(H₃VO₄) + H₂O → ≡Al(OH)₂ + H₃VO₄(ads)   (3.6)

Third cleavage and detachment: the aluminium atom is fully separated from the framework and a silanol nest remains   (3.7)

Each of these states was generated at the GFN2-xTB level by driving the appropriate internal coordinate and then relaxing the resulting structure, and each candidate was carried forward to the density functional level. Where a candidate saddle point was obtained, its identity was tested as described in Section 3.6.

### 3.5.4 Stationary points along the steam route

The water series was generated in the same way and in the same sequence, so that the two routes are directly comparable. The reaction sequence for steam is the one established in the literature (Malola et al., 2012), in which water adsorbs on the aluminium atom in the position anti to the Brønsted acid site before any bond is broken, the aluminium oxygen bond is hydrolysed, and the process repeats until the aluminium has been extracted as Al(OH)₃(H₂O).

### 3.5.5 Saddle point location

Three techniques were used to find transition states. A relaxed potential energy scan was run along the coordinate expected to change, and the structure at the maximum of the scan was used as a starting point. The nudged elastic band method was used to trace a minimum energy path between two known minima, and the highest image on the path was taken as a transition state candidate. Finally, the candidate was refined by a transition state optimisation with an exact initial Hessian computed at the same level.

### 3.5.6 Intrinsic reaction coordinate

Where a saddle point was accepted, the intrinsic reaction coordinate was followed in both directions from the transition state to confirm that the two ends of the path are the intended minima. This is the standard test of whether a saddle point connects the states that the mechanism requires.

## 3.6 Criteria for Accepting a Stationary Point

A computed structure was accepted as a minimum only if the geometry optimisation terminated normally, the program reported that the optimisation had converged according to its own criteria, and the frequency calculation returned no imaginary modes.

A structure was accepted as a transition state only if all five of the following were satisfied.

1. The transition state optimisation converged and the run terminated normally.

2. Exactly one imaginary mode was found, and its frequency was chemically credible for the motion it represents. A magnitude below 20 cm⁻¹ was treated as presumptive numerical noise rather than a real saddle.

3. The energy of the candidate lay above the energies of both states it is supposed to connect.

4. Displacing the structure along the imaginary mode in both directions led to two different minima, each within 5 kJ mol⁻¹ of the corresponding endpoint.

5. The energy, the log file and the test calculation all referred unambiguously to one and the same structure.

The fourth criterion deserves explanation because it is the one that rejected the most candidates in this work. A structure can satisfy the first three criteria and still not be the saddle point that connects the two states of interest. Displacing it along its imaginary mode should carry the system downhill to the two minima on either side. If instead the displacement carries the system into a well that is not one of the two endpoints, the structure is a saddle point of some other reaction or a numerical artefact of the optimisation, and it was rejected on that ground.

## 3.7 Data Handling and Verification

Because the number of calculations was large and because the repository accumulated several attempts at some states, a program was written to read every ORCA output file and extract its termination status, its convergence status, its final energy, its convergence gradient, its imaginary mode count and its wall clock time into a single machine readable table. That program, the register it produced and the script that generates the tables of Chapter Four from the register are all retained in the project archive, so that every number reported in this thesis can be traced back to the specific log file it came from.

Two handling details are recorded because they caused errors before they were corrected. First, the output files of the laptop runs are UTF-16 encoded while the cloud runs are UTF-8, and a parser that assumes one encoding silently returns empty results for half of the archive. Second, ORCA echoes the input file into the log before it does any work, so a search for a status keyword will match the text of an input comment if the input echo is not stripped first. Both issues were resolved before the tables in Chapter Four were generated.

## 3.8 Thermochemistry

Electronic energies alone are not sufficient for a comparison at a temperature of 1003 K. The frequency calculation of each converged structure supplied the zero point energy and the thermal corrections to the enthalpy and the Gibbs energy at two temperatures, 298.15 K and 1003.15 K. The second temperature was chosen to represent the regenerator, where the temperature is of the order of 700 to 760 °C.

For a reaction of the form cluster + adsorbate → complex, the adsorption energy was computed as

ΔE = E(complex) − E(cluster) − E(adsorbate)            (3.8)

and the corresponding Gibbs energy as

ΔG = ΔE + ΔG_corr(complex) − ΔG_corr(cluster) − ΔG_corr(adsorbate)   (3.9)

where the correction terms are the G − E(el) values printed by ORCA in the frequency output. The zero point corrected energy and the enthalpy were computed in the same way using the corresponding corrections.

One further caution applies and was taken from the auditing literature on this system. Where a cluster changes its geometry during a reaction, the frequencies of the initial and final states are not a consistent basis for a Gibbs energy difference unless both are true minima of the same cluster, because the harmonic approximation assumes small displacements about a single well. The corrections reported in Chapter Four are therefore used to describe the direction and rough magnitude of the temperature effect, not to assign precise free energy values.

## 3.9 Counterpoise Correction

When two molecules are brought together and their energies computed in a finite basis set, each fragment can borrow basis functions from the other and thereby lower its own energy artificially. The resulting error is called basis set superposition error, and it inflates the computed binding energy of a complex. The standard correction is the counterpoise procedure of Boys and Bernardi, in which each fragment is re-computed in the presence of the other fragment's basis functions with that fragment's nuclei removed.

The procedure was set up for the two adsorption complexes of this work. In ORCA the fragments must be declared explicitly and one of them marked as a ghost, as follows.

```
%frag
  Definition
    1 {0 1 2 ... 21} end
    2 {22 23 ... 29} end
  end
end
%geom
  GhostFrags {1} end
end
```

Table 3.4: Fragment definition required by ORCA for a counterpoise calculation, shown for the thirty atom vanadic acid complex in which atoms one to twenty two are the cluster and atoms twenty three to thirty are the adsorbate.

Two calculations are needed for each complex, one in which the first fragment is ghosted and one in which the second is. In this work the counterpoise jobs for the vanadic acid complex did not complete within the computing budget, and the two jobs for the water complex completed but returned energies that were not carried forward into the analysis. The reported adsorption energies are therefore uncorrected, and the binding energies in Chapter Four are identified accordingly. This is a known and quantified limitation of the present results rather than an oversight, and it is listed again in Section 1.8 and in the recommendations of Chapter Five.

## 3.10 Summary of Method

Table 3.5 collects the essential parameters of the calculation for reference.

| Item | Setting |
|---|---|
| Program | ORCA 6.1.0 and 6.1.1 |
| Exploratory method | GFN2-xTB |
| Principal density functional | B3LYP with D3 dispersion and Becke-Johnson damping |
| Second density functional | PBE0 with D3 dispersion and Becke-Johnson damping |
| Basis set | def2-TZVP with def2/J auxiliary basis |
| Integration grid | DefGrid3 throughout |
| Acceleration | RIJCOSX for exact exchange, resolution of identity for Coulomb |
| Geometry optimisation threshold | TightOpt |
| Frequencies | Computed for every accepted stationary point, at 298.15 K and 1003.15 K |
| Saddle point validation | One imaginary mode, energy ordering, and two sided displacement test |
| Hardware | Dell Latitude E6430, 16 GB RAM, SSD for the semi-empirical level; four process virtual machine for density functional work |

Table 3.5: Summary of the computational parameters used in this study.
