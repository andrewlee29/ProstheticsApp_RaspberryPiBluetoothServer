import mysql.connector

class loadData:
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database= "prostheticsData"
            )
        self.mycursor = mydb.cursor()
        
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
            message += "|"
        return message
    

### open database 
loaddata = loadData()
x = loaddata.getCurrentSum()
print(x)