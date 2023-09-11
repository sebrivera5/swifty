import pandas as pd
import mysql.connector


db = mysql.connector.connect(host='localhost', user='root',password='password')

mycursor = db.cursor()

