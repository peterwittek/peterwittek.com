Title: End-of-year updates on quantum machine learning
Date: 2014-12-31 17:10 
Author: Peter 
Category: Quantum machine learning 
Tags: Quantum machine learning, Quantum information theory, Machine learning 
Slug: end-of-year-update-quantum-machine-learning
Summary: Another handful of papers on quantum machine learning that appeared in the last two months of 2014, and perhaps slightly earlier.

Over the past two months since I [last]({filename}/recent-advances-in-quantum-machine-learning.md)
discussed the latest papers, there has been quite a bit of progress. A
[Wikipedia page](https://en.wikipedia.org/wiki/Quantum_machine_learning)
on quantum machine learning was launched in mid-November -- I am hoping
to start helping out editing it soon. Many new papers appeared on
arXiv -- once there were three in one day -- and I also found some which
I missed earlier. Here I quickly jot down a few notes relating to these
manuscripts.

New papers
----------

It is hard not to get excited about a paper with the title "Quantum Deep
Learning". The content is even better. The way we train neural networks
did not change that much since the perceptron appeared in the sixties:
we either do some kind of a gradient descent if the optimization is
such, or some heuristic search for the optimum with nonconvex objective
functions. This is true for deep learning networks too. This paper
bypasses the iterative training all together. The authors suggest a
state preparation followed by sampling. The focus is on Boltzmann
machines, where the output of the network is based on the Gibbs
distribution. The main challenge is the state preparation: this should
be such that it approximates the optimal Gibbs distribution. Efficient
sampling of the state is comparatively simpler. Apart from having a
lower complexity -- especially for fully connected networks -- another
advantage is that the quantum state preparation and sampling achieves a
better optimum than classical heuristics, leading to better
generalization performance.

Sticking with neural networks, to my best knowledge, it has been exactly
two decades since the first proposal of quantum perceptrons. Yet, how to
train one has been an open question. Now there is one algorithm that
teaches a quantum perceptron in *O*(*n*) time (Schuld, Sinayskiy, and
Petruccione 2014a). The same authors in a new paper discuss the
advantages of applying a quantum associative memory -- essentially a
generalized Hopfield network -- to real-world data (Schuld, Sinayskiy,
and Petruccione 2014b).

Alex Monràs and Andreas Winter published a work on hidden Markov models
where the hidden states are quantum (Monràs and Winder 2014). The idea
is to generalize what we know about realization problems: modelling
stochastic processes by vector space operations. Roughly speaking, a
quasi-representation consists of matrices *D*(**u**) that we assign to
elements **u** of the stochastic process. We also take a fixed vector
*τ* of the vector space on which the matrices act, and another one *π*
from its conjugate space. Then, under some conditions, these should
reproduce the probabilities of the stochastic process:
*p*(**u**) = *πD*(**u**)*τ*. The quasi-representation is, of course,
not unique. The lowest-dimensional quasi-representation of a process is
called regular representation. In a regular representation, we want to
have objects such that they correspond to a valid quantum physical
system. Most notably, the linear maps must be completely positive, and
to achieve this, we lift the number of dimensions from a regular
representation. The paper is about this generalization and lifting.

A quantum associative memory had several proposed forms before. In an
adiabatic setting, Seddiqi and Humble 2014 studied different training
strategies and found that the system size and strategy had a great
impact on the performance.

Adiabatic quantum optimization is very much relevant to learning theory,
so it is worth keeping track of the developments there. While there are
alternative proposals, we understand the minimum energy gap during the
adiabatic change decides the speed at which the process can complete.
This way, the gap defines computational complexity. Finding an
analytical solution to the gap is hard in general. A paper titled
"Dimensionality Reduction for Adiabatic Quantum Optimizers: Beyond
Symmetry Exploitation" suggest a new way of reducing the dimensionality
of the Hilbert space of the physical system to be able to calculate the
gap (Mandrà, Guerreschi, and Aspuru-Guzik 2014). The title is easily
misleading to anyone coming from machine learning -- this is a different
dimensionality reduction. Another manuscript argues that the gap will
always be exponentially small in a wide range of combinatorial
optimization problems (Laumann et al. 2014). In a final bit of adiabatic
news, the quest for proving what the D-Wave processor actually does
continues. A new manuscript argues that multiple qubit tunnel and this
effect is important in the optimization over a nonconvex objective
(Boixo et al. 2014).

It is also interesting to note that applying classical machine learning
in quantum information theory problems is gain traction. Apart from
previous work on quantum metrology and heuristic optimization by
particle-swarms and differential evolution, a new manuscript applies
nonlinear SVMs to improve the fidelity of measurements (Magesan et al.
2014).

Papers I missed earlier
-----------------------

I still found some papers that I have not seen earlier, but they are
less closely related to machine learning -- subject, of course, to your
definition of the domain. Two papers deal with least-squares fitting of
data by using quantum algorithms (Wiebe, Braun, and Lloyd 2012,Wang
(2014)). The former relies on a trick similar to the one used in
least-squares support machines, using a quantum algorithm to solve
linear equations. The latter extends the result to the dense case.

I spotted the experimental realization of Seth Lloyd's *k*-means
clustering algorithm using a photonic quantum computer at the Hefei
National Laboratory before, but I missed an NMR realization of the
quantum support vector machines in the same lab (Li et al. 2014).
Four qubits deal with a character recognition problem.

While I recently read up on [causal structures and Bayesian networks in
a quantum
setting]({filename}/causal-structures-bayesian-nets-and-quantum-systems.md),
I missed this paper: Quantum Inference on Bayesian Networks (Low, Yoder,
and Chuang 2014). The paper achieves a quadratic speedup in the
probability of evidence.

References
----------

Boixo, Sergio, Vadim N. Smelyanskiy, Alireza Shabani, Sergei V. Isakov,
Mark Dykman, Vasil S. Denchev, Mohammad Amin, Anatoly Smirnov, Masoud
Mohseni, and Hartmut Neven. 2014. “Computational Role of Collective
Tunneling in a Quantum Annealer.” *[arXiv:1411.4036](http://arxiv.org/abs/1411.4036)*.

Laumann, Christopher R., Roderich Moessner, Antonello Scardicchio, and
S. L. Sondhi. 2014. “Quantum Annealing: The Fastest Route to Quantum
Computation?” *[arXiv:1411.5710](http://arxiv.org/abs/1411.5710)*.

Low, Guang Hao, Theodore J. Yoder, and Isaac L. Chuang. 2014. “Quantum
Inference on Bayesian Networks.” *Physics Review A* 89 (6). American
Physical Society: 062315.
doi:[10.1103/PhysRevA.89.062315](http://dx.doi.org/10.1103/PhysRevA.89.062315).

Magesan, Easwar, Jay M. Gambetta, A.D. Córcoles, and Jerry M. Chow.
2014. “Machine Learning for Discriminating Quantum Measurement
Trajectories and Improving Readout.” *[arXiv:1411.4994](http://arxiv.org/abs/1411.4994)*.

Mandrà, Salvatore, Gian Giacomo Guerreschi, and Alán Aspuru-Guzik. 2014.
“Dimensionality Reduction for Adiabatic Quantum Optimizers: Beyond
Symmetry Exploitation.” *[arXiv:1407.8183](http://arxiv.org/abs/1407.8183)*.

Monràs, Alex, and Andreas Winder. 2014. “Quantum Learning of Clasiccal
Stochastic Processes: The Completely-Positive Realization Problem.”
*[arXiv:1412:3634](http://arxiv.org/abs/1412:3634)*.

Schuld, Maria, Ilya Sinayskiy, and Francesco Petruccione. 2014a.
“Simulating a Perceptron on a Quantum Computer.” *[arXiv:1412.3635](http://arxiv.org/abs/1412.3635)*.

———. 2014b. “Quantum Computing for Pattern Classification.” In
*Proceedings of PRICAI-14, 13th Pacific Rim International Conference on
Artificial Intelligence*, edited by Duc-Nghia Pham and Seong-Bae Park,
8862:208–20. Lecture Notes in Computer Science. Springer International
Publishing.
doi:[10.1007/978-3-319-13560-1\_17](http://dx.doi.org/10.1007/978-3-319-13560-1_17).

Seddiqi, Hadayat, and Travis S Humble. 2014. “Adiabatic Quantum
Optimization for Associative Memory Recall.” *Frontiers in Physics* 2
(79).
doi:[10.3389/fphy.2014.00079](http://dx.doi.org/10.3389/fphy.2014.00079).

Wang, Guoming. 2014. “Quantum Algorithms for Curve Fitting.”
*[arXiv:1402.0660](http://arxiv.org/abs/1402.0660)*.

Wiebe, Nathan, Daniel Braun, and Seth Lloyd. 2012. “Quantum Algorithm
for Data Fitting.” *Physical Review Letters* 109 (5). American Physical
Society (APS).
doi:[10.1103/physrevlett.109.050505](http://dx.doi.org/10.1103/physrevlett.109.050505).

Li, Zhaokai, Xiaomei Liu, Nanyang Xu, and Jiangfeng Du. 2014.
“Experimental Realization of Quantum Artificial Intelligence.”
*[arXiv:1410.1054](http://arxiv.org/abs/1410.1054)*.
