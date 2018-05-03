import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Class ... """
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = 'very_secret_key_but_needs_2_b_changed'


class ProductionConfig(Config):
    """docstring for ."""
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
