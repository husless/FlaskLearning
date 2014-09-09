#!flask/bin/python
# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app, bindAddress='/tmp/microblog-fcgi.sock', umask=73).run() #umask is decimal, not oct.
