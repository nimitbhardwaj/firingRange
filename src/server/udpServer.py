import asyncio
import src.config as config
from src.controller.controller import controller

class udpServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = tuple(data.decode())
        print(message)
        androidId, seqNo, data = message[0], message[1], message[2]
        seqNo = int(seqNo)
        config.sensorDeviceDict[androidId].data.append((seqNo, data))
        if seqNo % 100 == 0:
            controller(androidId)