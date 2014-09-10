#!flask/bin/python
# -*- coding: utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
os.system('{0} extract -F babel.cfg -k lazy_gettext -o messages.pot app'.format(pybabel))
os.system('{0} update -i messages.pot -d app/translations'.format(pybabel))
os.unlink('messages.pot')
