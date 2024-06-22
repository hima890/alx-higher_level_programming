#!/usr/bin/python3
"""
A script that changes the name of a State object from the
database hbtn_0e_6_usa.
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

    try:
        # Create a new State object
        state_id = 2
        state_toUpdate = session.query(State).filter(
            State.id == state_id
        ).order_by(State.id).first()

        if state_toUpdate:
            # Update the state name
            state_toUpdate.name = 'New Mexico'

            # Commit the session to insert the new State into the database
            session.commit()
        else:
            print(f"State with id {state_id} not found")

    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
