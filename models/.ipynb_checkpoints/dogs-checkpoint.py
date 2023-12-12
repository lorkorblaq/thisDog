from . import db
class Dogz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    aggression = db.Column(db.Integer, nullable=False)
    intel = db.Column(db.Integer, nullable=False)
    descrip = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Dog(name = {self.name}, descrip = {self.descrip}, breed = {self.breed}, aggression = {self.aggression}, intel = {self.intel})"