import cv2
import urllib.request
import numpy as np

stream = urllib.request.urlopen('http://localhost:5014?type=.mjpg')
bytes = b''
while True:
    bytes += stream.read(1024)
    a = bytes.find(b'\xff\xd8') #frame starting 
    b = bytes.find(b'\xff\xd9') #frame ending
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('image', img)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
