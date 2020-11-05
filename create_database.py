import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS prostheticsData")
mydb.close()

# open database 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database= "prostheticsData"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS customers(name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS summarydata (cid INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(255)), environmentStatus VARCHAR(255) , muscleStatus VARCHAR(255)")
mycursor.execute("CREATE TABLE IF NOT EXISTS sensordata (sid INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255)), mV VARCHAR(255) , emgsensor VARCHAR(255) , temperature VARCHAR(255) , humidity VARCHAR(255) ,FOREIGN KEY(cid) REFERENCES SummaryData(cid)")
