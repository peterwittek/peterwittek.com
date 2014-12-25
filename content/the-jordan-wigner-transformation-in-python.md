Title: The Jordan-Wigner transformation in Python
Date: 2014-06-03 10:19
Author: Peter
Category: Python, Quantum information theory, SymPy
Slug: the-jordan-wigner-transformation-in-python

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

*This post is
[available](http://nbviewer.ipython.org/github/peterwittek/ipython-notebooks/blob/master/Jordan-Wigner_Transform_in_Python.ipynb "The Jordan-Wigner transform in Python")
as an IPython notebook.*

Hamiltonians on one dimensional chains provide a good sanity check when
trying out new numerical methods. The Jordan-Wigner transform is an easy
way to obtain the eigenvalues of systems of fermions. For an
annihiliation operator <span class="math">\\(a\_j\\)</span>, the
transform is defined as <span class="math">\\(a\_j = -
(\\otimes\_{k=1}\^{j-1} \\sigma\_z)\\otimes \\sigma\_j\\)</span>, where
<span class="math">\\(\\sigma\_z\\)</span> is the Pauli operator along
the <span class="math">\\(z\\)</span> axis, and <span
class="math">\\(\\sigma\_j\\)</span> is the operator <span
class="math">\\(|0\\rangle\\langle 1|\\)</span> acting on site <span
class="math">\\(j\\)</span>.

The series of Kronecker products would be an ideal application of a nest
function, but Python does not have such a function built in. Instead, we
define a recursive function to get the desired Kronecker product:

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

    import numpy as np

    def nested_kronecker_product(a):
        if len(a) == 2:
            return np.kron(a[0],a[1])
        else:
            return np.kron(a[0], nested_kronecker_product(a[1:]))

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

With this function, the transform is easy to define. We pad the
transform with identity operators to match the lattice length:

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

    def jordan_wigner_transform(j, lattice_length):
        sigma = np.array([[0, 1], [0, 0]])
        sigma_z = np.array([[1, 0], [0, -1]])
        I = np.eye(2)
        operators = []
        for k in range(j):
            operators.append(sigma_z)
        operators.append(sigma)
        for k in range(lattice_length-j-1):
            operators.append(I)
        return -nested_kronecker_product(operators)

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

Now we can get our transformed fermionic operators:

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

    lattice_length = 4
    a = []
    for i in range(lattice_length):
        a.append(jordan_wigner_transform(i, lattice_length))

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

Next we define a Hamiltonian of interest, namely spinless fermions on an
open chain:

<span class="math">\\(H=\\sum\_{\<rs\>}\\left(c\_{r}\^{\\dagger}
c\_{s}+c\_{s}\^{\\dagger} c\_{r}-\\gamma(c\_{r}\^{\\dagger}
c\_{s}\^{\\dagger}+c\_{s}c\_{r}
)\\right)-2\\lambda\\sum\_{r}c\_{r}\^{\\dagger}c\_{r},\\)</span>

where <span class="math">\\(r\\)</span> and <span
class="math">\\(s\\)</span> indicate neighbors on the chain. The Python
definition of this Hamiltonian is

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

    def hamiltonian(gam, lam, a, lattice_length):
        H = 0
        for i in range(lattice_length - 1):
            H += a[i].T.dot(a[i+1]) - a[i].dot(a[i+1].T)
            H -= gam*(a[i].T.dot(a[i+1].T) - a[i].dot(a[i+1]))
        for i in range(lattice_length):
            H -= 2*lam*(a[i].dot(a[i].T))
        return H

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

Here we observed the fermionic canonical commutation relations and
performed substitutions. To get the eigenvalues for a particular
parameter combination, we write

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

    gam, lam =1, 1
    H = hamiltonian(gam, lam, a, lattice_length)
    eigenvalues = np.linalg.eig(H)[0]
    sorted(eigenvalues)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[5]:

</div>

<div class="output_text output_subarea output_pyout">

    [-8.7587704831436479,
     -8.0641777724759276,
     -6.7587704831436497,
     -6.0641777724759232,
     -5.694592710667723,
     -5.0000000000000036,
     -4.9999999999999991,
     -4.3054072893322797,
     -3.6945927106677212,
     -3.0000000000000004,
     -2.9999999999999991,
     -2.3054072893322788,
     -1.9358222275240897,
     -1.241229516856365,
     0.064177772475912706,
     0.75877048314363438]

</div>

</div>

</div>

</div>

</div>
