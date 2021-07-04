import os
import sys


class BaseConfig(object):
    # 设置URI地址
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 

class DevConfig(BaseConfig):
    DEBUG = True


class ProConfig(BaseConfig):
    pass



config_map = {
    'dev': DevConfig,
    'pro': ProConfig
}