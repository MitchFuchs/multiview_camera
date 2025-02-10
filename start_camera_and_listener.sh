#!/bin/bash

# Start libcamera-vid with signal support and output to a file
libcamera-vid -n -t 0 --framerate 60 --width 1920 --height 1080 --initial pause --signal --split --inline -o /mnt/data/202/output%04d.h264 &

# Capture the PID of libcamera-vid
LIBCAMERA_PID=$!

# Wait a bit to ensure libcamera-vid is fully up and running
sleep 5

# Start the Python UDP listener script with the PID as an argument
python /home/pi/udp_listener.py $LIBCAMERA_PID
