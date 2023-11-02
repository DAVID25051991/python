import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Evenat1123*"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")