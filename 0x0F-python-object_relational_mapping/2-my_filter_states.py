#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states where name matches the input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Disconnect from server
    db.close()

if __name__ == "__main__":
    main()
