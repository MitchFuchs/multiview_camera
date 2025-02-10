arecord -D hw:3,0 -f cd -c1 --max-file-time=10 --use-strftime --process-id-file=/home/pi/arecord.pid /mnt/data/audio/%Y-%m-%d-%H-%M-%S.wav
