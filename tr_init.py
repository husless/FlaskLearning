#!flask/bin/python
# -*- coding: utf-8 -*-

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'
if len(sys.argv) != 2:
    print("usage: tr_init <language-code>")
    sys.exit(1)
os.system('{0} extract -F babel.cfg -k lazy_gettext -o messages.pot app'.format(pybabel))
os.system('{0} init -i messages.pot -d app/translations -l {1}'.format(pybabel, sys.argv[1]))
os.unlink('messages.pot')
