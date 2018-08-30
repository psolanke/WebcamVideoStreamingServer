import cv2
from cameraUtils import Camera
import numpy as np

camera = Camera(0, 10)

while True:
    frame = camera.getNextFrame()
    camera.showFrame(frame)

camera.releaseAllResources()