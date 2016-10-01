Title: Comparing three numerical solvers of the Gross-Pitaevskii equation
Date: 2016-02-03 16:59
Author: Peter
Category: Quantum information theory
Tags: Quantum information theory, GPU
Slug: gpe-comparison
Summary: A quick comparison of Trotter-Suzuki-MPI, GPELab, and GPUE for simulating the evolution of Bose-Einstein Condensates

The numerical simulation of Bose-Einstein condensates is a challenging task, even more so if we are interested in fast rotating vortices. We compare two implementations that rely on time-splitting pseudospectral methods, [GPELab](http://gpelab.math.cnrs.fr/) and [GPUE](https://mlxd.github.io/GPUE/), and one that uses the Trotter-Suzuki approximation ([Trotter-Suzuki-MPI](http://trotter-suzuki-mpi.github.io/)). I am involved in the development of the last one and I was curious how it performs compared to other methods. This comparison is joint work with [Luca Calderaro](https://github.com/Lucacalderaro), my co-developer in the Trotter-Suzuki project who did all the coding of the test cases, and we also received help from [Lee James O'Riordan](https://www.researchgate.net/profile/Lee_ORiordan), the main developer of GPUE, for which we are grateful.

Features
========
When it comes to the physics of the problem, GPELab takes the prime: it can tackle the widest range of problems in arbitrary spatial dimensions. Furthermore, its documentation is extensive. TS-MPI lags behind in documentation, but the latest release made progress in making problem definition more straightforward. GPUE can be hard to fathom.

| Physics Modelling          |&nbsp;TS-MPI  |&nbsp;GPUE   |&nbsp;GPELab |
| -------------------------- |:-------:|:------:|:------:|
| Dimension                  | 2D      | 2D     |1D/2D/3D|
| Linear Schrödinger Equation| Yes     | Yes    | Yes    |
| Vortices in BEC            | Yes     | Yes    | Yes    |
| 2-Component BEC            | Yes     | No     | Yes    |

GPELab's main weakness is that it only runs in MATLAB, with all the pain that implies from licence fees to the 1970s syntax. Running it on a supercomputer is an exceptional challenge, which puts severe limitations on GPELab's scalability. GPUE runs from the command line and it has a handful of Python routines to process the output. TS-MPI is the most flexible, as it allows the computational core to be called [interactively from Python](https://trotter-suzuki-mpi.readthedocs.io/), but it also exposes a C++ API for more scalable calculations on a cluster. On the other hand, only a fraction of its functionality is exposed through its command-line interface, and MATLAB support was dropped in version 1.5.

| Computational Environment   |&nbsp;TS-MPI  |&nbsp;GPUE   |&nbsp;GPELab |
| --------------------------- |:-------:|:------:|:------:|
| Command line                | Partial | Yes    | No     |
| C++ API                     | Yes     | No     | No     |
| Python                      | Yes     | Partial| No     |
| MATLAB                      | Partial | No     | Yes    |

GPELab uses multicore CPUs, but MATLAB puts performance constraints on the calculations. The main selling point of GPUE is, naturally, that it uses the GPU. Apart from the GPU routines, some auxiliary computations are also parallelized on the CPU. GPUE can use only one GPU. TS-MPI was conceived to be massively parallel, so it can use several GPUs and it also runs on a cluster, but in the absence of these resources, a multicore CPU will do. Its GPU kernel can handle several types of the Gross-Pitaevskii equation, but it is not extended yet to work with a nonzero angular velocity.

| Parallel and Distributed Computing|&nbsp;TS-MPI  |&nbsp;GPUE   |&nbsp;GPELab |
| --------------------------------- |:-------:|:------:|:------:|
| Multicore                         | Yes     | Partial| Yes    |
| GPU                               | Partial | Yes    | No     |
| Cluster                           | Yes     | No     | No     |

Experiments
===========
We created two test cases. One is a real time evolution of a Gaussian initial state in a harmonic potential with open boundary conditions on a 2D lattice of 256x256 points. We measured the wall clock time of the kernel execution. The GPU kernels were tested on an Nvidia Tesla C2050 card, and the CPU kernels ran on a four-core Intel i7-4790 @ 3.60GHz. The purpose was measuring the performance on a single node, so we did not use TS-MPI's distributed capabilities.

The test cases for TS-MPI are included in the source code of the library ([harmonic_osc_real.cpp](https://github.com/trotter-suzuki-mpi/trotter-suzuki-mpi/blob/master/examples/harmonic_osc_real.cpp) and [harmonic_osc_imag.cpp](https://github.com/trotter-suzuki-mpi/trotter-suzuki-mpi/blob/master/examples/harmonic_osc_imag.cpp)). GPUE was run with the following commands:


    $ gpue -x 256 -y 256 -T 1e-4 -t 1e-4 -n 1e6 -g 0 -e 2e4 -p 1000 -r 0 -w 0. -o 0 -d 0 -l 0 -s 0 -i 1.0 -P 0.0 -G 1.0 -L 0 -X 1 -Y 1 -k 0 -O 0.0 -W 1 -U 0 -V 0 -S 0.0 -a 0
    $ gpue -x 256 -y 256 -T 1e-4 -t 1e-4 -n 1e6 -g 4.01e4 -e 0 -p 1000 -r 0 -w 0. -o 0 -d 0 -l 0 -s 0 -i 1.0 -P 0.0 -G 1.0 -L 0 -X 1 -Y 1 -k 0 -O 0.0 -W 1 -U 0 -V 0 -S 0.0 -a 0*

The MATLAB scripts for GPELAB are available [here](https://gist.github.com/Lucacalderaro/a67269cfe3d494bebf59) for the real-time evolution and [here](https://gist.github.com/Lucacalderaro/4bf51c7ca2b0603174b4) for the imaginary-time evolution.

The following table summarizes the execution time of the kernels (in seconds, see also the figure):

| Implementation    |&nbsp;Real-Time Evolution|&nbsp;Imaginary-Time Evolution|
| ------------------|:-------:|:------:|
| GPUE              | 9       | 19     |
| GPELab            | 1859.7  | 2796.2 |
| TS-MPI CPU kernel | 50.3    | 66.1   |
| TS-MPI GPU kernel | 10.7    | 22.9   |


Looking at the execution time, GPUE is the clear winner. It has a marginal advantage over TS-MPI with the GPU kernel in real-time evolution, but it is faster in imaginary-time evolution. This is a limitation of the Trotter-Suzuki approximation when applied to imaginary-time evolution: the state has to be renormalized in every iteration, which results in a substantial increase in computational time.

The overhead of MATLAB is stunning. To keep the comparison apples to apples, the closest equivalent is the CPU kernel of TS-MPI. Even compared to that, it is 37x slower in real-time evolution, and 42x slower in imaginary-time evolution.

<center>![GPE comparison chart]({filename}/images/gpe_comparison.png)</center>

The precision of all kernels were very close, so a detailed comparison is unnecessary. All in all, there is a huge price to pay for using MATLAB both in terms of licence fees and in computational time, whereas GPUE and TS-MPI are head to head in raw performance.
