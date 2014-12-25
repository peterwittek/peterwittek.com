Title: Reproducible research, literate programming, IPython, and GitHub
Date: 2014-05-16 18:28
Author: Peter
Category: Academic publishing, Python
Slug: reproducible-research-literate-programming-ipython-and-github

I came across [this
thread](https://news.ycombinator.com/item?id=7699935) on Hacker News,
which links to a curated gallery of IPython notebooks, including
countless interesting topics, most notably, [reproducible academic
publications](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks#reproducible-academic-publications).
I am a fan of IPython, combined with [a few other
tools](http://peterwittek.com/2013/08/spyder-closer-to-a-mathematica-alternative/),
it makes a great replacement for Mathematica, but I never thought of it
as a way to make research results more accessible. This is because I was
using it from [Spyder](https://code.google.com/p/spyderlib/), avoiding
its notebook interface. Hosting notebooks on GitHub and displaying them
with [nbviewer](http://nbviewer.ipython.org/) provide a simple mechanism
to produce reproducible research. Even more so now, as GitHub is [making
changes](https://github.com/blog/1840-improving-github-for-science) to
appeal more to scientists.

When I still had a Mathematica license, I was fond of its notebook
mechanism. I loved mixing code, notes, diagrams, and mathematical
formulas. It was an example of [literate
programming](https://en.wikipedia.org/wiki/Literate_programming), a form
of coding where natural language and source code blend, making it a lot
easier to digest. Wolfram advocates the use of the notebook interface
for publishing results by providing a repository for notebooks, and also
providing a free player for reading them if you do not have a copy of
Mathematica. I do not think the free player caught on, and, of course,
you cannot edit the notebooks if you want to tinker with the published
results. A combination of GitHub and Ipython sounds like a much more
viable option.

Enter IPython
=============

Unfortunately, the console and qtconsole environments of IPython will
not allow to mix code with anything. The only option is the
browser-based notebook, which runs a lightweight server called Tornado.
[Sage](http://sagemath.org/) made me dislike browser-based computer
algebra systems. I find the solution clunky.

To reduce clunkiness, I set up a Firefox profile dedicated to running
IPython notebooks. It is an empty profile without plugins, and I set the
home page to http://127.0.0.1:8888/, which is where the IPython notebook
server runs. I disabled the address bar following
[these](https://support.mozilla.org/en-US/questions/939601)
instructions:

<div class="highlight">

    mkdir ${FIREFOX_IPYTHON_PROFILE}/chrome
    echo '#nav-bar { display: none !important; }' > ${FIREFOX_IPYTHON_PROFILE}/chrome/userChrome.css

</div>

IPython also allows creating profiles, so I set up one exclusively for
the notebook interface:

<div class="highlight">

    ipython profile create browser

</div>

To achieve the same functionality as in Spyder, I put the following to
\~/.ipython/profile\_browser/startup/00-first.ipy:

<div class="highlight">

    from sympy import init_printing
    init_printing()
    x, y, z, t = symbols('x y z t')
    %pylab inline

</div>

I use the following script to start the IPython server and the Firefox
profile. The script also shuts down the IPython server if I close the
Firefox instance:

<div class="highlight">

    #!/bin/bash
    ipython2 notebook --no-browser --profile browser &amp;
    sleep 1
    firefox -P ipython -no-remote
    pid=`ls ${HOME}/.ipython/profile_browser/security/nbserver-*|  
     sed -e 's/.*nbserver-//'|sed -e 's/\..*//'`
    kill $pid

</div>

The result looks like the following:

[![ipython-notebook](http://peterwittek.com/wp-content/uploads/2014/05/ipython-notebook.png)](http://nbviewer.ipython.org/github/peterwittek/ipython-notebooks/blob/master/Comparing_DMRG_ED_and_SDP.ipynb)

Parallel to Spyder, I use the notebook interface for writing notes and
record meaningful lines of code. It would be wonderful to develop code
in Spyder, and taking notes in the notebook interface, while sharing the
same kernel. Unfortunately, we
[cannot](https://github.com/ipython/ipython/issues/4066) launch new
IPython kernels in the notebook server from outside the browser.
Theoretically Spyder can connect to an existing kernel, but I could only
connect to console and qtconsole kernels. So at this point, you need to
re-run calculations in the notebook interface.

Sharing the work
================

Putting every bit of code or text under version control is a good habit.
It is only natural to put the notebooks in git repositories. From here,
it is an effort of two clicks to add a new repository on GitHub for the
notebooks, and push them online.

The project nbviewer renders static HTML pages of online notebooks,
making it spectacularly easy to share them. This solution also allows
downloading the notebook, and it has a direct link to the GitHub repo
where the notebook is developed. Reproducible research does not get
easier than this. I tried it on a [small
problem](http://nbviewer.ipython.org/github/peterwittek/ipython-notebooks/blob/master/Comparing_DMRG_ED_and_SDP.ipynb)
just to see how it works. IPython digest Markdown in the text sections,
and also renders LaTeX equations through MathJax. I am pleased with the
result.

A few arXiv papers link to notebooks through nbviewer. The comment
section allows adding URLs, like in [this
paper](http://arxiv.org/abs/1305.0215). While not the most transparent
method, it is a lot better than leaving the reader to re-implement
everything to reproduce the results. We are facing a crisis with
reproducible research, and this approach is a step forward.

