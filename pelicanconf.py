#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rodrigo Oliveira'
SITENAME = 'Rodrigo Oliveira'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Bahia'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

PLUGINS=['pelican.plugins.simple_footnotes']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'brutalist'
FIRST_NAME = 'Rodrigo Oliveira'
ATTRIBUTION = True
STATIC_PATHS = ['img']
