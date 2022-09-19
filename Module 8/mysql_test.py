""" 
    mysql_test.py
    Jessica Harman
    Date: September 18, 2022
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "dQZI15Hi@09omSu7",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_ warnings": True
}

try:
    """ Searching for MySQL database errors """ 

    db = mysql.connector.connect(**config) 

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are wrong")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  Database does not exist")

    else:
        print(err)

finally:
    """ Closing Connection to MySQL """

    db.close()