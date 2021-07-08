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

    # 配置会话信息
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 60*60

    SESSION_FILE_DIR = './session' 
    SESSION_FILE_THRESHOLD = 500  # 存储session的个数如果大于这个值时，就要开始进行删除了
    SESSION_USE_SIGNER = True   #  是否对发送到浏览器上session的cookie值进行加密
    # SESSION_PERMANENT = True    # 如果设置为False，则关闭浏览器session就失效。
    SESSION_KEY_PREFIX = 'session'


class ProConfig(BaseConfig):
    pass



config_map = {
    'dev': DevConfig,
    'pro': ProConfig
}