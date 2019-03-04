import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import requests
import json
import cv2
import numpy as np
from haarCascadeClassifier import HaarFaceDectector
face_detector = HaarFaceDectector()
print('Connected')
count = 0

while True:
    requests.get('http://0.0.0.0:5000/setup_rgb_video')
    for i in range(10000):
        rgb_request = requests.get('http://0.0.0.0:5000/RGB_video_feed')
        rgb_frame = cv2.imdecode(np.fromstring(rgb_request.content, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('RGB_frame', rgb_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
        	cv2.destroyAllWindows()
        	break
    requests.get('http://0.0.0.0:5000/destroy_rgb_video')
    thermal_request = requests.get('http://0.0.0.0:5000/setup_thermal_video')
    for i in range(10000):
        thermal_request = requests.get('http://0.0.0.0:5000/thermal_video_feed')
        thermal_frame = cv2.imdecode(np.fromstring(thermal_request.content, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Thermal_frame', thermal_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
        	cv2.destroyAllWindows()
        	break
    requests.get('http://0.0.0.0:5000/destroy_thermal_video')
    #if count > 3:
    #    print('Detecting')
    #    count = 0
    #    rgb_frame = face_detector.detect_face(rgb_frame)
    
    count += 1 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        
