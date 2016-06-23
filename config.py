import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    '''This base class contains configuration
    that is common in all environments
    '''
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'loloaloki'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopementConfig(Config):
    '''This class configures the development
    environment properties
    '''
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    


class ProductionConfig(Config):
    '''This class cofigures the production
    environment properties
    '''
    
    DEBUG = False


config = {
    'development': DevelopementConfig,
    'production': ProductionConfig,
    'default': DevelopementConfig
}
