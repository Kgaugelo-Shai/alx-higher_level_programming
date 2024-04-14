#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) from the
    database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establish connection
    conn_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # create a cursor for the connection
    cursor = conn_db.cursor()
    # execute query with cursor
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'"
                   " ORDER BY states.id")
    # Fetch the results
    rows = cursor.fetchall()
    # iterate through list
    for row in rows:
        print(row)
    # close cursor
    cursor.close()
    # close connection
    conn_db.close()
