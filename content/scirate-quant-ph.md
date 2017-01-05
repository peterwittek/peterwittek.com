Title: Hot authors and topics in quant-ph in 2016 and how to generate a sexy abstract
Date: 2017-01-06 03:51
Author: Peter
Category: Academic publishing
Tags: Academic publishing, Machine learning
Slug: scirate-quant-ph
Summary: SciRate gives instant gratification for our precious preprints on arXiv. We analyse the metadata of the papers that appeared in quant-ph in 2016 to find out the hottest authors and topics, and we train a recurrent neural network to generate fake abstracts.

I had a conjecture that none of the topics I work on is hot. To verify this, I needed data. Citation counts have a long time lag, so do journal publications. SciRate is fairly well known among the poor souls who study the quant-ph category daily on arXiv. I noticed that after the initial two-three weeks, the number of Scites a paper gets hardly increases further. Since the number of Scites is both immediate and near constant after a short while, it makes a reasonable measure for hotness.

I crawled SciRate for metadata of the papers that had at least 10 Scites, spent some time normalizing it, and I summarize my findings here. I made the [data available](https://www.kaggle.com/peterwittek/scirate-quant-ph) if you want to dive into it. The matching source files were also pulled from arXiv for 2016, but I am not sure if I can legally share this. The corpus contains five years of metadata, 2012-2016. My chief interest was the hottest topics, so this article works only on the manuscripts from 2016.

Hottest authors
---------------
Tenures will be distributed based on these results. First I counted the number of papers each author had in the corpus. This is akin to the i10 index, but adapted to grant agencies with a short attention span. The top authors are plotted in the following figure.

<center>![Authors ranked according to the number of papers with at least 10 Scites.]({filename}/images/top_authors_sci10.png)<br>
Authors ranked according to the number of papers with at least 10 Scites.</center>

I marked my group leader in red, hoping to earn some brownie points.

Next I ranked the authors according to the total number of Scites they got across all their papers. The following figure plots the top thirty authors.

<center>![Authors ranked according to the total number of Scites across all their papers with at least 10 Scites.]({filename}/images/top_authors_total_scites.png)<br>
Authors ranked according to the total number of Scites across all their papers with at least 10 Scites.</center>

My group leader ranks 74, which is actually below me. I will not get any brownie points for this finding.

Hot topics
----------
I did some basic NLP on the titles, abstracts, and full texts: tokenization, stopword removal, POS tagging, and lemmatization using WordNet. I also identified the bi- and trigrams using pointwise mutual information.

As a basic visualization method, I tried word clouds. Using all words, the result was not saying much: 'quantum' and 'classical' showed enormous. I got a better mileage indexing with the bi- and trigrams alone. Here is the plot for the titles:

<center>![Word cloud using bi- and trigrams in titles.]({filename}/images/wordcloud_titles_bitrigram.png)<br>
Word cloud using bi- and trigrams in titles.</center>

Machine learning is right there, and its font is bigger than that of de Finetti theorems! I also generated a word cloud on the abstracts:

<center>![Word cloud using bi- and trigrams in abstracts.]({filename}/images/wordcloud_abstracts_bitrigram.png)<br>
Word cloud using bi- and trigrams in abstracts.</center>

The overlap is obvious, although it is strange how tensor networks are less prominent in the abstracts. Notice that "et al" is as hot as "surface code".

Naturally, we should not expect too much from a word cloud, as it is based on simple frequency counts. The word cloud for the full text documents is not even worth showing. I turned to more sophisticated methods to gain insights on the full texts, and used [adaptively regularized topic  models](http://dx.doi.org/10.1007/s10994-014-5476-6).  After playing around with the parameters for a while, I got reasonable topics, although I failed to suppress the common words. The topics with the top-ranking words within each of them are as follows (I corrected the syntax compared to the automatic lemmatization to improve readibility):

- Topic 0: set, algorithm, problem, group, since, thus, function, element, also, party;
- Topic 1: key, scheme, adversary, message, definition, security, attack, classical, quantum, Alice;
- Topic 2: code, lattice, operator, stabilizer, boundary, model, fig, qubits, generator, term;
- Topic 3: also, circuit, algorithm, error, case, gate, time, qubits, function, since;
- Topic 4: model, boundary, term, Hamiltonian, bulk, region, spin, large, energy, eq;
- Topic 5: channel, entanglement, eq, subsystem, Bob, quantum, classical, measurement, entropy, information;
- Topic 6: gate, error, photon, noise, qubits, measurement, qubit, time, experiment, code;
- Topic 7: energy, system, Hamiltonian, time, measurement, work, thus, quantum, operation, process;
- Topic 8: protocol, bound, Bob, verifier, proof, probability, game, Alice, input, first;
- Topic 9: error, tensor, MPS, PEPS, currency, protocol, cost, measurement, MPO, method;
- Topic 10: also, matrix, case, since, operator, hence, theorem, proof, fact, invariant;
- Topic 11:  theory, set, coherence, operation, particular, example, condition, hence, definition, general;
- Topic 12: channel, theorem, inequality, norm, constraint, well, bound, hence, fact, lemma;
- Topic 13: gate, solution, eq, operator, circuit, point, manifold, phase, therefore, set;
- Topic 14: network, channel, node, capacity, may, entanglement, eq, edge, point, thus.

I tried to dump all common words to five background topics, but some were notorious. About five of the above topics are too general, but the rest could be assigned a label. I was glad to see Alice and Bob showing up, in fact, in topic 8, they gaily verify proofs together. Eve also dropped by, but in the end, she got lost in the hyperparameter optimization.

Generating fake abstracts
-------------------------
I am mesmerized by the accuracy of [SnarXiv](http://snarxiv.org/), which can fool many human readers. It builds on a context-free grammar. I wanted to see whether we could do something similar, but using character-level language generators. I trained a [phased LSTM](https://arxiv.org/abs/1610.09513), which should have a reasonable mid-term memory, so it should be able to stick to a topic. Unfortunately, the total length of the concatenated abstracts is less than 600 kilobytes, which is a tiny dataset for a neural network learning at character level, but it picked up some basic rules of English fairly accurately in a matter of hours. Here I give some 1000-character samples. In each sample, the first forty characters were the seed -- these are set in bold.

Our network has a lot to say about the foundations of quantum physics:

<i>**the foundations of quantum physics are f**ermionic data processes that complete convergence of a result of the first environment. we finally articousl define a number of the contriting contraction of the constrained for any classical algorithm for quantum computation of the problem of the problem for the pure states for the first encryption of a theorem to provide the theorem of entanglement by the pure convergic set of local hamiltonian theorem to derive a state of the classical connection and construction. we finally a string of the maximal entanglement of the most problem entropy and the description of the concept of the connection of continuous that are are recent of the ball special concepk with converge constrained by an operator, computational for any at the concept of the connection in the multi-shan any strategy multi-prove that the parametric quantum computation in the constrained for the state of the connection of the state of the constraint. this is the problem of entanglement constraint. we provide that the channe</i>

Let us see what it has to say about something more practical, fault-tolerant quantum computations:

<i>**fault-tolerant quantum computation is im**proved the channel we determine an entanglement that context of particles, and we consider only the positive probability of the form of the channel with a resource theories of our factors that can be bell inequality for entanglement of the contextualiby transformation where the condens of the conver significantly simulated in the space-constraint. the three position of the state in the construction of quantum computation is particles the possess a new construction of the contextual concepts of a complexity is the connection of the construction related in the resource of quantum computation and by the local hamiltonian algorithm is are in the set of a state of the maximal constraint by a precise and the constant for any any particular to sign for a local hamiltonian of the continuons the robust entangled states of the context of a finally beneficing an entanglement of the measurements of the construction of the menimal space connection of the entanglement of a model for any quantum algo</i>

I think we need to invent new pseudo-particles called "continuons" to develop fault-tolerant quantum computation. How about some machine learning?

<i>**quantum-enhanced machine learning is exp**loloton of the construction of this work of the planal for a probability of this processes that all complexity can be used a local hamiltonian of a local operation of the constant to detain the connection of the entanglement correlations the constraint of the test of the connection of the formal entanglement of the multiplications that if the constraint of the entanglement of the state of only single-qubit in a larger state in the most function of the channel with the problem to the set of the construction of the concept of the context of entanglement results for the local operational systems and the constraint of a single phase in a rounent that alice of the final quantum computation of the connection in the classical simulation of the construction to the for approximate the context of the constant to determine any strategy as contried algorithm that channel case of the spectrum of a single concatenation of the connection of the channel and by the construction of the channel with the</i>

Well, it needs to learn a bit more classical machine learning first.

A fellow Kaggler [used a Markov generator](https://www.kaggle.com/speckledpingu/d/peterwittek/scirate-quant-ph/markov-generated-abstracts-w-predicted-scites) to the same end, and given the tiny size of the corpus, his results are impressive.

Closing thoughts
----------------
Publishers add [little to no value](https://arxiv.org/abs/1604.05363) to preprints. We could dump all manuscripts on [Quantum](http://quantum-journal.org/) -- I am certain the founders would appreciate my suggestion -- and let Scites decide academic progression. It is high time we forgot about the Impact Factor and toppled the exploitative institution of academic publishing.

I feel my initial conjecture was corroborated: even the fake abstract generator can't make any sense of quantum machine learning. Perhaps I should move on and get a life.

Acknowledgement
---------------
A Tesla K40 was used in training the neural network, which was donated by NVidia.
