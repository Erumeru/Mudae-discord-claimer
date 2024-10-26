import json
import asyncio
import websockets

async def get_session_id(token):
    gateway_url = "wss://gateway.discord.gg/?v=10&encoding=json"

    async with websockets.connect(gateway_url) as websocket:
        # Receive the hello packet
        hello = await websocket.recv()
        hello_data = json.loads(hello)
        heartbeat_interval = hello_data['d']['heartbeat_interval'] / 1000

        # Send identify packet
        identify_payload = {
            "op": 2,
            "d": {
                "token": token,
                "intents": 513,  # Minimal intents, adjust as needed
                "properties": {
                    "$os": "linux",
                    "$browser": "my_library",
                    "$device": "my_library"
                }
            }
        }
        await websocket.send(json.dumps(identify_payload))

        # Handle the response
        while True:
            message = await websocket.recv()
            message_data = json.loads(message)

            if message_data['t'] == 'READY':
                session_id = message_data['d']['session_id']
                print(f"Session ID: {session_id}")
                break

            await asyncio.sleep(heartbeat_interval)

# Replace with your bot token
TOKEN = "YOUR_BOT_TOKEN"
asyncio.run(get_session_id(TOKEN))
