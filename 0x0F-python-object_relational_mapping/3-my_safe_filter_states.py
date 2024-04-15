#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # create a cursor
    cursor = conn_db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
