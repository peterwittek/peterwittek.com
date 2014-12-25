Title: Approximating the Ground State of a Many-Particle Quantum System with Semi-Definite Relaxations
Date: 2013-10-29 08:13
Author: Peter
Slug: approximating-the-ground-state-with-sdp
Status: hidden

Approximating the Ground State of a Many-Particle Quantum System with Semi-Definite Relaxations
===============================================================================================

Numerical methods represent an essential ingredient for the study of
many-body systems. A paradigmatic problem is to compute the ground state
of a many-particle quantum system whose interactions are described by a
Hamiltonian H. The goal is to identify the quantum state that minimizes
the energy. In general, an analytic solution to the problem is out of
reach as there are many parameters involved in the optimization. The
common approach, then, consists of variational methods in which one
first defines a physically motivated ansatz for the ground state that
depends on much fewer parameters and then optimizes over these
parameters. These methods provide the searched solution if the ground
state happens to be part of the variational ansatz or a hopefully good
upper bound to the ground-state energy otherwise.
Density-matrix-renormalization-group (DMRG) algorithms [1] are one of
the most popular examples of this variational approach.

During the last decade, different relaxations of the above Hamiltonian
minimization problem have been proposed. Interestingly, they provide
lower bound to the ground-state energy, complementing the upper bounds
that are obtainable using variational methods. These algorithms can be
understood as lower levels of a general hierarchy of semi-definite
programming (SDP) relaxations for non-commutative polynomial
optimization developed recently in [2]. Recent applications of this
approach to Hamiltonian problems involving coupled fermions can be found
in [3,4] for one-dimensional systems. The goal of this activity is to
test the ultimate power of these SDP relaxations. In particular, we plan
to tackle the much more interesting and challenging case of
two-dimensional systems, considering interacting fermions or more exotic
systems as in [5].

Our method hinges on a conversion from a computationally hard problem to
a semidefinite programming (SDP) relaxation that is easily solved on a
cluster. The conversion is a difficult problem that requires symbolic
calculations. We identified two libraries, SymPy for Python and
SymbolicC++ for C++. We developed code in these two languages to solve
the problem of translation, and we made it available under GNU Public
License version 3. The two implementations are hosted at the following
links:

<http://peterwittek.github.io/ncpol2sdpa/>

<http://peterwittek.github.io/ncpol2sdpa-cpp/>

These implementations bypass any other supporting libraries that are
commonly used in converting and formatting optimization problems. The
problem domains where polynomial optimization problems of noncommuting
variables arrive from are quantum physics and quantum correlations. Such
problems are replete with sparse structures in the constraints, and to
ensure high efficiency, we had to address this sparsity. Thus the
conversion engine does not use third-party helper libraries, apart from
the ones used for noncommuting symbolic operations. We achieved a
scalability up to a hundred noncommuting variables in problems where the
number of constraints increases quadratically in the number of
variables. This is the size of the problems we would like to solve.

This work is supported by the European Commission Seventh Framework
Programme under Grant Agreement Number FP7-601138
[PERICLES](http://pericles-project.eu/ "PERICLES"), by the [Red Española
de Supercomputación](http://www.bsc.es/RES "RES") grants number
FI-2013-1-0008 and  FI-2013-3-0004, and by the [Swedish National
Infrastructure for Computing](http://www.snic.se/ "SNIC")project number
SNIC 2014/2-7.

[1] S. White, Phys. Rev. Lett. 69, 2863 (1992).  
[2] S. Pironio, M. Navascues, A. Acin, SIAM J. Optim. 20, 5, 2157
(2010).  
[3] T. Baumgratz, M. B. Plenio, New J. Phys. 14, 023027 (2012).  
[4] T. Barthel, R. Hübener, Phys. Rev. Lett. 108, 200404 (2012).  
[5] A. E. Feiguin, E. Rezayi, C. Nayak, S. Das Sarma, Phys. Rev. Lett.
100, 166803 (2008).

