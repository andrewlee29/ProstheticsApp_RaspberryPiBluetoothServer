import mysql.connector

class loadData:
    def _init_(self):
        self.currsum = []
        self.currdata = []
        self.historylist = []
        self.historyinfo = []
def getCurrentSum(self):
    mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
    data = mycursor.fetchall()
    for row in data:
        # environmentStatus
        self.currsum.append(row[2])
        # muscleStatus
        self.currsum.append(row[3])
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