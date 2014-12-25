Title: Some recent advances in quantum machine learning
Date: 2014-10-30 15:49
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Quantum information theory, Machine learning
Slug: recent-advances-in-quantum-machine-learning

*Update: A paper on the quantum learning of coherent states came out
just a day after writing this up. I added a paragraph on it.*

Since I submitted the manuscript of the [book](http://peterwittek.com/book) on quantum machine learning to the
publisher, quite a bit of progress has been made on the topic. In this
post, I quickly go through the new papers that came to my attention
recently.

To start with, a South African group at the University of KwaZulu-Natal
published an introduction to quantum machine learning [(Schuld et al, 2014a)](#schuld2014introduction). The paper is easy to read, and, apart
from supervised and unsupervised learning, it also mentions
reinforcement learning, albeit there is no mentioning of a quantum
flavour of this kind of problems. Apart from the usual suspects, the
authors pay special attention to methods closer to classical statistics,
such as Bayesian inference and Markov models, which I find refreshing.
Furthermore, they mention quantum decision tree classifiers, pointing
out that key steps of the algorithms remain obscure.

While writing the book, I struggled the most with quantum neural
networks. This was not because the subject matter is difficult to
comprehend: it is fairly light. The problem was the vast number of
papers published, not all of which was truly quantum: some were
quantum-like learning methods, presenting a classical algorithm that was
inspired by quantum mechanics. Even if we filter out those, the numbers
were still intimidating. The same South African group as above published
a good review on quantum neural networks recently [(Schuld et al, 2014c)](#schuld2014quest). I wish I had this when I was writing the
chapter on this subject. They highlight the usual problem of closed
quantum systems having a neat unitary evolution, whereas neural networks
work with a nonlinear activation. They enumerate the potential solutions
explored so far in the literature. They also did original research on
the topic in an earlier paper, which I regrettably missed before,
linking Hopfield networks to quantum random walks [(Schuld et al, 2014b)](#schuld2014quantum).

Talking about random walks and reinforcement learning, I missed a paper
that was published two years ago, connecting these two in a model based
on intelligent agents who constantly search a memory space and also
generate new possible solutions [(Briegel & De las Cuevas, 2014)](#briegel2012projective). Moreover, the authors extended the
method to quantum random walks in an open quantum system. To my
knowledge, this is the first link between reinforcement learning and
quantum information theory.

From Seth Lloyd's collection of three papers last year, the one on
quantum principle component analysis was published in Nature Physics. He
and a new batch of co-authors posted a new manuscript on arXiv with 'big
data' in the title, again. The paper is curious: it deals with the
quantum variant of topological methods in machine learning [(Lloyd et al., 2014)](#lloyd2014quantumalgorithms). A
[workshop](http://topology.cs.wisc.edu/index.html) was recently
organized on topological methods at ICML-14, but it is still far from
being mainstream. It is a more algebraic view on manifold learning, and
we already have a quantum variant of it.

One last bit of Seth Lloyd-related news: a group implemented his
*k*-means clustering algorithm using a photonic quantum computer up to
eight dimensions [(Cai et al., 2014)](#cai2014entanglement).

Moving on to a more combinatorial approach to machine learning,
identifying an *n*-bit parity function is equivalent to a binary
classification problem with an *n*-dimensional binary feature space. If
we talk about learning parity with noise, then not all the binary labels
are correct. A new paper proves that without noise, the computational
complexity of learning with classical and quantum methods is the same,
but the noise turns the complexity of classical methods to
superpolynomial, whereas the increase with quantum algorithms is only
logarithmic [(Cross et al., 2014)](#cross2014quantum). This is certainly
an exciting take on the problem of separating classical and quantum
learning algorithms. Working with the same n-bit parity functions
without noise, [Yoo et al. (2014)](#yoo2014quantum) prove a large, but
constant-factor speedup for quantum algorithms.

Quantum learning of unitary transformations is
[similar](http://www.slideshare.net/peter_wittek/aqis14poster) to
transduction: we have a limited number of future targets on which we
want to apply the function -- the unitary in the quantum case. A new
paper proves super-replication of unitaries: given *n* copies, we can
get *n*^2^ almost perfect copies, with exponentially decreasing
probability of success [(Dür et al., 2014)](#dur2014deterministic). The
result holds for unitaries of the form \$\$U(\\theta) =
exp(-\\imath\\theta H)\$\$, where the Hamiltonian *H* is known, but the
interaction strength \$\$\\theta\$\$ is unknown. Generalization of this
result would be exciting.

It is also interesting to see how learning methods enhance problems in
quantum information theory. A new paper investigates the optimal
strategy to distinguish two states: a signal (a quantum state) of
unknown amplitude is beamed at a classical bit [(Sentís et al., 2014)](#sentis2014quantum). The signal either goes through a transparent
medium if the stored bit is zero, or it is perfectly reflected and
captured by a detector. The detector is also supplied n copies of the
quantum state. Now the question is whether it is better to estimate the
amplitude first and then do a measurement on the reflection, or do a
collective measurement. The result is similar in broad outlines to the
quantum learning of unitaries, although for only small amplitudes: a
collective measurement is optimal.

<a name="briegel2012projective"></a>Briegel, H. J. & De las Cuevas, G.
[Projective Simulation for Artificial Intelligence](http://dx.doi.org/10.1038/srep00400). Scientific Reports,
2012, 2, 1--16.

<a name="cai2014entanglement"></a>Cai, X.-D.; Wu, D.; Su, Z.-E.; Chen,
M.-C.; Wang, X.-L.; Li, L.; Liu, N.-L.; Lu, C.-Y. & Pan, J.-W.
[Entanglement-Based Quantum Machine Learning](http://arxiv.org/abs/1409.7770). arXiv:1409.7770, 2014.

<a name="cross2014quantum"></a>Cross, A. W.; Smith, G. & Smolin, J. A.
[Quantum Learning Robust to Noise](http://arxiv.org/abs/1407.5088).
arXiv:1407.5088, 2014.

<a name="dur2014deterministic"></a>Dür, W.; Sekatski, P. & Skotiniotis,
M. [Deterministic Super-Replication of Unitary Operations](http://arxiv.org/abs/1410.6008). arXiv:1410.6008, 2014.

<a name="lloyd2014quantumalgorithms"></a>Lloyd, S.; Garnerone, S. &
Zanardi, P. [Quantum Algorithms for Topological and Geometric Analysis of Big Data](http://arxiv.org/abs/1408.3106). arXiv:1408.3106, 2014.

<a name="schuld2014introduction"></a>Schuld, M.; Sinayskiy, I. &
Petruccione, F. [An Introduction to Quantum Machine Learning](http://dx.doi.org/10.1080/00107514.2014.964942). Contemporary
Physics, 2014, 0, 1--14.

<a name="schuld2014quantum"></a>Schuld, M.; Sinayskiy, I. & Petruccione,
F. [Quantum Walks on Graphs Representing the Firing Patterns of a Quantum Neural Network](http://dx.doi.org/10.1103/PhysRevA.89.032333).
Physics Review A, American Physical Society, 2014, 89, 032333.

<a name="schuld2014quest"></a>Schuld, M.; Sinayskiy, I. & Petruccione,
F. [The Quest for a Quantum Neural Network](http://dx.doi.org/10.1007/s11128-014-0809-8). Quantum
Information Processing, Springer US, 2014, 13, 2567--2586.

<a name="sentis2014quantum"></a>Sentís, G.; Guţă, M. & Adesso, G.
[Quantum Learning of Coherent States](http://arxiv.org/abs/1410.8700).
arXiv:1410.8700, 2014.

<a name="yoo2014quantum"></a> Yoo, S.; Bang, J.; Lee, C. & Lee, J. [A Quantum Speedup in Machine Learning: Finding an N-bit Boolean Function for a Classification](http://dx.doi.org/10.1088/1367-2630/16/10/103014).
New Journal of Physics, 2014, 16, 103014.

