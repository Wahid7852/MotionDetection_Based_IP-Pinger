# Motion Detection and IP Ping Project

This project uses a webcam to detect motion. When motion is detected, it opens a PowerPoint presentation in full-screen mode and asynchronously pings different groups of IP addresses using WebSocket connections.

## Features

- Motion detection using webcam
- Opening PowerPoint presentation in full-screen mode
- Asynchronous pinging of IP addresses
- WebSocket server-client communication

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/motion-detection-project.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

## Configuration

- Modify the `ip_groups` list in `main.py` to specify the IP addresses to ping.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
