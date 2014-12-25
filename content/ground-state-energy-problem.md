Title: Converting a ground-state energy problem to a semidefinite programme
Date: 2013-06-03 09:45
Author: Peter
Category: Semidefinite programming
Tags: Noncommutative polynomials, Semidefinite programming, SymPy
Slug: ground-state-energy-problem
Summary: Generating the SDP relaxation of the ground-state energy problem of a Hamiltonian.

We are interested in finding the ground state energy of the following
Hamiltonian ([Corboz et al., 2009](#corboz2009simulation)):  
$$H_{\mathrm{free}}=\sum_{}\left[c_{r}^{\dagger}
c_{s}+c_{s}^{\dagger} c_{r}-\gamma(c_{r}^{\dagger}
c_{s}^{\dagger}+c_{s}c_{r}
)\right]-2\lambda\sum_{r}c_{r}^{\dagger}c_{r},$$  
where \<rs\> goes through nearest neighbour pairs in a two-dimensional
lattice. The fermionic operators are subject to the following
constraints:  
$$\{c_{r}, c_{s}^{\dagger}\}=\delta_{rs}I_{r},$$

$$\{c_{r}, c_{s}\}=0,$$

$$\{c_{r}^\dagger, c_{s}^\dagger\}=0.$$

We fix γ=1 and λ=2. Treating the problem as an instance of
noncommutative polynomial optimization, we convert it to a semidefinite
programme (SDP) relaxation ([Pironio et al., 2010](#pironio2010convergent)).

Generating the relaxation
=========================

[Ncpol2sdpa](http://peterwittek.github.io/ncpol2sdpa/) is a tool to
generate the SDP relaxation given a noncommutative polynomial
optimization. It works both in Matlab and Python. The Matlab variant has
serious limitations, as it uses
[Yalmip](http://users.isy.liu.se/johanl/yalmip/) as its back-end, which
only has rudimentary support for noncommutative variables. Hermitian
variables are not supported, which makes generating relaxations
error-prone. On the other hand, this variant efficiently deals with
equality constraints by solving the set of equalities with QR
decomposition. It is also capable of using a wide range of solvers. The
Matlab version does not scale beyond a lattice of 2×2, and numerical
errors appear, leaving imaginary values in the objective function.

The Python variant uses [SymPy](http://sympy.org/), which excels at
noncommutative and Hermitian variables, allowing operations such
Hermitian conjugates, commutators, and anticommutators. To solve the SDP
relaxation or export it to sparse SDPA format, Ncpol2sdpa uses
[PICOS](http://picos.zib.de/). Translation between noncommutative SymPy
monomials and PICOS variables is mechanical. Equations are converted to
a pair of inequalities in the background, making the SDP relaxations
large.

To get started with the Python version, we need to get our variables
first:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [4]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from sympy.physics.quantum.dagger import Dagger
    from ncpol2sdpa import SdpRelaxation, generate_variables,   
                          fermionic_constraints, get_neighbors, solve_sdp

    gam, lam = 0, 1
    lattice_length = 3
    lattice_width = 3
    n_vars = lattice_length * lattice_width
    C = generate_variables(n_vars, name='C')

</div>

</div>

</div>

</div>

</div>

Defining the objective function is straightforward:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [5]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    hamiltonian = 0
    for r in range(n_vars):
        hamiltonian -= 2*lam*Dagger(C[r])*C[r]
        for s in get_neighbors(r, lattice_length, W=lattice_width):
            hamiltonian += Dagger(C[r])*C[s]+Dagger(C[s])*C[r]
            hamiltonian -= gam*(Dagger(C[r])*Dagger(C[s])+C[s]*C[r])

</div>

</div>

</div>

</div>

</div>

The code gets inefficient at defining the equalities. Most of the
equalities in the problem have a monomial on one side, and another
monomial on the other side. These simple substitutions could be removed
from the monomial basis. Monomial substitutions work for simple cases,
such as idempotent variables, but unfortunately the equalities in this
problem fail as substitutions.

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [3]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    monomial_substitutions = {}
    equalities = []
    inequalities = []
    for i in range(n_vars):
        for j in range(i + 1, n_vars):
            equalities.append(Dagger(C[j]) * C[i] + C[i] * Dagger(C[j]))
            equalities.append(C[j] * Dagger(C[i]) + Dagger(C[i]) * C[j])
            equalities.append(C[j] * C[i] + C[i] * C[j])
            equalities.append(Dagger(C[j]) * Dagger(C[i]) +
                              Dagger(C[i]) * Dagger(C[j]))

    for Cr in C:        
        equalities.append(Cr ** 2)
        equalities.append(Dagger(Cr) ** 2)
        equalities.append(Cr * Dagger(Cr) + Dagger(Cr) * Cr - 1.0)
        inequalities.append(Dagger(Cr)*Cr)
        inequalities.append(1-Dagger(Cr)*Cr)

</div>

</div>

</div>

</div>

</div>

The number of equalities grows quickly with the lattice size. Since each
of them means two inequalities, problems are expected. The code for this
Hamiltonian is included in Ncpol2sdpa.  

![equalities](http://peterwittek.com/wp-content/uploads/2013/06/equalities.png)

Results
=======

We used the cr1.8xlarge [instance
type](https://aws.amazon.com/ec2/instance-types/#instance-details "AWS instance types")
of Amazon Web Services, which has 244 GByte of main memory. This
instance type has the largest amount of memory among cloud instances.
The computational time and memory use grow exponentially.

![picos_timing](http://peterwittek.com/wp-content/uploads/2013/06/picos_timing.png)

For lattice dimension 5×5, the memory use was so excessive the operating
system killed the process.

Limitations
===========

Generating an SDP relaxation and solving it are two different matters.
PICOS interfaces with SDP solvers implemented in Python. These are not
scalable to a cluster. PICOS can also export to sparse SDPA format,
which is far more desirable, given SDPARA can solve a problem on a
cluster. Yet, writing the problem to the disk is not as straightforward
as it seems. Memory use increases further, and the process will be
killed even in the case of a 4×4 lattice. It is interesting to note that
the 3×3 lattice takes about a hundred seconds to generate and write, and
solving it on a single node using SDPARA with twelve cores takes about
the same time. Perhaps distributing the generation of the problem would
help overcome the memory and time constraints.

References
==========

<a name="corboz2009simulation"></a>Corboz, P.; Evenbly, G.; Verstraete,
F. & Vidal, G. [Simulation of interacting fermions with entanglement renormalization](http://arxiv.org/abs/0904.4151). *Physics Review A*,
2010, 81, pp. 010303.

<a name="pironio2010convergent"></a>Pironio, S.; Navascués, M. & Acín,
A. [Convergent relaxations of polynomial optimization problems with noncommuting variables](http://arxiv.org/abs/0903.4368). *SIAM Journal
on Optimization*, 2010, 20, pp. 2157-2180.

