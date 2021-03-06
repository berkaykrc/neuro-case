class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
class ProductionConfig(Config):
    SECRET_KEY=""
    DATABASE_URI = ''
class DevelopmentConfig(Config):
    ENV="development"
    SECRET_KEY=""
    DEBUG = True
class TestingConfig(Config):
    TESTING = True