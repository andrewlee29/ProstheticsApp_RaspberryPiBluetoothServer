#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages "LOW" and "HIGH" based on values received from
client

Copyright Simon D. Levy 2018

MIT License
'''

from bluetooth_server import BluetoothServer

class LowHighServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

    def handleMessage(self, message):

        print(message)
        if message == 'a':
            self.send('A function')
        elif message == 'b':
            self.send('B function')
        elif message == 'au':
            self.send('auto function execute XZZZZZZZZZZZZZZ')
        else:
            self.send('unknown function')
        #self.send('LOW' if int(message) < 50 else 'HIGH')

if __name__ == '__main__':

    server = LowHighServer()

    server.start()
