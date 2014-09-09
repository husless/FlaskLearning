<<<<<<< HEAD
#!flask/bin/python
=======
#!/usr/bin/env python
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b
# -*- coding: utf-8 -*-

import imp
from migrate.versioning import api
<<<<<<< HEAD
from app import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

migration = SQLALCHEMY_MIGRATE_REPO + '/versions/{0:0>3d}_migration.py'.format(
        api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)+1)

tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec old_model in tmp_module.__dict__
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
        tmp_module.meta, db.metadata)
=======
from flaskr import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

migration = SQLALCHEMY_MIGRATE_REPO + '/versions/{:03d}_migration.py'.format(
    api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1)

tmp_model = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

exec old_model in tmp_model.__dict__

script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, \
    SQLALCHEMY_MIGRATE_REPO, tmp_model.meta, db.metadata)
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b

with open(migration, 'wt') as f:
    f.write(script)

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
<<<<<<< HEAD

print('New migration saved as {}'.format(migration))
print('Current database version: {}'.format(api.db_version(SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO)))
=======
print('New migration saved as {0}'.format(migration))
print('Current database version: {0}'.format(str(api.db_version(SQLALCHEMY_DATABASE_URI,\
        SQLALCHEMY_MIGRATE_REPO))))
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b

