class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
class ProductionConfig(Config):
    SECRET_KEY=""
    DATABASE_URI = ''
class DevelopmentConfig(Config):
    ENV="development"
    SECRET_KEY="6ae4a778-a51a-4fda-9efa-a074d41fd768"
    DEBUG = True
class TestingConfig(Config):
    TESTING = True