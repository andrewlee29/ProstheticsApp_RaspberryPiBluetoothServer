import mysql.connector

### create database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS prostheticsData")
mydb.close()

### open database 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database= "prostheticsData"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS summarydata (cid INT AUTO_INCREMENT PRIMARY KEY, date VARCHAR(255), environmentStatus VARCHAR(255) , muscleStatus VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS sensordata (sid INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), mV VARCHAR(255) , emgsensor VARCHAR(255) , temperature VARCHAR(255) , humidity VARCHAR(255) , cid INT, FOREIGN KEY(cid) REFERENCES summarydata(cid))")

### insert data

# ycursor.execute("INSERT INTO summarydata (date, environmentStatus, muscleStatus) VALUES (%s,%s,%s)", ("2020/11/5", "good", "good"))
### automatic generate id 
# cid = mycursor.lastrowid
#mycursor.execute("INSERT INTO sensordata (time, mV, emgsensor, temperature, humidity, cid) VALUES (%s,%s,%s,%s,%s,%s)", ("1", "50", "1", "70", "30",1))
#sid = mycursor.lastrowid
### need commit to apply store 
# mydb.commit()

### select data and print 
mycursor.execute("SELECT * FROM summarydata")
### get the lastest record
# mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
### get limit the result first 10
# mycursor.execute("SELECT * FROM summarydata LIMIT 5")
myresult = mycursor.fetchall()


for row in myresult:
  print(type(row[0]))
  print("\n")
  print("Id: ", row[0])
  print("date: ", row[1])
  print("environmentStatus: ", row[2])
  print("muscleStatus: ", row[3])
  print("\n")




mydb.close()