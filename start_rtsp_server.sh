#/bin/bash

libcamera-vid -t 0 --width 1280 --height 720 --inline -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}' :demux=h264
