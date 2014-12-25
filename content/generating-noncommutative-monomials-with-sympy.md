Title: Generating noncommutative monomials with SymPy
Date: 2013-05-06 00:05
Author: Peter
Category: Python
Tags: Noncommutative polynomials, Python, SymPy
Slug: generating-noncommutative-monomials-with-sympy

We are not spoilt for choices to work with polynomials of noncommutative
variables. [Yalmip](http://users.isy.liu.se/johanl/yalmip/ "Yalmip") has
undocumented noncommutative functionality for Matlab. While the rest of
the toolbox is regularly updated, the noncommutative parts are
neglected. [NCAlgebra](http://www.math.ucsd.edu/~ncalg/ "NCAlgebra") is
a package for Mathematica, but its semidefinite programming functions do
not seem to be working, and those are the ones we need.
[SymPy](http://sympy.org/ "SymPy"), a Python library for symbolic
mathematics, has basic functionality for noncommutative variables, so I
took a closer look whether it is able to generate monomials of arbitrary
order. Given that this is an open source solution, I would love to see
it working. The discussion below uses SymPy 0.7.5.

To start with, we have to import the library:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [1]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from sympy import *
    init_printing() 

</div>

</div>

</div>

</div>

Defining an arbitrary number of noncommutative variables is easy:

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [2]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    a=symbols('a0:2', commutative=False)

</div>

</div>

</div>

</div>

Behold the result:

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [3]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    simplify(a[0]*a[1] + a[1]*a[0])

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[3]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$a\_{0} a\_{1} + a\_{1} a\_{0}\$\$

</div>

</div>

</div>

</div>

</div>

Trying to generate the monomials of order two, the situation is less
rosy:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [4]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    itermonomials([a[0], a[1]], 2)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[4]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\left\\{1, a\_{0}, a\_{0}\^{2}, a\_{1}, a\_{1}\^{2}, a\_{0}
a\_{1}\\right\\}\$\$

</div>

</div>

</div>

</div>

</div>

The polynomial functions do not support noncommutative variables. An
additional problem is that the noncommutative variables are not complex:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [5]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    a[0].assumptions0

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

    {'commutative': False,
     'complex': False,
     'composite': False,
     'even': False,
     'imaginary': False,
     'integer': False,
     'irrational': False,
     'negative': False,
     'noninteger': False,
     'nonnegative': False,
     'nonpositive': False,
     'nonzero': True,
     'odd': False,
     'positive': False,
     'prime': False,
     'rational': False,
     'real': False,
     'zero': False}

</div>

</div>

</div>

</div>

</div>

The library will drop an error message if you want to define symbols
that are both noncommutative and complex. We are not going to get
Hermitian conjugates with these variables. A project from Google Summer
of Code 2010 took care of such matters:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [6]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from sympy.physics.quantum.operator import HermitianOperator, Operator
    from sympy.physics.quantum.dagger import Dagger
    A = Operator('A')
    B = Operator('B')
    Dagger(A)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[6]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$A\^{\\dagger}\$\$

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [7]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    simplify(A*B + B*A)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[7]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$A B + B A\$\$

</div>

</div>

</div>

</div>

</div>

A new problem is that obtaining an arbitrary number of operators needs
extra work:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [8]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    n = 2
    X=[]
    for i in range(n):
        X.append(HermitianOperator('X%s' % i))

</div>

</div>

</div>

</div>

</div>

Sympy will not generate the correct monomials of operators either:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [9]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    itermonomials([X[0], X[1]],2)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[9]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\left\\{1, X\_{0} X\_{1}, X\_{0}, \\left(X\_{0}\\right)\^{2},
X\_{1}, \\left(X\_{1}\\right)\^{2}\\right\\}\$\$

</div>

</div>

</div>

</div>

</div>

A not particularly sophisticated function will do the job for me, but it
is probably not sufficiently generic:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [10]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    def get_ncmonomials(variables, degree):
        if not variables:
            return [S.One]
        else:
            _variables = variables[:]
            _variables.insert(0, 1)
            ncmonomials = [S.One]
            for _ in range(degree):
                temp = []
                for var in _variables:
                    for new_var in ncmonomials:
                        temp.append(var * new_var)
                        if var != 1 and not var.is_hermitian:
                            temp.append(Dagger(var) * new_var)
                ncmonomials = unique(temp[:])
            return ncmonomials

    def unique(seq):
        seen = {}
        result = []
        for item in seq:
            marker = item
            if marker in seen:
                continue
            seen[marker] = 1
            result.append(item)
        return result

</div>

</div>

</div>

</div>

</div>

It apparently works:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [11]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    get_ncmonomials(X,2)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[11]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\begin{bmatrix}1, & X\_{0}, & X\_{1}, & \\left(X\_{0}\\right)\^{2},
& X\_{0} X\_{1}, & X\_{1} X\_{0}, &
\\left(X\_{1}\\right)\^{2}\\end{bmatrix}\$\$

</div>

</div>

</div>

</div>

</div>

What is astonishing is just how fast it is compared to Yalmip. Matlab
finds it hard to handle problems as small as 512 variables with
monomials of order 2. The speedup is in the range of 100–400x. The
computational complexity of generating monomials does not change, but
practical problems are within range.

[caption id="attachment\_225" align="alignnone" width="600"]![Timing
results for generating monomials of order
2](http://peterwittek.com/wp-content/uploads/2013/05/order2.png) Timing
results for generating monomials of N noncommutative operators of order
2.[/caption]

[caption id="attachment\_226" align="alignnone" width="600"]![Timing
results for generating monomials of order
4](http://peterwittek.com/wp-content/uploads/2013/05/order4.png) Timing
results for generating monomials of N noncommutative operators of order
4.[/caption]

The next question is whether SymPy is able to do a QR decomposition of a
matrix of noncommutative symbolic variables. That would be an overkill.

