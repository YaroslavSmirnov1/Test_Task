import asyncio
import websockets
import random


async def sender():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:                                                         # вставил бесконечный цикл просто чтобы показать бесконечный обмен данными
            rand_number = random.randint(0, 1000)
            await websocket.send(str(rand_number))

            msg = await websocket.recv()
            print(f"From Server: {msg}")
            await asyncio.Future()                 #чтобы начать бесконечный обмен данными, пожалуйста, закомментируйте эту строчку.
asyncio.run(sender())
