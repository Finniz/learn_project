from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Share(db.Model):
    Stock_Symbol = db.Column(db.String, unique=True, primary_key=True)
    EPS = db.Column(db.Float, nullable=False)
    Volume = db.Column(db.Float, nullable=False)
    PE_Ratio = db.Column(db.Float, nullable=False)
    Prev_Close = db.Column(db.Float, nullable=True)

    def __repr__(self):
            return '<Share {} {}>'.format(self.Stock_Symbol, self.Prev_Close)