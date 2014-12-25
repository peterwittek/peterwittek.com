Title: Memory use of translating SDP problems
Date: 2013-07-01 00:01
Author: Peter
Category: Python
Tags: Python, Semidefinite programming, SymPy
Slug: memory-use-of-translating-sdp-problems
Summary: Generating semidefinite programming relaxations of a noncommutative polynomial optimization problem is memory-hungry: some solutions are explored.

Trying to generate the semidefinite programming relaxation of a ground
state problem, we quickly run into memory constraints. Lattices above
4×4 require memory above 220 GByte, which is hardly feasible. Treating
the underlying third-party tools as a black box, I looked into whether
different Python flavours or other techniques would yield a more
efficient use of memory. All experiments used Cvxopt 1.1.6, PICOS 0.1.3,
and Sympy 0.7.2. The baseline implementation of
[Ncpol2sdpa](http://peterwittek.github.io/ncpol2sdpa/ "Ncpol2sdpa")
relied on CPython 2.7.5.

Pypy
====

[Pypy](http://pypy.org/ "Pypy") is an alternative implementation of
Python that promises using less memory. The latest version is 2.0.2. It
installed to an alternative directory and it does not see the installed
Python modules by default; we must set the ``PYTHONPATH`` variable manually:

    :::bash
    $ export PYTHONPATH=/usr/lib64/python2.7/site-packages

Unfortunately, Pypy does not like Cvxopt:

    :::bash
    $ pypy hamiltonian.py
    Traceback (most recent call last):
    File "app_main.py", line 72, in run_toplevel
    File "hamiltonian.py", line 18, in
    from sdprelaxation import get_relaxation
    File "/home/wittek/wrk/python/ncpol2sdpa-pypy/sdprelaxation.py", line 11, in
    import picos
    File "/usr/lib64/python2.7/site-packages/picos/__init__.py", line 28, in
    from problem import *
    File "/usr/lib64/python2.7/site-packages/picos/problem.py", line 29, in
    import cvxopt as cvx
    File "/usr/lib64/python2.7/site-packages/cvxopt/__init__.py", line 32, in
    import cvxopt.base
    ImportError: No module named cvxopt.base

Installing Cvxopt from source with Pypy as the interpreter lead to a
compilation error. Apparently, [others](http://morepypy.blogspot.com/2011/05/playing-with-linear-programming-on-pypy.html) also ran into problems when interfacing Cvxopt and Pypy.

Python 3
========

An obvious candidate is the latest release of Python, version 3.3.2.
Numpy, Cvxopt, and Sympy are known to work with Python 3. PICOS is not.
Having zero proficiency in 2 to 3 conversion, and no interest in
learning it, I ran the script to translate the source, and then install
PICOS.

    :::bash
    $ 2to3 -w *.py
    $ python setup.py install --user

Starting Ncpol2sdpa, an error message halts the script:

    :::bash
    idmat=cvx.spmatrix(V,I,J,(s0*s0,s0*(s0+1)/2))
    TypeError: invalid dimension tuple

The error string is defined in Cvxopt. PICOS needs an undefined amount
of work to be compatible with Python 3.

Cython 2
========

[Cython](http://cython.org/ "Cython") is the beacon of hope, generating
C code from Python scripts, which are then compiled by GCC. Since Cvxopt
uses Blas and Lapack as its backend, it should be efficient. My goal was
to compile PICOS and Ncpol2sdpa, and it was straightforward with Cython
0.19.1. This script compiles shared libraries of the modules of both
PICOS and Ncpol2sdpa:

    :::bash
    #!/bin/bash
    cython2 *.py
    for i in `ls *.c`; do
      gcc -c -fPIC -O3 -I/usr/include/python2.7 "${i%.*}.c"
    done
    for i in `ls *.o`; do
      gcc "${i%.*}.o" -shared -o "${i%.*}.so"
    done

The script to execute must have a main function, and we must link
external libraries:

    :::bash
    $ cython2 --embed hamiltonian.py
    $ gcc -c -O3 -I/usr/include/python2.7 hamiltonian.c
    $ gcc -o hamiltonian -lpython2.7 ncutils.o sdp_relaxation.o hamiltonian.o

The execution time for a lattice of 3×3 barely improved. The Cython
variant finished in 24.16 s, whereas the CPython took 24.97 s. Memory
use was marginally more for Cython: 406072k versus 404400k.

Finding the source of high memory use
=====================================

As Python interpreters and compilers failed me, I turned to profiling to
find which module took up so much memory.
[Meliae](https://launchpad.net/meliae "Meliae") dumped memory
information to a file by including these two lines in the Hamiltonian
script:

    :::python
    from meliae import scanner
    scanner.dump_all_objects( "memorydump" )

[Runsnakerun](http://www.vrplumber.com/programming/runsnakerun/ "Runsnakerun")
plotted the result:

[![Memory use with a 3x3
lattice](http://peterwittek.com/wp-content/uploads/2013/06/hamiltonian3x3memoryuse-1024x578.png)](http://peterwittek.com/wp-content/uploads/2013/06/hamiltonian3x3memoryuse.png)

This is a sad diagram to look at. There is no single culprit, the memory
use is fragmented to thousands of unrelated modules. The module
sympy.plotting.textplot was suspicious, as it was called many times, it
was also one of the bigger memory hogs, and the code never textplotted
anything. The reasons behind calling textplot remain obscure, but Sympy
did turn out to be memory-inefficient due to its cache mechanism for
symbolic variables. I turned the cache off with an environment variable:

    :::bash
    $ export SYMPY_USE_CACHE=no

The running time was about 30 % longer (33.41 s versus 24.97 s), and
memory use decreased by nearly 10 % (down to 368264k from 404400k).
Unfortunately, the decrease was less than a 1 % for a lattice of 4×4.

To check whether it was Sympy that used most of the memory, I removed
all references to PICOS calls. The memory use dropped to 65028k. Sympy
was innocent.

Cvxopt only accepts basic types in matrix variables
===================================================

Digging deeper into PICOS calls, the source of problems boiled down to
defining the entries of SDP constraints. For instance, an equality with
a matrix variable is defined as follows:

    :::python
    Meq = prob.add_variable('Meq', (size, size), vtype = 'symmetric')
    prob.add_constraint(Meq == 0)

The next step is to add the entries of the symmetric matrix. If the
entries are numbers, this is very simple, a list or a Numpy array will
do:
  
    :::python
    Meq.value = whatEverListOrNumpyArray

The above line will drop an error if the list or array contains an
affine expression. The problem is with Cvxopt, it accepts only basic
types as matrix entries, as it was noted
[elsewhere](http://ask.sagemath.org/question/743/lovasz-number "Sage and Cvxopt").
Since we only have affine expressions of relaxed equality constraints,
our only option is to force constraints on each (i,j) element of the
matrix in the following form

    :::python
    prob.add_constraint(Meq[i, j] == eqrelax)

So if PICOS and Cvxopt are used, memory use will always limit the size
of the problems you can solve.
