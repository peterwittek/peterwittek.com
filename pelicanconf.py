#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Wittek'
SITENAME = 'Peter Wittek'
SITEURL = 'http://peterwittek.com'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('ResearchGate', 'http://www.researchgate.net/profile/Peter_Wittek'),
          ('Scholar', 'http://scholar.google.com/citations?user=tEd_agoAAAAJ'),
          ('LinkedIn', 'https://sg.linkedin.com/in/peterwittek'),
          ('GitHub', 'https://github.com/peterwittek'),
          ('SlideShare','https://www.slideshare.net/peter_wittek'),
          ('Email','/email-instructions.html'),
          )

DEFAULT_PAGINATION = 1000

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_ORDER_BY = 'date'
PAGE_ORDER_BY = 'order'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'blog.html'
STATIC_PATHS = ['images']
AUTHOR_SAVE_AS = ''

# Plugin-related settings
PLUGIN_PATHS = ['../pelican_plugins']
PLUGINS = ['ipynb', 'render_math', 'bibtex']

# Theme-related settings
THEME = 'themes/octopress-simplegrey'
#THEME = 'pelican-octopress-theme'
