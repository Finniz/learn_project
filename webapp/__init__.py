from flask import Flask
from webapp.model import db
from webapp.config import Config
from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app

#from webapp import routes, model
