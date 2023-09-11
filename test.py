import pandas as pd
import mysql.connector


db = mysql.connector.connect(
    host='localhost', 
    user='root',
    password='password', 
    database='spotify'
)


if db.is_connected():
    print("successful")

cursor = db.cursor()

cursor.execute("SELECT * FROM spotify")

myresult = cursor.fetchall()

for x in myresult:
  print(x)

