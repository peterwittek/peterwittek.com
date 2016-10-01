Title: Migrating an academic website from Wordpress to Pelican
Date: 2014-12-28 16:59
Author: Peter
Category: Academic publishing
Tags: Academic publishing, Python
Slug: academic-website-with-pelican
Summary: In pursuit of open science, academics should blog. As good nerds, they should opt for static website generators. Pelican is a great option, but caveats apply.

*Update: The source code of my website is [available on GitHub](https://github.com/peterwittek/peterwittek.com).*

I am a firm believer of the openness of science, which is also the reason why I blog about issues I encounter during my work. My website used Wordpress for two years, but I figured that using a static website generator would be a more elegant solution that would make it easier for me to write and publish posts.

Reasons
-------

I contemplated the move for a long time as I felt increasingly unhappy with Wordpress for the following reasons:

1. Wordpress is not great for academic writing. The MathJax plugin was giving me pain. Papercite is great for generating a list of papers, but when I was using it to generate the bibliography of individual articles -- aka Bibtex -- it was horribly slow. At some point, I switched to using Pygments and inserted formatted code in HTML, making revisions of posts difficult. IPython notebooks were difficult to integrate. So I ended up writing fewer mathematical formulas, avoiding code snippets, and having ten different forms of referencing across articles.
2. From the log files, I could see that my Wordpress installation was under constant attack. I minimized the number of plugins used to reduce potential vulnerabilities. Login to the Wordpress Admin panel was insecure, as I never wanted to learn how to set up a certificate, but this was a major weakness.
3. I craved for using git. The content here is neither peer-reviewed nor cast in stone. If I discover a mistake in an older post, I correct it. To make the revisions transparent, git would be great.

So to make myself write more and in a consistent style, to minimize attack surface, and to have a transparent version control system, I decided to try a static site generator.

Static site generators
----------------------

While the world experiences shortages of water, food, love and caring, nobody can complain about the sheer amount of static site generators. After a quick look at the [statistics](https://staticsitegenerators.net/), the choice boiled to two options, [Jekyll](http://jekyllrb.com/) and [Pelican](http://docs.getpelican.com/). Jekyll is in Ruby and Pelican is in Python -- I harbour an old hostility towards Ruby and I am already familiar with Python. Moreover, the Jekyll packages were orphaned in my distribution's repository, so right from the start I focused on Pelican.

Posts are written in Markdown, which is the second best thing after LaTeX. Importing all the content from Wordpress was ridiculously easy. An export option hides under Tools in the Wordpress control panel, which exports everything in a single XML file. Pelican has an import script that magically converts everything to the correct Markdown files, including metadata:

    :::bash
    $ pelican-import -m markdown --wpfile -o ./content ./content.xml

The XML file also contains the comments, but the conversion won't include them.

After rearranging the files into pages and posts, I initialized git and pushed the content to [GitHub](https://github.com/peterwittek/peterwittek.com). Version control was working from here, and sources were made open, as they should be. While I was at it, I read up on licenses on content. I always choose GPLv3 for code -- I believe this is the best for academic software -- and I found a good match for content in [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

Mathematical formulas and syntax highlighting
---------------------------------------------
Syntax highlighting worked magically. I did not have to do anything to get it work. MathJax required a [plugin](https://github.com/getpelican/pelican-plugins/tree/master/render_math), but then it worked just fine. Javascript is, of course, necessary to render the formulas, so extreme privacy freaks will be unhappy.

IPython support is more difficult, but it would be important to promote [literate programming]({filename}/reproducible-research-literate-programming-ipython-and-github.md). Theoretically you can add an IPython notebook, and it processed the same way as the rest of the content, the corresponding HTML is rendered when the site is generated. This, however, is a flawed process. [Pandoc](http://johnmacfarlane.net/pandoc/) is necessary, and I have mixed experiences using it. I ended up [forking](https://github.com/peterwittek/pelican-ipynb) the pelican-ipynb plugin repository to get the summary metadata field correct and to have better support for MathJax. Node.js should not be installed when using the plugin. The solution is still not perfect, but I am not a CSS wizard to sort out the remaining visual issues, nor I want to become one. The result looks okay on a laptop screen and bad on a phone.

The hardest part: bibliography and references
---------------------------------------------
This took me a day to work out. I love Bibtex and preferably I would like to use the same single database when writing for this blog as when writing a paper, with the same convenience as in LaTeX. Not so fast. I divide the issue into two separate parts: generating a list of references as in my publication list, and creating a bibliography as in an article.

The first one is actually harder. I ended up using [Bibtex2html](https://www.lri.fr/~filliatr/bibtex2html/), an ugly series of ``sed``-s, and Pandoc. It works except when it does not. The script is as follows:

    :::bash
    #!/bin/bash
    years="2014 2013 2012 2011 2010 2009 2008 2007"
    rm processed.html
    for year in $years; do
        bib2bib -oc cite${year} -ob ${year}.bib -c "year=${year}" mybibliography.bib
        bibtex2html --no-keywords --no-abstract --no-header --nobibsource --sort-by-date --reverse-sort -dl -f code -f slides -f web -nodoc -citefile cite${year} ${year}.bib
        echo "<h2>${year}<h2>" >> processed.html
        cat ${year}.html | sed -e 's/>bib</><img src="images\/bibtex\.png" alt="[BIBTEX]"></'|sed -e 's/\.pdf<\/a>/<img src="images\/pdf\.png" alt="[PDF]"><\/a>/'|sed -e 's/DOI<\/a>/<img src="images\/doi\.png" alt="[DOI]"><\/a>/'|sed -e 's/github\(.*\)http/github\1<img src="images\/github\.png" alt="[GitHub]">/'|sed -e 's/slideshare\(.*\)http/slideshare\1<img src="images\/slideshare\.jpg" alt="[Slides]">/'|sed -e 's/>http</><img src="images\/external\.png" alt="[Link]"></'|sed -e 's/\[&nbsp;/<br>/'|sed -e 's/|//' |sed -e 's/&nbsp;]//'|sed -e 's/<dl>/<ul>/'|sed -e 's/<\/dl>/<\/ul>/'|sed -e 's/.*dt>.*//'|sed -e 's/<dd>/<li>/'|sed -e 's/<\/dd>/<\/li>/'|sed -e 's/\[[0-9]*\]//'|sed -e 's/<hr><p><em>This file was generated by//'|sed -e 's/<a href="http:\/\/www\.lri\.fr.*//'|uniq >> processed.html
        rm *${year}*
    done
    pandoc -f html -t markdown_github processed.html > publications.md

Compared to this, configuring the [Papercite plugin](https://wordpress.org/plugins/papercite/) of Wordpress is a breeze.

As for the articles, Pandoc can process [@bibkey] entries in the Markdown text the same way as LaTeX and Bibtex would do. The trick here is that you should tell Pandoc that the output Markdown is a different flavour than the input:

    :::bash
    $ pandoc --bibliography bibliography.bib -f markdown -t markdown_strict input.md > output.md

This does not parse the eprint links and capitalizes arXiv, so I follow it up by a one-liner:

    :::bash
    cat output.md|sed -e 's/ArXiv:\(.*\)\*/\[arXiv:\1\](http:\/\/arxiv.org\/abs\/\1)\*/'

If you miss one entry, it is a pain to do the process again.

The nasty aspect of the solution is that this conversion should be invoked on the fly, just before the HTML files are generated. The module [Pyandoc](https://github.com/kennethreitz/pyandoc) should help setting up a hook from Python, but so far I could not be bothered. Another problem is internal href-s from the point of the reference to the citation are not added. This would require preprocessing and postprocessing the Markdown files around Pandoc. One day I will do that. Till then, citations in Markdown remain inconvenient.

Comments and sharing
--------------------
My posts are not flooded with comments, but I appreciate the few that I receive. Static sites by definition cannot have a dynamic comments section. I briefly contemplated using [Discourse](http://discourse.org/), but it was way beyond what I needed, especially since I am on a cheap shared webhost, which would make deployment a true challenge. I dismissed [Juvia](https://github.com/phusion/juvia) on the same grounds. Disqus was not an option, since I do not want my readers to be exposed to commercial espionage.

Pelican has some static comments plugins that send an email to me when somebody wants to post a comment, but it is impossible to go down this path without exposing my email address in the wild. My inbox is already overflowing with spam.

Apparently, I am [not the only one](http://dumbmatter.com/2011/08/jekyll-and-other-static-site-generators-are-currently-harmful-to-the-free-open-source-software-movement/) concerned about comments and static sites. Then, reading through a [thread on Hackernews](https://news.ycombinator.com/item?id=4859094), I figured that any kind of self-hosted comment system is redundant, unless you are [Daniel Lemire](http://lemire.me/blog/). So I decided to do away with comments, cherish and archive the ones I already have -- all twenty of them -- and improve the sharing options of my posts.

Previously sharing was limited to copying the URL from the address bar. Clearly there was room for improvement. In the new version, I mainly relied on the [share_post](https://github.com/getpelican/pelican-plugins/tree/master/share_post) plugin, which I extended to include LinkedIn, using these [advices](http://daniemon.com/blog/static-social-media-share-buttons/).

As a good theoretician, I never use any of these services to share anything, so I have no clue of their practical relevance. I briefly considered adding a submit to HackerNews button -- a site I actually read -- but my chances of getting on it are about as high as being published in Nature.

The share buttons are completely ordinary hyperlinks without any tracking feature. This way I leave it to the readers how much they want to compromise their privacy and by what means.

Link structure and sitemap
--------------------------
My posts had long links that included the year and month of posting, which were redundant. I simplified the structure. Given that the site URL is already twenty-three characters, saving those seven characters was important. In the new structure, a post's URL ends with .html, which is four characters longer then the single slash in Wordpress. We are still looking at a net saving of three characters.

Since some of my posts got highly ranked in search results, one or two were even linked from elsewhere, preserving the link structure was important. A bash one-liner parsed the old sitemap.xml, and converted into a .htaccess file to redirect old links to the new ones.

I generate the new sitemap with a Pelican [plugin](https://github.com/getpelican/pelican-plugins/tree/master/sitemap).

Publishing new posts and updates
--------------------------------
This is my favourite part. For this alone, the conversion was worthwhile. I no longer have to rely on insecure login, Javascript-based editor, and the rest of the Wordpress misery. Once I have a new post finished, I move it to the content directory, and issue

    :::bash
    make rsync_upload

It is magical. The rsync part had to be tweaked to make it work, as my shared webhost does not allow ssh. I mount a Webdav directory and to the syncing on the local filesystem. My webhost uses CPanel and it was trivial to add Webdav access -- the menu item is called Web Disk. To mount this folder by a user, I added a line to fstab:

    :::bash
    https://shared.hostname.net:dav_port /mnt/webdav davfs user,noauto 0 0

I store the username and password in ``~/.davfs2/secrets``. Then I replaced the relevant lines in the default Pelican Makefile to this:

    :::makefile
    rsync_upload: publish
      mount /mnt/webdav
      rsync -P -vrz --cvs-exclude --size-only --no-whole-file --inplace output/ /mnt/webdav
      umount /mnt/webdav

Notice the ``--size-only`` restriction. This means that a file is copied if and only if its size is different at the target destination. The restriction is due to a limitation in the Webdav implementation, and I'd better not forget it when I make changes that do not influence the size of the output HTMLs.

Conclusions
-----------
The whole process took me a lot longer than I am willing to admit. I gained a slightly better insight on web technologies and I appreciate even more that I do not have to make a living as a web developer. Markdown sources, version control, and an rsync-based secure publishing process make me happy.

I must account for the things lost in the process:

1. Comments are gone as I could not find an easy, non-spying third-party alternative.
2. Pings and trackbacks are also gone. Without a comment section, it is not surprising.
3. Easy traffic statistics are gone. In Wordpress, I used the [Popular Posts plugin](https://wordpress.org/plugins/wordpress-popular-posts/). It was great to generate a list of posts on the sidebar that would help the visitors discover more content. I also used it to generate hidden pages with the monthly and daily statistics of all posts for my own analytical pleasure. Now I have to figure a way to parse either the raw log files or the daily output of Awstats. With Webdav and a few lines of Python or shell code, it should not be too hard, but I have not got around it yet.

So all in all, it is not too bad. I like Pelican, but if I knew how much time it would take me to go through the migration, I would not have started it.
