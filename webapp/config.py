import os
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dsD243k%2lkjskad6&!@dfkslodjak'
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
