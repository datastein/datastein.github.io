#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeanette Stein'
SITENAME = u'My Data Science Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'En'

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
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mjeanettestein/'),
         ('github', 'https://github.com/datastein'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['img', 'pdf']

MARKUP = ('md', 'ipynb') 

PLUGIN_PATH = './plugins' 
#PLUGINS = ['ipynb.markup'] 

# THEMES: Here is me playing with a few themes

##Uncomment for Flex
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
#SITELOGO = '/img/SNLogo.jpg'
#FAVICON = '/img/JS_profile.png'
##SITELOGO = SITEURL + 'pelican/img/JS_profile.png'
##SITELOGO = SITEURL + '/images/JS_profile.png'
#BROWSER_COLOR = '#1569C7'

#***************************************
# Theme Attila
#***************************************


PAGINATION_PATTERNS = (

    (1, '{base_name}/', '{base_name}/index.html'),

    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),

)


# Post and Pages path

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_URL = 'pages/{slug}/'

PAGE_SAVE_AS = 'pages/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'


# Tags and Category path

CATEGORY_URL = 'category/{slug}'

CATEGORY_SAVE_AS = 'category/{slug}/index.html'

CATEGORIES_SAVE_AS = 'catgegories.html'

TAG_URL = 'tag/{slug}'

TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_SAVE_AS = 'tags.html'



# Author

AUTHOR_URL = 'author/{slug}'

AUTHOR_SAVE_AS = 'author/{slug}/index.html'

AUTHORS_SAVE_AS = 'authors.html'



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

HOME_COVER = '/img/Sea_Sky.jpg'
AUTHORS_BIO = {

  "Stein": {

    "name": "Stein",

    "cover":  '/img/Sea_Sky.jpg',

    "image": '/img/JS_profile.png',

    "website": "https://datastein.github.io/",

    "linkedin": "unavailable",

    "github": "datastein",

    "location": "Seattle",

    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"

  }

}