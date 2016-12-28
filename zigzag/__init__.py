import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask

#TODO: 根据http://www.cnblogs.com/txw1958/archive/2011/10/21/2220636.html重构日志初始化代码
app = Flask(__name__)
app.config.from_object('config')
handler = TimedRotatingFileHandler('zigzag.log', when = 'd', backupCount = 1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

from zigzag import views, models