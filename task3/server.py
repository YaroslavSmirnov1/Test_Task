import asyncio
import websockets


async def response(websocket):
    while True:  # вставил бесконечный цикл просто чтобы показать бесконечный обмен данными
        text = ""

        rand_number = int(await websocket.recv())

        if rand_number % 3 == 0 and rand_number % 5 == 0 and rand_number != 0:
            text = f'МаркоПоло'
        elif rand_number % 3 == 0 and rand_number != 0:
            text = f'Марко'
        elif rand_number % 5 == 0 and rand_number != 0:
            text = f'Поло'
        print(text)
        await websocket.send(text)


async def main():
    async with websockets.serve(response, "localhost", 8765):
        await asyncio.Future()  # run forever


asyncio.run(main())
asyncio.run(response())
