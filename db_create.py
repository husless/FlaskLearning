<<<<<<< HEAD
#!flask/bin/python
# -*- coding: utf-8 -*-

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import db
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from flaskr import db
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b
import os

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
<<<<<<< HEAD
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
        api.version(SQLALCHEMY_MIGRATE_REPO))
=======
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,\
            api.version(SQLALCHEMY_MIGRATE_REPO))
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b

