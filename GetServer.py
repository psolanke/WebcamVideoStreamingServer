import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import time
from flask import Flask, render_template, Response, g
rgb_cam = None
thermal_cam = None
def create_app():
    app = Flask(__name__)
    app.config["rgb"] = None
    app.config["thermal"] = None
    @app.route('/')
    def index():
        return render_template('index.html')

    def gen(camera):
        ret, frame = camera.read()
        return cv2.imencode('.jpg', frame)[1].tostring()
    
    def destroy_camera(camera):
        if camera == None:
            return
        camera.release()

    def get_camera(id):
        print(id)
        cap = cv2.VideoCapture(id)
        is_connected = False
        connection_timeout = 30
        start_time = time.time()
        while (time.time() - start_time) < connection_timeout:
            print(id)
            cap = cv2.VideoCapture(id)
            is_connected = cap.isOpened()
            if is_connected:
                break
        if is_connected:
            print('Camera Is Connected....')
        else:
            print('Camera Is Not Connected...')
        return cap
   
    @app.route('/setup_rgb_video')
    def setup_rgb_video_feed():
        destroy_camera(app.config['rgb'])
        app.config['rgb'] = get_camera(0)
        return Response('setup Done')

    @app.route('/destroy_rgb_video')
    def destroy_rgb_camera():
        destroy_camera(app.config['rgb'])
        app.config['rgb'] = None

    @app.route('/RGB_video_feed')
    def RGB_video_feed():
        return Response(gen(app.config['rgb']))

    @app.route('/setup_thermal_video')
    def setup_thermal_video_feed():
        destroy_camera(app.config['thermal'])
        app.config['thermal'] = get_camera(1)

    @app.route('/destroy_thermal_video')
    def destroy_thermal_camera():
        destroy_camera(app.config['thermal'])
        thermal_cam = None

    @app.route('/thermal_video_feed')
    def thermal_video_feed():
        return Response(gen(app.config['thermal']))

    @app.route('/get_chunk_size')
    def get_chunk_size():
        return 512

    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
