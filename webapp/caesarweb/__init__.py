#coding:utf-8
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')   # 从settings.py中导入设置
# 去除jinja模板中的空白行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

try:
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)
except:
    pass

from CaesarWeb import views


