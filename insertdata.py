import sched, time
import mysql.connector
import random
from datetime import date

class loadData:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database= "prostheticsData"
            )
        self.mycursor = self.mydb.cursor()
        self.todaycid = 0
    
    def checktodayexist(self):
        ##check today is exist in database
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        self.mycursor.execute("SELECT cid,date FROM summarydata WHERE date= '" +d1+ "'")
        data = self.mycursor.fetchall()
        if not data:
            print("today not exist")
            print(data)
            ## if not exist, create one in summary
            self.mycursor.execute("INSERT INTO summarydata (date, environmentStatus, muscleStatus) VALUES (%s,%s,%s)", (d1, "good", "good"))
            ## automatic generate id 
            cid = self.mycursor.lastrowid
            self.todaycid = cid
            self.mydb.commit()
            
        else:
            self.todaycid = data[0][0]
            print ("todaycid = ",self.todaycid)

    def insertsensordata(self): 
        print("Insert data...")
        ## test data : random int generte
        a = str(random.randint(1,100))
        b = str(random.randint(1,100))
        c = str(random.randint(1,2))
        d = str(random.randint(0,25))
        e = str(random.randint(1,100))
        self.mycursor.execute("INSERT INTO sensordata (time, mV, emgsensor, temperature, humidity, cid) VALUES (%s,%s,%s,%s,%s,%s)", (a, b, c, d, e,self.todaycid))
        ## automatic generate id 
        sid = self.mycursor.lastrowid
        ## need commit to apply insert 
        self.mydb.commit()

loadd = loadData()
loadd.checktodayexist()
loadd.insertsensordata()