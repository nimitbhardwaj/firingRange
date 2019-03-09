# #!/usr/bin/env python3

import asyncio
import time

host = ''
tcpPort = 65432
udpPort = 65433

sensorDeviceDict = {}
availableSensorId = 0

class sensorDevice: 
    def __init__(self, androidId_=None, timeStamp_=None, ipAddr_ = None, geoLocation_ = None ):
        self.androidId = androidId_
        self.timeStamp = timeStamp_
        self.ipAddr = ipAddr_
        self.geoLocation = geoLocation_
        
class tcpServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        androidId, lng, lat = message.split("|")
        if androidId in sensorDeviceDict:
            self.transport.write("Already connected".encode())
        else:
            print(self.transport.get_extra_info('peername'))
            peername = self.transport.get_extra_info('peername')
            sensorDeviceDict[androidId] = sensorDevice(androidId, time.time(), peername, (lng, lat))
            self.transport.write("OK".encode())
        print('Close the client socket')
        self.transport.close()

class udpServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message, addr))
        self.transport.sendto(data, addr)



async def main():
    loop = asyncio.get_running_loop()

    tcpServerConn = await loop.create_server(lambda: tcpServer(), host, tcpPort)
    udpTransport, udpProtocol = await loop.create_datagram_endpoint(lambda: udpServer(), local_addr = ('192.168.225.37', udpPort))

    async with tcpServerConn:
        await tcpServerConn.serve_forever()

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()

asyncio.run(main())