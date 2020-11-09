import mysql.connector

class loadData:
    def _init_(self):
        self.currsum = []
        self.currdata = []
        self.historylist = []
        self.historyinfo = []
        self.message = ""
    def getCurrentSum(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
        for row in data:
            # environmentStatus
            self.currsum.append(row[2])
            # muscleStatus
            self.currsum.append(row[3])
            # return string
            for ele in self.currsum:
                self.message += ele
                self.message += "|"
            return self.message
    def getCurrentData(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
        for row in data:
            # environmentStatus
            self.currsum.append(row[2])
            # muscleStatus
            self.currsum.append(row[3])
    def gethistorylist(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
        for row in data:
            # environmentStatus
            self.currsum.append(row[2])
            # muscleStatus
            self.currsum.append(row[3])
    def gethistoryinfo(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
        for row in data:
            # environmentStatus
            self.currsum.append(row[2])
            # muscleStatus
            self.currsum.append(row[3])

### open database 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database= "prostheticsData"
)

mycursor = mydb.cursor()
loaddata = loadData()
x = loaddata.getCurrentSum()
print(x)