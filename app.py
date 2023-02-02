
import asyncio
import signal
import json
import websockets
from test1 import run_program
import http

async def hello():  # put application's code here
    await run_program()
    return json({'about': "Hello world"})

async def echo(websocket):
    async for message in websocket:
        print(message)
        message=message.split(" ")
        if message[0] == "start":
            final_message = run_program(message[1])
            print("jjj",final_message)

        await websocket.send(json.dumps(final_message))



async def health_check(path, request_headers):
    if path == "/healthz":
        return http.HTTPStatus.OK, [], b"OK\n"



async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=8080,
        process_request=health_check,
    ):
        await stop

if __name__ == "__main__":
    asyncio.run(main())
