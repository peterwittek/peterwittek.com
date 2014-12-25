Title: Quantum bound on the CHSH inequality using semidefinite relaxations
Date: 2014-06-03 09:56
Author: Peter
Category: Noncommutative polynomials, Python, Quantum information theory, Semidefinite programming, SymPy
Slug: quantum-bound-on-the-chsh-inequality-using-sdp

<div id="notebook" class="border-box-sizing" tabindex="-1">

<div id="notebook-container" class="container">

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

*This post is
[available](http://nbviewer.ipython.org/github/peterwittek/ipython-notebooks/blob/master/Quantum_Bound_on_CHSH.ipynb "The Jordan-Wigner transform in Python")
as an IPython notebook.*
</p>
The Tsirelson bound on the Clauser-Horne-Shimony-Holt inequality defines
the maximum value on quantum correlations in a bipartite system where
the two sites have two measurements each, with two possible outcomes
[1].

The problem of finding the maximum quantum violation can be cast as a
polynomial optimization problem of noncommuting variables, which in turn
is approximated by a hierarchy of semidefinite programming (SDP)
relaxations [2]. The probabilities are described by projection operators
over normalized states -- we label the projectors by <span
class="math">\\(E\_i\\)</span>. They pairwise belong to measurements
<span class="math">\\(M\_k\\)</span>, where <span
class="math">\\(M\_1\\)</span> and <span class="math">\\(M\_2\\)</span>
are on one site of the system, and <span class="math">\\(M\_3\\)</span>
and <span class="math">\\(M\_4\\)</span> are on the other site. Hence,
for instance, <span class="math">\\(E\_1, E\_2\\in M\_1\\)</span>, <span
class="math">\\(E\_3, E\_4\\in M\_2\\)</span>, and so on. The
optimization problem becomes

\$\$\\max\_{E,\\phi} \\langle \\phi, \\sum\_{ij} c\_{ij} E\_i E\_j\\phi
\\rangle\$\$

subject to

\$\$\\begin{split}\\|\\phi\\| & =1,\\\\ E\_i\^\\dagger & = E\_i & \\quad
\\forall i,\\\\ E\_i E\_j & = \\delta\_{ij}E\_i & \\quad E\_i,E\_j \\in
M\_k, \\forall k,\\\\ \\sum\_i E\_i & = 1 & \\quad \\forall M\_k,\\\  
\\lbrack E\_i,E\_j\\rbrack & = 0 &\\quad \\forall E\_i \\in M\_1\\cup
M\_2, E\_j\\in M\_3\\cup M\_4.\\end{split}\$\$

We use the latest git version of
[Ncpol2sdpa](http://peterwittek.github.io/ncpol2sdpa/) to translate the
polynomial optimization problem to an SDP [3], and then we solve it with
[SDPA](http://sdpa.sourceforge.net/download.html). To begin with, we
import the necessary functions from Ncpol2sdpa:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [1]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from ncpol2sdpa import generate_variables, SdpRelaxation, solve_sdp,  
                          projective_measurement_constraints

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

We cast the problem in the form of expectation values to get the
familiar value of the maximum violation, <span
class="math">\\(2\\sqrt{2}\\)</span>. This requires defining a helper
function to generate the expectation values given the projectors and the
outcomes:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [2]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    def expectation_values(M, outcomes):
        exp_values = []
        for k in range(len(M)):
            exp_value = 0
            for i in range(len(M[k])):
                exp_value += outcomes[k][i]*M[k][i]
            exp_values.append(exp_value)
        return exp_values

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

The total number of variables is 8 (<span class="math">\\(2\^2
2\^2\\)</span>). We generate the necessary number of Hermitian variables
and divide them into the appropriate measurements:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [3]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    n_vars = 8
    E = generate_variables(n_vars, name='E', hermitian=True)
    M, outcomes = [], []
    for i in range(n_vars/2):
        M.append([E[2*i], E[2*i+1]])
        outcomes.append([1, -1])
    A = [M[0], M[1]]
    B = [M[2], M[3]]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Ncpol2sdpa has a built-in function to generate the constraints for
projective measurements. With that, we define the constraints of the
optimization problem:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [4]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    inequalities= []
    monomial_substitutions, equalities = projective_measurement_constraints(A, B)

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

The objective function uses the expectation values. We have to take the
negative of it, as the SDP solver can only minimize a function. The
objective for the maximum violation thus becomes:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [5]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    C = expectation_values(M, outcomes)
    objective = -(C[0]*C[2] + C[0]*C[3] + C[1]*C[2] - C[1]*C[3])

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Setting the relaxation level to one, the solution already converges:

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [6]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    level = 1
    sdpRelaxation = SdpRelaxation(E, verbose=2)
    sdpRelaxation.get_relaxation(objective, inequalities, equalities,
                                 monomial_substitutions, level)
    print solve_sdp(sdpRelaxation)

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

    Number of SDP variables: 44
    Generating moment matrix...
    Reduced number of SDP variables: 32
    Processing 8 inequalities...
    (-2.828427226880054, -2.8284273492092673)

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

**References**
==============

[1] Clauser, J. F.; Horne, M. A.; Shimony, A. & Holt, R. A. Proposed
Experiment to Test Local Hidden-Variable Theories. *Physical Review
Letters*, 1969, 23, 880-884.

[2] Navascués, M.; Pironio, S. & Acín, A. A convergent hierarchy of
semidefinite programs characterizing the set of quantum correlations.
*New Journal of Physics*, 2008, 10, 073013.

[3] Wittek, P. Ncpol2sdpa -- Sparse Semidefinite Programming Relaxations
for Polynomial Optimization Problems of Noncommuting Variables.
*arXiv:1308.6029*, 2013.

</div>

</div>

</div>

</div>

</div>
