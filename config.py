# coding=utf-8
# FIXME: 加入开发时和发布时的不同配置
#
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'W8%*bq9TvEXECR~A.3J4Zqmq'

# i18n config
LANGUAGES = {
    'en': 'English',
    'zh': 'Simplified Chinese'
}
BABEL_DEFAULT_LOCALE = 'zh'

# database config
# FIXME: 将相关配置转移到instance/config.py中
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
