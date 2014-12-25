Title: About Me
Date: 2013-01-04 11:46
Author: Peter
Slug: home
Order: 3

![profile\_photo](http://peterwittek.com/wp-content/uploads/2013/01/profile_photo.jpg)I
am a research scientist working on quantum machine learning,
computational methods in quantum simulations, and scalable learning
algorithms on supercomputers. Trained as a mathematician and computer
scientist, I received my PhD from the National University of Singapore.
I have been involved in major EU research projects, and obtained several
national and industry grants. Currently I work as a research fellow in
the Quantum Information Theory group in ICFO-The Institute of Photonic
Sciences. Previously I worked for the University of Borås, and I am
still an external employee of the university.

Being location-independent, I lived in nearly two dozen countries, and
did research stints at several institutions, including the Indian
Institute of Science, Barcelona Supercomputing Center, Bangor
University, Tsinghua University,  the Centre for Quantum Technologies in
the National University of Singapore, and the Institute of Photonic
Sciences.

Research Interests
==================

**Quantum Machine Learning**: The intersection of quantum computing and
machine learning is an emergent research topic with exciting new
possibilities for learning theory. Apart from reduced time complexity of
quantum learning algorithms, generalization performance may also improve
compared to classical optimization methods.

**Computational methods in quantum physics**: The inherent complexity of
quantum mechanics implies simulations with a limited scope even on a
supercomputer. Novel algorithms may allow researchers to model far more
intricate systems in the near future. Topics include obtaining upper and
lower bounds on the ground state and calculating the evolution of
quantum systems.

**Machine learning with high-performance computers**: The range of
machine learning algorithms is diverse, but effective ones come with
high computational requirements. To scale them to real-world
applications, a high degree of parallelism is an inevitable requirement.
Machine learning on HPC resources investigates algorithms that scale in
an embarrassingly parallel environment, such as a distributed GPU
cluster.

Current Projects
================

**[![ncpol2sdpa](http://peterwittek.com/wp-content/uploads/2013/01/ncpol2sdpa.png)](http://peterwittek.com/approximating-the-ground-state-with-sdp "Approximating the Ground State of a Many-Particle Quantum System with Semi-Definite Relaxations")Approximating
the Ground State of a Many-Particle Quantum System with Semi-Definite
Relaxations** (2013-2014): Identifying the ground state of a
many-particle system whose interactions are described by a Hamiltonian
is an important problem in quantum physics. During the last decade,
different relaxations of the previous Hamiltonian minimization problem
have been proposed. Interestingly, they provide lower bound the
ground-state energy, complementing the upper bounds that are obtainable
using variational methods. These algorithms can be understood as lower
levels of a general hierarchy of semi-definite programming (SDP)
relaxations for non-commutative polynomial optimization. The main goal
is to identify physically relevant situations in which SDP relaxations
beat any of the existing numerical methods to establish lower bounds to
the ground-state energy and, in particular, exact diagonalization of the
Hamiltonian. Sponsored by European Commission Seventh Framework
Programme under Grant Agreement Number FP7-601138
[PERICLES](http://pericles-project.eu/ "PERICLES"), by the [Red Española
de Supercomputación](http://www.bsc.es/RES "RES") and by the [Swedish
National Infrastructure for Computing](http://www.snic.se/ "SNIC").

[![Pericles
logo](http://peterwittek.com/wp-content/uploads/2013/01/pericles1.png)](http://www.pericles-project.eu/)**Pericles**
(2013-2017): Promoting and Enhancing Reuse of Information throughout the
Content Lifecycle taking account of Evolving Semantics (Pericles) is an
integrated project in which academic and industrial partners have come
together to investigate the challenge of preserving complex digital
information in dynamically evolving environments, to ensure that it
remains accessible and useful for future generations. We address
contextuality and scalability within the project. Contextuality refers
to probabilistic framework that considers the broader and narrower
context of the data within a quantum-like formulation, whereas
scalability allows executing algorithms on massive data sets using
heterogeneous accelerator architectures. Funded by [European Commission
Seventh Framework
Programme](http://cordis.europa.eu/fp7/ict/telearn-digicult/home_en.html "FP7").

Completed Projects
==================

[![CHiP-SL](http://peterwittek.com/wp-content/uploads/2013/01/chip-sl.png "Cloud for High-Performance Statistical Learning")](http://peterwittek.com/research/chip-sl/)

**ChiP-SL** (2013-2014): Big data asks for scalable algorithms, but
scalability is just one aspect of the problem. Many applications also
require the speedy processing of large volumes of data. Examples include
supporting financial decision making, advanced services in digital
libraries, mining medical data from magnetic resonance imaging, and also
analyzing social media graphs. The velocity of machine learning is often
boosted by deploying GPUs or distributed algorithms, but rarely both. We
are developing high-performance supervised and unsupervised statistical
learning algorithms that are accelerated on GPU clusters. Since the cost
of a GPU cluster is high and the deployment is far from being trivial,
the project Cloud for High-Performance Statistical Learning (ChiP-SL)
enables the verification, rapid dissemination, and quick adaptation of
the algorithms being developed. Funded by [Amazon Web
Services](http://aws.amazon.com/ "Amazon Web Services").

[![tsa](http://peterwittek.com/wp-content/uploads/2013/01/tsa.png)](http://peterwittek.github.io/trotter-suzuki-mpi/ "Implementation of Trotter-Suzuki Approximation")**TSA**
(2012): The Trotter-Suzuki approximation leads to an efficient algorithm
for solving the time-dependent Schrödinger equation. Using existing
highly optimized CPU and GPU kernels, we developed a distributed version
of the algorithm that runs efficiently on a cluster. Our implementation
also improves single node performance, and is able to use multiple GPUs
within a node. The scaling is close to linear using the CPU kernels,
whereas the efficiency of GPU kernels improve with larger matrices. We
also introduced a hybrid kernel that simultaneously uses multicore CPUs
and GPUs in a distributed system. This project was a research visit to
the [Barcelona Supercomputing
Centre](http://bsc.es/ "Barcelona Supercomputing Centre") funded by
[HPC-EUROPA2](http://www.hpc-europa.org/ "HPC-EUROPA2").

[![squalar](http://peterwittek.com/wp-content/uploads/2013/01/squalar.png)](http://peterwittek.com/squalar "SQUALAR")**SQUALAR**
(2011): High-performance computational resources and distributed systems
are crucial for the success of real-world language technology
applications. The novel paradigm of general-purpose computing on
graphics processors offers a feasible and economical alternative: it has
already become a common phenomenon in scientific computation, with many
algorithms adapted to the new paradigm. However, applications in
language technology do not readily adapt to this approach. Recent
advances show the applicability of quantum metaphors in language
representation, and many algorithms in quantum mechanics have already
been adapted to GPU computing. Scalable Quantum Approaches in Language
Representation (SQUALAR) aimed to match quantum-inspired algorithms with
heterogeneous computing to develop new formalisms of information
representation for natural language processing. Co-funded by [Amazon Web
Services](http://aws.amazon.com/ "Amazon Web Services").

[![logo-shaman](http://peterwittek.com/wp-content/uploads/2013/01/logo-shaman.png)](http://shaman-ip.eu/ "SHAMAN")
**SHAMAN** (2010-2011) was an integrated project on large-scale digital
preservation. As part of the preservation framework, advanced services
aid the discovery of archived digital objects. These services are based
on machine learning and data processing, which in turn asks for scalable
distributed computing models. Given the requirements for reliability,
the project took a middleware approach based on MapReduce to perform
computationally demanding tasks. Since memory organizations which are
involved in digital preservation potentially lack the necessary
infrastructure, a high-performance cloud computing component was also
developed. Funded by [Framework Programme
7](http://cordis.europa.eu/fp7/ict/telearn-digicult/home_en.html "FP7").

