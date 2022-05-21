import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'alguma frase muito segura'
    API_KEY = os.environ.get("WEATHER_API") or None

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "production": ProductionConfig,
    "testing": TestingConfig,
    "development": DevelopmentConfig,

    "default": DevelopmentConfig
}