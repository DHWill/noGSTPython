import cv2
import urllib.request
import numpy as np

with urllib.request.urlopen('   ') as stream:

#stream = urllib.urlopen('http://localhost:5014')
    bytes = ''
    while True:
        bytes += stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
            cv2.imshow('i', i)
            if cv2.waitKey(1) == 27:
                exit(0)  