#!/usr/bin/python3

import socket
from tqdm import tqdm
import time

def send_udp_request(source_port, server_ip, server_port, msg):
    try:
        print("Sending UDP request...")
        print("Source port:", source_port)
        print("Destination IP address:", server_ip)
        print("Destination port number:", server_port)
        print("Message sent:", msg)

        # Show a red progress bar when the process starts
        for _ in tqdm(range(10), desc="Sending", colour='red'):
            time.sleep(0.1)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', source_port))  # Set the source port based on the user input
        sock.sendto(msg.encode(), (server_ip, server_port))
        
        data, addr = sock.recvfrom(1024)
        print("Response received:")
        print(data.decode())

        sock.close()
        print("Process completed successfully.")
    except socket.error as e:
        print("Socket error:", e)
    except Exception as e:
        print("An error occurred:", e)

def main():
    try:
        print("Enter the required information to send the UDP request:")
        source_port = int(input("Enter the source port number: "))
        server_ip = input("Enter the destination IP address: ")
        server_port = int(input("Enter the destination port number: "))
        request_msg = input("Enter the message to send: ")
        
        send_udp_request(source_port, server_ip, server_port, request_msg)
    except ValueError:
        print("Invalid port number. Please enter an integer value for the port number.")
    except KeyboardInterrupt:
        print("\nProcess cancelled by the user.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
