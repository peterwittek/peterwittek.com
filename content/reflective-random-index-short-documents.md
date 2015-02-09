Title: Reflective random indexing on short documents with fixed vocabulary
Date: 2015-02-06 17:10
Author: Peter
Category: Machine learning
Tags: Machine learning
Slug: reflective-random-index-short-documents
Summary: Reflective random indexing can lead to strange results: if the vocabulary is small compared to the number of documents, term vectors will show little variety.

We observed a strange phenomenon while analysing the term vector space of a reflective random index: the term vectors clustered around a handful of central points. This was a blocking issue, so we reverted to random indexing, but the problem deserved further investigation.

Scenario
--------

The corpus was a collection 12.8 million [book reviews on Amazon](http://snap.stanford.edu/data/amazon/amazon_readme.txt). The reviews were short, about 80 words on average. We used a stemmer based on WordNet, keeping only nouns and verbs; the code and further details are available [here](https://github.com/peterwittek/concept_drifts). This gave us 50672 index terms.

Reflective random indexing
-------------------------
Vanilla [random indexing](https://en.wikipedia.org/wiki/Random_indexing) has one training cycle: we generate a random basis, we use this to build term vectors based on the corpus statistics, and we create document vectors as weighted sums of the term vectors.

[Reflective random indexing](http://www.biomedsearch.com/nih/Reflective-Random-Indexing-indirect-inference/19761870.html) adds another cycle by restarting the construction of the term vectors using the basis of document vectors, and then creating the document vectors again using the term vectors. This step can be repeated.

Using [SemanticVectors](https://code.google.com/p/semanticvectors/), we created the reflective random index in two training cycles with the following command:

    :::bash
    java -Xmx40000m pitt.search.semanticvectors.BuildIndex -trainingcycles 2  -luceneindexpath index

We also extracted the term vectors of the first training cycle for comparison.


The structure of the term space
-------------------------------
The average distance of terms in a random index is fairly large, which is not surprising, as the vectors are approximately orthogonal. We calculated all pairwise distances and plotted the histogram:

<center>![Histogram of distances]({filename}/images/distance_histogram1.png)</center>
<center>Histogram of distances in the term space of a random index.</center>

Curiously, the structure of distance changes completely in the reflective index. Most terms become very similar:

<center>![Histogram of distances]({filename}/images/distance_histogram2.png)</center>
<center>Histogram of distances in the term space of a reflective random index.</center>

Why is this? The small vocabulary is to blame. The first-round document vectors are superpositions of a few term vectors. Some of these nouns and verbs are frequent, others not so much. When we re-index the term vectors in the basis of the documents, the contribution of the frequent terms in the superposition gets smeared out: infrequent terms will also have a vector similar to that of frequent ones.

This is usually desirable, as we want to see connections between words which we would otherwise not see: the term and document spaces are normally extremely sparse. This is not the case here with a very high number of documents and a tiny set of index terms: there are 250 times more documents than index terms, whereas the ratio is usually the other way around. Because of this, the smearing effect becomes overwhelming, making the term vectors too similar to one another. This, unfortunately, means that we had to rule out reflective random indexing in our analysis.

