from webapp.model import db

class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String, unique=True)
    eps = db.Column(db.String, nullable=False)
    volume = db.Column(db.String, nullable=False)
    pe_ratio = db.Column(db.String, nullable=False)
    prev_close = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Share {} {}>'.format(self.stock_symbol, self.prev_close)