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
        self.s = sched.scheduler(time.time, time.sleep)
    
    def checktodayexist(self):
        today = date.today()
        d1 = today.strftime("%Y/%m/%Y")
        self.mycursor.execute("INSERT INTO summarydata (date, environmentStatus, muscleStatus) VALUES (%s,%s,%s)", (d1, "good", "good"))
        ## automatic generate id 
        cid = self.mycursor.lastrowid

    def do_something(self): 
        print("Insert data...")
        self.mycursor.execute("INSERT INTO sensordata (time, mV, emgsensor, temperature, humidity, cid) VALUES (%s,%s,%s,%s,%s,%s)", ("1", "50", "1", "70", "30",1))
        ## automatic generate id 
        sid = self.mycursor.lastrowid
        ## need commit to apply insert 
        self.mydb.commit()
        # repeat task in 1 second
        self.s.enter(1, 1, do_something)
        self.s.run()

