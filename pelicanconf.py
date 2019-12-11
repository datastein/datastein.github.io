#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeanette Stein'
SITENAME = u'My Data Science Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['img', 'pdf']

MARKUP = ('md', 'ipynb') 

PLUGIN_PATH = './plugins' 
PLUGINS = ['ipynb.markup'] 

# THEMES: Here is me playing with a few themes

#Uncomment for Flex
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
THEME = 'Flex'
STATIC_PATHS = ['img']

AUTHOR = 'Jeanette Stein'
SITEURL = 'https://datastein.github.io'
SITENAME = 'Jeanette\'s Data Blog'
SITETITLE = 'Jeanette\'s Data Blog'
SITESUBTITLE = 'Blogging in Seattle'
SITEDESCRIPTION = 'Jeanette\'s Thoughts and Writings'
SITELOGO = SITEURL + '/img/JS_profile.png'
#SITELOGO = SITEURL + '/images/JS_profile.png'
BROWSER_COLOR = '#1569C7'

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mjeanettestein/'),
          ('github', 'https://github.com/datastein'))
