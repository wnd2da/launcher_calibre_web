# -*- coding: utf-8 -*-
#########################################################
# python
import os
import traceback
import json

# third-party

# sjva 공용
from framework.logger import get_logger
from framework import db, app, path_app_root
# 패키지
from .plugin import package_name, logger


if app.config['config']['run_by_real']:
    db_file = os.path.join(path_app_root, 'data', 'db', '%s.db' % package_name)
    app.config['SQLALCHEMY_BINDS'][package_name] = 'sqlite:///%s' % (db_file)


class ModelSetting(db.Model):
    __tablename__ = 'plugin_%s_setting' % package_name
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    __bind_key__ = package_name

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.String, nullable=False)
 
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return repr(self.as_dict())

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

#########################################################

