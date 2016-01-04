Title: Quantum machine learning in 2015
Date: 2016-01-04 17:10
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Machine learning, Quantum information theory
Slug: qml-in-2015
Summary: Quantum machine learning as a research field is exploding: here we give a brief overview of the relevant papers that appeared on arXiv in 2015.

It is getting really difficult to keep track of the developments of the
field. I counted nearly seventy relevant papers on arXiv alone, and my
scope is rather narrow. The first [QML
workshop](http://research.microsoft.com/en-us/events/qml/default.aspx)
happened at [NIPS](https://nips.cc/Conferences/2015) in December.
More workshops are coming: there will be a workshop on [Physics and
Machine Learning: Emerging
Paradigms](https://www.elen.ucl.ac.be/esann/index.php?pg=specsess#Physics)
at [ESANN](https://www.elen.ucl.ac.be/esann/index.php) in April, and
another [QML workshop](http://www.quantummachinelearning.org/) in South
Africa in July, followed by a summer school in 2017.

The year certainly revolved around adiabatic quantum optimization and
D-Wave. Apart from the big guys investing in it, a [new
company](http://1qbit.com/) started to offer consulting, and they also
do genuine research on the side.

The whole exercise of writing up the year's advances is somewhat
redundant, as an overview article appeared less than a month ago (Adcock
et al. 2015). Nevertheless, I like to collect references and links for
my own benefit, so here they are.

A year of annealing
===================

Most of the activity focus on D-Wave and much progress has been made
understanding its limits and advantages. There was also a scattering of
papers talking about quantum annealing and optimization with no
reference to implementation.

Hardware
--------

A few papers dealt with understanding the implementation issues that one
faces when using a D-Wave system. For instance, the couplings might have
persistent biases, and if we are able to recalibrate them, optimization
performance is bound to improve (Perdomo-Ortiz et al. 2015). A similar
problem appears in large optimization problems: they are annealed at
higher temperatures due analogue control errors, which can be addressed,
yielding better scaling (King 2015).

Apparently, a small number very hard instances disproportionally
increase the total time to solve a set of random input instance of an
optimization problem, which we can call "heavy tails". It is possible to
suppress such degenerate cases in the D-Wave annealer, leading to a
performance that is magnitudes better (A. D. King et al. 2015)

Finally, a manuscript studied the vulnerability of quantum annealers to
qubit and coupler failures on Chimera topologies (Melchert, Katzgraber,
and Novotny 2015).

Benchmarking and quantum advantage
----------------------------------

Great progress has been made to verify the advantages of using a quantum
annealer. To start of, we need rigorous verifiable benchmarks in place
of arguments over the physical properties (Katzgraber et al. 2015). The
Time-to-target metric is such, identifying low-cost target solutions
found by the D-Wave processor within very short time limits, and then
asking how much time competing software solvers need to find solution
energies of matching or better quality (J. King et al. 2015)

A wave of papers suggest comparing simulated (thermal) annealing,
simulated quantum annealing, and physical quantum annealing to
understand the limits and advantages of the adiabatic method (Sowa et
al. 2015). Simulated quantum annealing itself has clear advantages over
simulated annealing in a physics problem (Zanca and Santoro 2015), but
the relationship between simulated and physical quantum annealing is
more interesting. Simulated quantum annealing relies on different
flavours of quantum Monte Carlo simulations. The path-integral quantum
Monte Carlo algorithm was found to succeed in the same regimes where
quantum adiabatic optimization succeeds (Brady and Dam 2015, Isakov et
al. (2015)), while the projective variant seems to be more efficient in
simulations (Inack and Pilati 2015).

What type of objective functions work well? Not all that surprisingly,
tall and narrow energy barriers are best (Denchev, Boixo, et al. 2015).
In a more surprising turn, in some cases, short and narrow barriers can
also give a quantum advantage, and we might even relax the adiabatic
dynamics (Muthukrishnan, Albash, and Lidar 2015). Non-adiabatic
annealing schedules apparently also help with the "heavy tails"
(Steiger, Rønnow, and Troyer 2015). These are indications that a pure,
idealistic adiabatic quantum optimization might actually be overrated.

In any case, the annealing schedule depends on the gap between the
ground state and the lowest excited state throughout the adiabatic
change. Identifying this analytically is a hard problem in general.
There is a new analytical result for the case of tall and narrow cost
functions (Kong and Crosson 2015). Then introducing intermediate
Hamiltonians can help achieving better gaps (Zeng, Zhang, and Sarovar
2015). It seems, however, that these Hamiltonians have to be carefully
crafted, as randomly constructed ones improve the gap only by a small
margin. The relationship between the gap and the annealing time is not
entirely well understood either, and sometimes we end up with
intractable problems while respecting the scaling law (Knysh 2015).

Sampling a Boltzmann distribution
---------------------------------

It is tempting to be able to a sample a Boltzmann (Gibbs) distribution
for a variety of applications. With the D-Wave hardware, the
distribution of the ground state and excited states roughly follows the
Boltzmann distribution, which can be used for studying spin glasses and
probing the performance of quantum annealing (Chancellor et al. 2015).

A few papers before suggested training reduced or full Boltzmann
machines this way, because then we can entirely bypass the contrastive
divergence algorithm that is normally used to train these networks.
Using the D-Wave machine, we can obtain some tangible results (Adachi
and Henderson 2015), even if we can only estimate the effective
temperature (Benedetti et al. 2015). Three talks at the NIPS workshop
were also about this approach.

Other applications
------------------

[Structural risk
minimization](https://en.wikipedia.org/wiki/Structural_risk_minimization)
pivots on regularization, which ensures the sparsity of a learned model.
We usually cheat on the regularization on relax the optimization problem
underlying learning to end up with a convex objective function, which in
turn we can solve efficiently. This is exactly where quantum adiabatic
optimization could be huge from the perspective of statistical learning
theory: theoretically we can solve nonconvex objectives fast. Totally
corrective boosting aims to do just that, either by simulated quantum
annealing or by the real physical process (Denchev, Ding, et al. 2015).

Last year we have seen a paper on applying quantum resources to a
topological learning method called persistent homology. Keeping the
topological theme, a paper proposes using quantum annealing to calculate
the homology of point clouds (Dridi and Alghassi 2015).

Moving on to more generic optimization problems, we can solve larger
problems on the D-Wave annealer by iteratively finding the local optimum
of smaller chunks (Rosenberg et al. 2015). Inequality constraints are
always trouble because they cannot be simply added with Lagrange
multipliers to the objective function, but there is a new way of dealing
with them using the quantum adiabatic approach (Ronagh, Woods, and
Iranmanesh 2015). A curious application of the D-Wave hardware is
job-shop scheduling (Venturelli, Marchand, and Rojo 2015).

More neural networks
====================

Returning for a moment to Boltzmann sampling, following last years
proposal for training a Boltzmann machine with state preparation and
subsequent sampling, a paper by the same authors follows the same
protocol with a classical simulation. The resulting algorithm is called
quantum-inspired deep learning (Wiebe et al. 2015). It is an interesting
way how insights from quantum computing can give hints to improve
classical algorithms.

A new training algorithm for a quantum perceptron can compute the XOR
function (Seow, Behrman, and Steck 2015). This [XOR
problem](https://en.wikipedia.org/wiki/Perceptrons_%28book%29#The_XOR_affair)
with the perceptron has been around for about fifty years.

The great thing about quantum neural networks that they are the closest
to physical implementations, apart from adiabatic quantum optimization.
In 2015, there was a proposal for a classical optical system for
recurrent neural networks (Hermans et al. 2015), a nano-optical
perceptron (Tezak and Mabuchi 2015), and an actual implementation using
quantum dots (M. V. Altaisky et al. 2015, Mikhail V. Altaisky et al.
(2015)).

Causal networks
===============

Probabilistic inference, Bayesian or causal networks lie closer to
symbolic AI, and naturally the progress continues to generalize results
to the quantum case. For a starter, we can use quantum conditional
operators to talk about probabilistic inference, with an immediate
application to the Monty Hall problem (Glos and Kurzyk 2015).

Nevertheless, the task in general is hard, primarily due to the
entanglement and nonlocal correlations. Even defining causality is
difficult, and we need to extend the notion (Oreshkov and Giarmatzi
2015). Then, the original Reichenbach Common Cause Principle assumed
that the arrow between cause and effect and time direction are the same.
A new manuscript goes beyond this, giving algorithmic rather than
statistical foundations to causal inference (Janzing, Chaves, and
Schoelkopf 2015). Another generalization uses open quantum systems and
quantum channels, and avoids Bayesian inference (Costa and Shrapnel
2015). Despite the progress, it is still an open problem how causal
models, nonlocality, and the nonsignalling principle fit together (Evans
2015).

Privacy
=======

On a good day, quantum cryptography cannot be broken. For this reason,
the UK government will probably ban it soon enough. Until then, there is
a series of proposals to perform quantum machine learning either
remotely or by slicing up the learning problem to small chunks (Bang,
Lee, and Jeong 2015, Ying, Ying, and Feng (2015), Sheng and Zhou
(2015)). It is a fun idea to play with, especially when the learning
algorithm itself cannot compromise privacy.

Machine learning applied on quantum physics problems
====================================================

This topic leads out of the domain of quantum machine learning, as here
we are interested in applying the principles of learning theory to solve
problems in quantum physics. Yet, there is a smooth transition. For
instance, we can use a quantum neural network to learn the unknown
entanglement of a system in a way that is robust to noise and
decoherence (Behrman et al. 2015). Another manuscript derived limits on
the learnability of quantum measurements and quantum state (Cheng,
Hsieh, and Yeh 2015). In all cases the authors used quantum resources
and ideas from learning theory to derive results in quantum physics.

If we abandon quantum resources in learning and uses classical
algorithms in quantum physics problems, we encounter a flood of new
papers. Two paper suggests learning target quantum gates: in one case,
we would like to map the gates to a spin system consisting of target and
ancilla qubits (Banchi, Pancotti, and Bose 2015), in the other case,
differential evolution approximates three-qubit gates on an architecture
of nearest-neighbor-coupled superconducting artificial atoms
(Zahedinejad, Ghosh, and Sanders 2015). Refreshingly for a physics
paper, the code for the latter is
[available](https://github.com/ezahedin/DE_high-dimensional) under an
open source licence.

Calibration is core to quantum computers at any scale, and naturally the
same stands for quantum simulators. (Wiebe, Granade, and Cory 2015)
proposes learning a Hamiltonian model for a larger quantum system using
a small quantum simulator using Bayesian updates, then iteratively
building up larger and larger systems.

Moving beyond quantum computation, a reinforcement learning scheme helps
producing Bose-Einstein condensates (Wigley et al. 2015). The code is
also [available](https://github.com/michaelhush/M-LOOP) for this
project. An evolutionary learning algorithms helps characterizing
decohering quantum systems (Stenberg, Köhn, and Wilhelm 2015). On the
more general level of quantum control, a manuscript proposes training on
a sample, followed by testing, which eerily resembles supervised
learning (Dong et al. 2015).

Others
======

Departing from the angle of the theory of computation and focusing on a
very specific learning problem of a binary-output function, a manuscript
demonstrates a quantum advantage in the number oracle queries using a
system of five transmon qubits (Ristè et al. 2015).

Proposals for exponential speedup in quantum machine learning tend to
stem from the HHL algorithm for solving a linear system. There is an
update to this algorithm with exponentially improved dependence on
precision (Childs, Kothari, and Somma 2015).

The concept of agency has not been well explored thus far. We can ask
what it means to have a quantum agent: what does it learn, how do we
know it learns, and how does it interact with its (quantum) environment?
(Dunjko, Friis, and Briegel 2015, Dunjko, Taylor, and Briegel (2015),
Wiebe and Granade (2015)). These are important questions, but the
answers remain elusive.

References
==========

Adachi, Steven H., and Maxwell P. Henderson. 2015. “Application of
Quantum Annealing to Training of Deep Neural Networks.”
*[arXiv:1510.06356](http://arxiv.org/abs/1510.06356)*.

Adcock, Jeremy, Euan Allen, Matthew Day, Stefan Frick, Janna Hinchliff,
Mack Johnson, Sam Morley-Short, Sam Pallister, Alasdair Price, and
Stasja Stanisic. 2015. “Advances in Quantum Machine Learning.”
*[arXiv:1512.02900](http://arxiv.org/abs/1512.02900)*.

Altaisky, M. V., N. N. Zolnikova, N. E. Kaputkina, V. A. Krylov, Yu. E.
Lozovik, and N. S. Dattani. 2015. “Towards a Feasible Implementation of
Quantum Neural Networks Using Quantum Dots.” *[arXiv:1503.05125](http://arxiv.org/abs/1503.05125)*.

Altaisky, Mikhail V., Nadezhda N. Zolnikova, Natalia E. Kaputkina,
Victor A. Krylov, Yurii E. Lozovik, and Nikesh S. Dattani. 2015.
“Entanglement in a Quantum Neural Network Based on Quantum Dots.”
*[arXiv:1512.01141](http://arxiv.org/abs/1512.01141)*.

Banchi, Leonardo, Nicola Pancotti, and Sougato Bose. 2015. “Quantum Gate
Learning in Engineered Qubit Networks: Toffoli Gate with Always-on
Interactions.” *[arXiv:1509.04298](http://arxiv.org/abs/1509.04298)*.

Bang, Jeongho, Seung-Woo Lee, and Hyunseok Jeong. 2015. “Protocol for
Secure Quantum Machine Learning at a Distant Place.” *[arXiv:1504.04929](http://arxiv.org/abs/1504.04929)*.

Behrman, E. C., N. H. Nguyen, J. E. Steck, and M. McCann. 2015. “Quantum
Neural Computation of Entanglement Is Robust to Noise and Decoherence.”
*[arXiv:1510.09173](http://arxiv.org/abs/1510.09173)*.

Benedetti, Marcello, John Realpe-Gómez, Rupak Biswas, and Alejandro
Perdomo-Ortiz. 2015. “Estimation of Effective Temperatures in a Quantum
Annealer and Its Impact in Sampling Applications: A Case Study Towards
Deep Learning Applications.” *[arXiv:1510.07611](http://arxiv.org/abs/1510.07611)*.

Brady, Lucas T., and Wim van Dam. 2015. “Quantum Monte Carlo Simulations
of Tunneling in Quantum Adiabatic Optimization.” *[arXiv:1509.02562](http://arxiv.org/abs/1509.02562)*.

Chancellor, Nicholas, Szilard Szoke, Walter Vinci, Gabriel Aeppli, and
Paul A. Warburton. 2015. “Maximum-Entropy Inference with a Programmable
Annealer.” *[arXiv:1506.08140](http://arxiv.org/abs/1506.08140)*.

Cheng, Hao-Chung, Min-Hsiu Hsieh, and Ping-Cheng Yeh. 2015. “The
Learnability of Unknown Quantum Measurements.” *[arXiv:1501.00559](http://arxiv.org/abs/1501.00559)*.

Childs, Andrew M., Robin Kothari, and Rolando D. Somma. 2015. “Quantum
Linear Systems Algorithm with Exponentially Improved Dependence on
Precision.” *[arXiv:1511.02306](http://arxiv.org/abs/1511.02306)*.

Costa, Fabio, and Sally Shrapnel. 2015. “Quantum Causal Modelling.”
*[arXiv:1512.07106](http://arxiv.org/abs/1512.07106)*.

Denchev, Vasil S., Sergio Boixo, Sergei V. Isakov, Nan Ding, Ryan
Babbush, Vadim Smelyanskiy, John Martinis, and Hartmut Neven. 2015.
“What Is the Computational Value of Finite Range Tunneling?”
*[arXiv:1512.02206](http://arxiv.org/abs/1512.02206)*.

Denchev, Vasil S., Nan Ding, Shin Matsushima, S. V. N. Vishwanathan, and
Hartmut Neven. 2015. “Totally Corrective Boosting with Cardinality
Penalization.” *[arXiv:1504.01446](http://arxiv.org/abs/1504.01446)*.

Dong, Daoyi, Mohamed A. Mabrok, Ian R. Petersen, Bo Qi, Chunlin Chen,
and Herschel Rabitz. 2015. “Sampling-Based Learning Control for Quantum
Systems with Uncertainties.” *IEEE Transactions on Control Systems
Technology*. IEEE, 1–1.
doi:[10.1109/tcst.2015.2404292](https://doi.org/10.1109/tcst.2015.2404292).

Dridi, Raouf, and Hedayat Alghassi. 2015. “Homology Computation of Large
Point Clouds Using Quantum Annealing.” *[arXiv:1512.09328](http://arxiv.org/abs/1512.09328)*.

Dunjko, Vedran, Nicolai Friis, and Hans J. Briegel. 2015.
“Quantum-Enhanced Deliberation of Learning Agents Using Trapped Ions.”
*New J. Phys.* 17 (2). IOP Publishing: 023006.
doi:[10.1088/1367-2630/17/2/023006](https://doi.org/10.1088/1367-2630/17/2/023006).

Dunjko, Vedran, Jacob M. Taylor, and Hans J. Briegel. 2015. “Framework
for Learning Agents in Quantum Environments.” *[arXiv:1507.08482](http://arxiv.org/abs/1507.08482)*.

Evans, Peter W. 2015. “Quantum Causal Models, Faithfulness and
Retrocausality.” *[arXiv:1506.08925](http://arxiv.org/abs/1506.08925)*.

Glos, Adam, and Dariusz Kurzyk. 2015. “Quantum Inferring Acausal
Structure.” *[arXiv:1504.01917](http://arxiv.org/abs/1504.01917)*.

Hermans, Michiel, Miguel Soriano, Joni Dambre, Peter Bienstman, and Ingo
Fischer. 2015. “Photonic Delay Systems as Machine Learning
Implementations.” *[arXiv:1501.02592](http://arxiv.org/abs/1501.02592)*.

Inack, E. M., and S. Pilati. 2015. “Simulated Quantum Annealing of
Double-Well and Multi-Well Potentials.” *[arXiv:1510.04650](http://arxiv.org/abs/1510.04650)*.

Isakov, Sergei V., Guglielmo Mazzola, Vadim N. Smelyanskiy, Zhang Jiang,
Sergio Boixo, Hartmut Neven, and Matthias Troyer. 2015. “Understanding
Quantum Tunneling Through Quantum Monte Carlo Simulations.”
*[arXiv:1510.08057](http://arxiv.org/abs/1510.08057)*.

Janzing, Dominik, Rafael Chaves, and Bernhard Schoelkopf. 2015.
“Algorithmic Independence of Initial Condition and Dynamical Law in
Thermodynamics and Causal Inference.” *[arXiv:1512.02057](http://arxiv.org/abs/1512.02057)*.

Katzgraber, Helmut G., Firas Hamze, Zheng Zhu, Andrew J. Ochoa, and H.
Munoz-Bauza. 2015. “Seeking Quantum Speedup Through Spin Glasses: The
Good, the Bad, and the Ugly.” *Physical Review X* 5 (3). American
Physical Society (APS).
doi:[10.1103/physrevx.5.031026](https://doi.org/10.1103/physrevx.5.031026).

King, Andrew D. 2015. “Performance of a Quantum Annealer on
Range-Limited Constraint Satisfaction Problems.” *[arXiv:1502.02098](http://arxiv.org/abs/1502.02098)*.

King, Andrew D., Emile Hoskinson, Trevor Lanting, Evgeny Andriyash, and
Mohammad H. Amin. 2015. “Degeneracy, Degree, and Heavy Tails in Quantum
Annealing.” *[arXiv:1512.07325](http://arxiv.org/abs/1512.07325)*.

King, James, Sheir Yarkoni, Mayssam M. Nevisi, Jeremy P. Hilton, and
Catherine C. McGeoch. 2015. “Benchmarking a Quantum Annealing Processor
with the Time-to-Target Metric.” *[arXiv:1508.05087](http://arxiv.org/abs/1508.05087)*.

Knysh, Sergey. 2015. “Computational Bottlenecks of Quantum Annealing.”
*[arXiv:1506.08608](http://arxiv.org/abs/1506.08608)*.

Kong, Linghang, and Elizabeth Crosson. 2015. “The Performance of the
Quantum Adiabatic Algorithm on Spike Hamiltonians.” *[arXiv:1511.06991](http://arxiv.org/abs/1511.06991)*.

Melchert, O., Helmut G. Katzgraber, and M. A. Novotny. 2015. “Site and
Bond Percolation Thresholds in *K*<sub>*n*, *n*</sub>-Based Lattices:
Vulnerability of Quantum Annealers to Random Qubit and Coupler Failures
on Chimera Topologies.” *[arXiv:1511.07078](http://arxiv.org/abs/1511.07078)*.

Muthukrishnan, Siddharth, Tameem Albash, and Daniel A. Lidar. 2015.
“Tunneling and Speedup in Quantum Optimization for Permutation-Symmetric
Problems.” *[arXiv:1511.03910](http://arxiv.org/abs/1511.03910)*.

Oreshkov, Ognyan, and Christina Giarmatzi. 2015. “Causal and Causally
Separable Processes.” *[arXiv:1506.05449](http://arxiv.org/abs/1506.05449)*.

Perdomo-Ortiz, Alejandro, Bryan O’Gorman, Joseph Fluegemann, Rupak
Biswas, and Vadim N. Smelyanskiy. 2015. “Determination and Correction of
Persistent Biases in Quantum Annealers.” *[arXiv:1503.05679](http://arxiv.org/abs/1503.05679)*.

Ristè, D., Marcus P. da Silva, Colm A. Ryan, Andrew W. Cross, John A.
Smolin, Jay M. Gambetta, Jerry M. Chow, and Blake R. Johnson. 2015.
“Demonstration of Quantum Advantage in Machine Learning.”
*[arXiv:1512.06069](http://arxiv.org/abs/1512.06069)*.

Ronagh, Pooya, Brad Woods, and Ehsan Iranmanesh. 2015. “Solving
Constrained Quadratic Binary Problems via Quantum Adiabatic Evolution.”
*[arXiv:1509.05001](http://arxiv.org/abs/1509.05001)*.

Rosenberg, Gili, Mohammad Vazifeh, Brad Woods, and Eldad Haber. 2015.
“Building an Iterative Heuristic Solver for a Quantum Annealer.”
*[arXiv:1507.07605](http://arxiv.org/abs/1507.07605)*.

Seow, Kok-Leong, Elizabeth Behrman, and James Steck. 2015. “Efficient
Learning Algorithm for Quantum Perceptron Unitary Weights.”
*[arXiv:1512.00522](http://arxiv.org/abs/1512.00522)*.

Sheng, Yu-Bo, and Lan Zhou. 2015. “Blind Quantum Machine Learning.”
*[arXiv:1507.07195](http://arxiv.org/abs/1507.07195)*.

Sowa, A P, M J Everitt, J H Samson, S E Savel’ev, A M Zagoskin, S
Heidel, and J C Zúñiga-Anaya. 2015. “Recursive Simulation of Quantum
Annealing.” *Journal of Physics A: Mathematical and Theoretical* 48
(41). IOP Publishing: 415301.
doi:[10.1088/1751-8113/48/41/415301](https://doi.org/10.1088/1751-8113/48/41/415301).

Steiger, Damian S., Troels F. Rønnow, and Matthias Troyer. 2015. “Heavy
Tails in the Distribution of Time to Solution for Classical and Quantum
Annealing.” *Physical Review Letters* 115 (23). American Physical
Society (APS).
doi:[10.1103/physrevlett.115.230501](https://doi.org/10.1103/physrevlett.115.230501).

Stenberg, Markku P. V., Oliver Köhn, and Frank K. Wilhelm. 2015.
“Characterization of Decohering Quantum Systems: Machine Learning
Approach.” *[arXiv:1510.05655](http://arxiv.org/abs/1510.05655)*.

Tezak, Nikolas, and Hideo Mabuchi. 2015. “A Coherent Perceptron for
All-Optical Learning.” *[arXiv:1501.01608](http://arxiv.org/abs/1501.01608)*.

Venturelli, Davide, Dominic J. J. Marchand, and Galo Rojo. 2015.
“Quantum Annealing Implementation of Job-Shop Scheduling.”
*[arXiv:1506.08479](http://arxiv.org/abs/1506.08479)*.

Wiebe, Nathan, and Christopher Granade. 2015. “Can Small Quantum Systems
Learn?” *[arXiv:1512.03145](http://arxiv.org/abs/1512.03145)*.

Wiebe, Nathan, Christopher Granade, and D G Cory. 2015. “Quantum
Bootstrapping via Compressed Quantum Hamiltonian Learning.” *New Journal
of Physics* 17 (2). IOP Publishing: 022005.
doi:[10.1088/1367-2630/17/2/022005](https://doi.org/10.1088/1367-2630/17/2/022005).

Wiebe, Nathan, Ashish Kapoor, Christopher Granade, and Krysta M Svore.
2015. “Quantum Inspired Training for Boltzmann Machines.”
*[arXiv:1507.02642](http://arxiv.org/abs/1507.02642)*.

Wigley, P. B., P. J. Everitt, A. van den Hengel, J. W. Bastian, M. A.
Sooriyabandara, G. D. McDonald, K. S. Hardman, et al. 2015. “Fast
Machine-Learning Online Optimization of Ultra-Cold-Atom Experiments.”
*[arXiv:1507.04964](http://arxiv.org/abs/1507.04964)*.

Ying, Shenggang, Mingsheng Ying, and Yuan Feng. 2015. “Quantum
Privacy-Preserving Data Mining.” *[arXiv:1512.04009](http://arxiv.org/abs/1512.04009)*.

Zahedinejad, Ehsan, Joydip Ghosh, and Barry C. Sanders. 2015. “Designing
High-Fidelity Single-Shot Three-Qubit Gates: A Machine Learning
Approach.” *[arXiv:1511.08862](http://arxiv.org/abs/1511.08862)*.

Zanca, Tommaso, and Giuseppe E. Santoro. 2015. “Quantum Annealing
Speedup over Simulated Annealing on Random Ising Chains.”
*[arXiv:1511.01906](http://arxiv.org/abs/1511.01906)*.

Zeng, Lishan, Jun Zhang, and Mohan Sarovar. 2015. “Schedule Path
Optimization for Quantum Annealing and Adiabatic Quantum Computing.”
*[arXiv:1505.00209](http://arxiv.org/abs/1505.00209)*.


