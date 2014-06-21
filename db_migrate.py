#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imp
from migrate.versioning import api
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

with open(migration, 'wt') as f:
    f.write(script)

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as {0}'.format(migration))
print('Current database version: {0}'.format(str(api.db_version(SQLALCHEMY_DATABASE_URI,\
        SQLALCHEMY_MIGRATE_REPO))))

