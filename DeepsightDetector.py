import requests 
import argparse 
import cv2      

cap = cv2.VideoCapture(0)

face_api="http://localhost:5000/inferImage?detector=%s&dblScale=%d"%('hog',0)

while True:   
    _, frame = cap.read()  
    r, imgbuf = cv2.imencode(".bmp", frame)    
    image = {'pic':bytearray(imgbuf)}
    r = requests.post(face_api,files=image)
    result = r.json()

    # The result is a list as follows 
    # [{face1},
    #  ...
    # {faceN},
    # {diagnostics}]
    if len(result) < 2:
        print("No detections! Try image with larger face! or try next tutorial with advanced request params") 
    else:    
        faces = result[:-1]
        diag = result[-1]['diagnostics']        
        #print(diag)

        for face in faces:
            rect = [face[i] for i in ['faceRectangle']][0]
            x,y,w,h, confidence = [rect[i] for i in ['left', 'top', 'width', 'height', 'confidence']]

            if confidence < 0.8:
                continue

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,255),5,8)        
                   
        cv2.putText(frame, diag['elapsedTime'], (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
           

    for i,face in enumerate(result[:-1]):
        print("Face %d  "%i, face)
        

    cv2.imshow("face_detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.waitKey(0)
cv2.destroyAllWindows()