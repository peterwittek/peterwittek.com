Title: Using Cython with Pypy and Numpy
Date: 2014-11-13 14:57
Author: Peter
Category: C++, Python
Slug: cython-with-pypy-and-numpy

Pypy is making tremendous progress with its fork of Numpy.
Unfortunately, Scipy is currently not supported. I wanted to use a
particular bit of Scipy from Pypy, and I noticed that there was some
Cython wizardry involved. So I had to piece together how these things
would work together.

I used Pypy 2.4.0 and the latest git of the Numpy
[fork](https://bitbucket.org/pypy/numpy), which I installed manually:

<div class="highlight">

    git clone https://bitbucket.org/pypy/numpy.git
    cd numpy; pypy setup.py install --user

</div>

I used the Pypy version of Cython, which I installed from
[AUR](https://aur.archlinux.org/packages/pypy-cython/). It was version
0.21.1.

I adapted
[this](http://docs.cython.org/src/userguide/numpy_tutorial.html) example
to test whether it works. We need to rely on Pypy's cpyext module to
load the C extension, which has been around for four years, but
documentation is extremely sparse.

The Cython file, named convolve.pyx, is an unmodified version from the
Cython tutorial:

<div class="highlight">

    from __future__ import division
    import numpy as np
    def naive_convolve(f, g):
        # f is an image and is indexed by (v, w)
        # g is a filter kernel and is indexed by (s, t),
        #   it needs odd dimensions
        # h is the output image and is indexed by (x, y),
        #   it is not cropped
        if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
            raise ValueError("Only odd dimensions on filter supported")
        # smid and tmid are number of pixels between the center pixel
        # and the edge, ie for a 5x5 filter they will be 2.
        #
        # The output size is calculated by adding smid, tmid to each
        # side of the dimensions of the input image.
        vmax = f.shape[0]
        wmax = f.shape[1]
        smax = g.shape[0]
        tmax = g.shape[1]
        smid = smax // 2
        tmid = tmax // 2
        xmax = vmax + 2*smid
        ymax = wmax + 2*tmid
        # Allocate result image.
        h = np.zeros([xmax, ymax], dtype=f.dtype)
        # Do convolution
        for x in range(xmax):
            for y in range(ymax):
                # Calculate pixel value for h at (x,y). Sum one component
                # for each pixel (s, t) of the filter g.
                s_from = max(smid - x, -smid)
                s_to = min((xmax - x) - smid, smid + 1)
                t_from = max(tmid - y, -tmid)
                t_to = min((ymax - y) - tmid, tmid + 1)
                value = 0
                for s in range(s_from, s_to):
                    for t in range(t_from, t_to):
                        v = x - smid + s
                        w = y - tmid + t
                        value += g[smid - s, tmid - t] * f[v, w]
                h[x, y] = value
        return h

</div>

I generated the C file and compiled it with GCC:

<div class="highlight">

    cython-pypy convolve.pyx
    gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing   
       -I/opt/pypy/include -I$HOME/.local/lib/pypy2.7/include   
       -o convolve.so convolve.c

</div>

If you run into weird missing Numpy header files during compilation,
check whether the include directory under Pypy contains a numpy with
just three files or many. If there are only three, you did not install
numpy as above. For instance, the AUR variant pypy-numpy-git does this,
which is why I install the library manually to my home folder.

The following test works:

<div class="highlight">

    import numpy as np
    import cpyext
    cpyext.load_module("convolve.so","convolve")
    import convolve

    print convolve.naive_convolve(np.array([[1, 1, 1]], dtype=np.int),
         np.array([[1],[2],[1]], dtype=np.int))

</div>
