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
        # Query all State objects with a name containing the letter 'a'
        states_to_delete = session.query(State).filter(
            State.name.like('%a%')
            ).all()
        if states_to_delete:
            # Delete each state
            for state in states_to_delete:
                session.delete(state)

            # Commit the changes to the database
            session.commit()

    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
