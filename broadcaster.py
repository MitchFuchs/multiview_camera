# broadcaster.py
import socket
import time

def broadcast():

    # Create a unique ID (timestamp in this case)
    unique_id = str(time.time())

    # Message to be broadcasted
    message = f'START_RECORDING {unique_id}'.encode()

    # Set up the UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send the broadcast message
    sock.sendto(message, ('<broadcast>', 12345))
    sock.close()

    print("Broadcast message sent with ID:", unique_id)


if __name__ == "__main__":
    broadcast()
