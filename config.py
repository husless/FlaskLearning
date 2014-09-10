# -*- coding: utf-8 -*-
CSRF_ENABLED = True
SECRET_KEY = "you-son-of-bitch"

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_RECORD_QUERIES = True

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'https://api.screenname.aol.com/auth/openid/name/<username>' },
    ]

# mail server settings
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'samhus@163.com'
MAIL_PASSWORD = '123456mnbv'

# administrator list
ADMINS = ['samhus@163.com', 'systmdenable@aol.com']

# pagination
POSTS_PER_PAGE = 5

# full text search
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

# available languages
LANGUAGES = {
    'en': 'English',
    'cn_zh': 'Simplified Chinese',
    'cn_tw': 'Traditional Chinese',
    }

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = '0xsystmd'
MS_TRANSLATOR_CLIENT_SECRET = 'n6HwS6G28TCGOVcst53N6xE+WkApAycmFBPreRepcGc=' 
