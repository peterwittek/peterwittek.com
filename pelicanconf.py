#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Wittek'
SITENAME = 'Peter Wittek'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/peterwittek'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_ORDER_BY = 'date'
PAGE_ORDER_BY = 'order'
AUTHOR_SAVE_AS = ''
THEME = 'notmyidea'
#INDEX_SAVE_AS = 'blog.html'
MENUITEMS = [('Blog', '/')]
THEME = 'pelican-octopress-theme'
