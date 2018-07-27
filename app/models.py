from app import db



class Pokes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False, unique=True)
    best_recipe = db.Column(db.String(100), index=True)
    percent = db.Column(db.Integer)
    info = db.Column(db.Text)
    attracted = db.Column(db.Boolean)
    recipe_type = db.Column(db.String(100))


    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)