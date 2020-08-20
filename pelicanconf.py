#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter W Setter'
SITENAME = 'peterwsetterdotcom'
SITEURL = ''
SITETITLE = "Peter W Setter"
#SITESUBTITLE = "Web Developer"
#SITEDESCRIPTION = "Foo Bar's Thoughts and Writings"
SITELOGO = "/static/img/peterwsetter_profile.jpg"

ROBOTS = "index, follow"

PATH = 'content'
ARTICLE_PATHS = ['blog']
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['static']

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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/peterwsetter'),
          #('Another social link', '#'),
           )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/Flex'

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = "UA-1234-5678"

#MENUITEMS = (
#    ("Archives", "/archives.html"),
#    ("Categories", "/categories.html"),
#    ("Tags", "/tags.html"),
#)