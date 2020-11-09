#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages "LOW" and "HIGH" based on values received from
client

Copyright Simon D. Levy 2018

MIT License
'''
import InitDataBase
from bluetooth_server import BluetoothServer
from loadsqldata import loadData

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
            self.send('')
        elif 'getHisDate' in message:
            # Return that date message
            self.send('')
        else:
            self.send('unknown function')

if __name__ == '__main__':
    # setup Database
    InitDataBase.setupdatabase()
    loaddata = loadData()
    # start server
    server = DataServer()
    server.start()
