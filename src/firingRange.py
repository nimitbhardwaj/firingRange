import asyncio
from src.server.server import server

class firingRange:
    def __init__(self):
        pass

    def run(self):
        asyncio.run(server())
