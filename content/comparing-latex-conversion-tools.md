Title: Comparing LaTeX conversion tools
Date: 2013-11-25 02:38
Author: Peter
Category: Academic publishing
Tags: Academic publishing
Slug: comparing-latex-conversion-tools
Summary: Converting LaTeX to word processor formats is the holy grail of document conversion. Perhaps we are getting closer to a viable solution.

One of the great joys of working in an EU consortium is that members
will enforce their standards on others. This means using Google Docs for
collaborative document editing, which is painful: the result will look
abysmal, and LaTeX users will not rejoice -- this category includes
myself. Using LaTeX and Git on a server hosted by a consortium member
would solve all problems, but if this was an option, Europe would not be
descending to oblivion and irrelevance. So I find myself with the
age-old problem of LaTeX to word processor format conversion.

Playing around with some tools, I soon figured that the problem is still
unsolved. I created a small test case for the features I need, and
checked which tool would fit the bill. This post is about the results.

Tools
-----

For the past thirteen years since I have been facing this problem, the
range of tools does not seem to expanding much. The usual suspects are
latex2rtf and latex2html -- the latter was not updated in recent times.

Texlive's tex4ht has been around for a while; updates are sporadic. It
splits into mk4ht, a script that generates OpenDocument format, and
htlatex, which produces HTML.

[Pandoc](http://johnmacfarlane.net/pandoc/) is a newcomer that promises
to convert from any markup format to any other. With Pandoc, the
theoretical possibility is there to convert directly from LaTeX to
everybody's favourite ISO standard Office Open XML, otherwise known as
docx -- a format untouched by
[controversy](https://en.wikipedia.org/wiki/Standardization_of_Office_Open_XML#Process_manipulation).
Its Office Math Markup Language (OMML) allows embedding mathematical
formulae; fortunately OMML is incompatible with W3C's MathML.

Here is a summary of the versions of the tools tested:


**Tool**    |**Version**
------------|---------------
latex2html  |2008-2 (1.71)
latex2rtf   |2.3.3
Pandoc      |1.12.1
tex4ht      |2013.31548


The environment for testing was Arch Linux, up to date with packages as
of 2013-11-22. The word processors were LibreOffice 4.1.3 and OpenOffice
4.0.0.

Test case
---------

The test case involves common LaTeX features that I frequently use.
Crucial packages include amsmath, amssymb, graphicx, subfigure, url.
Less crucial packages are times, latexsym, microtype, todonotes, natbib,
hyperref, and multirow. Nagging and warnings are enabled to force me to
write crispy clean LaTeX code. By default, PDF version 1.4 is enforced.

Inline formulae should display fractions, subscripts and superscripts,
and mathematical symbols. The same applies to equations. Arrays should
also work in math environment.

Citations and cross-references should work without a hitch. External
Bibtex bibliography should be handled.

Figures and subfigures should work with both PNG and PDF images. The
vector graphic image in the test case was created with Inkscape, and it
was saved as PDF 1.4. Imagemagick generated the raster image without
specifying any option.

Basic tables should convert flawlessly. If multirow or multicolumn
tables convert, that is a great advantage.

Ridiculous as it is, I would expect file names to be arbitrary.
Unfortunately, on a 21st Unix system, several LaTeX-related tools will
complain if a file name contains multiple '.' characters. Accordingly,
the file names in the test case were kept simple.

The test case is available on
[GitHub](https://github.com/peterwittek/test-latex-converters). Tex4ht
will not work with the default LaTeX file, so a modified file is also
included. A script is added to generate the output with all the tools
outlined.

Results
-------

Before the tools were tested, LaTeX and Bibtex ran on the source files
to generate the auxiliary files. Several parameters were tested for each
tool. Only the best setting was included in the comparison.

Latex2html ran indefinitely: it did not terminate even after an hour.
Its output cannot be evaluated.

For Pandoc, OpenDocument, RTF, Office Open XML, and HTML outputs were
produced. They looked almost identical. Pandoc cannot include PDF
figures. Its mathematical formulae are mixed -- basic ones translate,
more or less. There is no sign of OMML support -- blank spaces are
inserted where OMML should be in the docx file. Complicated tables and
cross-references do not work.

With latex2rtf, all figures are correct, cross-references work.
Citations show only the Bibtex key. Only the simplest equations are
inlined. Multicolumn tables work.

As for mk4ht, explicit specification of PDF output confuses the parser.
The amsmath pmatrix and the basic array in math mode are
[out](http://tex.stackexchange.com/questions/42690/latex-to-odf-doc-using-mk4ht-oolatex-failing-on-equation-arrays)
by default, but adding an extra line in the preamble partially solves
the problem:

    :::latex
    \let\columnlines\empty

Opening and closing brackets will be the wrong size. Cross-references
work, the formulae are all there, they can even be edited. References
are also there. Neither the PNG nor the PDF figures show.

Htlatex has similar limitations to mk4ht, but ``pmatrix`` and ``array`` in math
mode work. PDF images are processed with ImageMagick if an extra
[configuration
file](http://tex.stackexchange.com/questions/46156/pdf-image-files-and-htlatex/46210#46210)
is supplied. By default, ugly horizontal bars surround tables and
figures; this needs [further
configuration](http://tex.stackexchange.com/questions/60912/how-to-remove-horizontal-lines-around-figures-for-htlatex-output).
Theoretically, MathML and MathJax would be a better option for HTML --
adding a few [more
lines](http://www.albany.edu/~hammond/demos/Html5/arXiv/) to the
configuration file should do this. Yet, since the final target is a
certain proprietary word processor, you are better off converting
everything to PNG.

The results are compared in the following table:


**Tool** | **PDF figs.** | **Inline math** | **Eqs.** | **Ams- symb** | **Ams- math** | **Cites** | **X-refs.** | **Multi table**
------------|---------------|-----------------|----------------|---------------|---------------|-----------|-------------|-----------------
latex2html | ? | ? | ? | ? | ? | ? | ? | ?
latex2rtf | Yes | Yes | Yes | Ugly | No | Yes | Yes | Yes
Pandoc | No | Partial | Basic | Ugly | No | Yes | No | No
mk4ht | No | Yes (editable) | Yes (editable) | Ugly | Ugly | Yes | Yes | Yes
htlatex | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes

LibreOffice could not open the RTF and ODT files. The flaw is probably
with this version of LibreOffice, and not with the tools, as all files
opened in OpenOffice.

Conclusions
-----------

Htlatex won out, but tinkering is still necessary. You must convert all
your vector images to a raster format. Then generate HTML, and open it
in a word processor. Theoretically this last conversion [could be
done](http://uce.uniovi.es/tips/Latex/HtLatexConfig.html) on the command
line with [unoconv](http://dag.wiee.rs/home-made/unoconv/), but I had no
luck. Ensure the images are embedded, and not referenced when you save
the file in a word processor format.

The damage done by word processors is irreversible. They will cripple
workflows for centuries to come. Smooth translation between the two
worlds will remain a dream. So long simplicity.

