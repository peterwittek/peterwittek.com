Title: Random number generation with C++11 and VSL
Date: 2014-12-05 17:12
Author: Peter
Category: C++
Tags: C++, GPU
Slug: random-number-generation-with-c11-and-vsl
Summary: Benchmarking the speed of random number generation in C++11 with GCC and with VSL and ICC.

I have to generate a large amount of Gaussian random numbers and I was
curious how good stock RNGs are, as opposed to rolling our own
Box-Muller transform over ``rand()``. Options were the new RNG in C++11 with
GCC, and Intel's VSL in MKL with ICC.

The C++11 version is simple. It uses a base RNG,
[probably](http://www.cplusplus.com/reference/random/default_random_engine/)
a linear congruential engine, to generate uniform random numbers. Then
it applies a transformation, which happens to be the Box-Muller
transform. The code is:

    :::c++
    #include <iostream>
    #include <ctime>
    #include <random>

    using namespace std;

    int main(int argc, char **argv) {
      
        const int nrolls=500000000;
      
        default_random_engine generator;
        normal_distribution<double> distribution(0.0,1.0);
        
        time_t start_time = time(NULL);
        
        double number = 0;
        for (int i=0; i<nrolls; ++i) {
          number = distribution(generator);
        }    
        
        cout << difftime(time(NULL),start_time) << " " << number << endl;

        return 0;
    }

The VSL version uses the same split between base RNG and transformation.
Apart from the Box-Muller transform, it is also able to use the inverse
cumulative distribution function (ICDF) method to generate a Gaussian
random number. A crucial difference is that it can vectorize the
generation, which yields a massive speedup in theory. The code is here,
switching around the numbers in nrolls and N flips between vectorized
and non-vectorized variants:

    :::c++
    #include <iostream>
    #include <ctime>
    #include "mkl_vsl.h"
    #define SEED 0
    #define BRNG VSL_BRNG_MCG31
    #define METHOD VSL_METHOD_DGAUSSIAN_ICDF

    using namespace std;

    main() {
        const int nrolls= 1;//500000000;
        const int N = 500000000;//500000000;
        double* r=new double[N];
        double a = 0, sigma = 1.0;
        VSLStreamStatePtr stream;
        int errcode;
        errcode = vslNewStream( &stream, BRNG, SEED );
        time_t start_time = time(NULL);
        for (int i=0; i<nrolls; ++i) {
          errcode = vdRngGaussian( METHOD, stream, N, r, a, sigma );
        }
        cout << difftime(time(NULL),start_time) << endl;
        errcode = vslDeleteStream( &stream );
        delete r;
    }

The table below summarizes the results with linear congruential engines
as the base RNG. I did not see much difference between the execution
time by changing the base RNG. The hardware was AMD, so it is possible
that the Intel compiler and VSL give poorer results. The results are in
seconds.

Method                       |Time
-----------------------------|-----
Own Box-Muller               |33
C++11                        |33
VSL, not vectorized, ICDF    |132
VSL, vectorized, ICDF        |4
VSL, vectorized, Box-Muller  |9

Without vectorization, VSL performs poorly. The kind of transformation
also makes a big difference. With vectorized generation and the ICDF
method, we are looking at a speedup around 8x.

I would also be curious to see how the results compare to cuRAND. Nvidia
claim a [75x](https://developer.nvidia.com/cuRAND) speedup over MKL with
Keppler hardware, which sounds exciting.

