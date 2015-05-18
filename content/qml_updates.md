Title: Machine learning and quantum physics in the first third of 2015
Date: 2015-05-16 21:05
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Machine learning, Quantum information theory
Slug: qml-updates-may-2015
Summary: Looking at the crop of quantum machine learning manuscripts on arXiv from the beginning of 2015 until the middle of May.

The first four months of the year saw some interesting papers showing up
on arXiv. They cluster around well-defined topics: issues related to
quantum annealing naturally continue to be a hot topic, then there were
a few papers on applying learning in quantum physics problems, the
obsession with neural networks is eternal, and a couple of manuscripts
study implementation issues in Grover's search and quantum RAM.

Beyond arXiv, Scott Aaronson wrote an insightful
[essay](http://www.scottaaronson.com/papers/qml.pdf) on framing the
expectations about exponential speedup in quantum machine learning. He
talks about learning algorithms that rely on solving a linear
equation -- for instance, quantum least-squares support vector machines
belong to this category. The essay focuses on computational complexity:
claimed speedups may or may not be there. This is one more reason why we
should also analyse quantum machine learning algorithms from other
aspects of machine learning: generalization performance, for instance,
seldom gets any attention.

Annealing
---------

Finally research is coming out on the theoretical learning aspects of
quantum annealing. We saw some numerical results on adiabatic
classification with low-precision weights many years ago (Neven et al.
2008), and, counterintuitively, lower bit depth lead to higher
generalization performance. Apparently, the precision of representation
is part of model complexity. A new manuscripts studies this, leading to
16-bit floats in a deep learning scenario (Gupta et al. 2015).

Following this theme, a manuscript is dedicated to a form of
regularization in a method called totally corrective boosting (Denchev
et al. 2015). It leads to sparser models that also play nicer with
annealing hardware.

A paper points out that quantum tunneling may not play a role in
annealing -- the evolution may be diabatic (Muthukrishnan, Albash, and
Lidar 2015). This is the case with certain objective functions with long
plateaus.

The gap between the ground state and the first excited state decides the
time necessary for an adiabatic evolution. It can pay off to violate
this time, repeat the evolution several times, and sample the output.
This time to solution might prove to be a better benchmark for adiabatic
optimization. It turns out that there is a heavy tail for time to
solution even for the same type of optimization problems (Steiger,
Rønnow, and Troyer 2015). Introducing intermediate Hamiltonians can help
achieving better gaps (Zeng, Zhang, and Sarovar 2015). It seems,
however, that these Hamiltonians have to be carefully crafted, as
randomly constructed ones improve the gap only by a small margin.

A couple of new manuscripts deal specifically with the D-Wave annealing
hardware. Not surprisingly, noise leads to suboptimal solutions. If we
are able to determine the persistent biases in quantum annealers, we are
able to recalibrate them, leading to better optimization performance
(Perdomo-Ortiz et al. 2015). A similar problem manifests in large
optimization problems: they are annealed at higher temperatures due
analogue control errors, which can be addressed, yielding better scaling
(King 2015).

Machine learning in quantum physics problems
--------------------------------------------

A new eprint derives limits on the learnability of quantum measurements
and quantum state (Cheng, Hsieh, and Yeh 2015). There is plenty of
emphasis on sample and model complexity, and they are able to show that
a classical neural network is able to perform this dual learning task.
The paper is especially lucid, giving a good overview of the various
approaches to the interaction of machine learning and quantum physics.
It is also exceptionally well referenced.

Calibration is core to quantum computers at any scale, and naturally the
same stands for quantum simulators. Wiebe, Granade, and Cory (2015)
proposes learning a Hamiltonian model for a larger quantum system using
a small quantum simulator using Bayesian updates, then iteratively
building up larger and larger systems.

Reinforcement learning was suggested before for various tasks, e.g., for
adaptive phase estimation (Hentschel and Sanders 2010) and for
correcting measurement-based quantum computing in the presence of a
stray magnetic field (Tiersch, Ganahl, and Briegel 2014). The latter was
based on an agent-like learning algorithm (H. J. Briegel and De las
Cuevas 2012), which was extended to anchor it better to the concept of
generalization performance (Melnikov et al. 2015).

A curious twist at using machine learning in quantum physics is to
perform the learning remotely. Bang, Lee, and Jeong (2015) introduces a
protocol for secure machine learning at a distant place.

Neural networks
---------------

There is quite a bit of interest in implementing neural networks. There
is a proposal for a classical optical system for recurrent neural
networks (Hermans et al. 2015), a nano-optical perceptron (Tezak and
Mabuchi 2015), and a quantum neural network using quantum dots (Altaisky
et al. 2015).

A more far-fetched line of research relates Penrose's theory of quantum
consciousness to qudit-based quantum Hopfield networks (Srivastava,
Sahni, and Satsangi 2015).

Implementation
--------------

In the presence of decoherence, quantum metrology cannot get much beyond
the standard quantum limit. A new paper links this bound on the
precision to the erosion of speed-up in quantum
search(Demkowicz-Dobrzanski and Markiewicz 2014). Quantum search must
stop after a certain number of iterations, otherwise the probability of
getting the correct state will not be maximal. The number of iterations
depend on the fraction of the target states, which has to be known in
advance. Fixed-point search requires only a lower bound on this
fraction, but it sacrifices the quadratic speedup. A new paper suggest a
fixed-point search based on Grover's search that still keeps the
quadratic speedup(Yoder, Low, and Chuang 2014).

The issues surrounding the implementation of any kind of quantum memory
are countless. Following Giovannetti, Lloyd, and Maccone (2008)'s
proposal for a bucket-brigade quantum RAM, Arunachalam et al. (2015)
analyzes the robustness of this approach, and argues that the need for
error correction does not make it attractive.

The D-Wave hardware performs a search for the ground state of an Ising
model -- optimization problems had to be translated to this form.
Following a similar translation but entirely different hardware,
Haribara et al. (2015) proposes a coherent Ising machine based on a
degenerate optical parametric oscillator. It achieves a constant time
scaling, albeit results cannot beat simulated annealing.

References
----------

Altaisky, M. V., N. N. Zolnikova, N. E. Kaputkina, V. A. Krylov, Yu. E.
Lozovik, and N. S. Dattani. 2015. “Towards a Feasible Implementation of
Quantum Neural Networks Using Quantum Dots.” *[arXiv:1503.05125](http://arxiv.org/abs/1503.05125)*, Mar.

Arunachalam, Srinivasan, Vlad Gheorghiu, Tomas Jochym-O’Connor, Michele
Mosca, and Priyaa Varshinee Srinivasan. 2015. “On the Robustness of
Bucket Brigade Quantum RAM.” *[arXiv:1502.03450](http://arxiv.org/abs/1502.03450)*, Feb.

Bang, Jeongho, Seung-Woo Lee, and Hyunseok Jeong. 2015. “Protocol for
Secure Quantum Machine Learning at a Distant Place.” *[arXiv:1504.04929](http://arxiv.org/abs/1504.04929)*,
Apr.

Briegel, Hans J., and Gemma De las Cuevas. 2012. “Projective Simulation
for Artificial Intelligence.” *Scientific Reports* 2 (400): 1–16.
doi:[10.1038/srep00400](http://dx.doi.org/10.1038/srep00400).

Cheng, Hao-Chung, Min-Hsiu Hsieh, and Ping-Cheng Yeh. 2015. “The
Learnability of Unknown Quantum Measurements.” *[arXiv:1501.00559](http://arxiv.org/abs/1501.00559)*, Jan.

Demkowicz-Dobrzanski, Rafal, and Marcin Markiewicz. 2014. “From Quantum
Metrological Precision Bounds to Quantum Computation Speed-up Limits.”
*[arXiv:1412.6111](http://arxiv.org/abs/1412.6111)*, December.

Denchev, Vasil S., Nan Ding, Shin Matsushima, S. V. N. Vishwanathan, and
Hartmut Neven. 2015. “Totally Corrective Boosting with Cardinality
Penalization.” *[arXiv:1504.01446](http://arxiv.org/abs/1504.01446)*, Apr.

Giovannetti, Vittorio, Seth Lloyd, and Lorenzo Maccone. 2008. “Quantum
Random Access Memory.” *Physical Review Letters* 100 (16). APS: 160501.
doi:[10.1103/PhysRevLett.100.160501](http://dx.doi.org/10.1103/PhysRevLett.100.160501).

Gupta, Suyog, Ankur Agrawal, Kailash Gopalakrishnan, and Pritish
Narayanan. 2015. “Deep Learning with Limited Numerical Precision.”
*[arXiv:1502.02551](http://arxiv.org/abs/1502.02551)*, Feb.

Haribara, Yoshitaka, Yoshihisa Yamamoto, Ken-ichi Kawarabayashi, and
Shoko Utsunomiya. 2015. “A Coherent Ising Machine with Quantum
Measurement and Feedback Control.” *[arXiv:1501.07030](http://arxiv.org/abs/1501.07030)*, Jan.

Hentschel, Alexander, and Barry C. Sanders. 2010. “Machine Learning for
Precise Quantum Measurement.” *Physical Review Letters* 104 (6).
American Physical Society: 063603.
doi:[10.1103/PhysRevLett.104.063603](http://dx.doi.org/10.1103/PhysRevLett.104.063603).

Hermans, Michiel, Miguel Soriano, Joni Dambre, Peter Bienstman, and Ingo
Fischer. 2015. “Photonic Delay Systems as Machine Learning
Implementations.” *[arXiv:1501.02592](http://arxiv.org/abs/1501.02592)*, Jan.

King, Andrew D. 2015. “Performance of a Quantum Annealer on
Range-Limited Constraint Satisfaction Problems.” *[arXiv:1502.02098](http://arxiv.org/abs/1502.02098)*,
Feb.

Melnikov, Alexey A., Adi Makmal, Vedran Dunjko, and Hans J. Briegel.
2015. “Projective Simulation with Generalization.” *[arXiv:1504.02247](http://arxiv.org/abs/1504.02247)*,
Apr.

Muthukrishnan, Siddharth, Tameem Albash, and Daniel A. Lidar. 2015.
“When Diabatic Trumps Adiabatic in Quantum Optimization.”
*[arXiv:1505.01249](http://arxiv.org/abs/1505.01249)*, May.

Neven, Hartmut, Vasil S. Denchev, Geordie Rose, and William G. Macready.
2008. “Training a Binary Classifier with the Quantum Adiabatic
Algorithm.” *[arXiv:0811.0416](http://arxiv.org/abs/0811.0416)*.

Perdomo-Ortiz, Alejandro, Bryan O’Gorman, Joseph Fluegemann, Rupak
Biswas, and Vadim N. Smelyanskiy. 2015. “Determination and Correction of
Persistent Biases in Quantum Annealers.” *[arXiv:1503.05679](http://arxiv.org/abs/1503.05679)*, Mar.

Srivastava, Dayal Pyari, Vishal Sahni, and Prem Saran Satsangi. 2015.
“Modelling Microtubules in the Brain as N-Qudit Quantum Hopfield Network
and Beyond.” *[arXiv:1505.00774](http://arxiv.org/abs/1505.00774)*, May.

Steiger, Damian S., Troels F. Rønnow, and Matthias Troyer. 2015. “Heavy
Tails in the Distribution of Time-to-Solution for Classical and Quantum
Annealing.” *[arXiv:1504.07991](http://arxiv.org/abs/1504.07991)*, Apr.

Tezak, Nikolas, and Hideo Mabuchi. 2015. “A Coherent Perceptron for
All-Optical Learning.” *[arXiv:1501.01608](http://arxiv.org/abs/1501.01608)*, Jan.

Tiersch, M., E. J. Ganahl, and H. J. Briegel. 2014. “Adaptive Quantum
Computation in Changing Environments Using Projective Simulation.”
*[arXiv:1407.1535](http://arxiv.org/abs/1407.1535)*, Jul.

Wiebe, Nathan, Christopher Granade, and D G Cory. 2015. “Quantum
Bootstrapping via Compressed Quantum Hamiltonian Learning.” *New Journal
of Physics* 17 (2). IOP Publishing: 022005.
doi:[10.1088/1367-2630/17/2/022005](http://dx.doi.org/10.1088/1367-2630/17/2/022005).

Yoder, Theodore J., Guang Hao Low, and Isaac L. Chuang. 2014.
“Fixed-Point Quantum Search with an Optimal Number of Queries.”
*Physical Review Letters* 113 (21). American Physical Society.
doi:[10.1103/physrevlett.113.210501](http://dx.doi.org/10.1103/physrevlett.113.210501).

Zeng, Lishan, Jun Zhang, and Mohan Sarovar. 2015. “Schedule Path
Optimization for Quantum Annealing and Adiabatic Quantum Computing.”
*[arXiv:1505.00209](http://arxiv.org/abs/1505.00209)*, May.
