from flask import Flask
from .extensions import db
from .books.routes import api as books_api

def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)
    books_api.init_app(app)

    return app
