from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session


db = SQLAlchemy()
session = Session()

def create_app(config_name):
    # 工厂模式
    app = Flask(__name__)
    app.config.from_object(config_map.get(config_name))

    # 绑定插件
    db.init_app(app)
    session.init_app(app)
    # CSRFProtect(app)

    # 注册蓝图
    from watchlist.views import bp_index,bp_edit
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_edit)
    
    return app