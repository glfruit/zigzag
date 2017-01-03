# coding=utf-8
#FIXME: 加入开发时和发布时的不同配置
from zigzag import app

# 模板内容更改时自动加载
TEMPLATES_AUTO_RELOAD = True

#
WTF_CSRF_ENABLED = True
SECRET_KEY = 'W8%*bq9TvEXECR~A.3J4Zqmq'

# database config
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# flask uploads config
UPLOAD_FOLDER = app.instance_path

# i18n config
LANGUAGES = {
    'en': 'English',
    'zh': 'Simplified Chinese'
}
BABEL_DEFAULT_LOCALE='zh'
