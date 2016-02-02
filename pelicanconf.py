#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark' 
SITENAME = u'Keep Coding'
#SITESUBTITLE = u'My blood will never run cold.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
        ('ICRC', 'https://www.icrc.org/'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/profile.php?id=100011152545986'),
        ('github','https://github.com/MarkWh1te'),
        ('twitter', 'https://twitter.com/markw1te'))

DEFAULT_PAGINATION = 4
DISQUS_SITENAME = "markwh1te"
GITHUB_URL = 'https://github.com/MarkWh1te'
THEME = "/home/mark/pelican-themes/pelican-blue"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#page
DISPLAY_CATEGORIES_ON_MENU = True
#TIMEZONE
DEFAULT_DATE = 'fs'
#sidebar
SIDEBAR_DIGEST = 'programming reading & sporting!'
FAVICON = 'http://7xq2dq.com1.z0.glb.clouddn.com/Letter-M-blue-icon.png'
MENUITEMS = (('Blog','http://markwh1te.github.io'),
            ('category','http://markwh1te.github.io/categories.html'),
            ('archives','http://markwh1te.github.io/archives.html'))
