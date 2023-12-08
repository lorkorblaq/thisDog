from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Userz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User(name = {name}, email = {email})"


class Dogz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    aggression = db.Column(db.Integer, nullable=False)
    intel = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Dog(name = {self.name}, breed = {self.breed}, aggression = {self.aggression}, intel = {self.intel})"

class Bidder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=True)
    id_user = db.Column(db.Integer, ForeignKey('userz.id'), nullable=False)
    user = relationship("userz", backref="bids")
    id_dog = db.Column(db.Integer, ForeignKey('dogz.id'), nullable=False)
    dog = relationship("dogz", backref="bids")
    initial_price = db.Column(db.Integer, nullable=True)
    last_price = db.Column(db.Integer, nullable=True)
    current_price = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"Bid(id_user = {self.id_user}, id_dog = {self.id_dog}, initial_price = {self.initial_price}, last_price = {self.last_price}, current_price = {self.current_price}, sold = {self.sold})"