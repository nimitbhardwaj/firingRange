# #!/usr/bin/env python3

import asyncio

host = ''
tcpPort = 65432
udpPort = 65433

class sensorDevice: 
    def __init__(self):
        pass

    def gedId(self):
        return self.id

    def setId(self, id_):
        self.id = id_
        
class tcpServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

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
    udpTransport, udpProtocol = await loop.create_datagram_endpoint(lambda: udpServer(),local_addr=('127.0.0.1', udpPort))

    async with tcpServerConn:
        await tcpServerConn.serve_forever()

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()

asyncio.run(main())