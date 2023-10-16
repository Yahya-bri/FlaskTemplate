import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base config class."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    LOGIN_DISABLED = False
    ENV = 'development'
    DEBUG = True