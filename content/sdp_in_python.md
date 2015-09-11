Title: Semidefinite programming in Python
Date: 2015-09-11 18:33
Author: Peter
Category: 
Tags: Semidefinite programming, Python
Slug: sdp-in-python
Summary: A brief overview of SDP solvers and tools in Python

Python is becoming an outstanding environment for doing semidefinite programming. Many solvers have a Python interface, and we have a few tools to help defining SDPs. It is worth taking a brief overview at the available options. Please drop me a note if you think something is missing and I update the post.

Fortunately, almost all of the tools listed here are compatible with both Python 2 and 3. Only CVXOPT is included in [Anaconda](https://store.continuum.io/cshop/anaconda/), but most of the other tools (CVXPY, PICOS, Ncpol2sdpa) can be installed from PyPI. A convenient install of these modules is important in making MATLAB obsolete.

As most of the tools rely on sparse matrices for representing data and sometimes on C or C++ for implementing computationally intensive parts, Pypy will usually not work. The exceptions are PyLMI-SDP and Ncpol2sdpa. From the commercial solvers, I only tested Mosek, which works just fine. The table below summarizes the key characteristics of the tools.

Tool      |Python 2|Python 3|Pypy|PyPI| Anaconda
----------|:------:|:------:|:--:|:--:|:-------:
CVXOPT    |Yes     |Yes     | No | No | Yes
SDPA-P    |Yes     |?       |?   | No | No
Mosek     |Yes     |Yes     |Yes | No | No
SMCP      |Yes     |No      |No  | No | No
SCS       |Yes     |Yes     |No  | Yes| No
CVXPY     |Yes     |Yes     |No  | Yes| No
PICOS     |Yes     |Yes     |No  | Yes| No
PyLMI-SDP |Yes     |Yes     |Yes | No | No
Ncpol2sdpa|Yes     |Yes     |Yes | Yes| No


Solvers
--------
[CVXOPT](http://cvxopt.org/) is a convex solver in Python that includes SDPs. It uses its own sparse matrix implementation, which is almost identical to SciPy's `lil_matrix`. Computationally intensive parts are implemented in C. Unfortunately, as of version 1.1.7, CVXOPT is a bit fragile and sometimes chokes on correctly formed SDPs.

The SDP solver family [SDPA](http://sdpa.sourceforge.net/) has a Python interface called SDPA-P. It was last updated three years ago, and its capabilities are now mostly available in PICOS (see below). SDPA remains challenging to compile, and this applies to Python version too.

The commercial optimization products [Mosek](http://mosek.com/), [CPLEX](http://www-01.ibm.com/software/commerce/optimization/cplex-optimizer/), and [Gurobi](http://www.gurobi.com) all have a Python interface.

[SMCP](https://smcp.readthedocs.org/) can solve sparse matrix cone problems in Python.

[SCS](https://github.com/cvxgrp/scs) solves convex cone problems via operator splitting and it has a Python interface. It might prove faster but less accurate than other solvers.

Defining problems
-------------------
Having an SDP solver is awesome, but it is even better if we have handy tools to define SDP problems. 

[CVXPY](http://www.cvxpy.org/) uses the disciplined convex programming paradigm similar to [CVX](http://cvxr.com/cvx/) in MATLAB. On the back-end, it can use either CVXOPT or SCS for solving SDPs.

[PICOS](http://picos.zib.de/) is the Python Interface for Conic Optimization Solvers, which resembles [Yalmip](http://users.isy.liu.se/johanl/yalmip/) in MATLAB. For solving SDPs, it can use CVXOPT, SDPA, Mosek, CPLEX, and Gurobi.

[PyLMI-SDP](https://github.com/cdsousa/PyLMI-SDP) provides symbolic linear matrix inequalities (LMI) and SDP tools for Python. It has some similar functionality to PICOS, but it relies on [SymPy](http://www.sympy.org/) for symbolic operations, whereas PICOS does all symbolic operations itself. Not reinventing the wheel always sounds good, but unfortunately this module sees limited development.

SDP relaxations of polynomial optimization problems
----------------------------------------------------------
[Ncpol2sdpa](https://ncpol2sdpa.readthedocs.org/) generates semidefinite relaxations of polynomial optimization problems. If the variables are commutative, it generates the Lasserre hierarchy, similarly to  [Gloptipoly](http://homepages.laas.fr/henrion/software/gloptipoly/) in MATLAB. It is also able to use the sparse structure of such problems, like [SparsePOP](http://sparsepop.sourceforge.net/) in MATLAB. If the variables are noncommutative, it generates various incarnations of the NPA hierarchy. For instance, in Bell scenarios, it can calculate maximum violations similarly to [NPAHierarchy](http://www.qetlab.com/NPAHierarchy) in MATLAB, but it also encompasses a wider ranger of applications, such as calculating the ground-state energy of certain Hamiltonians. 
