import cv2
import numpy

class HaarFaceDectector(object):
    def __init__(self):
        self.profile_face_cascade = cv2.CascadeClassifier('./haarCascades/profileFace.xml')
        self.frontal_face_cascade = cv2.CascadeClassifier('./haarCascades/frontalFaceHaar.xml')
    
    def detect_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        profile_faces = self.profile_face_cascade.detectMultiScale(gray, 1.3, 5)
        frontal_faces = self.frontal_face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in profile_faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        for (x,y,w,h) in frontal_faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        return frame