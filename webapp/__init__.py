from flask import Flask
from webapp.model import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    return app
