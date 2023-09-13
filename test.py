import pandas as pd
import mysql.connector 
import sys



db = mysql.connector.connect(
    host='localhost', 
    user='root',
    password='password', 
    database='spotify'
)
   
if db.is_connected():
    print("Successful connection")
    cursor = db.cursor()
else:
   print('Could not connect to MySQL Databse')
   sys.exit()




cursor = db.cursor()

cursor.execute("SELECT MAX(streams) FROM spotify")

myresult = cursor.fetchall()

for x in myresult:
  print(x)

