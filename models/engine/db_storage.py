from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Interger, DateTime, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker

password= 518Oloko.
Base = declarative_base()
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/thisdog")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session= Session()


class Userz(Base):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(100), nullable=False)
    email = Column(db.String(200), nullable=False)
    password = Column(db.String(100), nullable=False)
    def __repr__(self):
        return f"User(name = {name}, email = {email})"


class Dogz(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False)
    breed = Column(String(100), nullable=False)
    aggression = Column(Integer, nullable=False)
    intel = Column(Integer, nullable=False)
    def __repr__(self):
        return f"Dog(name = {self.name}, breed = {self.breed}, aggression = {self.aggression}, intel = {self.intel})"

class Bidder(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=True)
    id_user = Column(Integer, ForeignKey('userz.id'), nullable=False)
    user = relationship("userz", backref="bids")
    id_dog = Column(Integer, ForeignKey('dogz.id'), nullable=False)
    dog = relationship("dogz", backref="bids")
    initial_price = Column(Integer, nullable=True)
    last_price = db.Column(Integer, nullable=True)
    current_price = Column(Integer, nullable=False)
    sold = Column(Boolean, nullable=True)
    def __repr__(self):
        return f"Bid(id_user = {self.id_user}, id_dog = {self.id_dog}, initial_price = {self.initial_price}, last_price = {self.last_price}, current_price = {self.current_price}, sold = {self.sold})"
