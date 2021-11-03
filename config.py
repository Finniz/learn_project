import os
import sys
from datetime import timedelta
from dotenv import load_dotenv

sys.path.append("C:\projects\learn_project\webapp")
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dsD243k%2lkjskad6&!@dfkslodjak'
REMEMBER_COOKIE_DURATION = timedelta(days=14)