import requests
import json

r = requests.get('http://0.0.0.0:5000/video_feed', stream=True)
print(r.encoding)
print('Connected')
for line in r.iter_lines():
    print('Reading')
    if line:
        print('Valid Content')
        decoded_line = line.decode('utf-8')
        print(decoded_line)