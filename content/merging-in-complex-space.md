Title: Merging a distributional and a semantic vector space in complex Hilbert space
Date: 2013-07-15 00:03
Author: Peter
Category: Machine learning
Tags: Machine learning
Slug: merging-in-complex-space
Summary: Describing how to build a complex-valued random index using a term and a concept vector space.

As described in [Wittek et. al, 2013](#wittek2013combining), we can
easily merge two random indices in complex space. Using a random index
is useful for querying and text classification, and the same random
index works for a concept representation. Merging the two
representations allows us to leverage on the strength of both, yielding
higher recall rates. The steps below outline how the merge works.

Downloads
=========

The modified source code of SemanticVectors is available
[here](http://peterwittek.com/files/semanticvectors-3.8-modified-src.tar.gz "Source files").
There are notable changes to the original SemanticVectors classes. Most
importantly, the distance function in the ``CompexVector`` class was
rewritten and the dominant mode was set at ``CARTESIAN``. The
``CompoundVectorBuilder`` class strictly does not normalize vectors. Since
all distance functions are inner products, normalization is unnecessary.
The concepts are identified by a number, which are filtered out by
SemanticVectors, unless the flag ``filteroutnumbers`` is set to false.
Unfortunately this flag cannot be flipped from the command line due to a
bug how boolean variables are parsed. A modified ``FlagConfig`` class takes
false as the default value for ``filteroutnumbers``. There is also an extra
classes helping with the new complex space (``ComplexSpaceMerger``).

Assumptions
===========

We assume that the document collection is indexed by Lucene  in the
folder ``lucene-index-term_representation``. We further assume that a
concept representation is available, e.g., created by MetaMap ([Aronson and Lang, 2010](#aronson2010overview)). The Lucene index of the concept
representation is in ``lucene-index-concept_representation``.

Procedure
=========

The instructions below assume that all data, including the Lucene index
directories, are in the same folder as the jar file. Set up environment
variables. Notice that there is a new jar dependency:

    :::bash
    export CLASSPATH=PATH/TO/LUCENE/3.6.2/lucene-core.jar:PATH/TO/LUCENE/3.6.2/contrib/demo/lucene-demo-3.6.2.jar:./semanticvectors-3.8.jar


Build random indices for the term and concept spaces:

    :::bash
    java pitt.search.semanticvectors.BuildIndex -luceneindexpath lucene-index-term_representation
    java pitt.search.semanticvectors.BuildIndex -docvectorsfile conceptdocvectors -termvectorsfile concepttermvectors -luceneindexpath lucene-index-concept_representation

This will produce four vector spaces: termvectors.bin, docvectors.bin,
concepttermvectors.bin, and conceptdocvectors.bin. Notice that the
docvectors.bin and conceptdocvectors.bin are both document vector spaces
of the same collection, yet the physical order in the files is quite
arbitrary. This does not cause a problem with regular searches, but it
is a problem when merging the two document spaces in a complex space. A
shell script is provided to fix the order:

    :::bash
    ./fix_order.sh conceptdocvectors.bin
    ./fix_order.sh docvectors.bin

Then the spaces can be merged:

    :::bash
    java pitt.search.semanticvectors.ComplexSpaceMerger docvectors.bin conceptdocvectors.bin complexdocvectors.bin

If the purpose is information retrieval, the next step is to map the
query vectors in the same complex space. Again, the real and imaginary
components of the query must belong to the same query, otherwise
querying is straightforward.

References
==========

<a name="aronson2010overview"></a> Aronson, A. R. & Lang, F.-M. An
overview of MetaMap: historical perspective and recent advances.
*Journal of the American Medical Informatics Association*, 2010, 17,
229-236.  
  
<a name="wittek2013combining"></a> Wittek, P.; Koopman, B.; Zuccon, G.
& Darányi, S. Combining Word Semantics within Complex Hilbert Space for
Information Retrieval. *Proceedings of QI-13, 7th International Quantum
Interaction Symposium*, July, 2013. Leicester, UK.

