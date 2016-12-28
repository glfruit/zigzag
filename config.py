
## TODO: 加入开发时和发布时的不同配置
from zigzag import app

#
WTF_CSRF_ENABLED = True
SECRET_KEY = 'W8%*bq9TvEXECR~A.3J4Zqmq'

# flask uploads config
UPLOAD_FOLDER = app.instance_path

# i18n config
LANGUAGES = {
    'en': 'English',
    'zh': 'Simplified Chinese'
}
BABEL_DEFAULT_LOCALE='zh'
