""" 
    mysql_test.py
    Jessica Harman
    Date: September 25, 2022
"""
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "dQZI15Hi@09omSu7",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    #Records display using INNER JOIN STATEMENT
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS USING INNER JOIN --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    #Records display using LEFT OUTER JOIN
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player LEFT OUTER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS USING LEFT OUTER JOIN--")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
   
    #Records display using RIGHT OUTER JOIN
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player RIGHT OUTER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS USING RIGHT OUTER JOIN--")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    #Records display using where clause for player 2
    cursor.execute("SELECT first_name, last_name FROM player WHERE player_id = 2")
    players = cursor.fetchall()
    print("\n  -- DISPLAYING PLAYER RECORDS FOR PLAYER 2 USING WHERE CLAUSE--")
    for player in players:
        print("  First Name: ", player[0])
        print("  Last Name: ", player[1])

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()