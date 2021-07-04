from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


db = SQLAlchemy()


def create_app(config_name):
    # 工厂模式
    app = Flask(__name__)
    app.config.from_object(config_map.get(config_name))

    # 绑定插件
    db.init_app(app)

    from watchlist.views import bp_index
    app.register_blueprint(bp_index)
    
    return app