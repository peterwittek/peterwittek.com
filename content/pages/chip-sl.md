Title: CHiP-SL
Date: 2013-01-07 09:04
Author: Peter
Slug: chip-sl
Status: hidden

![CHiP-SL](http://peterwittek.com/wp-content/uploads/2013/01/chip-sl.png)

<style type="text/css"><!--<br />
@page { size: 8.5in 11in; margin: 0.79in }<br />
        P { margin-bottom: 0.08in; direction: ltr; color: #000000; text-align: left; widows: 0; orphans: 0 }<br />
        P.western { font-family: "Times New Roman", serif; font-size: 12pt; so-language: en-US }<br />
        P.cjk { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: zh-CN }<br />
        P.ctl { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: hi-IN }<br />
        A.cjk:link { so-language: zxx }<br />
        A.ctl:link { so-language: zxx }<br />
--></style>
Cloud for High-Performance Statistical Learning {lang="en-US" align="CENTER"}
===============================================

<style type="text/css"><!--<br />
@page { size: 8.5in 11in; margin: 0.79in }<br />
        P { margin-bottom: 0.08in; direction: ltr; color: #000000; text-align: left; widows: 0; orphans: 0 }<br />
        P.western { font-family: "Times New Roman", serif; font-size: 12pt; so-language: en-US }<br />
        P.cjk { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: zh-CN }<br />
        P.ctl { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: hi-IN }<br />
        A.cjk:link { so-language: zxx }<br />
        A.ctl:link { so-language: zxx }<br />
--></style>
Big data asks for scalable algorithms, but scalability is just one
aspect of the problem. Many applications also require the [speedy
processing](http://www.datanami.com/datanami/2012-09-11/the_gpu_sweet_spot_for_big_data.html "The GPU "Sweet Spot" for Big Data")
of large volumes of data. Examples include supporting financial decision
making, advanced services in digital libraries, mining medical data from
magnetic resonance imaging, and also analyzing social media graphs. The
velocity of machine learning is often boosted by deploying graphics
processing units (GPUs) or distributed algorithms, but rarely both. We
are developing high-performance supervised and unsupervised statistical
learning algorithms that are accelerated on GPU clusters. The tools in
our current scope are dimensionality reduction by [random
projection](http://dx.doi.org/10.1016/j.jpdc.2012.10.001 "Accelerating text mining workloads in a MapReduce-based distributed GPU "),
low-dimensional embedding by [self-organizing
maps](http://bada.hb.se/bitstream/2320/10966/2/esann12gpusom.pdf "A GPU-Accelerated Algorithm for Self-Organizing Maps in a Distributed Environment"),
clustering by[nature-inspired
methods](http://bada.hb.se/bitstream/2320/11759/1/jcomp12dqc.pdf "High-Performance Dynamic Quantum Clustering on Graphics Processors"),
classification by [support vector
machines](http://mklab.iti.gr/files/wiamis11.pdf "GPU acceleration for support vector machines"),
and further methods are constantly being considered. While MapReduce is
commonly used in [distributed-memory machine
learning](http://mahout.apache.org/ "Mahout"), and there are MapReduce
frameworks that can easily be made
[GPU-aware](http://mapreduce.sandia.gov/ "MR-MPI"), and one that was
specifically [designed for distributed
GPUs](https://code.google.com/p/gpmr/ "GPMR"), we believe that higher
performance can be achieved in a less restrictive communication model.
This design decision should not affect the modularity of a data mining
workflow, as given an efficient distributed storage model, the learning
algorithms smoothly integrate with the rest of the processing steps,
irrespective of whether they use the MapReduce model.

<style type="text/css"><!--<br />
@page { size: 8.5in 11in; margin: 0.79in }<br />
        P { margin-bottom: 0.08in; direction: ltr; color: #000000; text-align: left; widows: 0; orphans: 0 }<br />
        P.western { font-family: "Times New Roman", serif; font-size: 12pt; so-language: en-US }<br />
        P.cjk { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: zh-CN }<br />
        P.ctl { font-family: "DejaVu Sans", "MS Mincho"; font-size: 12pt; so-language: hi-IN }<br />
        A.cjk:link { so-language: zxx }<br />
        A.ctl:link { so-language: zxx }<br />
--></style>
Since the cost of a GPU cluster is high and the deployment is far from
being trivial, Cloud for High-Performance Statistical Learning
(ChiP-SL)  enables the verification, rapid dissemination, and quick
adaptation of the algorithms being developed. Based on our past
experience, such a solution is particularly relevant in organizations
which do not normally require high computational power, such as [digital
libraries](http://bada.hb.se/bitstream/2320/9695/1/hpccloud11leveraging.pdf "Leveraging on High-Performance Computing and Cloud Technologies in Digital Libraries"),
or
[social](http://bada.hb.se/bitstream/2320/11757/1/cloudcom12hpc.pdf "Scalable Agent-based Modelling with Cloud HPC Resources for Social Simulations")
and [archaeological
simulations](http://bada.hb.se/bitstream/2320/11758/1/cloud4sim12simulation.pdf "Military Reconstructive Simulation in the Cloud to Aid Battlefield Excavations").
By benchmarking on [cloud GPU
instances](http://aws.amazon.com/hpc-applications/ "High Performance Computing on Amazon Web Services"),
we may provide a turn-key solution for the instant deployment of
high-performance machine learning algorithms by sharing the respective
images of the virtual servers. This saves the trouble of getting the
relevant libraries of the correct version number working, compiling the
code, and setting up paths, making these solution more accessible for
both academic and commercial users.

This work is supported by [AWS in
Education](http://aws.amazon.com/education/ "AWS in Education") Machine
Learning Grant award.

