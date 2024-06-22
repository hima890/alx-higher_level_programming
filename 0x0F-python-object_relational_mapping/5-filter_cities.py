#!/usr/bin/python3
""""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
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
    SELECT cities.name AS city_name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s;
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    cities = cursor.fetchall()
    # Extract city names from the result set
    city_names = [city[0] for city in cities]
    # Print the formatted output
    if city_names:
        print(", ".join(city_names))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
