Title: Comparing three numerical solvers of the Gross-Pitaevskii equation
Date: 2016-02-03 16:59
Author: Peter
Category: Quantum information theory
Tags: Quantum information theory
Slug: gpe-comparison
Summary: A quick comparison of Trotter-Suzuki-MPI, GPELab, and GPUE for simulating Bose-Einstein Condensates

The numerical simulation of Bose-Einstein condensates is a challenging task, even more so if we are interested in fast rotating vortices. We compare two implementations that rely on time-splitting pseudospectral methods, [GPELab](http://gpelab.math.cnrs.fr/) and [GPUE](https://mlxd.github.io/GPUE/), and one that uses the Trotter-Suzuki approximation ([Trotter-Suzuki-MPI](http://trotter-suzuki-mpi.github.io/)). I am involved in the development of the last one and I was curious how it performs compared to other methods. This comparison is joint work with [Luca Calderaro](https://github.com/Lucacalderaro), my co-developer in the Trotter-Suzuki project who did all the coding of the test cases, and we also received help from [Lee James O'Riordan](https://www.researchgate.net/profile/Lee_ORiordan), the main developer of GPUE, for which we are grateful.

Features
========
When it comes to the physics of the problem, GPELab takes the prime: it can tackle the widest range of problems in arbitrary spatial dimensions. Furthermore, its documentation is extensive. TS-MPI lags behind in documentation, but the latest release made progress in making problem definition more straightforward. GPUE can be hard to fathom.

| Physics Modelling          | TS-MPI  | GPUE   | GPELab |
| -------------------------- |:-------:|:------:|:------:|
| Dimension                  | 2D      | 2D     |1D/2D/3D|
| Linear Schrödinger Equation| Yes     | Yes    | Yes    |
| Vortices in BEC            | Yes     | Yes    | Yes    |
| 2-Component BEC            | Yes     | No     | Yes    |

GPELab's main weakness is that it only runs in MATLAB, with all the pain that implies from licence fees to the 1970s syntax. Running it on a supercomputer is an exceptional challenge, which puts severe limitations on GPELab's scalability. GPUE runs from the command line and it has a handful of Python routines to process the output. TS-MPI is the most flexible, as it allows the computational core to be called interactively from Python, but it also exposes a C++ API for more scalable calculations on a cluster. On the other hand, only a fraction of its functionality is exposed through the command line, and MATLAB support was dropped in version 1.5.

| Computational Environment   | TS-MPI  | GPUE   | GPELab |
| --------------------------- |:-------:|:------:|:------:|
| Command line                | Partial | Yes    | No     |
| C++ API                     | Yes     | No     | No     |
| Python                      | Yes     | Partial| No     |
| MATLAB                      | Partial | No     | Yes    |

GPELab uses multicore CPUs, but of course MATLAB puts performance constraints on the calculations. The main selling point of GPUE is, naturally, that it uses the GPU. Apart from the GPU routines, some auxiliary computations are also parallelized. GPUE can use one GPU. TS-MPI was conceived to be massively parallel, so it can use several GPUs and it also runs on a cluster, but in the absence of these resources, a multicore CPU will do.

| Parallel and Distributed Computing| TS-MPI  | GPUE   | GPELab |
| --------------------------------- |:-------:|:------:|:------:|
| Multicore                         | Yes     | Yes    | Yes    |
| GPU                               | Yes     | Yes    | No     |
| Cluster                           | Yes     | No     | No     |

Experiments
===========
We created two test cases. One is a real time evolution of a Gaussian initial state in a harmonic potential with closed boundary conditions on a 2D lattice of 256x256 points. We measured the wall clock time of the kernel execution. The GPU kernels were tested on an Nvidia Tesla C2050 card, and the CPU kernels ran on a four-core Intel i7-4790 @ 3.60GHz. The purpose was measuring the performance on a single node, so we did not use TS-MPI's distributed capabilities.

The test cases for TS-MPI are included in the source code of the library ([harmonic_osc_real.cpp](https://github.com/trotter-suzuki-mpi/trotter-suzuki-mpi/blob/master/examples/harmonic_osc_real.cpp) and [harmonic_osc_imag.cpp](https://github.com/trotter-suzuki-mpi/trotter-suzuki-mpi/blob/master/examples/harmonic_osc_imag.cpp)). GPUE was run with the following commands:

::
    gpue -x 256 -y 256 -T 1e-4 -t 1e-4 -n 1e6 -g 0 -e 2.01e4 -p 1000 -r 0 -w 0. -o 0 -d 0 -l 0 -s 0 -i 1.0 -P 0.0 -G 1.0 -L 0 -X 1 -Y 1 -k 0 -O 0.0 -W 1 -U 0 -V 0 -S 0.0 -a 0*

::
    gpue -x 256 -y 256 -T 1e-4 -t 1e-4 -n 1e6 -g 2.01e4 -e 0 -p 1000 -r 0 -w 0. -o 0 -d 0 -l 0 -s 0 -i 1.0 -P 0.0 -G 1.0 -L 0 -X 1 -Y 1 -k 0 -O 0.0 -W 1 -U 0 -V 0 -S 0.0 -a 0*

Speed
-----

Real time evolution

GPUE: 9


Imaginary time evolution

GPUE: 10

Accuracy
--------
