import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Ethio4life(001)")
    #database="tractotek")

my_cursor = mydb.cursor()

#my_cursor.execute("IF EXIST DROP DATABASE TractorTek")
my_cursor.execute("CREATE DATABASE TractorTek")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
