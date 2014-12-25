Title: Spyder: Getting closer to a viable Mathematica alternative
Date: 2013-08-07 04:00
Author: Peter
Category: Python
Tags: Python, SymPy, Spyder
Slug: spyder-closer-to-a-mathematica-alternative
Summary: A combination of Spyder, IPython, SymPy, NumPy, and Matplotlib gets pretty close to replace Mathematica in most of my use cases.

We still do not quite have a
[Mathematica](http://www.wolfram.com/mathematica/ "Mathematica") killer,
but we are inching closer.
[Sage](http://www.sagemath.org/index.html "Sage") is supposed to fill
that niche, but I always found its browser-based notebook interface
tedious. [Spyder](https://code.google.com/p/spyderlib/ "Spyder"), on the
other hand, is a nifty piece of software. Combined with a couple of
other tools, it is set to become an indispensible tool for symbolic
calculations, and it is also has a collection of slick features that
Mathematica does not.

Preliminaries
=============

The discussion uses Spyder 2.2.1,
[IPython](http://www.ipython.org/ "IPython") 0.13.2, Python 2.7.5,
[SymPy](http://sympy.org/en/index.html "SymPy") 0.7.3,
[NumPy](http://www.numpy.org/ "NumPy") 1.7.1, and
[Matplotlib](http://matplotlib.org/ "Matplotlib") 1.3.0. To enable
symbolic calculations and nice printing, tick
Tools-\>Configuration-\>IPython console-\>Advanced Settings-\>Use
symbolic math. The disadvantage of this that if you restart the IPython
console, you may not get your SymPy libraries back. In this case, set up
the IPython startup file accordingly, and also at this to
``~/.config/ipython/profile_default/ipython_config.py``:

    :::python
    c.InteractiveShellApp.extra_extension = sympy.interactive.ipythonprinting

This formats mathematical formulae nicely.

For decent plotting, activate Tools-\>Configuration-\>IPython
console-\>Support for graphics (Pylab). It is also a good idea to
automatically load Pylab and NumPy.

Interface
=========

The main window of Spyder is a hybrid between Mathematica and Matlab.
Most action happens in the IPython console, which numbers inputs and
outputs just like Mathematica. Moving to previously issued commands is
more bash-like. The IPython shell's content can be saved, but only the
instructions -- internal states are not preserved. You are also
augmented by an editor and a history log, so you can easily fish out the
relevant bits and save them to a script. While Mathematica's notebook
interface reigns king, it is much easier to write reproducible code this
way.

[caption id="attachment\_397" align="aligncenter" width="620"][![The
main window of
Spyder](http://peterwittek.com/wp-content/uploads/2013/08/spyder_main_window-1024x563.png)](http://peterwittek.com/wp-content/uploads/2013/08/spyder_main_window.png)
The main window of Spyder[/caption]

The editor itself is okay. Basic Python idiosyncrasies, such as
indentations and the occasional colon, are catered for, and there is
also simple spelling completion. A neat shortcut is F9, which runs the
current selection. Otherwise F5 will run the current script, and Ctrl+F6
will run the previous execution.

The IPython console prints mathematical formulae the way we like them:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [2]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    diff(sin(x*y)**x,x)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[2]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\left(\\frac{x y \\cos{\\left (x y \\right )}}{\\sin{\\left (x y
\\right )}} + \\log{\\left (\\sin{\\left (x y \\right )} \\right
)}\\right) \\sin\^{x}{\\left (x y \\right )}\$\$

</div>

</div>

</div>

</div>

</div>

Plots are either displayed in-line (Mathematica style), or in a window,
like in Matlab:

[![spyder\_plot](http://peterwittek.com/wp-content/uploads/2013/08/spyder_plot.png)](http://matplotlib.org/mpl_examples/images_contours_and_fields/streamplot_demo_features.py)

Symbolic Calculations
=====================

SymPy takes care of symbolic manipulations. It is quite efficient, its
performance is comparable to the C++ library SymbolicC++. It does
numerical evaluation only when it is asked to, just like Mathematica:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [3]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    sqrt(2)*pi

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[3]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\sqrt{2} \\pi\$\$

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [4]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    N(sqrt(2)*pi)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[4]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$4.44288293815837\$\$

</div>

</div>

</div>

</div>

</div>

Simplify and expand are here to solve your grade-five algebra homework:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [5]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from sympy import sin, cos, simplify

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [6]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    a = (x + x**2)/(x*sin(y)**2 + x*cos(y)**2)

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [7]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    a

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[7]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\frac{x\^{2} + x}{x \\sin\^{2}{\\left (y \\right )} + x
\\cos\^{2}{\\left (y \\right )}}\$\$

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [8]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    simplify(a)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[8]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$x + 1\$\$

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [9]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    ((x + y + z)**2).expand(basic=True)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[9]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$x\^{2} + 2 x y + 2 x z + y\^{2} + 2 y z + z\^{2}\$\$

</div>

</div>

</div>

</div>

</div>

Limits also work:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [10]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    from sympy import limit
    limit(1/x,x,oo)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[10]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$0\$\$

</div>

</div>

</div>

</div>

</div>

Sympy also has functions for more advanced applications, such as
[Hermitian Operators](http://peterwittek.com/2013/05/generating-noncommutative-monomials-with-sympy/ "Generating noncommutative monomials with SymPy")
for quantum physics simulations.

Functional Programming
======================

Mathematica is first and foremost a functional programming language, but
due to its highly opportunistic nature, it also caters to procedural
programmers. Python is just about that opportunistic, throwing in
object-oriented models in the mix.

Mathematica's almighty Map function has a rough equivalent in the
Pythonesque list comprehensions. In Mathematica, you write:

![\#\^2 & /@ {x, y,
z}](http://peterwittek.com/wp-content/uploads/2013/08/mathematica_map1.png)

The Python variant is:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [11]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    [ s**2 for s in [x, y, z]]

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[11]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\begin{bmatrix}x\^{2}, & y\^{2}, & z\^{2}\\end{bmatrix}\$\$

</div>

</div>

</div>

</div>

</div>

Python may also use a map function to the same extent.

The lambda operator was introduced for creating anonymous functions --
this is similar to Mathematica's pure function (&). While pure functions
dot every Mathematica notebook, lambda functions are far clunkier to
use. They come handy in some cases:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [12]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    map(lambda x: x%3 == 0, [1, 2, 3])

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[12]:

</div>

<div class="output_text output_subarea output_pyout">

    [False, False, True]

</div>

</div>

</div>

</div>

</div>

MapIndexed can be emulated by the enumerate function:

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In [13]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight">

    [ [a,i] for i,a in enumerate([sqrt(2), pi, x])]

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out[13]:

</div>

<div class="output_latex output_subarea output_pyout">

\$\$\\begin{bmatrix}\\begin{bmatrix}\\sqrt{2}, & 0\\end{bmatrix}, &
\\begin{bmatrix}\\pi, & 1\\end{bmatrix}, & \\begin{bmatrix}x, &
2\\end{bmatrix}\\end{bmatrix}\$\$

</div>

</div>

</div>

</div>

</div>

Do not have high expectations, though. Functional programming in Python
was an afterthought. Nest and FixedPoint would be nice to have.

Mathematica has nice parallel routines, and lets you launch parallel
kernels. The solution is not spectacularly great, for instance, parallel
kernels go through a different initialization than the default kernel.
Yet it is nice that if you adhere to the functional programming
paradigm, your code will more or less automatically run in parallel.
With a bit of extra work, IPython can do something similar. If you have
four cores, then launch an IPython parallel controller with four
engines:

    :::bash
    $ ipcluster start -n 4

This starts the engines and creates a couple of files in
``~/.config/ipython/profile_default/security``. Those files will be parsed
when you start the IPython shell. Then create a parallel environment in
the shell:

    :::python
    from IPython.parallel import Client
    rc = Client()
    dview = rc[:]

You are ready to use your parallel map function:

    :::python
    dview.map_sync(lambda x: x**10, range(32))

What Mathematica Cannot Do
==========================

Mathematica will never tell you how it arrived at a result. Given that
the tools used here are open source, if you have enough time, you can
always figure how a particular result was derived. A caveat: 'enough
time' might be a period longer than your life span.

Theoretically Spyder could [run on my phone.](http://peterwittek.com/2013/09/computer-algebra-system-on-a-cell-phone/ "Computer Algebra System on a Cell Phone")
It requires bootstrapping a Linux and starting X in the framebuffer.
None of this is rocket science, but I have not tried it yet. VNC-based
solutions to run X as a virtual screen are inefficient.

At the other end of the spectrum, if you have your code developed and
you would like to run it on an HPC workstation, there is nothing
preventing you from doing so. Say, you know your symbolic calculations
are memory-hungry, then launch a
[cr1.8xlarge](https://aws.amazon.com/ec2/instance-types/#instance-details "AWS instance types")
instance on Amazon Web Services with 244 GByte of memory, do some basic
configuration, and launch your code. Mathematica ties your hands with
licences, you cannot just upload your copy to a workstation of your
choice. While the Mathematica Player is free and it comes with the full
Mathematica kernel, its primary purpose is interaction, not headless
execution on a cloud-based server.

IPython bridges different levels of the software stack. I can do a
symbolic integral, then run a bash command:

    :::python
    display(integrate(sin(x),x))
    !uname -a

I cannot come up with an obvious application scenario, but executing
external commands in Mathematica was always troublesome.

Debugging is not a strength of Mathematica, perhaps under the assumption
that good functional programmers never-ever make a mistake. Spyder is
more realistic in this regard. Breakpoins, conditional breakpoints, and
the usual assortment of debugging tools are at your fingertips. You may
also have a chance that you get meaningful error messages, which seldom
happens with Mathematica (and never with GCC).

Grievances
==========

Most issues go back to Python itself and have nothing to do with Spyder
per se. One exception is the way to break execution in the IPython
console. This is annoying. The IPython interpreter is split in two tabs:
the client where you issue commands, receive output and error message,
and do all your work, and a 'console', where the execution takes place.
Breaking the execution is a stochastic process: keep pressing Control+C
in the console and the client, and hope that your execution stops.
Strange enough, Mathematica suffers from similar problems. While Alt+,
and Alt+. normally work, these shortcuts will fail you miserably if you
are plotting an intricate diagram. This only got worse in recent
Mathematica versions, as Wolfram is keen on separating the kernel and
and the graphics engine, leading to frequent freezes of the interface.
ListPlot3D is the worst offender.

Forget multicore execution with Python. Python's Global Interpreter Lock
will not let you get away with simple solutions, unless you can express
the problem in functional programming terms. You must run multiple
Python processes to have parallelism, and then the onus is yours to
organize communication, share data, pass messages, and so on. OpenMP?
Not for Python. Crazy as it is, C code is easier to parallelize than
Python.

A curse of Python is the proliferation of mutually incompatible
interpreters. The Mathematica kernel does not suffer from this, and if
there are changes which are not backward compatible, the interface
guides you through the changes required in your notebook. With Python,
your only option is to cross your fingers and hope your code will not
break between versions x.y.z.a.b.c and x.y.z.a.b.d.

Performance is not outstanding, but it is not terrible either. If you
are among the lucky few, then your code will work with Pypy. Executing a
programme with Pypy can be four to six times faster than with the
default CPython interpreter. Let us not talk about memory use, though,
that is bound to be abysmal with any given Python interpreter or
compiler.
