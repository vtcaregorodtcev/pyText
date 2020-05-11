from flask import Flask
from flask_cors import CORS

from os import environ

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    CORS(app)

    with app.app_context():
        from . import routes  # Import routes

        if not database_exists(environ.get("SQLALCHEMY_DATABASE_URI")):
            db.create_all()  # Create database tables for our data models

        return app
