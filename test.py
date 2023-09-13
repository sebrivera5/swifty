'''
Might make this a website UI using Flask. Not exactly sure yet, but this can be used to query for now rather than using 
an SQL terminal


'''


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

cursor.execute("SELECT MAX(streams), track_name FROM spotify")

myresult = cursor.fetchall()

for x in myresult:
  print(x)



#Simple terminal sql
while True:
   query = input("Enter your query\n")

   if query == ("exit" or "Exit"):
    print('exiting because query = {}', query)
    sys.exit()
      
   cursor.execute(query)
   result = cursor.fetchall()

   for x in result:
      print(x)

    




