import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 邮箱相关设置
    SECRET_KEY = os.environ.get("SECRET_KEY") or " guess something"
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.163.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", '110'))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "true").lower() in ['true', 'on', 1]
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT_PREFIX = "[blog]"
    MAIL_SENDER = "blog Admin <blog@example.com>"
    ADMIN = os.environ.get("ADMIN")
    
    # db不跟踪动态更改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    
class TestingConfig(Config):
    """测试环境"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite://"
        
class ProductionConfig(Config):
    """生产环境"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data.sqlite")
    
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    
    "default": DevelopmentConfig
}
