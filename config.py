import os


class Config:

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class Testing(Config):
    DATABASE_URL = os.getenv('DATABASE_URL')


config = {
    'development': Development,
    'testing': Testing
}
