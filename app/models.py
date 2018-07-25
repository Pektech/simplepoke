from app import db



class Pokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    best_recipe = db.Column(db.String(100), index=True)
    percent = db.Column(db.Integer)
    info = db.Column(db.Text)


    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)