Title: Quantum process tomography and machine learning
Date: 2013-11-01 06:31
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Quantum information theory, Machine learning
Slug: quantum-process-tomography-and-machine-learning
Summary: The optimal estimation of a group of unitary transforms allows for learning an unknown function: this is similar to regression in classical machine learning.

***Update****: An extended version of this post will appear in the
upcoming book [Quantum Machine Learning: What Quantum Computing Means to Data Mining]({filename}/pages/book.md "Quantum Machine Learning").*  
***Update 2****: Some clarifications are made in a [new post]({filename}/more-on-quantum-learning-of-unitaries.md).*

Take a high-level view on machine learning: given a training set
$\{(\mathbf{x}_1,y_1),\ldots,(\mathbf{x}_N,y_N)\},$ where
$\mathbf{x}_i$ is a finite dimensional data point, and
$y_i$ is an associated outcome, the task is to approximate an
unknown function $f$ with $\hat{f}$ such that
$\hat{f}(\mathbf{x}_i)=y_i$ for all $i.$ Then,
encountering a previously unseen $\mathbf{x},$ we calculate
$\hat{f}(\mathbf{x}).$

This task translates well to quantum process tomography -- a problem
when an unknown quantum dynamical process has to be identified. The
dynamical process is a series of unitary transformations, also called a
channel. If we denote the unitary by $U,$ the goal becomes to
derive an estimate $\hat{U}$ such that
$\hat{U}(\rho_{in})=\rho_{out}.$ Then, just as in the
classical case, we would like to calculate $\hat{U}(\rho)$ for a
new state $\rho$ ([Bisio et al., 2010](#bisio2010optimal)).

In a classical setting, we define an objective function, and we seek an
optimum subject to constraints and assumptions. For instance, in [linear least squares](https://en.wikipedia.org/wiki/Least_squares#Problem_statement),
we assume that the unknown function has the form
$f(\mathbf{x},\mathbf{\beta})=\beta_0+\beta_1\mathbf{x}.$
We seek to minimize the squared residual $S=\sum_{i=1}^N
(y_i-f(\mathbf{x},\mathbf{\beta}))^2.$ The assumption in
learning by quantum process tomography is that the channel is unitary
and that the unitary transformation is drawn from a group -- that is, it
meets basic symmetry conditions ([Chiribella et al., 2005](#chiribella2005optimal)). The objective function is replaced by
the [fidelity of quantum states](https://en.wikipedia.org/wiki/Fidelity_of_quantum_states).

Apart from these similarities, the rest of the learning process does not
resemble the classical variant. Unlike in the classical setting,
learning a unitary requires a double maximization: we need an optimal
measuring strategy that optimally approximates the unitary, *and* we
also need an optimal input state that best captures the information of
the unitary ([Acín et al., 2001](#acin2001optimal)). The key steps are
as follows.

-   Storage and parallel application of the unitary on a suitable input
    state that achieve optimum storage.
-   A superposition of maximally entangled states is the optimal input
    state.
-   A measure-and-prepare strategy on the ancilla with an optimal POVM
    is best for applying the learned unitary on an arbitrary number of
    new states.

This blog post interprets [Bisio et al., 2010](#bisio2010optimal) by
following through these steps.

Parallel application and storage of unitary
-------------------------------------------

The task is simple: we have a black box that implements an unknown
unitary $U,$ and we can make $N$ calls to it to identify the
unitary. $U$ acts on a finite $d$-dimensional Hilbert space,
and performs a deterministic transformation belonging to a given
[representation of a compact Lie group](https://en.wikipedia.org/wiki/Representation_of_a_Lie_group)
([Chiribella, 2011](#chiribella2011group)). The deterministic
transformation is also known as a quantum channel.

Two immediate problems arise: (i) How do we store the approximated
unitary? (ii) How do we dispose the $N$ uses? In parallel or in
sequence?

The first question is easier to address: the [Choi-Jamiołkowsky duality](https://en.wikipedia.org/wiki/Channel-state_duality) enables
storing the unitary as a state. Denote the stored state as
$|\phi_U\rangle.$

If we take the fidelity of output quantum states as the figure of merit,
the optimal storage is achieved by a parallel application of the
unitaries on an input state. Denote by $\mathcal{H}_{i}$ the
Hilbert space of all inputs of the $N$ examples, and by
$\mathcal{H}_o$ the Hilbert space of all outputs. With
$U^{\otimes{}N}$ acting on $\mathcal{H}_o$, we have the
following lemma ([Bisio et al., 2010](#bisio2010optimal)):

**Lemma (Optimality of parallel storage)** The optimal storage of
$U$ can be achieved by applying
$U^{\otimes{}N}\otimes{}\,\mathbb{I}^{\otimes{}N}$ on a
suitable multipartite input state
$|\phi\rangle\in\mathcal{H}_o\otimes\mathcal{H}_i.$

The next question is what that suitable input state might be.

Optimal state for learning
--------------------------

Classical learning takes the training examples, and tries to make the
best of them. Some variants may ask for specific extra examples, as in
[active learning](https://en.wikipedia.org/wiki/Active_learning_%28machine_learning%29),
which is, in turn, a flavour of semi-supervised learning. Other
algorithms learn to ignore irrelevant examples, such [support vector machines with *C*-regularization](https://en.wikipedia.org/wiki/Support_vector_machines#Soft_margin).
Quantum process tomography, on the other hand, requires and *optimal*
input state, which also has to be entangled.

To give an intuition why entanglement is necessary, consider [superdense coding](https://en.wikipedia.org/wiki/Superdense_coding): two classical
bits are sent over a quantum channel by a single qubit. The two
communicating parties, Alice and Bob, have a half of two entangled
qubits -- in fact, a Bell state -- each. Alice applies one of four
unitary transformations on her part, translating the Bell state into a
different one, and sends the qubit over. Bob measures the state, and
deduces which one of the four operations was used, thus retrieving two
classical bits of information. The use of entanglement with an ancillary
system improves the discrimination of unknown transformations; this
motivates using such states in generic process tomography ([Chiribella, 2011](#chiribella2011group)).

A representation of the unitary group is *irreducible* in an invariant
subspace, if the subspace does not have a proper subspace that is
invariant. Any unitary representation $\{U_g\}$ of a compact
Lie group can be decomposed into the direct sum of a discrete number of
irreducible representations ([Chiribella, 2006](#chiribella2006optimal),
p.22).

The Clebsch-Gordan tensor product structure (or Clebsch-Gordan
decomposition) of unitary representation $\{U_g\}$ is given by
$U_g=\oplus_{\mu\in{}\textrm{Irr}(U_g)}U_g^\mu\otimes\mathbb{I}_{m_\mu},$
acting on
$\mathcal{H}=\oplus_{\mu\in{}\textrm{Irr}(U_g)}\mathcal{H}_\mu\otimes\mathbb{C}^{m_\mu}$
([Chiribella et al., 2005](#chiribella2005optimal); [Chiribella, 2006](#chiribella2006optimal), p.26). $\mathcal{H}_\mu$ is
called the representation space, and $\mathbb{C}^{m_\mu}$ is
the multiplicity space. $\mathbb{I}_{m_\mu}$ is the identity
on the $m_\mu$-dimensional Hilbert space.

Using the decomposition of $U^{\otimes{}N}$, we have the
following lemma to identify the optimal input state ([Bisio et al., 2010](#bisio2010optimal)):

**Lemma (Optimal states for storage)** The optimal input state for
storage can be taken of the form $|\phi\rangle =
\oplus_{j\in\mathrm{Irr}(U^{\otimes{}N})}
\sqrt{p_j/d_j}|\mathbb{I}_j\rangle\in\mathcal{\tilde{H}},$
where $p_j$ are probabilities, the index $j$ runs over the
set $\mathrm{Irr}(U^{\otimes{}N})$ of all irreducible
representations $\{U_j\}$ contained in the decomposition of
$\{U^{\otimes{}N}\},$ $d_j$ is the dimension of the
corresponding subspace, and
$\mathcal{\tilde{H}}=\oplus_{j\in\mathrm{Irr}(U^{\otimes{}N})}(\mathcal{H}_j\otimes{}\mathcal{H}_j)$
is a subspace of $\mathcal{H}_o\otimes{}\mathcal{H}_i$
carrying the representation
$\tilde{U}=\oplus_{j\in\mathrm{Irr}(U^{\otimes{}N})}(U_j\otimes{}\mathbb{I}_j)$,
$\mathbb{I}_j$ being the identity in $\mathcal{H}_j.$

The optimal state for the estimation of an unknown unitary is always a
superposition of maximally entangled states ([Chiribella et al., 2011](#chiribella2005optimal)).

Applying the learned function
-----------------------------

A measure-and-prepare strategy is optimal for applying the learned
function an arbitrary number of times. This strategy consists of
measuring the state $|\phi_U\rangle$ in the quantum memory with
an optimal POVM, and performing the unitary on the new input state.

There is no loss of generality in restricting the search space to
covariant POVMs ([Holevo, 2011](#holevo2011probabilistic)) of the form
$M(g) = U_g\Xi{}U_g^{\dagger},$ with a positive operator
$\Xi$ satisfying the normalizing condition $\int_G
\mathrm{d}gM(g)=\mathbb{I}$ ([Chiribella et al., 2005](#chiribella2005optimal)). The following theorem provides the
optimal measurement to retrieve the approximated unitary ([Bisio et al., 2010](#bisio2010optimal)):

**Theorem (Optimal retrieving strategy)** The optimal retrieving of
$U$ from the memory state $|\phi_U\rangle$ is achieved by
measuring the ancilla with the optimal POVM
$P_{\hat{U}}=|\eta_{\hat{U}}\rangle\langle\eta_{\hat{U}}|$
given by
$|\eta_{\hat{U}}\rangle=\oplus_j\sqrt{d_j}|\hat{U}_j\rangle,$
and, conditionally on outcome $\hat{U},$ by performing the
unitary $\hat{U}$ on the new input system.

The measurement will be optimal in the fidelity of quantum states, and
it is also optimal for the maximization of the single-copy fidelity of
all locals channels. The fidelity does not degrade with repeated
applications.

Closing remarks
---------------

From the perspective of machine learning, restricting the approximated
function to unitaries is a serious constraint. It implies that the
function is a bijection, ruling classification out. This methodology is
relevant in regression problems.

The necessity of an optimal input state is interesting, but it is
unclear what it means to learning performance, and especially to
generalization power. The Clebsch-Gordan decomposition vaguely resembles
a form of biclustering, followed by a transformation. It would be good
to see a formal link between these concepts.

References
----------

<a name="acin2001optimal"></a>Acín, A.; Jané, E. & Vidal, G. [Optimal estimation of quantum dynamics](http://arxiv.org/abs/quant-ph/0012015).
*Physical Review A*, 2001, 64, 050302.  
<a name="bisio2010optimal"></a>Bisio, A.; Chiribella, G.; D'Ariano, G.;
Facchini, S. & Perinotti, P. [Optimal quantum learning of a unitary transformation](http://arxiv.org/abs/0903.0543). *Physical Review A*,
2010, 81, 032324.  
<a name="chiribella2005optimal"></a>Chiribella, G.; D'ariano, G. &
Sacchi, M. [Optimal estimation of group transformations using entanglement](http://arxiv.org/abs/quant-ph/0506267). *Physical Review
A*, 2005, 72, 042338.  
<a name="chiribella2006optimal"></a>Chiribella, G. [Optimal estimation of quantum signals in the presence of symmetry](http://www.qubit.it/educational/thesis/ThesisRevised.pdf). PhD
thesis. *University of Pavia*, 2006.  
<a name="chiribella2011group"></a>Chiribella, G. [Group theoretic structures in the estimation of an unknown unitary transformation](http://arxiv.org/abs/1012.2130). *Journal of Physics:
Conference Series*, 2011, 284, 012001.  
<a name="holevo2011probabilistic"></a>Holevo, A. *Probabilistic and
statistical aspects of quantum theory*. Springer, 2011.
