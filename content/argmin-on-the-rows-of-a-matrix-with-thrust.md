Title: Argmin on the rows of a matrix with Thrust
Date: 2013-04-07 09:36
Author: Peter
Category: C++, GPU
Slug: argmin-on-the-rows-of-a-matrix-with-thrust

[Thrust](https://github.com/thrust/thrust/ "Thrust") is fairly efficient
in saving you from hand-crafting optimized CUDA kernels, but it is
limited to vectors and a couple of basic operations. Working on matrices
is much harder. Suppose you are interested in getting the argmin for
each row in a matrix.

The core idea is to use reduce\_by\_key with a custom argmin function
for the reduction, and making sure that the 2D layout of the matrix is
respected. Dealing with the layout is probably the easiest. We need to
map the linear array index to a row index with a custom unary function:

<div class="highlight">

    template <typename T>
    struct linear_index_to_row_index : public thrust::unary_function<T,T>
    {
      T C; // number of columns
      
      __host__ __device__
      linear_index_to_row_index(T C) : C(C) {}

      __host__ __device__
      T operator()(T i)
      {
        return i / C;
      }
    };

</div>

A transform iterator will serve as the input iterator for
reduce\_by\_key:

<div class="highlight">

    thrust::make_transform_iterator(
      thrust::counting_iterator<int>(0),
      linear_index_to_row_index<int>(nColumns))

</div>

Things get murkier with the reduction operation. To deal with the argmin
with a simple binary function call without any reference to data
external to the function, we define a new type that store the argmin as
well as the minimum value:

<div class="highlight">

    typedef thrust::tuple<int,float> argMinType;

</div>

With this structure, we extend the binary function class to define an
argmin function:

<div class="highlight">

    struct argMin : public thrust::binary_function
                                    <argMinType,argMinType,argMinType>
    { 
      __host__ __device__
      argMinType operator()(const argMinType& a, const argMinType& b) const
      {
        if (thrust::get<1>(a) < thrust::get<1>(b)){
          return a;
        } else {
          return b;
        }
      }
    };

</div>

The input to this binary function will be a tuple where the first
element is the linear index of the matrix array, and the second element
is the corresponding entry in the matrix. The tuple needs to be zipped.
This is just a way of using a structure of arrays rather than an array
of structures.

<div class="highlight">

    thrust::make_zip_iterator(
      thrust::make_tuple(thrust::counting_iterator<int>(0),A.begin()))

</div>

Given the above preparations, we need to put it together in a function
call:

<div class="highlight">

    // allocate storage for row argmins and indices
    thrust::device_vector<argMinType> row_argmins(nRows);
    thrust::device_vector<int> row_indices(nRows);          
     
    // compute row argmins by finding argmin values with equal row indices
    thrust::reduce_by_key
      (thrust::make_transform_iterator(
         thrust::counting_iterator<int>(0),
         linear_index_to_row_index<int>(nColumns)),
       thrust::make_transform_iterator(
         thrust::counting_iterator<int>(0),
         linear_index_to_row_index<int>(nColumns)) + (nRows*nColumns),
       thrust::make_zip_iterator(
         thrust::make_tuple(thrust::counting_iterator<int>(0),A.begin())),
       row_indices.begin(),
       row_argmins.begin(),
       thrust::equal_to<int>(),
       argMin());

</div>

The above call is beginning to compete in complexity with an optimized
CUDA kernel. A full example is provided
[here](https://gist.github.com/peterwittek/6303575 "Source"), which
should easily compile with nvcc.

