from flask_sqlalchemy import sqlalchemy
from webapp import db, create_app

db.create_all(app=create_app())
