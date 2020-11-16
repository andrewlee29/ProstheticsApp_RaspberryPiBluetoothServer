import json
import mysql.connector

class loadData:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database= "prostheticsData"
            )
        self.mycursor = self.mydb.cursor()
        
    def getCurrentSum(self):
        self.mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = self.mycursor.fetchall()
        for row in data:
            # to json
            x = {
                "date": row[1],
                "environmentStatus": row[2],
                "muscleStatus" : row[3]
            }
            jsonstring = json.dumps(x)
            # return string
        return jsonstring

    def getHistList(self):
        self.mycursor.execute("SELECT summarydata.date, AVG(sensordata.temperature), AVG(sensordata.humidity) FROM summarydata JOIN sensordata ON summarydata.cid = sensordata.cid GROUP BY summarydata.date")
        data = self.mycursor.fetchall()
        currsum = []
        message = ""
        for row in data:
            # date
            currsum.append(row[0])
            # temp
            currsum.append(round(row[1],2))
            # humid
            currsum.append(round(row[2],2))
            
         # return string
        for ele in currsum:
            message += str(ele)
            message += "#"
        return message
        
    def getHistDetail(self,getdate):
        #get the avg temp & humid & that day cid
        self.mycursor.execute("SELECT summarydata.date, summarydata.cid, AVG(sensordata.temperature), AVG(sensordata.humidity) FROM summarydata JOIN sensordata ON summarydata.cid = sensordata.cid GROUP BY summarydata.date")
        data = self.mycursor.fetchall()
        currsum = []
        message = ""
        cid = -1
        for row in data:
            if (str(row[0]) == getdate):
                # temp
                currsum.append(round(row[2],2))
                # humid
                currsum.append(round(row[3],2))
                cid = row[1]
        if (cid == -1):
            return "error"
        #get the emg data (sensor1)
        self.mycursor.execute("SELECT time,mV FROM sensordata WHERE cid= " +str(cid)+ " AND emgsensor = '1'")
        data = self.mycursor.fetchall()
        for row in data:
            # time
            currsum.append(row[0])
            # temp
            currsum.append(row[1])
        # return string
        for ele in currsum:
            message += str(ele)
            message += "#"
        return message
    
### open database 
# loaddata = loadData()
# x = loaddata.getCurrentSum()
# print(x)