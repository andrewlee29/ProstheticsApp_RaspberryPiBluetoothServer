import mysql.connector

class loadData:
    def getCurrentSum(self):
        mycursor.execute("SELECT * FROM summarydata WHERE cid=(SELECT max(cid) FROM summarydata)")
        data = mycursor.fetchall()
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
    

# ### open database 
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="123456",
#   database= "prostheticsData"
# )

# mycursor = mydb.cursor()
# loaddata = loadData()
# x = loaddata.getCurrentSum()
# print(x)