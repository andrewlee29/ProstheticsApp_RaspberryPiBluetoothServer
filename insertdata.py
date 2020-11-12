import sched, time
import mysql.connector
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
        self.todaycid=""
    
    def checktodayexist(self):
        ##check today is exist in database
        today = date.today()
        d1 = today.strftime("%Y/%m/%d")
        self.mycursor.execute("SELECT cid,date FROM summarydata WHERE date="+d1)
        data = self.mycursor.fetchall()
        if not data[0][0]:
            ## if not exist, create one in summary
            self.mycursor.execute("INSERT INTO summarydata (date, environmentStatus, muscleStatus) VALUES (%s,%s,%s)", (d1, "good", "good"))
            ## automatic generate id 
            cid = self.mycursor.lastrowid
            self.todaycid = str(cid)
            self.mydb.commit()
            
        else:
            a = str(data[0][0])
            print ("todaycid = "+a)

    def do_something(self): 
        print("Insert data...")
        self.mycursor.execute("INSERT INTO sensordata (time, mV, emgsensor, temperature, humidity, cid) VALUES (%s,%s,%s,%s,%s,%s)", ("1", "50", "1", "70", "30",self.todaycid))
        ## automatic generate id 
        sid = self.mycursor.lastrowid
        ## need commit to apply insert 
        self.mydb.commit()

loadd = loadData()
loadd.checktodayexist()