from engine import db
from datetime import datetime

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    id_user = db.Column(db.Integer, ForeignKey("userz.id"), nullable=False)
    user = relationship("Userz", backref="bids", foreign_keys=[id_user])
    id_dog = db.Column(db.Integer, ForeignKey('dogz.id'), nullable=False)
    dog = relationship("Dogz", backref="bids", foreign_keys=[id_dog])
    initial_price = db.Column(db.Integer, nullable=True)
    last_price = db.Column(db.Integer, nullable=True)
    current_price = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Bidder(id_user = {self.id_user}, id_dog = {self.id_dog}, initial_price = {self.initial_price}, last_price = {self.last_price}, current_price = {self.current_price}, sold = {self.sold})"