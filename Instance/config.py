# configurations class
import os


class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'sweet-secret')


# development environment configurations
class DevelopmentConfig(Config):
    DEBUG = True


# testing environment configurations
class TestingConfig(Config):
    TESTING = True
    DEBUG = True


# staging environment configurations
class StagingConfig(Config):
    DEBUG = True


# production environment configurations
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


# configurations dictionary
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
