import mysql.connector

class loadData:
    def _init_(self):
        self.message = ""
    def getCurrentSum(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
        currsum = []
        for row in data:
            # environmentStatus
            currsum.append(row[2])
            # muscleStatus
            currsum.append(row[3])
            # return string
            for ele in currsum:
                self.message += ele
                self.message += "|"
            return self.message

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