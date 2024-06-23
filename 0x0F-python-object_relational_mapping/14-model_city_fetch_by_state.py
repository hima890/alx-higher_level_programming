#!/usr/bin/python3
"""
A script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    Base.metadata.create_all(engine)
    try:
        city = session.query(State, City).join(City).order_by(City.id)
        for state, city in city:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()
