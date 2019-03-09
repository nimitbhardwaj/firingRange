import asyncio
import src.config as config
import array
from src.controller.controller import Cont

c = Cont()

def getSeqNo(A):
    x = 0
    k = 1
    for i in A:
        x += k*i
        k += 1
    return x

class udpServer:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        config.sensorDeviceDict[addr[0]].data.extend(list(data))
        # config.sensorDeviceDict[addr[0]].data.append(data)
        if len(config.sensorDeviceDict[addr[0]].data) >= (44100*2)/512:
            c.controller(addr[0])

