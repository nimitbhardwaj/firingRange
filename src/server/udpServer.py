import asyncio
import src.config as config
from src.controller.controller import controller

class udpServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        androidId, seqNo, data = message.split("|")
        seqNo = int(seqNo)
        config.sensorDeviceDict[androidId].data.append(seqNo, data)
        if seqNo % 100 == 0:
            controller(androidId)