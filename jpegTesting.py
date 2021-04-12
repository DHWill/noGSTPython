import cv2
import numpy as np
import urllib.request
import socket
import struct

bytes=''
MAX_DGRAM = 2**16


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 5014))
    
while True:
    seg, addr = s.recvfrom(MAX_DGRAM)
    data = struct.unpack(">H", seg)
    #print(seg)
    dataIn = np.frombuffer(seg, dtype=np.uint8)
    bytes += data  
    a = bytes.find(b'\xff\xd8') # JPEG start
    b = bytes.find(b'\xff\xd9') # JPEG end
    print(a, "////", b)
    if a!=-1 and b!=-1:

        jpg = bytes[a:b+2] # actual image
        tytes= bytes[b+2:] # other informations
        
        # decode to colored image ( another option is cv2.IMREAD_GRAYSCALE )
        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR) 
        cv2.imshow('Window name',img) # display image while receiving data
        if cv2.waitKey(1) ==27: # if user hit esc
            exit(0) # exit program