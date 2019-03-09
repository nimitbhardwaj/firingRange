import asyncio
import src.config as config

class udpServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        androidId, seqNo, data = message.split("|")
        config.sensorDeviceDict[androidId].data.append((int(seqNo), data))