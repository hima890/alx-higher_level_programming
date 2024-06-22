#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the
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
        new_state = State(name='Louisiana')

        # Add the new State object to the session
        session.add(new_state)

        # Commit the session to insert the new State into the database
        session.commit()

        # Print the id of the new state
        print(f"{new_state.id}")

    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
