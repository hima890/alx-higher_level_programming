#!/usr/bin/python3
"""
A script that creates the State “California” with the City “San Francisco”
in the database hbtn_0e_100_usa.
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
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a sessionmaker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    try:
        # Create new State and City objects
        new_state = State(name='California')
        new_city = City(name='San Francisco')
        
        # Add City to State
        new_state.cities.append(new_city)
        
        # Add State to session and commit
        session.add(new_state)
        session.commit()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
