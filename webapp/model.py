from flask_sqlalchemy import SQLAlchemy

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
    

subs = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('share_id', db.Integer, db.ForeignKey('share.id'))
)   