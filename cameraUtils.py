import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import time

# class SingletonCamera:
#     class __SingletonCamera:
#         def __init__(self):
#             self.camera = Camera(0,60)
#         def getCameraObj():
#             return camera

#     instance = None
#     def __init__(self):
#         if not SingletonCamera.instance:
#             SingletonCamera.instance = SingletonCamera.__SingletonCamera()

#     def getCameraObj():
#         return SingletonCamera.instance.getCameraObj()

class Camera(object):
    def __init__(self, deviceID, connection_timeout):
       # print('Initialising')
        #print(deviceID)
        self.cap = cv2.VideoCapture(deviceID)
        self.is_connected = False
        self.connection_timeout = connection_timeout
        
        #print('Waiting for {} secs for the camera to connect...'.format(connection_timeout))
        #start_time = time.time()
        #while (time.time() - start_time) < connection_timeout:
        #    self.cap = cv2.VideoCapture(deviceID)
        #    self.is_connected = self.cap.isOpened()
        #    if self.is_connected:
        #        break
        #if self.is_connected:
        #    print('Camera Is Connected....')
        #else:
        #    print('Camera Is Not Connected...')

    def isConnected(self):
        return self.is_connected

    def getNextFrame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = cv2.resize(frame, (600, 600)) 
        return frame
        #return cv2.imencode('.jpg', frame)[1].tostring()

    def showFrame(self, name, frame):
        #if not self.is_connected:
        #    print('Camera is not connected...')
        #    return
        #ret, frame = self.cap.read()
        cv2.imshow(name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def releaseAllResources(self):
        #print('Resource Released')
        self.cap.release()

# class Camera(object):

#     instance = None
#     def __init__(self):
#         if not Camera.instance:
#             Camera.instance = Cam(0,30)

#     def getCameraObj(self):
#         print('Get Camera Object Called')
#         return Camera.instance

