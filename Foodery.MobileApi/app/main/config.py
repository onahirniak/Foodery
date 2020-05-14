import os

# uncomment the line below for postgres database url from environment variable
mysql_local_base = os.getenv('DATABASE_URL') 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class LocalConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = mysql_local_base or 'mysql+pymysql://root:password@localhost:3306/foodery'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = "34a1271dcc3b4ef992eaadbb367a1de4"
    SPOONACULAR_BASE_URL = "https://api.spoonacular.com"

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = mysql_local_base or 'mysql+pymysql://admin:Longpassword!@dev-foodery.cgwhc8ydmgbf.us-west-2.rds.amazonaws.com/foodery'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = "34a1271dcc3b4ef992eaadbb367a1de4"
    SPOONACULAR_BASE_URL = "https://api.spoonacular.com"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = mysql_local_base or 'mysql+pymysql://root:password@localhost:3306/foodery_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = "34a1271dcc3b4ef992eaadbb367a1de4"
    SPOONACULAR_BASE_URL = "https://api.spoonacular.com"


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    #SQLALCHEMY_DATABASE_URI = mysql_local_base or 'mysql+pymysql://root:password@localhost:3306/foodery'


config_by_name = dict(
    local=LocalConfig,
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY