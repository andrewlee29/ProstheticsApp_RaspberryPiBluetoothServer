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
        currsum = []
        message = ""
        for row in data:
            # Date
            currsum.append(row[1])
            # environmentStatus
            currsum.append(row[2])
            # muscleStatus
            currsum.append(row[3])
            # return string
        for ele in currsum:
            message += ele
            message += "#"
        return message

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
        self.mycursor.execute("SELECT time, mV FROM sensordata WHERE cid= '" +cid+"'")
        data = self.mycursor.fetchall()
        currsum = []
        message = ""
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
loaddata = loadData()
x = loaddata.getHistDetail("2020/11/05")
print(x)