<<<<<<< HEAD
#!flask/bin/python
# -*- coding: utf-8 -*-

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: {}'.format(api.db_version(SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO)))
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('Current database version: {0}'.format(str(api.db_version(SQLALCHEMY_DATABASE_URI,\
        SQLALCHEMY_MIGRATE_REPO))))
>>>>>>> 3dc8f7d140153de7b99aa2add9964d39eb54f57b
