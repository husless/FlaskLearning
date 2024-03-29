#!flask/bin/python
# -*- coding: utf-8 -*-
from werkzeug.contrib.profiler import ProfilerMiddleware
from app import app

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions = [30])
app.run('0.0.0.0',debug = True)
