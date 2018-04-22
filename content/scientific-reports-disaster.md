Title: The real price of publishing in Scientific Reports
Date: 2018-04-22 17:51
Author: Peter
Category: Academic publishing
Tags: Academic publishing, Quantum machine learning
Slug: scientific-reports-disaster
Summary: You pay a much higher price than the article processing fee if you publish in Scientific Reports: your inbox and your reputation are at stake.

The formal article processing fee in Scientific Reports is 1,370 euros, as of 22 April 2018. Open access is the way to go, and while [Quantum only charges 200 euros](https://quantum-journal.org/instructions/authors/), the price for Scientific Reports is not too bad. I also believe that the journal's mission to publish scientifically correct papers without evaluating impact is important and there is place for it in the publishing landscape. This is why we chose to publish our work, [Quantum Enhanced Inference in Markov Logic Networks](https://arxiv.org/abs/1611.08104): it is a quantum machine learning paper that 1) machine learning conferences rejected for not understanding it; 2) physics outlets would have rejected it for not having enough physics. Scientific Reports looked like a solid choice, so despite protests from my co-author, we submitted our work to the journal and eventually published it there. A year passed since the publication and now I know it was a terrible mistake: we paid a much higher price than the article processing fee.

Editorial malpractice
=====================
A journal is as good as its editorial board. They ensure the quality of the peer review cycle. One of the referees clearly had no understanding of the paper, but engaged in the abominable practice of reference harvesting. He asked us to cite five papers that were entirely unrelated to our work. The five papers mysteriously shared a common co-author. This should be a red flag for any editor.

We grumbled about it and decided to play a prank. We included the references and added this in the acknowledgement: "We would like to thank the anonymous referee 1 for suggesting to us Refs. X, Y, Z, W, V", specifying the actual papers. It did not only go through the next round of review, but the referee asked us to cite the five papers **in the abstract**!

This was when the fuses burned. I immediately started writing a scathing email to the editor that this is below any possible standard in refereeing. Before hitting "Send", I thought I would check if the editor and the anonymous referee co-authored anything. Well, they did, about a hundred papers.

So after pacifying my co-author, I wrote a nicer email, saying that the abstract should be self-contained, and we do not include references by principle. The paper was accepted the next day. The only mistake we did is that when the proofs came out, the references were re-ordered, so our acknowledgement to the dedication of the anonymous referee ended up not funny. For the record, the correct references in the published version are Refs. 11, 53, 54, 55, 56.

Forced inclusion of email address
=================================
Despite my fight not to include an email address, only a URL, the journal forced me to include one. I set up a new email address for this purpose to monitor how much spam I would recieve in the first year after publication. Here are the stats:

1) We received 134 spam emails. They are definitely on the lower end of the spectrum, targetting the academic variants of the audience of Viagra spam. Here are some great subjects:

  - “Boost your citation potential”
  
  - “2018年数据科学与商业分析国际会议srep2017”
  
  - “We Will Address the Bioinformatics Challenges for You”
  
  - “Struggling with your research?”
  
  - “Free Starbucks or Amazon gift card with your vector or virus order”

I find it even more hilarious that Elsevier was one of the spammers: they sent the mail “Struggling with your research?” and “Boost your citation potential.”

2) The number of spam emails is rising over time, as expected:

<center>![The distribution of spam email received in the first year after publication.]({filename}/images/sreps_spam_distribution2.png)<br>
The distribution of spam email received in the first year after publication.</center>

3) We received zero non-spam emails.

The shame
=========
Every time I talk about this work, I ashamedly admit that it was published in Scientific Reports, and I feel obliged to explain myself. This journal has no standards: it is evident in the review cycle and the actual papers they publish. As with any journal, there are some good papers unfortunately. I can only hope that quantum machine learning papers will find better places than this.
