import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class Testing(Config):
    DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'test-db.sqlite')


config = {
    'development': Development,
    'testing': Testing
}
