

class Config:
    DEBUG = True
    PRODUCTION = False
    BASE_URL = "http://localhost:5000"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True