import cv2
import time
class Camera(object):
    def __init__(self, deviceID, connection_timeout):
        print('Initialising')
        self.cap = cv2.VideoCapture(deviceID)
        self.is_connected = False
        self.connection_timeout = connection_timeout
        
        print('Waiting for {} secs for the camera to connect...'.format(connection_timeout))
        start_time = time.time()
        while (time.time() - start_time) < connection_timeout:
            self.cap = cv2.VideoCapture(deviceID)
            self.is_connected = self.cap.isOpened()
            if self.is_connected:
                break
        if self.is_connected:
            print('Camera Is Connected....')
        else:
            print('Camera Is Not Connected...')

    def isConnected(self):
        return self.is_connected

    def getNextFrame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        return cv2.imencode('.jpg', frame)[1].tobytes()

    def showFrame(self, frame):
        if not self.is_connected:
            print('Camera is not connected...')
            return

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def releaseAllResources(self):
        self.cap.release()
        cv2.destroyAllWindows()

