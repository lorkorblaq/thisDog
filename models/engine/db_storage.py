from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Interger, DateTime, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker

password = "518Oloko."
Base = declarative_base()
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/thisdog")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session= Session()

