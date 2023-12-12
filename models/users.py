from . import db
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Userz(db.Model,):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return {"name": self.name, "email": self.email}
    