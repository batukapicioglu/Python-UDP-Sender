Description:
This Python script allows users to send UDP requests to a specified server. It provides a simple command-line interface for users to enter the source port number, destination IP address, destination port number, and the message to send. 
The script utilizes the socket library for UDP communication and provides visual feedback using the tqdm library while the request is being sent. Upon receiving a response from the server, it prints the response message to the console. 
This script is useful for testing UDP communication or sending simple UDP requests to servers.

Features:
- Send UDP requests to a specified server.
- Visual feedback using tqdm during the request sending process.
- Print response messages from the server.
- Simple command-line interface for user interaction.

Usage:
1. Run the script.
2. Enter the required information when prompted (source port, destination IP address, destination port, message).
3. View the progress bar as the request is being sent.
4. View the response message from the server.

Dependencies:
- Python 3.x
- tqdm library

  ## Installation

```
   git clone https://github.com/batukapicioglu/UDP-SENDER.git
   sudo apt-get update
   sudo apt-get install python3
   pip install tqdm
   sudo chmod +x UDP-SENDER.py
   sudo python3 UDP-SENDER.py
   
```
## Sample Laboratory Environment:
* (https://tryhackme.com/r/room/bypass))
