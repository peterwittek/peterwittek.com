Title: Training emergent self-organizing maps on sparse data with Somoclu
Date: 2013-12-20 04:54
Author: Peter
Category: C++
Tags: Machine learning, C++
Slug: training-emergent-self-organizing-maps-with-somoclu
Summary: Self-organizing maps are computationally expensive to train -- emergent maps are even more so. This post looks at the constraints with sparse data.

Self-organizing maps are a topology-preserving embedding of
high-dimensional data to two-dimensional surfaces such as a plane or a
torus. Artificial neurons are arranged in a grid -- each neuron is
assigned a weight vector with identical number of dimensions as the data
to be embedded. An iterative procedure adjusts the weight vectors in
each step: first a neuron closest to a data point is sought, then its
weight vector and its neighbours' weight vectors are pulled closer to
the data point's. After a few iterations, the topology of the data set
arises in the grid in an unsupervised fashion.

If the number of nodes *k* in the grid is much smaller than the number
of data points *n*, SOM reduces to a clustering algorithm. Multiple data
points will share a best matching neuron in the grid.

Emergent self-organizing maps (ESOMs) are a variant in which *k*\>*n*.
In this arrangement, a data point will not only have a unique best
matching neuron, but the neuron's neighbourhood will also 'belong' to
the data point. Clustering structure will still show: some areas of the
map will be denser than others.

The extra information comes from the neighbourhoods of best matching
neurons. These interim neurons provide a smooth chain of transitions
between neurons that are assigned a data point. It is almost as if they
interpolate the space between data points. If a data point sits in
isolation far from other ones, it shows in the map, as its neighbourhood
will be sparse. These gaps gain meaning depending on the nature of the
data.

Computational requirements
==========================

Self-organizing maps are notoriously slow to train, and ESOMs are even
more so. [Somoclu](http://peterwittek.github.io/somoclu/) is a
high-performance implementation that accelerates computations on
multicore CPUs, GPUs, and even on multiple nodes ([Wittek, 2013](#wittek2013somoclu)).

Apart from training time, additional problems surface with ESOMs. The
codebook of the map -- the data structure that holds the weight vector
for each neuron in the grid -- grows quadratically in the number of
dimensions. We can distribute the data to a large number of nodes to
save memory, but distributing the codebook is not possible: each node
must have a copy of the full codebook. This puts constraints on how big
the codebook can be. For the same reason, calculations with very
high-dimensional data cannot be accelerated by GPUs, and the GPU memory
is much more limited in size than the main memory.

Memory problems persists with sparse data: while sparse structure will
drastically reduce memory requirements for holding the data, the
codebook will always be a dense structure.

Training the map
================

We constructed a term-document vector space from the Reuters-21578
collection. We filtered the terms space to remove words that occurred
less than three times or more often than the 90% most frequent words.
The resulting sparse documents space had 12,347 features.

Given the fuzzy nature of a neural network, Somoclu saves memory by
storing matrix entries in 4-byte floats. Even with the savings, a map
with 500x300 nodes takes nearly 13 GBytes of RAM. We trained the map
with the following settings:

    :::bash
    $ somoclu -k 2 -x 500 -y 300 -m 1 -s 2 data/reuters-nolabels.svm data/reuters

The parameter ``-k`` sets the sparse CPU kernel. The dimensions of the
neuron grid are passed in the parameters ``-x`` and ``-y``. We calculated a
toroid map with with the ``-m 1`` parameter. Finally, we saved all interim
data structures with ``-s 2``.

We observed a curious phenomenon in the training process. The first six
epoch took the same time each, nearly five hours (see the figure below).
Then a sharp rise occurred, epoch seven took over twenty-five hours. The
last two epoch took over two days each.

[caption id="attachment\_704" align="alignnone" width="486"]![Execution
time of
epochs](http://peterwittek.com/wp-content/uploads/2013/12/somoclu-timing.png)
Execution time of epochs.[/caption]

We thought it was a bug, but careful debugging showed that sparse
kernels will always slow down with large maps. The explanation lies in
the nature of floating point operations. Initially, the weight vectors
have random values, then they are pulled closer and closer to the sparse
data vectors. The vast majority of the weight vector entries will have
values very close to zero. We suspect that these fine-precision floating
operations cause the slow down.

Results
=======

The first three iterations resulted in maps so meaningless they were
discarded. Structures began to emerge from epoch six. The figure below
plots the U-matrix after epoch seven. Neighbourhoods are taking shape,
but the central part, where most of the cluster are, is still blur. Bear
in mind that this is a toroid map.

[caption id="attachment\_705" align="alignnone" width="500"]![Plot of
U-matrix after seven training
epochs.](http://peterwittek.com/wp-content/uploads/2013/12/plot-reuters.7.umx_.png)
Plot of U-matrix after seven training epochs[/caption]

The video below shows the U-matrices from epochs four to nine. The final
map -- looking like a honey comb -- clearly identifies hot clusters, and
more sparsely populated topical areas.

[video width="500" height="300"
mp4="http://peterwittek.com/wp-content/uploads/2013/12/time\_lapse.mp4"
ogv="movie.ogv"
webm="http://peterwittek.com/wp-content/uploads/2013/12/time\_lapse.webm"][/video]

Acknowledgemet
==============

This work was by supported by the European Commission Seventh Framework
Programme under Grant Agreement Number FP7-601138 PERICLES and by the
AWS in Education Machine Learning Grant award.

References
==========

<a name="wittek2013somoclu"></a> Wittek, P. [Somoclu: An Efficient Distributed Library for Self-Organizing Maps](http://arxiv.org/abs/1305.1422). *arXiv:1305.1422*, 2013.

