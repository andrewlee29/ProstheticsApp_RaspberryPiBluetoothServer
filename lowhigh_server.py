#!/usr/bin/python3

import InitDatabase
import threading
from bluetooth_server import BluetoothServer
from loadsqldata import loadData
from insertdata import InsertData

class DataServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

    def handleMessage(self, message):

        print(message)
        if message == 'requestSum':
            # Return Summary
            x = loaddata.getCurrentSum()
            print('returning: '+x)
            self.send(x)
        elif message == 'requestMore':
            # Return More data about current data
            self.send('')
        elif message == 'requestHis':
            # Return DateList and average temp & humid
            x = loaddata.getHistList()
            print('returning: '+x)
            self.send(x)
        elif 'getHisDate' in message:
            # Return that date message
            text = message.split(':')
            print(text[1])
            self.send('')
        else:
            self.send('unknown function')

if __name__ == '__main__':
    # setup Database
    InitDatabase.setupdatabase()
    loaddata = loadData()
    #start insert data
    insertd = InsertData()
    insertd.checktodayexist()
    threading.Thread(target=insertd.insertsensordata()).start()
    # start server
    server = DataServer()
    threading.Thread(target=server.start()).start()
    
