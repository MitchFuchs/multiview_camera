# listener.py
import os
import socket
import subprocess
from ip_ending import get_last_number

last_ip = get_last_number()
print(f'last ip number is {last_ip}')

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 12345))  # Bind to all interfaces on port 12345

print("Waiting for broadcast")

# Wait for a specific broadcast message
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.decode()
    if message.startswith('START_RECORDING'):
        unique_id = message.split()[1]  # Extract the unique ID
        print(f"Received broadcast from {addr}, starting recording with ID {unique_id}")
        # Replace 'raspivid' with the command you use to start recording
        subprocess.run(["libcamera-vid", "-n", "-o", f"/mnt/data/{last_ip}/video_{unique_id}.h264", "-t", "10000"])
        break  # Exit the loop if necessary, or continue if you expect more commands

sock.close()
