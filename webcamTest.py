import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
from cameraUtils import Camera
from YoloFaceDetection import YoloFaceDetection
import numpy as np
import time
count = 0
camera = cv2.VideoCapture(0)
is_connected = False
connection_timeout = 30
start_time = time.time()
while (time.time() - start_time) < connection_timeout:
    camera = cv2.VideoCapture(0)
    is_connected = camera.isOpened()
    if is_connected:
        break
while True:
    _, frame = camera.read()
    cv2.imshow('frame1', frame)
    count += 1 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
