#!/usr/bin/python3
"""
A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]
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

    # Query the first State object match
    filter_state = session.query(State).filter(
        State.name == state_name
        ).order_by(State.id).all()

    # Print the results
    if not filter_state:
        print("Not found",)
    else:
        for state in filter_state:
            print(f"{state.id}: {state.name}")
    # Close session
    session.close()
