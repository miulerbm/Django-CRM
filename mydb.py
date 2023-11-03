# Requirements for the DB:
# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

# Create the DB connection:

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1991'
)

# Create a cursor object to interact with the database and execute SQL commands.
# It is called cursor because it serves to move and interact with data (in RDBs).

cursorObject = dataBase.cursor()

# Execute a command to create a new database named 'elderco'.

cursorObject.execute("CREATE DATABASE elderco")

# Print a message to the console to indicate that the operation is complete.

print("ALl Done!")