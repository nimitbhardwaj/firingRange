import asyncio
import time
from src.server.tcpServer import tcpServer
from src.server.udpServer import udpServer

host = '192.168.43.87'
tcpPort = 65432
udpPort = 65433

async def server():
    loop = asyncio.get_running_loop()

    tcpServerConn = await loop.create_server(lambda: tcpServer(), host, tcpPort)
    udpTransport, udpProtocol = await loop.create_datagram_endpoint(lambda: udpServer(), local_addr = (host, udpPort))

    async with tcpServerConn:
        await tcpServerConn.serve_forever()

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()
