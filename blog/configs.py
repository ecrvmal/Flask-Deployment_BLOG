import os
from dotenv import load_dotenv
from sqlalchemy.dialects import postgresql

from blog.enums import EnvType


load_dotenv()
ENV = os.getenv('FLASK_ENV', default=EnvType.production)
API_URL = os.getenv('API_URL')


class BaseConfig(object):
    DEBUG = False
    # DEBUG = ENV == EnvType.development
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'postgres://user:CDu8F1LcFO42KbqGbyRVcBKXFYaE9h50@dpg-ch5sff4s3fvuobaiaun0-a/db_lj4s'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'z#if^%-_2j9o9*tjxn(^c3k(#q_gonx^nyf6m7_=$x@y&kqw2r'
    FLASK_ADMIN_SWATCH = "cerulean"
    OPENAPI_URL_PREFIX = '/api/docs'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
    API_URL = os.getenv('API_URL')


class DevConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'postgres://user:CDu8F1LcFO42KbqGbyRVcBKXFYaE9h50@dpg-ch5sff4s3fvuobaiaun0-a/db_lj4s'
    API_URL = os.getenv('API_URL')


class TestConfig(BaseConfig):
    TESTING = True
    API_URL = os.getenv('API_URL')


class ProductionConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_URI = 'postgres://user:CDu8F1LcFO42KbqGbyRVcBKXFYaE9h50@dpg-ch5sff4s3fvuobaiaun0-a/db_lj4s'
    DEBUG = False
    TESTING = False
    API_URL = os.getenv('API_URL')







