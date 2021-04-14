from __future__ import division
import cv2
import numpy as np
import socket
import struct
import sys
import time

width = 192
height = 108
#MAX_DGRAM = (width * 3) * height
MAX_DGRAM = 2**16
print(MAX_DGRAM)
np.set_printoptions(threshold=sys.maxsize)

def main():

    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 5014))
    
    
    while 1:
        seg, addr = s.recvfrom(MAX_DGRAM)
        dataIn = np.frombuffer(seg, dtype=np.uint8)
        _image = (len(dataIn) - ((width * height)  * 3))
        header, image = dataIn[:_image], dataIn[_image:]
        print("TWOT", seg)

        image = np.frombuffer(image, dtype=np.uint8)
        image = image.reshape(([height, width, 3]))
        cv2.imshow("image",image)
        print(header)
        #print(60/_total)

        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()
            s.close()
            break

if __name__ == "__main__":
    main()

    