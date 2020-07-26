#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter W Setter'
SITENAME = 'Error Log'
#SITETAGLINE = ''
SITEURL = ''
#FOOTERTEXTcd p
THEME = '../pelican-themes/cebong'

PATH = 'content'

TIMEZONE = 'America/Denver'

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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/peterwsetter'),)
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#DEFAULT_METADATA = {"yeah" : "it is"}

STATIC_PATHS = [
    'static'
]

ARTICLE_PATHS = ['posts']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True