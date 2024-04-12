import cv2, subprocess, asyncio, websockets

# Function to open Notepad
def open_notepad():
    subprocess.Popen(["notepad.exe"])

# Function to detect motion
async def detect_motion():
    cap = cv2.VideoCapture(0)
    motion_detected = False
    prev_frame = None

    while not motion_detected:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        if prev_frame is None:
            prev_frame = blurred
            continue

        frame_diff = cv2.absdiff(prev_frame, blurred)
        _, thresh = cv2.threshold(frame_diff, 85, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                motion_detected = True

        cv2.imshow('Motion Detection', frame)

        if motion_detected:
            open_notepad()
            ip_groups = [
                ["192.168.x.xyz", "192.168.x.xyz", "192.168.x.xyz"],
                ["192.168.x.xyz", "192.168.x.xyz"],
                ["192.168.x.xyz"],
            ]
            # Connect to each IP and send a message
            for group in ip_groups:
                for ip in group:
                    try:
                        async with websockets.connect(f"ws://{ip}:35369") as websocket:
                            await websocket.send("Motion detected")
                            print(f"Sent 'Motion detected' to {ip}")
                    except asyncio.TimeoutError:
                        print(f"Timeout connecting to {ip}. Moving to the next IP.")
                        continue
                await asyncio.sleep(3)

        prev_frame = blurred
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to start the WebSocket server
async def start_ws_server():
    async def ws_server(websocket, path):
        print("WebSocket server started.")
        try:
            async for message in websocket:
                print(f"Received message: {message}")
        except websockets.ConnectionClosedError:
            print("Connection closed.")

    # Start the WebSocket server
    start_server = websockets.serve(ws_server, "192.168.x.xyz", 35369)
    await start_server

# Main function
async def main():
    # Start the WebSocket server
    await start_ws_server()

    # Start motion detection
    await detect_motion()

# Run the main function
asyncio.run(main())
