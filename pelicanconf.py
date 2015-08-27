#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Peter Hsieh'
SITENAME = u"Peter's Coding Notes"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

DEFAULT_DATE_FORMAT = ('%b %d %Y')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SUMMARY_MAX_LENGTH = 100
THEME = 'themes/pelican-bootstrap3'
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True