Title: Causal structures, Bayesian nets, and quantum systems
Date: 2014-09-18 10:22
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Machine learning, Quantum information theory
Slug: causal-structures-bayesian-nets-and-quantum-systems
Summary: New characterizations of Bell inequalities in terms of causal structures are emerging: they can give rise to quantum versions of Bayesian networks.

[bibshow sort=firstauthor order=asc process\_titles=0
template=post-bibtex file=bibliography.bib]  
Correlation is a symmetric relation between random variables, but
causation is not: it says more, it implies an inference from a cause to
a consequence. Intuitively, there is no correlation without causation --
this is often referred to as [Reichenbach's common cause
principle](http://plato.stanford.edu/archives/fall2010/entries/physics-Rpcc/).
Given a set of random variables and joint or marginal probabilities, we
would like to learn the causal relations between the random variables. A
Bayesian network is a directed acyclic graph (DAG) which encodes these
dependences while reproducing the observed distribution.

Learning the structure of a classical Bayesian network is a hard task in
itself. Since we talk about correlations, it is also natural to ask how
we can extend these causal structures to quantum correlations,
particularly to instances of nonlocality. Based on a brief review of the
literature, three main research directions became apparent in recent
years:

-   Characterizing quantum correlations by causal structures.
-   Extending the d-seperation theorem to address quantum correlations
    in a Bayesian net.
-   Learning classical Bayesian networks by adiabatic or gate quantum
    computers.

In what follows, some relevant references are collected to each of these
directions.

Quantum correlations and causal structures
------------------------------------------

Bell inequalities are the traditional way of studying quantum
correlations. A recent body of work shows that various extensions of
Bell scenarios -- for instance, sequential correlation scenarios
[bibcite key=gallego2014nonlocality] -- can be captured by studying
causal structures on DAGs.

A seminal work in this area is by Wood and Spekkens (2012), which
asserts that while causal discovery algorithms cannot distinguish
between correlations that violate Bell inequalities from ones that do
not, the violating ones require fine-tuning of the causal parameters
[bibcite key=wood2012lesson]. Fine-tuning means that the conditional
independences of the model do not hold for variations of the
causal-statistical parameters of the model, and the lack of need for
fine-tuning is a core assumptions of causal discovery algorithms.

Leifer and Spekkens (2013) replace conditional probabilities with a
quantum analogue [bibcite key=leifer2013towards]. To treat spatial and
temporal conditioning on random variables in the same framework, they
introduce quantum conditional states. In this arrangement, the Hilbert
space is a region of space-time, and they define unifying manipulations.
Unfortunately the compound state may not be positive. Using the quantum
conditional states, the authors introduce a new Bayes' rule.

Likewise, Fritz (2014) starts by defining an event in space-time that
can be a source, choice of measurement setting, or measurement [bibcite
key=fritz2014beyond]. The paper uses this notion to define correlations
which are different from the traditional definition. With this
generalized concept, the author is able to unify different causal
structures and various configurations of Bell tests and various
generalizations of them.

Chaves et. al (2014) introduce an entropic framework for identifying
latent structures in classical Bayesian networks, and, as a byproduct,
adding an additional inequality on the entropies, they also suggest a
test for quantum nonlocality [bibcite key=chaves2014inferring].

Extending the d-separation theorem
----------------------------------

Papers in this category take a different angle at causal structures in
quantum correlation than the ones in the previous section. The focus is
on extending the classical
[d-separation](http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html) theorem,
which gives a graphically intuitive criterion that in a given DAG
whether a set of random variables is independent of another one
conditioned on a third one.

Henson et al. (2014) extend the criterion to arbitrary general,
nonsignalling correlations [bibcite key=henson2014theory]. They
introduce two distinct type of nodes in a DAG, observed and unobserved
ones. The former resemble classical nodes, in fact, a DAG with only
observed nodes is just a classical Bayesian net. Unobserved are generic
resources, for instance, the source of entangled particles in a Bell
test. The clever consequence of this generalized DAG is that the
d-separation theorem holds in almost identical form to the classical
variant. The quantum case of the generalization is similar to Tucci's
earlier work on the topic [bibcite key=tucci2007factorization].

Pienaar and Brukner (2014) treat all nodes are equal [bibcite
key=pienaar2014graph]. Instead, they forgo Reichenbach's common cause
principle, arguing that its validity is questionable in quantum
mechanics. Akin to a classical Bayesian model, the authors define a
quantum causal model and a corresponding q-separation criterion, and
they prove that this criterion has the same effect as the d-separation
in the classical case.

Learning classical networks
---------------------------

Learning the optimal network that might have produced a given set of
data is a major challenge in optimization theory: it is an NP-hard
problem. Using classical heuristics, simulated quantum annealing has
been suggested [bibcite key=sato2009quantumannealing]. Actual quantum
annealing follows a similar procedure to mapping boosting to an
annealing process: the learning problem is formulated as a quadratic
unconstrained binary optimization problem, which in turn maps to an
Ising model that can be solved in an annealing processor [bibcite
key=ogorman2014bayesian]. The binary variables become the directed edges
between random variables in the DAG: the presence of an directed edge
indicates causation. The objective function evaluates how well a
particular configuration of the directed edges matches the constraints
on the distribution.

There are many potentially good causal structures fitting a
distribution, and if a connection between two random variables is
important, the corresponding directed edge has a high probability of
appearing in most of the good candidates. The optimization is thus a
search over possible graphs for high-probability directed edges. The
search space is superexponential, but if we have some basic assumptions
on the graph structure, we can reduce the size of the search space. For
a target directed edge, we want to calculate the probability over the
search space. For this summation, Tucci suggested a variant of Grover's
search, hence opening up the way to learn classical Bayesian networks in
gate quantum computers [bibcite key=tucci2014quantum].

References
----------

[/bibshow]
