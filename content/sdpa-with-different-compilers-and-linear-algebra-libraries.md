Title: SDPA with different compilers and linear algebra libraries
Date: 2014-08-28 02:22
Author: Peter
Category: Semidefinite programming
Tags: Semidefinite programming, C++
Slug: sdpa-with-different-compilers-and-linear-algebra-libraries

I made a quick comparison between three compilers and three BLAS and
LAPACK implementations for using [SDPA](http://sdpa.sourceforge.net/).
The experiments were conducted on the fat nodes of the
[Abisko](http://www.hpc2n.umu.se/resources/abisko/cpuarch) cluster of
the High Performance Computing Center North, each having 48 AMD cores
arranged in NUMA blocks of 6 cores, and 512 GBytes of RAM. I tested GCC
4.6.3, ICC 14.0, and PGI 14.3 compilers. The Pathscale compiler was also
available, but I could not get it to compile MUMPS -- it is
[probably](https://www.olcf.ornl.gov/kb_articles/software-tpsl/) not
supported. OpenBLAS was version 0.2.9, LAPACK was 3.5.0, ACML 5.3.1, and
MKL 11.1. The [benchmark SDP problem](http://peterwittek.com/files/benchmark.dat-s) had nearly three
thousand variables and nineteen blocks.

Compilation was not entirely trivial; see the detailed instructions
below. The cluster used SLURM for job scheduling. I blocked an entire
fat node for each experiment. The job description followed this pattern:

    :::bash
    #!/bin/bash
    #SBATCH -A <project id>
    #SBATCH -N 1
    #SBATCH -n 1
    #SBATCH -c 48
    #SBATCH --ntasks-per-node=1
    #SBATCH -p bigmem
    #SBATCH --exclusive
    #SBATCH --time=00:01:00

    module load <necessary modules>
    export OMP_NUM_THREADS=48
    srun sdpa benchmark.dat-s benchmark.out

Results
=======

The comparison is not entirely fair, since I did not delve into
optimizing the individual compilers. The running time results were as
follows (the values are in seconds):

|BLAS/|MKL|ACML|LAPACK
------------------|------------------|------------------|------------------
|GCC|37.21|23.03|21.42
|ICC|37.31|11.48|18.83
|PGI|251.48|22.03|N/A

The proprietary compilers are certainly more annoying, as they have
unusual quirks that need to be addressed to compile SDPA. PGI's OpenMP
support is particularly obnoxious, and the configure script would not
run with the ACML parameters; I gave up after wasting forty-five minutes
on it.

Despite the gripes, ICC's performance with MKL is remarkable, especially
since the hardware was AMD. PGI was a disappointment: with the default
BLAS/LAPACK, its performance was abysmal, and with MKL, it had an
average result.

Apart from running time, there was not much difference between the
scenarios. Most notably, memory use was nearly identical in all cases.

Compiling SDPA with different compilers and libraries
=====================================================

The following settings summarize what was to be done to compile SDPA
with the various tools and libraries.

GCC and MKL
-----------
    
    :::bash
    module load mkl
    export CFLAGS=$MKL_INCLUDE
    export CXXFLAGS=$MKL_INCLUDE
    export FFLAGS=$MKL_INCLUDE
    export LIBS="-lmkl_intel_lp64 -lmkl_gf_lp64 -lmkl_core -lmkl_sequential -lpthread -lm"
    ./configure --with-blas="-L$MKL_LDFLAGS" --with-lapack="-L$MKL_LDFLAGS"
    make -s

GCC and ACML
------------

    :::bash
    module load acml/gcc
    export CFLAGS=$ACML_INCLUDE
    export CXXFLAGS=$ACML_INCLUDE
    export FFLAGS=$ACML_INCLUDE
    ./configure --with-blas="$ACML_LDFLAGS $ACML_LIBS" --with-lapack="$ACML_LDFLAGS $ACML_LIBS"
    make -s

ICC and BLAS/LAPACK
-------------------

    :::bash
    module load intel
    export CC=icc
    export CXX=icpc
    export FC=ifort
    ./configure
    make -s

ICC and MKL
-----------

    :::bash
    module load intel mkl
    export CC=icc
    export CXX=icpc
    export FC=ifort
    export CFLAGS=$MKL_INCLUDE
    export CXXFLAGS=$MKL_INCLUDE
    export FFLAGS=$MKL_INCLUDE
    ./configure --with-blas="-L$MKL_LDFLAGS -mkl" --with-lapack="-L$MKL_LDFLAGS -mkl"
    make -s

ICC and ACML
------------

    :::bash
    module load intel acml/intel
    export CC=icc
    export CXX=icpc
    export FC=ifort
    export CFLAGS=$ACML_INCLUDE
    export CXXFLAGS=$ACML_INCLUDE
    export FFLAGS=$ACML_INCLUDE
    ./configure --with-blas="$ACML_LDFLAGS -lintlc $ACML_LIBS" --with-lapack="$ACML_LDFLAGS -lintlc $ACML_LIBS"
    make -s

PGI and BLAS/LAPACK
-------------------

    :::bash
    module load pgi
    export CC=pgcc
    export CXX=pgc++
    export FC=pgfortran
    export LIBS=-lgfortran 
    export CFLAGS="-mp"
    export CXXFLAGS="-mp"
    export FFLAGS="-mp"
    cat configure|sed -e 's/-Wall//'|sed -e 's/-funroll-all-loops//' > configure.tmp
    mv configure.tmp configure
    chmod 755 configure
    ./configure
    make -s

PGI and MKL
-----------

    :::bash
    module load pgi mkl
    export CC=pgcc
    export CXX=pgc++
    export FC=pgfortran
    export CFLAGS="$MKL_INCLUDE -mp"
    export CXXFLAGS="$MKL_INCLUDE -mp"
    export FFLAGS="$MKL_INCLUDE -mp"
    cat configure|sed -e 's/-Wall//'|sed -e 's/-funroll-all-loops//' > configure.tmp
    mv configure.tmp configure
    chmod 755 configure
    ./configure --with-blas="$MKL_LDFLAGS -lmkl_intel_lp64 -lmkl_core -lmkl_sequential -lpthread -lm -lgfortran" --with-lapack="$MKL_LDFLAGS -lmkl_intel_lp64 -lmkl_core -lmkl_sequential -lpthread -lm -lgfortran"
    make -s
