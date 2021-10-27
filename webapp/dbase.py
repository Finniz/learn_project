from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db.session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)