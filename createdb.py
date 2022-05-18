import mysql.connector
import mysql 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Ethio4life(001)")
    #database="tractotek")

my_cursor = mydb.cursor()

my_cursor.execute("DROP DATABASE IF EXISTs tractortek")
my_cursor.execute("CREATE DATABASE tractortek")

