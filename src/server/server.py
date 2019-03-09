import asyncio
import time
from src.server.tcpServer import tcpServer
from src.server.udpServer import udpServer
import src.config as config

async def server():
    loop = asyncio.get_running_loop()

    tcpServerConn = await loop.create_server(lambda: tcpServer(), config.host, config.tcpPort)
    udpTransport, udpProtocol = await loop.create_datagram_endpoint(lambda: udpServer(), local_addr = (config.host, config.udpPort))

    async with tcpServerConn:
        await tcpServerConn.serve_forever()

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()
