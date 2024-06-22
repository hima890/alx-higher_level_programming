#!/usr/bin/python3
"""" A script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys


def lestStates(dbUsername, dbPassword, dbName):
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=dbUsername,
                         passwd=dbPassword, db=dbName, port=3306)
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    # Execute the query to get all states sorted by id
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


#  The code below runs only when the script is executed directly
if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    lestStates(username, password, db_name)
