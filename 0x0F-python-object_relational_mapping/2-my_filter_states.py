#!/usr/bin/python3
"""" Takes in an argument and displays all values in the
states table ofhbtn_0e_0_usa where name matches the argument """


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
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC;".format(
        state_name
        )
    cursor.execute(query)

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
