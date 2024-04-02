import asyncio, websockets, json, subprocess, sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import websockets
except ImportError:
    print("WebSockets is not installed. Installing...")
    install("websockets")

# For simplicity, hardcode the port number here
port = 8765

async def handle_ping(websocket, path):
    async for message in websocket:
        print(f"Received ping for port {message}")
        subprocess.Popen(["notepad.exe"])

start_server = websockets.serve(handle_ping, "localhost", port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()