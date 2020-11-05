import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS prostheticsData")
mydb.connector.close()

# open database 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database= "prostheticsData"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS SummaryData (cid INT AUTO_INCREMENT PRIMARY KEY, Date VARCHAR(255)), EnvironmentStatus VARCHAR(255) , MuscleStatus VARCHAR(255)")
mycursor.execute("CREATE TABLE IF NOT EXISTS SensorData (sid INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255)), mV VARCHAR(255) , emgsensor VARCHAR(255) , temperature VARCHAR(255) , humidity VARCHAR(255) ,FOREIGN KEY(cid) REFERENCES SummaryData(cid)")
