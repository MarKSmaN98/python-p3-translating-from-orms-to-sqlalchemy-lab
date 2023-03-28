from models import Dog, Base
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    query = session.query(Dog)
    return query

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name.like(name)).first()
    return query

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id.like(id)).first()
    return query

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return query

def update_breed(session, dog, breed):
    query = session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})