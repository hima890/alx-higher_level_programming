#!/usr/bin/python3
"""" A script that lists all cities from the database hbtn_0e_4_usa """


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
                        host="localhost",
                        user=username,
                        passwd=password,
                        db=db_name, port=3306,
                        charset="utf8"
                        )
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    # Execute the query to get all states sorted by id
    query = """
    SELECT cities.id, cities.name AS city_name, states.name AS state_name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
