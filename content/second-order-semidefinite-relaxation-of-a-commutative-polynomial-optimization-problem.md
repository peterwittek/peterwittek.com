Title: Second-order semidefinite relaxation of a commutative polynomial optimization problem
Date: 2013-05-17 07:22
Author: Peter
Category: Semidefinite programming
Tags: Semidefinite programming, Python
Slug: second-order-semidefinite-relaxation-of-a-commutative-polynomial-optimization-problem

Consider the following polynomial optimization problem:

\\[ \\min\_{x\\in \\mathbb{R}\^2}2x\_1x\_2\\]

such that

\\[ -x\_2\^2+x\_2+0.5\\geq 0\\]

\\[x\_1\^2-x\_1=0.\\]

This is the commutative toy example in [Pironio et al., 2010](#pironio2010convergent), which extends the semidefinite
relaxations of constrained polynomial optimization problems
([Lasserre, 2001](#lasserre2001global))  to noncommutative variables.
The number of variables in the corresponding semidefinite programming
(SDP) problem grows fast as the number of variables in the original
problem increases. To achieve a scalable solution, we would like to
solve the SDP with
[SDPARA](http://sdpa.sourceforge.net/ "SDPA family of solvers"), a
distributed solver that also has a new GPU-accelerated variant
([Fujisawa et al., 2012](#fujisawa2012high)). Working towards this goal,
we look at how the second order relaxation can be exported with
[PICOS](http://picos.zib.de/ "Python Interface for Conic Optimization Solvers").
The toy example in [Pironio et al., 2010](#pironio2010convergent)
applies a small trick, eliminating the equality constraint from the
monomial basis. This is a non-trivial problem in general. We look at two
solutions, the first one follows the toy example word by word, the
second deals with the equality by adding a localizing matrix.

Equality constraint eliminated manually
=======================================

The monomial basis for a second-order relaxation would be \$\$\\{1,
x\_1, x\_2, x\_1\^2, x\_1x\_2, x\_2\^2\\}\$\$, but \$\$x\_1\$\$ is an
idempotent variable, so the corresponding relaxation variables reduce to
\$\$\\{y\_0, y\_1, y\_2, y\_{12}, y\_{22}\\}\$\$. The relaxation is
written as

\\[ \\min\_{y}2y\_{12}\\]

such that  
\\[\\left[ \\begin{array}{c|cc|cc}1 & y\_{1} & y\_{2} & y\_{12} &
y\_{22}\\\\\\hline{}y\_{1} & y\_{1} & y\_{12} & y\_{12} &
y\_{122}\\\\y\_{2} & y\_{12} & y\_{22} & y\_{122} &
y\_{222}\\\\\\hline{}y\_{12} & y\_{12} & y\_{122} & y\_{122} &
y\_{1222}\\\\y\_{22} & y\_{122} & y\_{222} & y\_{1222} &
y\_{2222}\\end{array} \\right] \\succeq{}0\\]

\\[\\left[ \\begin{array}{c|cc}-y\_{22}+y\_{2}+0.5
& -y\_{122}+y\_{12}+0.5y\_{1}
& -y\_{222}+y\_{22}+0.5y\_{2}\\\\\\hline{}-y\_{122}+y\_{12}+0.5y\_{1}
& -y\_{122}+y\_{12}+0.5y\_{1}
& -y\_{1222}+y\_{122}+0.5y\_{12}\\\\-y\_{222}+y\_{22}+0.5y\_{2}
& -y\_{1222}+y\_{122}+0.5y\_{12}
& -y\_{2222}+y\_{222}+0.5y\_{22}\\end{array}\\right]\\succeq{}0.\\]  
Apart from the matrices being symmetric, notice other regular patterns
between the elements. We need to explicitly encode these.

To start with, we need to load Picos:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [1]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    import picos

</div>

</div>

</div>

</div>

</div>

The description of the problem is straightforward from the matrices
above:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [2]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    prob = picos.Problem()
    M = prob.add_variable('M',(5,5),vtype='symmetric')
    prob.add_constraint(M >> 0)
    prob.add_constraint(M[0,0]==1)
    prob.add_constraint(-M[1,1]+M[0,1]==0)
    #y_12
    prob.add_constraint(-M[0,3]+M[1,2]==0)
    prob.add_constraint(-M[0,3]+M[1,3]==0)
    #y_22
    prob.add_constraint(-M[0,4]+M[2,2]==0)
    #y_122
    prob.add_constraint(-M[1,4]+M[2,3]==0)
    prob.add_constraint(-M[1,4]+M[3,3]==0)
     
    prob.set_objective('min', 2*M[1,2])
     
    Mineq = prob.add_variable('Mineq',(3,3),vtype='symmetric')
    prob.add_constraint(Mineq >> 0)
     
    prob.add_constraint(Mineq[0,0]==-M[2,2]+M[0,2]+0.5)
    prob.add_constraint(Mineq[0,1]==-M[1,4]+M[0,3]+0.5*M[0,1])
    prob.add_constraint(Mineq[0,2]==-M[2,4]+M[0,4]+0.5*M[0,2])
    prob.add_constraint(-Mineq[1,1]+Mineq[0,1]==0)
    prob.add_constraint(Mineq[1,2]==-M[3,4]+M[2,3]+0.5*M[0,3])
    prob.add_constraint(Mineq[2,2]==-M[4,4]+M[2,4]+0.5*M[0,4])

</div>

</div>

</div>

</div>

</div>

We can solve the problem directly with
[Cvxopt](http://cvxopt.org/ "Python Software for Convex Optimization "),
a dependency of Picos:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [3]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    sol = prob.solve(solver='cvxopt', verbose = 0)

</div>

</div>

</div>

</div>

</div>

This yields the correct results (≈-0.7321). To keep in line with the
original goal, we can also export the problem in SDPA format:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [4]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    prob.write_to_file('example.dat-s')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt">

</div>

<div class="output_subarea output_stream output_stdout output_text">

    writing problem in example.dat-s...
    done.

</div>

</div>

</div>

</div>

</div>

Solving it on your favourite cluster, the result should be the same.

Equality constraint dealt with algorithmically
==============================================

In this case, we do not eliminate the idempotent element from the
monomial basis. For more complex equalities, this would prove difficult.
Instead, we define a new localizing matrix. The equality equation of the
localizing matrix is in turn converted to a pair of positive
semidefinite constraints in the background, which increases the size of
the problem. While seemingly undesirable, the solution is efficient.
Other methods of dealing with equalities, for instance, a QR
factorization and a subsequent projection to the new basis, would run on
a *single* node. Whereas if we increase the complexity of the SDP
problem, we multiple nodes and, potentially, GPU resources to compute
the optimum. Generating the SDP problem fast and solving it on a cluster
lead to an efficient solution in terms of computational time, and also
in terms of human effort.

The relaxation hence changes to the following:

\\[ \\min\_{y}2y\_{12}\\]

such that

\\[\\left[ \\begin{array}{c|cc|ccc}1 & y\_{1} & y\_{2} & y\_{11} &
y\_{12} & y\_{22}\\\\\\hline{}y\_{1} & y\_{11} & y\_{12} & y\_{111} &
y\_{112} & y\_{122}\\\\y\_{2} & y\_{12} & y\_{22} & y\_{112} & y\_{122}
& y\_{222}\\\\\\hline{}y\_{11} & y\_{111} & y\_{112} & y\_{1111} &
y\_{1112} & y\_{1122}\\\\y\_{12} & y\_{112} & y\_{122} & y\_{1112} &
y\_{1122} & y\_{1222}\\\\y\_{22} & y\_{122} & y\_{222} & y\_{1122} &
y\_{1222} & y\_{2222}\\end{array} \\right] \\succeq{}0\\]

\\[\\left[ \\begin{array}{c|cc}-y\_{22}+y\_{2}+0.5
& -y\_{122}+y\_{12}+0.5y\_{1}
& -y\_{222}+y\_{22}+0.5y\_{2}\\\\\\hline{}-y\_{122}+y\_{12}+0.5y\_{1}
& -y\_{1122}+y\_{112}+0.5y\_{11}
& -y\_{1222}+y\_{122}+0.5y\_{12}\\\\-y\_{222}+y\_{22}+0.5y\_{2}
& -y\_{1222}+y\_{122}+0.5y\_{12}
& -y\_{2222}+y\_{222}+0.5y\_{22}\\end{array}\\right]\\succeq{}0.\\]

\\[\\left[ \\begin{array}{c|cc}y\_{11}-y\_{1} & y\_{111}-y\_{11} &
y\_{112}-y\_{12}\\\\\\hline{}y\_{111}-y\_{11} & y\_{1111}-y\_{111} &
y\_{1112}-y\_{112}\\\\y\_{112}-y\_{12} & y\_{1112}-y\_{112} &
y\_{1122}-y\_{122}\\end{array}\\right]=0.\\]

Notice that the inequality matrix changed in only one element. The
Python code corresponding to this problem is as follows:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [5]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    prob = picos.Problem()
    M = prob.add_variable('M',(6,6),vtype='symmetric')
    prob.add_constraint(M >> 0)
    prob.add_constraint(M[0,0]==1)
    #y_11
    prob.add_constraint(-M[0,3]+M[1,1]==0)
    #y_12
    prob.add_constraint(-M[0,4]+M[1,2]==0)
    #y_22
    prob.add_constraint(-M[0,5]+M[2,2]==0)
    #y_112
    prob.add_constraint(-M[1,4]+M[2,3]==0)
    #y_122
    prob.add_constraint(-M[1,5]+M[2,4]==0)
    #y_1122
    prob.add_constraint(-M[3,5]+M[4,4]==0)
     
    prob.set_objective('min', 2*M[0,4])
     
    Mineq = prob.add_variable('Mineq',(3,3),vtype='symmetric')
    prob.add_constraint(Mineq >> 0)
     
    prob.add_constraint(Mineq[0,0]==-M[0,5]+M[0,2]+0.5)
    prob.add_constraint(Mineq[0,1]==-M[1,5]+M[0,4]+0.5*M[0,1])
    prob.add_constraint(Mineq[0,2]==-M[2,5]+M[0,5]+0.5*M[0,2])
    prob.add_constraint(Mineq[1,1]==-M[3,5]+M[1,4]+0.5*M[0,3])
    prob.add_constraint(Mineq[1,2]==-M[4,5]+M[1,5]+0.5*M[0,4])
    prob.add_constraint(Mineq[2,2]==-M[5,5]+M[2,5]+0.5*M[0,5])
     
    Meq = prob.add_variable('Meq',(3,3),vtype='symmetric')
    prob.add_constraint(Meq == 0)
    prob.add_constraint(Meq[0,0]==M[0,3]-M[0,1])
    prob.add_constraint(Meq[0,1]==M[1,3]-M[0,3])
    prob.add_constraint(Meq[0,2]==M[1,4]-M[0,4])
    prob.add_constraint(Meq[1,1]==M[3,3]-M[1,3])
    prob.add_constraint(Meq[1,2]==M[3,4]-M[1,4])
    prob.add_constraint(Meq[2,2]==M[3,5]-M[1,5])

</div>

</div>

</div>

</div>

</div>

Strangely, Cvxopt will not solve this problem, complaining of a rank
problem. Yet, exporting the problem and solving it with SDPA yield the
correct result.

Limitations
===========

The process of transcribing matrix constraints is tedious to say the
least, and the entire process should be automatic: enter a polynomial
optimization problem and receive an SDPA file. The root of the problem
is that Picos uses the symbolic variables internal to Cvxopt. This
architecture also rules out noncommutative variables. The way forward is
a translation layer between SymPy and Picos, which would also able to
deal with noncommutative variables.

References
==========

<a name="fujisawa2012high"></a> Fujisawa, K.; Sato, H.; Matsuoka, S.;
Endo, T.; Yamashita, M. & Nakata, M. High-performance general solver for
extremely large-scale semidefinite programming problems. *Proceedings of
SC-12, International Conference on High Performance Computing,
Networking, Storage and Analysis*, 2012, pp. 93:1-93:11.  
<a name="lasserre2001global"></a>Lasserre, J. Global optimization with
polynomials and the problem of moments. *SIAM Journal on Optimization*,
2001, 11, 796-817.  
<a name="pironio2010convergent"></a>Pironio, S.; Navascués, M. & Acín,
A. Convergent relaxations of polynomial optimization problems with
noncommuting variables. *SIAM Journal on Optimization*, 2010, 20, pp.
2157-2180.
