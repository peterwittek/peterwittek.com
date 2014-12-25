Title: Summing the entries of a matrix using a stencil with Thrust
Date: 2013-04-22 02:06
Author: Peter
Category: C++
Tags: C++, GPU
Slug: summing-the-entries-of-a-matrix-using-a-stencil-with-thrust
Summary: Thrust-based summing of the elements of a submatrix at a given offset according to a stencil.

The task sounds simple: sum every element according to a stencil in a
two-dimensional layout. Ideally it should be done on the GPU, provided
the input is already sitting in the device memory. This operation
occurs, for instance, in [agent-based modelling](http://on-demand.gputechconf.com/gtc/2013/poster/pdf/P0197_PeterWittek.pdf "GTC Poster"),
when the agent collects information about its environment. The stencil
in that case is a circle with a radius that corresponds to the agents'
horizon:

![An agent's horizon as a stencil](http://peterwittek.com/wp-content/uploads/2013/04/agent_stencil.png)

The idea would be to avoid hand-tuning CUDA reduction kernels, and rely
on Thrust to save work. The sum we need is a kind of inner product of
the stencil and the submatrix tile at a given offset:

    :::c++
    thrust::inner_product(tile.begin(), tile.end(),
                           stencil.begin(), 0);

Yet, given Thrust's fundamentally one-dimensional focus, it proves to be
a complicated task to accomplish. The difficulty arises that we need to
extract a 2D sub-array from a 2D matrix. We need to define a new class
tile, with its own ``begin()`` and ``end()`` functions that can serve as input
for the above call. The constructor simply fills in the values for its
private variables that keep track of the tile size and the leading
dimension of the matrix:

    :::c++
    tiled_range(Iterator first, Iterator last,
                data_type tile_size_x, data_type tile_size_y,
                data_type leading_dimension)
        : first(first), last(last),
        tile_size_x(tile_size_x), tile_size_y(tile_size_y),
        leading_dimension(leading_dimension) {}

To get the iterator right for the ``tiled_range`` class, we will need a
counting, a transform, and a permutation iterator, with the latter being
the iterator type for our class. To keep things short, these are
typedef-ed.

    :::c++
    typedef typename thrust::counting_iterator<data_type>
                      CountingIterator;
    typedef typename thrust::transform_iterator<tile_functor, CountingIterator>
                      TransformIterator;
    typedef typename thrust::permutation_iterator<Iterator,TransformIterator>
                      PermutationIterator;

The permuation iterator takes two arguments:

-   An iterator to the range V on which the permutation will be applied
-   The reindexing scheme that defines how the elements of V will be
    permuted.

The first one will be the entire matrix, whereas the "permutation" will
be a new transform iterator that ensures only the tile elements are
returned. The transform iterator in turn takes two parameters:

-   An ``Iterator`` pointing to the input to this ``transform_iterator``'s
    ``AdaptableUnaryFunction``.
-   An ``AdaptableUnaryFunction`` used to transform the objects pointed to
    by ``x``.

The iterator will be a counting operator starting at zero. The unary
function maps the linear counter to the correct index of the matrix
based on the tile parameters and the leading dimension of the matrix.
The functor itself is fairly simple:

    :::c++
    struct tile_functor : public thrust::unary_function<data_type,data_type>
    {
        data_type tile_size_x;
        data_type leading_dimension;
     
        tile_functor(data_type tile_size_x, data_type leading_dimension)
            : tile_size_x(tile_size_x), leading_dimension(leading_dimension) {}
     
        __host__ __device__
        data_type operator()(const data_type& i) const
        {
            int x=i % tile_size_x;
            int y=i / tile_size_x;
            return leading_dimension*y + x;
        }
    };

With all components prepared, the ``begin()`` function becomes

    :::c++
    PermutationIterator begin(void) const
    {
      return PermutationIterator(first, TransformIterator(CountingIterator(0),
               tile_functor(tile_size_x, leading_dimension)));
    }

The ``end()`` function is again very simple:

    :::c++
    PermutationIterator end(void) const
    {
      return begin() + tile_size_y * tile_size_x;
    }

A complete example is given
[here](https://gist.github.com/peterwittek/6303588 "Source"), which
should just compile with nvcc. The main problem is that the permutation
iterator has dubious efficiency in accessing the GPU memory, and
accesses are probably not as coalesced as they should be. The usage
example mentioned in the first paragraph uses small stencil at random
locations, which is pretty hard on the GPU. Speedups around 8x are still
apparent on Fermi hardware compared to a single core, which is not
great, but it is a workable solution in a hybrid scenario where other
CPU cores can be kept busy with OpenMP or MPI.

