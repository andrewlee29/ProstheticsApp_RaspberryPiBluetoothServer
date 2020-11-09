#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages "LOW" and "HIGH" based on values received from
client

Copyright Simon D. Levy 2018

MIT License
'''

from bluetooth_server import BluetoothServer
from loadsqldata import loadData

class DataServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

    def handleMessage(self, message):

        print(message)
        if message == 'requestSum':
            self.send('Return Summary')
        elif message == 'requestMore':
            self.send('Return More data about current data')
        elif message == 'requestHis':
            self.send('Return DateList and average temp & humid')
        elif 'getHisDate' in message:
            self.send('Return that date message')
        else:
            self.send('unknown function')

if __name__ == '__main__':

    server = DataServer()

    server.start()
