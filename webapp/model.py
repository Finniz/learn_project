from flask_sqlalchemy import SQLAlchemy
from webapp.dbase import Base, engine


db = SQLAlchemy()

class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String, unique=True)
    eps = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    pe_ratio = db.Column(db.Float, nullable=False)
    prev_close = db.Column(db.Float, nullable=False)
    todays_range = db.Column(db.Float,nullable=False)

    def __repr__(self):
        return '< {} close price: {} day change: {}%>'.format( self.stock_symbol, self.prev_close, self.todays_range)

if __name__==("__main__"):
    Base.metadata.create_all(bind=engine)      
