Title: Semidefinite programming in Python
Date: 2015-09-11 18:33
Author: Peter
Category: 
Tags: Semidefinite programming, Python
Slug: sdp-in-python
Summary: A brief overview of SDP solvers and tools in Python

Python is becoming an outstanding environment for doing semidefinite programming. Many solvers have a Python interface, and we have a few tools to help defining SDPs. It is worth taking a brief overview at the available options. Please drop me a note if you think something is missing and I update the post.

Fortunately, almost all of the tools listed here are compatible with both Python 2 and 3. Only CVXOPT is included in [Anaconda](https://store.continuum.io/cshop/anaconda/), but most of the other tools (CVXPY, PICOS, Ncpol2sdpa) can be installed from PyPI. A convenient install of these modules is important in making MATLAB obsolete.

As most of the tools rely on sparse matrices for representing data and sometimes on C or C++ for implementing computationally intensive parts, Pypy will usually not work. The exceptions are PyLMI-SDP and Ncpol2sdpa. From the commercial solvers, I only tested Mosek, which works just fine. The table below summarizes the key characteristics of the tools. The last column refers to whether complex Hermitian matrices are handled natively.

Tool      |Version|Python 2|Python 3|Pypy|PyPI| Anaconda|Hermitian
----------|:-----:|:------:|:------:|:--:|:--:|:-------:|:-------:
CVXOPT    |1.1.8  |Yes     |Yes     |No  | Yes| Yes     |No
SDPA-P    |0.2.1  |Yes     |?       |?   | No | No      |No
Mosek     |7.1    |Yes     |Yes     |Yes | No | No      |No
SMCP      |0.4.1  |Yes     |No      |No  | Yes| No      |No
SCS       |1.1.5  |Yes     |Yes     |No  | Yes| No      |No
CVXPY     |0.3.2  |Yes     |Yes     |No  | Yes| No      |No
PICOS     |1.1.1  |Yes     |Yes     |No  | Yes| No      |Yes
PyLMI-SDP |1.0    |Yes     |Yes     |Yes | No | No      |No
Ncpol2sdpa|1.9    |Yes     |Yes     |Yes | Yes| No      |Yes


Solvers
--------
[CVXOPT](http://cvxopt.org/) is a convex solver in Python that includes SDPs. It uses its own sparse matrix implementation, which is almost identical to SciPy's `lil_matrix`. Computationally intensive parts are implemented in C. Unfortunately, as of version 1.1.8, CVXOPT is a bit fragile and sometimes chokes on correctly formed SDPs. Support for complex matrices is under development.

The SDP solver family [SDPA](http://sdpa.sourceforge.net/) has a Python interface called SDPA-P. It was last updated three years ago, and its capabilities are now mostly available in PICOS (see below). SDPA remains challenging to compile, and this applies to Python version too.

The commercial optimization products [Mosek](http://mosek.com/), [CPLEX](http://www-01.ibm.com/software/commerce/optimization/cplex-optimizer/), and [Gurobi](http://www.gurobi.com) all have a Python interface.

[SMCP](https://smcp.readthedocs.io/) can solve sparse matrix cone problems in Python.

[SCS](https://github.com/cvxgrp/scs) solves convex cone problems via operator splitting and it has a Python interface. It might prove faster but less accurate than other solvers.

Defining problems
-------------------
Having an SDP solver is awesome, but it is even better if we have handy tools to define SDP problems. 

[CVXPY](http://www.cvxpy.org/) uses the disciplined convex programming paradigm similar to [CVX](http://cvxr.com/cvx/) in MATLAB. On the back-end, it can use either CVXOPT or SCS for solving SDPs.

[PICOS](http://picos.zib.de/) is the Python Interface for Conic Optimization Solvers, which resembles [Yalmip](http://users.isy.liu.se/johanl/yalmip/) in MATLAB. For solving SDPs, it can use CVXOPT, SDPA, Mosek, CPLEX, and Gurobi. It has support for complex and Hermitian matrices.

[PyLMI-SDP](https://github.com/cdsousa/PyLMI-SDP) provides symbolic linear matrix inequalities (LMI) and SDP tools for Python. It has some similar functionality to PICOS, but it relies on [SymPy](http://www.sympy.org/) for symbolic operations, whereas PICOS does all symbolic operations itself. Not reinventing the wheel always sounds good, but unfortunately this module sees limited development.

SDP relaxations of polynomial optimization problems
----------------------------------------------------------
[Ncpol2sdpa](https://ncpol2sdpa.readthedocs.io/) generates semidefinite relaxations of polynomial optimization problems. If the variables are commutative, it generates the Lasserre hierarchy, similarly to  [Gloptipoly](http://homepages.laas.fr/henrion/software/gloptipoly/) in MATLAB. It is also able to use the sparse structure of such problems, like [SparsePOP](http://sparsepop.sourceforge.net/) in MATLAB. If the variables are noncommutative, it generates various incarnations of the NPA hierarchy. For instance, in Bell scenarios, it can calculate maximum violations similarly to [NPAHierarchy](http://www.qetlab.com/NPAHierarchy) in MATLAB, but it also encompasses a wider ranger of applications, such as calculating the ground-state energy of certain Hamiltonians. It supports complex Hermitian matrices.
