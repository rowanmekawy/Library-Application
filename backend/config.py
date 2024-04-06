import os
class Config:
    MONGO_URI = os.environ.get('MONGODB_URI') or "mongodb://mongo:27017/mylibrary"
    # MONGO_URI = os.environ.get('MONGODB_URI') or "mongodb://172.17.0.1:27017/mylibrary"
    print("zzzzzzzzzzzzzzzzzzzzzzzzzmlkmlkmkmmmmmmmmmmmmmmongo:27017mmmmzzzzzzMongoDB URI:", MONGO_URI)

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/test_database"    
    MONGODB_SETTINGS = {
        'db': 'test_database',
        'host': 'localhost',
        'port': 27017,
    }

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'dev_database',
        'host': 'localhost',
        'port': 27017
    }


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'prod_database',
        'host': 'localhost',
        'port': 27017
    }

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}    