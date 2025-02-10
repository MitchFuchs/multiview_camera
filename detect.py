import os
import cv2
from ultralytics import YOLO
from datetime import datetime
from broadcaster import broadcast

img = 'val_0000003.jpg'

model = YOLO('best.pt')
print('model loaded')
#results = model('tcp://127.0.0.1:8888', stream=True)
results = model('tcp://172.20.67.205:8888', stream=True, verbose=False)
#results = model('demo1.mkv', stream=True)
#results = model(['detect.jpg'])
#results = model('val_0000003.jpg', stream=True)

#model.predict(img, save=True, imgsz=320, conf=0.5)

print('results')

while True:
    for result in results:
        #print(result.orig_img)
        conf = result.boxes.conf
        #probs = result.probs
        #print(len(conf))
        if len(conf) > 0:
            broadcast()
            #img_rgb = cv2.cvtColor(result.orig_img, cv2.COLOR_BGR2RGB) 
            #now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            #cv2.imwrite(f'/mnt/data/primate_detected_{now}.jpg', img_rgb)
