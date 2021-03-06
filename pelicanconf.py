#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Wittek'
SITENAME = 'Peter Wittek'
SITEURL = 'http://peterwittek.com'
DELETE_OUTPUT_DIRECTORY = False
RELATIVE_URLS = True

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
SOCIAL = (
#         ('ResearchGate', 'http://www.researchgate.net/profile/Peter_Wittek'),
#         ('Google Scholar', 'http://scholar.google.com/citations?user=tEd_agoAAAAJ'),
          ('GitHub', 'https://github.com/peterwittek'),
          ('LinkedIn', 'https://www.linkedin.com/in/peterwittek/'),
#         ('SlideShare','https://www.slideshare.net/peter_wittek'),
          ('Email','http://scr.im/3xuo'),
          )

MARKUP = ('md', 'ipynb')
DEFAULT_PAGINATION = 1000
DISPLAY_CATEGORIES_ON_MENU = False
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'order'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'blog.html'
STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {
    'static/.htaccess': {'path': '.htaccess'},
    }
AUTHOR_SAVE_AS = ''
#TYPOGRIFY = False
#TYPOGRIFY_IGNORE_TAGS = ['a']

# Plugin-related settings
PLUGIN_PATHS = ['../pelican_plugins']
IPYNB_USE_META_SUMMARY = True
PLUGINS = ['feed_summary', 'ipynb.markup', 'render_math', 'share_post', 'sitemap']
FEED_USE_SUMMARY = True
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme-related settings
THEME = 'themes/octopress-simplegrey'
