import os
import sys


class BaseConfig(object):
    # 设置URI地址
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(16)
    # 

class DevConfig(BaseConfig):
    DEBUG = True


class ProConfig(BaseConfig):
    pass



config_map = {
    'dev': DevConfig,
    'pro': ProConfig
}