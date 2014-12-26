Title: CuBlas matrix multiplication with C-style arrays
Date: 2013-06-17 06:48
Author: Peter
Category: C++
Tags: C++, GPU
Slug: cublas-matrix-c-style
Summary: Getting around Fortran-style array indexing in CuBlas from C code without transponation. Bonus Thrust vector casting added.

CuBlas has decently optimized calls, but it stuck with column-first
indexing, which makes it mind-bogglingly annoying to use in C code.
Refusing to switch to Fortran-style indexing, I spent some time figuring
which parameter should be what, and which matrix should be transposed
and which one should not be.

Suppose you want to calculate a plain old-school matrix product, where
there is nothing fancy about row lengths, the second row start right on
the spot where row length indicates it should. The two matrices are D
and E, the product is F=DE. None of the matrices exhibit any kind of
special structure, they are not symmetric or Hermitian, they are
definitely not square, and the elements are single-precision floats. You
would like to make the following function call:

    :::c
    cublasSgemm(cublasHandle_t handle,
                 cublasOperation_t transa, cublasOperation_t transb,
                 int m, int n, int k,
                 const float *alpha,
                 const float *A, int lda,
                 const float *B, int ldb,
                 const float *beta,
                 float *C, int ldc)

Some parameters are easier than others. The handle is just the usual
CuBlas handle which is better initialized somewhere before the call.
Parameter alpha will be one, and beta zero. The rest of the parameters
are trickier.

This is how the matrix D look like in memory with C-style indexing:

<center>![The memory layout of a matrix in C-style indexing]({filename}/images/c-matrix.png)</center>

This is how CuBlas sees them:

<center>![A matrix in C in Fortran-style memory layout]({filename}/images/c-matrix-fortran-view.png)</center>

The important thing to notice that they do not need to be transposed to
get the correct result, flipping their order will be sufficient. So DE
C-style will be ED Fortran-style. With this, we can establish five more
parameters: ``transa`` will be ``CUBLAS_OP_N`` (=not transposed), ``transb`` will
be ``CUBLAS_OP_N``, A will be E, B will be D, and the result C will be F.

The parameter ``m`` is the number of rows of matrices A and C. This will not correspond to
our row numbers because we flipped the order of multiplication. So this
value will be in fact the number of columns of E (denoted by ``colE``). The parameter ``n`` is
the number of columns of matrices B and C, which in our case will
correspond to ``rowD``. The parameter ``k`` is the number of columns of A and rows of B, in
our case, it will be colD.

Perhaps the hardest to figure out is the leading dimensions of the
matrices, ``lda``, ``ldb``, and ``ldc.`` In Fortran, this would be the distance in
memory between two consecutive *columns* of the respective matrices.
Since we have C-style arrays, this will be the distance between two
consecutive rows, which is, of course, the number of columns. So the
``lda``, ``ldb``, and ``ldc`` will become ``colE``, ``colD``, and ``colE``, respectively.

We would be fools not to make use of the excellent Thrust library in the
rest of our code, so let us further assume that the matrices are stored
as Thrust vectors, so they need to be cast in raw-pointer forms for the
CuBlas call. Putting it all together, the call will be:

    :::c++
    float alpha = 1.0f; float beta = 0.0f;
    status = cublasSgemm(handle, CUBLAS_OP_N, CUBLAS_OP_N,
                          colE, rowD, colD,
                          &alpha, thrust::raw_pointer_cast(&E[0]), colE,
                                  thrust::raw_pointer_cast(&D[0]), colD,
                          &beta,  thrust::raw_pointer_cast(&F[0]), colE);


[This](https://gist.github.com/peterwittek/6303527 "Matrix product") bit
of code shows a working example. It should compile with  ``nvcc -o
matrix_product_c_view matrix_product_c_view.cu -lcublas``.

