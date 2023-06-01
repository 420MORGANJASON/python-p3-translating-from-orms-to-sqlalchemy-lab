from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Dog(Base):
    __tablename__ = "dogs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)


def create_table():
    engine = create_engine("sqlite:///dogs.db")
    Base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()


def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()


def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()


def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()


# Create a session
engine = create_engine("sqlite:///dogs.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create the table if it doesn't exist
create_table()

# Testing the functions
dog1 = Dog(name="Fanny", breed="Cocker Spaniel")
dog2 = Dog(name="Joey", breed="Golden Retriever")

# Save the dogs to the database
save(session, dog1)
save(session, dog2)

# Retrieve all dogs from the database
dogs = get_all(session)
print("All dogs:")
for dog in dogs:
    print(dog.name, dog.breed)

# Find a dog by name
found_dog = find_by_name(session, "Fanny")
print("Found dog by name:", found_dog.name, found_dog.breed)

# Find a dog by ID
found_dog = find_by_id(session, 2)
print("Found dog by ID:", found_dog.name, found_dog.breed)

# Find a dog by name and breed
found_dog = find_by_name_and_breed(session, "Joey", "Golden Retriever")
print("Found dog by name and breed:", found_dog.name, found_dog.breed)

# Update the breed of a dog
update_breed(session, dog1, "Dalmatian")
print("Updated dog breed:", dog1.name, dog1.breed)
