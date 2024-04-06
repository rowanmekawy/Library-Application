import pytest
from app.extensions import db
from app import create_app
from config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope='function')
def mongo(request, app):
    with app.app_context():
        db.connection.drop_database(app.config['MONGODB_SETTINGS']['db'])
        db.connection.drop_database(app.config['MONGODB_SETTINGS']['db'])
    yield db
    with app.app_context():
        db.connection.drop_database(app.config['MONGODB_SETTINGS']['db'])

