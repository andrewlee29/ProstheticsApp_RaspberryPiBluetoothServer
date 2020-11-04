import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE prostheticsData")

mycursor.execute("CREATE TABLE CurrentData (cid INT AUTO_INCREMENT PRIMARY KEY, Date VARCHAR(255)), temperature VARCHAR(255) , humidity VARCHAR(255)")

