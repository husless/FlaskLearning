#!flask/bin/python
# -*- coding: utf-8 -*-
import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
os.system('{0} compile -d app/translations'.format(pybabel))
