from cameraUtils import Camera
from GetServer import create_app
print('Loads The whole file again')
if __name__ == '__main__':
    print('Creating APP') 
    app = create_app()
    app.run(host='0.0.0.0', use_reloader=False)
