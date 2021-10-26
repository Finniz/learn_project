import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
<<<<<<< Updated upstream
from dotenv import load_dotenv
=======
import config
>>>>>>> Stashed changes


<<<<<<< Updated upstream
DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL)
=======
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
>>>>>>> Stashed changes
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
def init_db():
<<<<<<< Updated upstream
    
=======
    from webapp.model import Share
>>>>>>> Stashed changes
    Base.metadata.create_all(bind=engine)