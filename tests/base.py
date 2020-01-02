from flask_testing import TestCase
from alembic import command, config

from app import create_app
from src.helpers.database import Base, engine


class BaseTest(TestCase):
    alembic_configuration = config.Config('./alembic.ini')

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

        with self.app.app_context():
            Base.metadata.create_all(bind=engine)
            command.stamp(self.alembic_configuration, 'head')
            command.upgrade(self.alembic_configuration, 'head')

    def tearDown():
        pass
