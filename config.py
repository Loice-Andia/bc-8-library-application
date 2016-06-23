import os
basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['DATABASE_URL'] = " postgres://ogctcvdfnhzxgh:2GzlGaS0rNu3bYVDwCUfYrsGBi@ec2-23-21-235-126.compute-1.amazonaws.com:5432/d8oo4j48fpnfp2"


class Config:
    '''This base class contains configuration
    that is common in all environments
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'loloaloki'

    @staticmethod
    def init_app(app):
        pass


class DevelopementConfig(Config):
    '''This class configures the development
    environment properties
    '''
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    '''This class cofigures the production
    environment properties
    '''
   
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False


config = {
    'development': DevelopementConfig,
    'production': ProductionConfig,
    'default': DevelopementConfig
}
