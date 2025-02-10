# listener.py
import os
import glob
import sys
import time
import signal
import socket
import subprocess
from ip_ending import get_last_number

def rename_output(save_dir, unique_id):
    trials = 0
    while len(glob.glob(f'{save_dir}/output*'))<1:
        print('file does not yet exist. Sleeping..')
        time.sleep(1)
        trials +=1
        if trials == 3:
            print('3 failed attempts. Restarting listener.service')
            sys.exit(1)
    list_of_files = glob.glob(f'{save_dir}/output*')
    if len(list_of_files) > 1:
        print('found more than one file')
    elif len(list_of_files) == 1:
        current_file_name = list_of_files[0]
#        latest_file = max(list_of_files, key=os.path.getctime)
        print(current_file_name)
        os.rename(os.path.join(save_dir, current_file_name), os.path.join(save_dir, f'video_{unique_id}.h264'))



recording = False
LIBCAMERA_PID = int(sys.argv[1])

last_ip = None

while last_ip is None:
	last_ip = get_last_number()

save_dir = f'/mnt/data/{last_ip}'

print(f'saving videos in {save_dir}')

counter = 0

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 12345))  # Bind to all interfaces on port 12345

print("Waiting for broadcast")

# Wait for a specific broadcast message
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.decode()
    start_recording, timestamp = message.split()
    if not recording and start_recording == 'True':
        os.kill(LIBCAMERA_PID, signal.SIGUSR1)
        recording = True
        unique_id = timestamp
        print(f"Received broadcast from {addr}, starting recording with ID {unique_id}")
    elif recording and start_recording == 'False':
        os.kill(LIBCAMERA_PID, signal.SIGUSR1)
        recording = False
        rename_output(save_dir, unique_id)
        print(f"Received broadcast from {addr}, stoping recording with ID {unique_id}")
    else:
        print(f"received message {message}, no action undertaken")

sock.close()
