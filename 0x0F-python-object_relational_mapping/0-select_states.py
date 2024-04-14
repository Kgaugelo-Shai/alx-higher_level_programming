#!/usr/bin/python3
""" Represents a script that lists all the states from the database hbtn_0e_usa
"""
import MySQLdb
import sys

# code must not be executed when imported
if __name__ == "__main__":
    # Connect to MySQL, script takes two arguments
    conn_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # create cursor
    cursor = conn_db.cursor()
    # execute MySQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # fetch reults
    rows = cursor.fetchall()
    # loop through results, print with every iteration
    for row in rows:
        print(row)
    # close cursor
    cursor.close()
    # close connection
    cursor.close()
