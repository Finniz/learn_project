from flask import Flask
from webapp.model import db
<<<<<<< Updated upstream
from webapp.config import Config
=======
>>>>>>> Stashed changes
from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    return app
<<<<<<< Updated upstream

#from webapp import routes, model
=======
>>>>>>> Stashed changes
