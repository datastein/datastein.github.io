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
#PLUGINS = ['ipynb.markup'] 

# THEMES: Here is me playing with a few themes

#Uncomment for Flex
#PLUGIN_PATH = './plugins'
#PLUGINS = ['ipynb.markup']
#THEME = 'Flex'
#STATIC_PATHS = ['img']

#AUTHOR = 'Jeanette Stein'
#SITEURL = 'https://datastein.github.io'
#SITENAME = 'Jeanette\'s Data Blog'
#SITETITLE = 'Jeanette\'s Data Blog'
#SITESUBTITLE = 'Blogging in Seattle'
#SITEDESCRIPTION = 'Jeanette\'s Thoughts and Writings'
#SITELOGO = SITEURL + '/img/JS_profile.png'
##SITELOGO = SITEURL + '/images/JS_profile.png'
#BROWSER_COLOR = '#1569C7'

#SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mjeanettestein/'),
#         ('github', 'https://github.com/datastein'))


THEME = 'attila'
PLUGINS = [

  'sitemap',

  'neighbors',

  'assets'

]



# Sitemap

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
### Theme specific settings
# To set background image for the home page.

HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'



# Custom Header



HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}



AUTHORS_BIO = {

  "zutrinken": {

    "name": "Zutrinken",

    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",

    "image": "img/Seattle_Skyline_F.jpg",

    "website": "https://datastein.github.io",

    "linkedin": "unavailable",

    "github": "arulrajnet",

    "location": "Chennai",

    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"

  }

}



COLOR_SCHEME_CSS = 'github.css'



CSS_OVERRIDE = ['assets/css/myblog.css']



# Jinja config - Pelican 4

JINJA_ENVIRONMENT = {

  'extensions' :[

    'jinja2.ext.loopcontrols',

    'jinja2.ext.i18n',

    'jinja2.ext.with_',

    'jinja2.ext.do'

  ]

}



JINJA_FILTERS = {'max': max}
