#!/usr/bin/python3
"""
A script that prints the first State object
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    # Create database connection URL
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database_name
    )

    # Create engine
    engine = create_engine(db_url)

    # Create a sessionmaker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print states in the desired format
    print(f"{first_state.id}: {first_state.name}")
    # Close session
    session.close()
