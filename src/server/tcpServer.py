import asyncio
import time
from src.sensorDevice import sensorDevice

import src.config as config

class tcpServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        peername = self.transport.get_extra_info('peername')
        lng, lat = message.split("|")
        if peername in config.sensorDeviceDict:
            self.transport.write("Already connected".encode())
        else:
            config.sensorDeviceDict[peername[0]] = sensorDevice(time.time(), peername, (lng, lat))
            self.transport.write("OK".encode())
        print('Close the client socket')
        self.transport.close()