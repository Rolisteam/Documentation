#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "''"
SITENAME = 'Documentation'
SITEURL = 'http://localhost:8000'

PATH = 'content'
STATIC_PATHS = ['iconfiles', 'images']

PLUGIN_PATHS = ['plugins','plugins/pelican-toc']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = "rolisteam_doc_theme"
# bootstrap*
# bricks* red to blue
# Flex
# gum
# notebook
# notmyidea-cms
# pelican-blue
# plumage
# tuxlite_tbs

# JINJA_ENVIRONMENT = {
#    "extensions": ['jinja2.ext.i18n'],
# }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Blogroll
LINKS = (('Connection Test', 'https://rolisteam.org/php/test_ip.php'),)

# Social widget
SOCIAL = (
    ('Github', 'http://github.com/Rolisteam'),
    ('Facebook', 'https://www.facebook.com/rolisteam'),
    ('Twitter', 'https://twitter.com/rolisteam'),
    ('Discord', 'https://discord.gg/MrMrQwX'),
    ('Liberapay', 'https://liberapay.com/rolisteam/donate'),
    ('Patreon', 'https://www.patreon.com/rolisteam'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.tables': {},
        'mdx_video': {},
        #      'markdown.extensions.toc': {'permalink': True},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
    'extentions': ['toc', 'codehilite', 'tables'],
}

MENUITEMS = (
    ('Rolisteam', 'http://www.rolisteam.org/'),
    ('Forum', 'http://forum.rolisteam.org'),
)
# THEME_STATIC_PATHS (['static'])

PLUGINS = ['pelican-toc']

TOC = {
    'TOC_HEADERS': '^h[1-2]',
    'TOC_RUN': 'true',
    'TOC_INCLUDE_TITLE': 'false',
}
I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'Documentation',
        'THEME': 'rolisteam_doc_theme',
        'LINKS': ()
    }
}
