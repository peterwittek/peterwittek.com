Title: Home
Date: 2013-01-04 11:46
Author: Peter
Slug: home
Order: 0
Status: hidden
Summary: Peter Wittek, research scientist in quantum machine learning, computational methods in quantum physics, and machine learning with high-performance computers.
URL:
save_as: index.html

About
-----
<img style="float:left; border-right:10px solid white" src="images/profile_photo.jpg" alt="profile_photo"/>I am a research fellow working on quantum machine learning, computational methods in many-body quantum physics, and scalable learning algorithms on supercomputers. Trained as a mathematician and computer scientist, I received my PhD from the [National University of Singapore](http://www.comp.nus.edu.sg/). I have been involved in major EU research projects, and obtained several national and industry grants. Currently I work in the [Quantum Information Theory group](http://www.icfo.eu/research/group_details.php?id=19) in ICFO-The Institute of Photonic Sciences. I have been affiliated with the [University of Borås](http://www.hb.se/en/) since 2010. I
did longer research stints at several institutions, including the [Indian Institute of Science](http://csa.iisc.ernet.in/), [Barcelona Supercomputing Center](http://www.bsc.es/computer-applications), [Tsinghua University](http://www.riit.tsinghua.edu.cn/docinfo_out/board5/boardlist.jsp?columnId=002010307&parentColumnId=0020103), the [Centre for Quantum Technologies](http://quantumlah.org/) in the National University of Singapore, and the [Quantum Information Group](http://www.eve.phys.s.u-tokyo.ac.jp/indexe.htm) in the University of Tokyo. I am also active in entrepreneurship: I serve as a scientific advisor to the [Creative Destruction Lab](http://creativedestructionlab.com/) in the University of Toronto, I serve in the same role for various startups, and I am a member of the [NUS Overseas Colleges Alumni](http://www.overseas.nus.edu.sg/).

Research Interests
------------------

**Quantum machine learning**: The intersection of quantum computing and
machine learning is an emergent research topic with exciting new
possibilities for learning theory. Apart from reduced time complexity of
quantum learning algorithms, generalization performance may also improve
compared to classical optimization methods. Interests range from foundational questions through practical quantum-enhanced learning protocols to classical machine learning algorithms in quantum physics problems.

**Computational methods in many-body quantum physics**: The inherent complexity of
quantum mechanics implies simulations with a limited scope even on a
supercomputer. Novel algorithms may allow researchers to model far more
intricate systems in the near future. Topics include obtaining upper and
lower bounds on the ground state, many-party quantum correlations,
and calculating the evolution of quantum systems.

**Machine learning with high-performance computing resources**: The range of
machine learning algorithms is diverse, but effective ones come with
high computational requirements. To scale them to real-world
applications, a high degree of parallelism is an inevitable requirement.
Machine learning on HPC resources investigates algorithms that scale in
an embarrassingly parallel environment, such as a distributed GPU
cluster. Further attention is paid to sparse, unstructured data, which is especially hard to deal with.

Current Projects
----------------
[<img style="float:left; border-right:8px solid white" src="images/pericles1.png" alt="pericles"/>](http://www.pericles-project.eu/)
**[Pericles](http://www.pericles-project.eu/)**
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
heterogeneous accelerator architectures. Funded by [European Commission Seventh Framework Programme](http://cordis.europa.eu/fp7/ict/telearn-digicult/home_en.html "FP7") (FP7-601138).

[<img style="float:left; border-right:8px solid white" src="images/quantum_gas61.png" alt="t-s-a"/>](https://github.com/trotter-suzuki-mpi)
**[Trotter-Suzuki Approximation](https://github.com/trotter-suzuki-mpi)**
(2012, 2015-2016): The Trotter-Suzuki decomposition leads to an efficient algorithm
for solving the time-dependent Schrödinger equation and the
Gross-Pitaevskii equation. Using existing
highly optimized CPU and GPU kernels, we developed a distributed version
of the algorithm that runs efficiently on a cluster. Our implementation
also improves single node performance, and is able to use multiple GPUs
within a node. The scaling is close to linear using the CPU kernels,
whereas the efficiency of GPU kernels improve with larger matrices. We
also introduced a hybrid kernel that simultaneously uses multicore CPUs
and GPUs in a distributed system.  The distributed extension was carried out while visiting the the [Barcelona Supercomputing
Centre](http://bsc.es/ "Barcelona Supercomputing Centre") funded by
[HPC-EUROPA2](http://www.hpc-europa.org/ "HPC-EUROPA2"). Generalizing the capabilities of kernels was carried out by Luca Calderaro sponsored by the [Erasmus+](http://ec.europa.eu/programmes/erasmus-plus/index_en.htm) programme. Computational resources were granted by the [Spanish Supercomputing Network](https://www.bsc.es/marenostrum-support-services/res) (FI-2015-2-0023), the [High Performance Computing Center North](https://www.hpc2n.umu.se/) ([SNIC](http://www.snic.se/) 2015/1-162 and SNIC 2016/1-320), and a hardware grant by [Nvidia](https://www.nvidia.com/).


[<img style="float:left; border-right:8px solid white" src="images/moment_matrix.png" alt="Moment matrix"/>](https://ncpol2sdpa.readthedocs.org/)
[**Studying Many-Body Quantum Systems with Semidefinite Programming Relaxations**](https://ncpol2sdpa.readthedocs.org/): Identifying the ground state of a
many-particle system whose interactions are described by a Hamiltonian
is an important problem in quantum physics. During the last decade,
different relaxations of the previous Hamiltonian minimization problem
have been proposed. Interestingly, they provide lower bound the
ground-state energy, complementing the upper bounds that are obtainable
using variational methods. These algorithms can be understood as lower
levels of a general hierarchy of semidefinite programming (SDP)
relaxations for non-commutative polynomial optimization. The main goal
is to identify physically relevant situations in which SDP relaxations
beat any of the existing numerical methods to establish lower bounds to
the ground-state energy and, in particular, exact diagonalization of the
Hamiltonian. The same methodology of SDP relaxations also applies to certain problems in quantum correlations. The set of quantum correlations is convex, but the boundary is hard to characterize. The hierarchy of SDP relaxations approximates this boundary from the outside and the approximation is often very accurate. The applications of this method include establishing the maximum quantum violation of Bell inequalities and calculating the maximum amount of randomness that can be extracted from certain multipartite quantum systems. Sponsored by the ERC grant [QITBOX](http://cordis.europa.eu/project/rcn/111554_en.html), by the [Spanish Supercomputing Network](https://www.bsc.es/marenostrum-support-services/res) (FI-2013-1-0008 and FI-2013-3-0004) and by the [Swedish National Infrastructure for Computing](http://www.snic.se/) (SNIC 2014/2-7 and 2015/1-162).

Past Projects
-------------
[<img style="float:left; border-right:8px solid white" src="images/chip-sl.png" alt="chip-sl"/>]({filename}/pages/chip-sl.md)
**[ChiP-SL]({filename}/pages/chip-sl.md)** (2013-2014): Big data asks for scalable algorithms, but
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

[<img style="float:left; border-right:8px solid white" src="images/squalar.png" alt="squalar"/>](http://peterwittek.com/squalar)
**[SQUALAR](http://peterwittek.com/squalar)**
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

<img style="float:left; border-right:8px solid white" src="images/logo-shaman.png" alt="shaman"/>
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
