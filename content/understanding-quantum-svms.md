Title: Understanding quantum support vector machines
Date: 2013-08-15 03:08
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Quantum information theory, Machine learning
Slug: understanding-quantum-svms

***Update****: An extended version of this post will appear in the
upcoming book [Quantum Machine Learning: What Quantum Computing Means to Data Mining](http://peterwittek.com/book/ "Quantum Machine Learning").*

A fascinating paper recently appeared on arXiv that proves the
exponential speedup of least-squares support vector machines (SVMs)
using quantum computing ([Rebentrost et al., 2013](#rebentrost2013quantum)). While the five-page eprint is fairly
accessible to readers who are not well-versed in quantum information
theory, I had a hard time understanding some steps. This write-up is a
diluted interpretation of the content, bringing it down to my level.

The paper is all the more interesting because it is barely a frame: it
connects some recent results with a formulation of SVMs. Least square
SVMs translate an optimization problem to a set of linear equations. The
linear equations require the quick calculation of the kernel matrix --
this is one source of the speedup. The other source of the speedup is
the efficient solution of the linear equations on quantum hardware.

Least Squares Support Vector Machines
=====================================

A support vector machine (SVM) is a supervised learning algorithm which
learns a given independent and identically distributed training example
set  
\\[\\{(\\mathbf{x}\_1,y\_1),\\ldots,(\\mathbf{x}\_M,y\_M)\\},\\]  
where \$\$\\mathbf{x}\_i\\in \\mathbf{R}\^N\$\$ are the data points,
and \$\$y\\in\\{-1,1\\}\$\$ are binary classes to which a data point
belongs. Here \$\$N\$\$ is the number of features that represent a
single data instance, and \$\$M\$\$ is the number of training instances.

In its simplest, linear form, a support vector machine is a hyperplane
that separates a set of positive examples from a set of negative
examples with maximum margin. The formula for the output of a linear
support vector machine is
\$\$y\_i:=\\textrm{sgn}(\\mathbf{u}\^T\\mathbf{x}\_i+b)\$\$, where
\$\$\\mathbf{x}\_i\$\$ is the \$\$i\$\$th training example, \$\$y\_i\$\$
is the output of the support vector machine for the \$\$i\$\$th training
example, \$\$\\mathbf{u}\$\$ is the normal vector to the hyperplane, and
parameter \$\$b\$\$ helps determine the offset of the hyperplane the
origin. The margin is defined by the distance of the hyperplane to the
nearest of the positive and negative examples. Support vectors are the
training data that lie on the margin.

SVMs allow a nonlinear kernel mapping that maps the training examples
from an input space into a feature space. This is important for problems
that are not linearly separable. SVMs with a \$\$\\phi\$\$ embedding
function require the solution of the following optimization problem:  
\\[\\text{Minimize} \\quad
\\frac{1}{2}\\mathbf{u}\^T\\mathbf{u}+C\\sum\_{i=1}\^M \\xi\_i\\]  
subject to  
\\[y\_i(\\mathbf{u}\^T\\phi(\\mathbf{x}\_i)+b)\\geq 1-\\xi\_i, \\quad
\\xi\_i\\geq 0, \\quad i=1,\\ldots,N.\\]  
Here \$\$\\xi\_i\$\$ stands for the classification error: this
formulation is a soft-margin classifier, allowing classes to mingle. The
\$\$C\$\$ cost parameter acts as a form of regularization: if the cost
of misclassification is higher, a more accurate model is sought with
increased complexity, i.e., with higher number of support vectors. The
decision function becomes
\$\$f(\\mathbf{x})=\\text{sgn}(\\mathbf{u}\^T\\phi(\\mathbf{x})+b).\$\$

In most practical applications, we solve the dual formulation of the
optimization problem. To obtain the dual problem, we introduce
Lagrangian multipliers to accommodate the constraints in the
minimalization problem. The partial derivatives in \$\$\\mathbf{u}\$\$,
\$\$b\$\$, and \$\$\\xi\$\$ define a saddle point of Lagrangian, with
which the dual formulation becomes the following quadratic programming
problem:

\\[\\text{Maximize}\\quad
\\sum\_{i=1}\^M\\alpha\_i-\\frac{1}{2}\\sum\_{i=1}\^M\\sum\_{j=1}\^M\\alpha\_i
y\_i \\alpha\_j y\_j K(\\mathbf{x}\_i,\\mathbf{x}\_j)\\]  
subject to  
\\[\\sum\_{i=1}\^M \\alpha\_i y\_i=0, \\quad \\alpha\_i\\in [0,C],
\\quad i=1,\\ldots, M.\\]

The function \$\$K(\\mathbf{x}\_i,\\mathbf{x}\_j)\$\$ is the kernel
function, the dot product of the embedding space. The kernel function
bypasses calculating the embedding itself, we use it directly to find
the optimum and subsequently to classify new instances. The decision
function for a binary decision problem becomes
\$\$f(\\mathbf{x})=\\text{sgn}\\left(\\sum\_{i=1}\^M \\alpha\_i y\_i
K(\\mathbf{x}\_i,\\mathbf{x})+b\\right).\$\$ On classical hardware, the
quadratic problem is solved by sequential minimum optimization.

Least squares SVMs modify the goal function of the primal problem by
using the \$\$l\_2\$\$ norm in the regularization term ([Suykens and Vandewalle, 1999](#suykens1999least)):

\\[\\text{Minimize} \\quad
\\frac{1}{2}\\mathbf{u}\^T\\mathbf{u}+\\frac{\\gamma}{2}\\sum\_{i=1}\^M
e\_i\^2\\]  
subject to the *equality* constraints  
\\[y\_i(\\mathbf{u}\^T\\phi(\\mathbf{x}\_i)+b)=1-e\_i,\\quad
i=1,\\ldots, N.\\]  
The parameter \$\$\\gamma\$\$ plays the same role as the cost parameter
\$\$C.\$\$ Seeking the saddle point of the corresponding Langrangian, we
obtain the following least-squares problem:  
\\[\\left(\\begin{array}{cc}0 & 1\^T \\\\ 1 & K+\\gamma\^{-1}I
\\end{array}\\right)\\left(\\begin{array}{c} b \\\\ \\mathbf{\\alpha}
\\end{array}\\right) = \\left(\\begin{array}{c} 0 \\\\ \\mathbf{y}
\\end{array}\\right)\\qquad (1)\\],  
where \$\$K\_{ij}=K(\\mathbf{x\_i}, \\mathbf{x\_j}).\$\$ The least
squares SVM trades off zero \$\$\\alpha\_i\$\$-s for nonzero error terms
\$\$e\_i\$\$-s, leading to increased model complexity.

Given a linear or polynomial kernel, the calculation of entry in the
kernel matrix takes \$\$O(N)\$\$ time, thus calculating the whole kernel
matrix has \$\$O(M\^2 N)\$\$ time complexity. Solving the quadratic dual
problem or the least squares formulation has \$\$O(M\^3)\$\$ complexity.
Combining the two steps, the classical SVM algorithm has at least
\$\$O(M\^2(M+N))\$\$ complexity. The quantum formulation yields an
exponential speedup in these two steps, leading to an overall complexity
of \$\$O(\\log(MN)).\$\$

Calculating the Kernel Matrix
=============================

In the quantum algorithm, the training instances are presented as
quantum states \$\$|\\mathbf{x}\_i \\rangle\$\$. We do not require the
training instances to be normalized, but the normalization must be given
separately. To reconstruct a state from quantum random access memory
(QRAM, [Giovannetti et al., 2008](#giovannetti2008quantum)), we need to
query the QRAM \$\$O(\\log N)\$\$ times.

To evaluate the dot product of two training instances, we need to do the
following ([Lloyd et al., 2013](#lloyd2013quantum)):

-   Generate two states, \$\$|\\psi\\rangle\$\$ and
    \$\$|\\phi\\rangle\$\$, with an ancilla variable;
-   Estimate the parameter
    \$\$Z=|\\mathbf{x}\_i|\^2+|\\mathbf{x}\_j|\^2\$\$ -- the sum of the
    squared norms of the two instances;
-   Perform a projective measurement on the ancilla alone, comparing the
    two states.

\$\$Z\$\$ times the probability of the success of the measurement yields
the square of the Euclidean distance between the two training instances:
\$\$|\\mathbf{x}\_i-\\mathbf{x}\_j|\^2\$\$. We calculate the dot product
in the linear kernel as
\$\$\\mathbf{x}\_i\^T\\mathbf{x}\_j=\\frac{Z-|\\mathbf{x}\_i-\\mathbf{x}\_j|\^2}{2}\$\$.

The state
\$\$|\\psi\\rangle=\\frac{1}{\\sqrt{2}}(|0\\rangle|\\mathbf{x}\_i\\rangle +
|1\\rangle|\\mathbf{x}\_j\\rangle)\$\$ is easy to construct by querying
the QRAM. We estimate the other state,
\$\$|\\phi\\rangle=\\frac{1}{Z}(|\\mathbf{x}\_i| |0\\rangle -
|\\mathbf{x}\_j| |1\\rangle)\$\$, and the parameter, \$\$Z\$\$,
together. We evolve the state
\$\$\\frac{1}{\\sqrt{2}}(|0\\rangle-|1\\rangle)\\otimes{}|0\\rangle\$\$
with the Hamiltonian \$\$H=(|\\mathbf{x}\_i|
|0\\rangle\\langle{}0|+|\\mathbf{x}\_j|
|1\\rangle\\langle{}1|)\\otimes\\sigma\_x.\$\$ The resulting state is  
\\[\\frac{1}{\\sqrt{2}}(\\cos(|\\mathbf{x}\_i|t)|0\\rangle -
\\cos(|\\mathbf{x}\_j|t)|1\\rangle)\\otimes|0\\rangle-\\frac{i}{\\sqrt{2}}(\\sin(|\\mathbf{x}\_i|t)|0\\rangle -
\\sin(|\\mathbf{x}\_j|t)|1\\rangle)\\otimes|1\\rangle.\\]

By an appropriate choice of \$\$t\$\$ (\$\$|\\mathbf{x}\_i|t\$\$,
\$\$|\\mathbf{x}\_j|t\\ll1\$\$), and by measuring the ancilla bit, we
get the state \$\$\\phi\$\$ with probability
\$\$\\frac{1}{2}Z\^2t\^2\$\$, which in turns allows the estimation of
\$\$Z\$\$. If the desired accuracy of the estimation is
\$\$\\epsilon\$\$, then the complexity of constructing
\$\$|\\phi\\rangle\$\$ and \$\$Z\$\$ is \$\$O(\\epsilon\^{-1}).\$\$

If we have \$\$|\\psi\\rangle\$\$ and \$\$|\\phi\\rangle\$\$, we perform
a swap test on the ancilla alone. A swap test is a sequence of a Fredkin
gate (CSWAP gate) and an Hadamard gate which checks the equivalence of
two states \$\$|f\\rangle\$\$ and \$\$|f'\\rangle\$\$. With an ancilla
state \$\$|a\\rangle\$\$, the schematic diagram is as follows:

[caption id="attachment\_782" align="aligncenter" width="294"]![A swap
test](http://peterwittek.com/wp-content/uploads/2013/08/swap_test.png) A
swap test[/caption]

The first transformation swaps \$\$|f\\rangle\$\$ and
\$\$|f'\\rangle\$\$ if the ancilla bit is \$\$|1\\rangle\$\$. The
Hadamard transformation is a one-qubit rotation mapping the qubit states
\$\$|0\\rangle\$\$ and \$\$|1\\rangle\$\$ to two superposition states.
With [basic
algebraic](https://en.wikipedia.org/wiki/Quantum_digital_signature#Public_Key_should_be_the_same_for_every_recipient_.28Swap_Test.29)
manipulation, we conclude that if \$\$|f\\rangle\$\$ and
\$\$|f'\\rangle\$\$ are equal, then the measurement in the end will
always give us zero.

With the QRAM accesses and the estimations, the overall complexity of
evaluating a single dot product \$\$\\mathbf{x}\_i\^T\\mathbf{x}\_j\$\$
is \$\$O(\\epsilon\^{-1}\\log N).\$\$

Obtaining the Optimum of the Least Squares Dual Formulation
===========================================================

If you only calculate the kernel matrix by quantum means, you have a
complexity of \$\$O(M\^2 (M + \\epsilon\^{-1}\\log N))\$\$. There is
more to gain, exponential speedup in the number of training examples is
also possible.

The algorithm hinges on three ideas:

-   Quantum matrix inversion is fast ([Harrow et al.,     2009](#harrow2009quantum)).
-   Simulation of sparse matrixes is efficient ([Berry et al.,     2007](#berry2007efficient));
-   Non-sparse density matrices reveal the eigenstructure exponentially
    faster than in classical algorithms ([Lloyd et al.,     2009](#lloyd2013quantum2));

To solve the linear equation (1), we need to invert
\$\$F=\\left(\\begin{array}{cc}0 & 1\^T \\\\ 1 & K+\\gamma\^{-1}I
\\end{array}\\right)\$\$. The matrix inversion algorithm needs to
simulate the matrix exponential of \$\$F\$\$. We split \$\$F\$\$ as
\$\$F=J+K\_{\\gamma}\$\$, where \$\$J=\\left(\\begin{array}{cc} 0 &
1\^T\\\\1 & 0\\end{array}\\right)\$\$ -- the adjacency matrix of a star
graph, and \$\$K\_{\\gamma}=\\left(\\begin{array}{cc} 0 & 0\\\\0 &
K+\\gamma\^{-1}I\\end{array}\\right).\$\$ We normalize \$\$F\$\$ with
its trace:
\$\$\\hat{F}=\\frac{F}{\\textrm{tr}F}=\\frac{F}{\\textrm{tr}K\_{\\gamma}}.\$\$
By using the [Lie product formula](https://en.wikipedia.org/wiki/Lie_product_formula "Lie product formula"),
or, more precisely, the[Baker-Campbell-Hausdorff formula](https://en.wikipedia.org/wiki/Baker%E2%80%93Campbell%E2%80%93Hausdorff_formula "Baker-Campbell-Hausdorff formula"),
we get the exponential by  

\\[e\^{-i\\hat{F}\\Delta{}t}=e\^{\\frac{-iJ\\Delta{}t}{\\textrm{tr}K\_{\\gamma}}}e\^{\\frac{-i\\gamma\^{-1}I\\Delta{}t}{\\textrm{tr}K\_{\\gamma}}}e\^{\\frac{-iK\\Delta{}t}{\\textrm{tr}K\_{\\gamma}}}+O(\\Delta{}t\^2).\\qquad
(2)\\]

To obtain the exponentials, the sparse matrices \$\$J\$\$ and the
constant multiply of the identity matrix are easy to simulate ([Berry et al., 2007](#berry2007efficient)).

On the other hand, the kernel matrix \$\$K\$\$ is not sparse. This is
where quantum self analysis helps: given multiple copies of a density
matrix \$\$\\rho\$\$, it is possible to perform \$\$e\^{-i\\rho{}t}\$\$
([Lloyd et al., 2013](#lloyd2013quantum2)). It is self analysis because
a state plays an active role in its measurement, by exponentiation it
functions as a Hamiltonian. With the quantum calculation of the dot
product and access to the QRAM, we obtain the normalized kernel matrix
\$\$\\hat{K} =
\\frac{K}{\\textrm{tr}K}=\\frac{1}{\\textrm{tr}K}\\sum\_{i,j=1}\^M\\langle{}\\mathbf{x}\_i|\\mathbf{x}\_j\\rangle|\\mathbf{x}\_i||\\mathbf{x}\_j||i\\rangle\\langle{}j|.\$\$
\$\$\\hat{K}\$\$ is a normalized Hermitian matrix, which makes it a
prime candidate for quantum self analysis. The exponentiation is done in
\$\$O(log N)\$\$ steps. We obtain \$\$e\^{-i\\hat{K}\\Delta{}t}\$\$ by
\$\$e\^{-i\\mathcal{L}\_{\\hat{K}}\\Delta{}t}\\approx{}I-i\\Delta{}t[\\hat{K},.]+O(\\Delta{}t\^2),\$\$
where \$\$\\mathcal{L}\_{\\hat{K}}=[K,.].\$\$

We use (2) to perform quantum phase estimation to get the eigenvalues
and eigenvectors. If the desired accuracy is \$\$\\epsilon\$\$, we need
\$\$n=O(\\epsilon\^{-3})\$\$ copies of the state. Then we express the
\$\$\\mathbf{y}\$\$ in (1) in the eigenbasis, and invert the eigenvalues
to obtain the solution \$\$|b, \\mathbf{\\alpha}\\rangle\$\$ of the
linear equation ([Harrow et al., 2009](#harrow2009quantum)).

With this inversion algorithm, the overall time complexity of training
the support vector parameters is \$\$O(\\log(NM))\$\$.

Limitations and Open Questions
==============================

The approach only works for dense training vectors, for obvious reasons.
In many classical algorithms, execution speed -- and not complexity --
is improved by exploiting sparse data structures. Such structures are
common in applications, such as text mining and recommendation engines.
It is unclear how a sparse vector maps to a quantum state.

The kernel function is restricted. Linear and polynomial kernels are
easy to implement, in fact, the inner product is evaluated directly in
the embedding space. Radial basis function kernels are much harder to
imagine in this framework, and these are the kernels the most common.

Non-symmetric kernels are out of reach for the time being. One
restriction is the linear or polynomial kernel. The other constraint is
the matrix inversion, although the generic method extends to
non-Hermitian matrices, so this problem is easier to sort out.

\$\$O(\\log(MN))\$\$ states are required to perform classification,
which is both good and bad. It is good because it compresses the kernel
exponentially. It is bad because the trained model is not sparse. A
pivotal point in the success of SVMs is [structural risk minimization](https://en.wikipedia.org/wiki/Structural_risk_minimization "Structural risk minimization"):
the learned model should not overfit the data, otherwise its
generalization performance will be poor. The quantum SVM massively
overfits the data, every single data instance will become a support
vector. None of the \$\$\\alpha\_i\$\$-s will be zero. It would be
interesting to see how this translates to actual classification
performance on real-world data sets.

References
==========

<a name="berry2007efficient"></a>Berry, D. W.; Ahokas, G.; Cleve, R. &
Sanders, B. C. [Efficient quantum algorithms for simulating sparse Hamiltonians](http://arxiv.org/abs/quant-ph/0508139). *Communications in
Mathematical Physics*, 2007, 270, 359-371.  
<a name="giovannetti2008quantum"></a>Giovannetti, V.; Lloyd, S. &
Maccone, L. [Quantum random access memory](http://arxiv.org/abs/0708.1879). *Physical Review Letters*,
2008, 100, 160501.  
<a name="harrow2009quantum"></a>Harrow, A. W.; Hassidim, A. & Lloyd, S.
[Quantum algorithm for linear systems of equations](http://arxiv.org/abs/0811.3171). *Physical Review Letters*,
2009, 103, 150502.  
<a name="lloyd2013quantum2"></a>Lloyd, S.; Mohseni, M. & Rebentrost, P.
[Quantum self analysis](http://arxiv.org/abs/1307.0401).
*arXiv:1307.0401*, 2013.  
<a name="lloyd2013quantum"></a> Lloyd, S.; Mohseni, M. & Rebentrost, P.
[Quantum algorithms for supervised and unsupervised machine learning](http://arxiv.org/abs/1307.0411). *arXiv:1307.0411*, 2013.  
<a name="rebentrost2013quantum"></a>Rebentrost, P.; Mohseni, M. &
Lloyd, S.[Quantum support vector machine for big feature and big data classification](http://arxiv.org/abs/1307.0471). *arXiv:1307.0471*,
2013.  
<a name="suykens1999least"></a> Suykens, J. A. & Vandewalle, J. [Least squares support vector machine classifiers](http://link.springer.com/article/10.1023/A:1018628609742).
*Neural Processing Letters*, 1999, 9, 293--300.
