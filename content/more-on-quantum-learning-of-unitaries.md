Title: More on the quantum learning of unitaries, process tomography, and classical regression
Date: 2014-08-26 06:05
Author: Peter
Category: Quantum machine learning
Tags: Quantum machine learning, Machine learning, Quantum information theory
Slug: more-on-quantum-learning-of-unitaries
Summary: Classical regression, induction, transduction and the quantum learning of unitaries, plus making the difference explicit to process tomography.

[AQIS](http://cs.e.yamagata-u.ac.jp/aqis14/) just concluded, and I
presented a [poster](http://dx.doi.org/10.13140/2.1.3901.1201) on
transductive and active learning in the [quantum learning of unitaries](http://peterwittek.com/2013/11/quantum-process-tomography-and-machine-learning/)
([Wittek, 2014](#wittek2014transduction)). We had some good discussions
on the topic, particularly on the differences between process tomography
and learning of unitary transformations, and whether this whole idea of
comparing to classical regression analysis makes any sense. This entry
summarizes some of the points made.

<iframe style="border: 1px solid #CCC; border-width: 1px; margin-bottom: 5px; max-width: 100%;" src="//www.slideshare.net/slideshow/embed_code/38081381" width="600" height="640" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen="allowfullscreen">
</iframe>

One of the referees of the extended abstract wrote:

*[I]t is essential to avoid the confusion between "learning" and
"tomography". In tomography, one tries to infer a classical description
of the unknown gate. In learning, the goal is to simulate the
application of the gate on a new input state, without necessarily having
a classical description. In general, gate tomography (or, more
precisely, gate estimation) is a suboptimal strategy for learning. The
fact that, in the presence of symmetry, estimation is sufficient to
achieve the optimal performance of gate learning is a highly non-trivial
result.*

This is a crucial distinction that I was not aware of. So in the case of
process tomography, we have an explicit, classical description of the
estimated transformation $\hat{U}$ that we can use on an
arbitrary number of states in the future. In classical learning, this is
a pure case of induction: based on some finite $N$ training
instances, we infer a function, which we deploy on other data instances
not present in the training set.

The poster did not concern this case, it only discussed the suboptimal
coherent and optimal incoherent strategies, and how they related to
transduction and induction. The interesting thing about the incoherent
strategy is that we perform an optimal POVM measurement, so we actually
learn classical information about the unitary, but not as much as in the
case of process tomography.

In classical regression, we have $N$ training instances, each with
a real-valued label: $\{(\mathbf{x}_1, y_1),\ldots,
(\mathbf{x}_N, y_N)\}$. In the quantum learning scenario, we have
$N$ disposal of a black box. If we want to match this in the
classical case, we would need the original function $f$ that
generates the training instances: $\{(\mathbf{x}_1,
f(\mathbf{x}_1)),\ldots, (\mathbf{x}_N, f(\mathbf{x}_N))\}$. It
would not make much difference to classical learning algorithms. In the
quantum case, there is an optimal input state that reveals the most
about the unitary in question (provided some symmetry, as pointed out by
the referee). Furthermore, this optimal input state should be used in
parallel, that is, applying the $N$-times tensor product of the
unitary on the state ([Bisio et al., 2010](#bisio2010optimal)).
Apparently, this theoretical result may not translate well to an
implementation: a sequential approach is more feasible. In this case,
subsequent optimal states would depend on what the previous state
revealed of the process. To spice things up, this sequence of optimal
states could be augmented by classical learning and the parametric
control of estimating the unitary ([Hentschel & Sanders, 2010](#hentschel2010machine))

The next question is what the input and output data might be. I believe
it is a clear case of quantum input and output, a
[distinction](http://scitechconnect.elsevier.com/brief-overview-quantum-machine-learning/)
I like to make. I find it useful to separate this class of algorithms
from ones that operate on classical data while still offering a speedup,
like Grover's search on classical databases and its variants. Yes, we
can argue that at some point the quantum states have to be initialized
classical, and at that time we introduce at least linear computational
complexity. At the other end of the pipeline, sooner or later we will
want classical information, which implies state tomography of the output
states with all its problems. As one visitor to the poster pointed out,
quantum machine learning is at severe disadvantage compared to classical
algorithms, and this is one of the reasons. Yet, we can picture learning
processes where several quantum learners are attached, or a learner aids
a quintessentially quantum procedure, obliterating the need for a
transition to the classical domain. So I maintain that it makes sense to
talk about quantum input and output data.

References
==========

<a name="bisio2010optimal"></a>Bisio, A.; Chiribella, G.; D'Ariano, G.;
Facchini, S. & Perinotti, P. [Optimal quantum learning of a unitary transformation](http://arxiv.org/abs/0903.0543). *Physical Review A*,
2010, 81, 032324.  
<a name="hentschel2010machine"></a>Hentschel, A. & Sanders, B. C.
[Machine Learning for Precise Quantum Measurement](http://arxiv.org/abs/0910.0762). *Physical Review Letters*,
2010, 104, 063603.  
<a name="wittek2014transduction"></a>Wittek, P. [Transduction and Active Learning in the Quantum Learning of Unitary Transformations](http://bada.hb.se/bitstream/2320/14001/1/transduction_and_active_learning.pdf).
*Poster Session at AQIS-14, 14th Asian Quantum Information Science
Conference*, 2014, Kyoto, Japan.

