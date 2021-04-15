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
    
    
<<<<<<< HEAD
    #while 1:
    seg, addr = s.recvfrom(MAX_DGRAM)
    #print(seg >> 0 & 8)
    dataIn = np.frombuffer(seg, dtype=np.uint8)
    packetInfo, header = dataIn[:12], dataIn[12:]
    header, _image = header[:8], header[8:]
    width, height = header[6] * 8, header[7] * 8
    print(header)
    print("width:", width)
    print("height:", height)
    print("qVAL:", header[5])
    header, _image = _image[:8], _image[8:]
    print("QHEAD", header)
    quantTableHeader = header[4:]
    print("quantTableHeader:", quantTableHeader)
    quantTableLength = quantTableHeader[3]
    print("quantTableLength:", quantTableLength)
    quantizationTable, _image = _image[:quantTableLength], _image[quantTableLength:]
    print("quantizationTable:", quantizationTable)
=======
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
>>>>>>> 780081fea657bc97b9d3f42896e8a2deb5adfaa6

    print("image length", len(_image))
    print("image", _image)
    #print(dataIn)
    #_image = (len(dataIn) - ((width * height)  * 3))
    #print(image)
    #image = image.reshape(([height, width, 3]))
    #print(header)
    
    #image = cv2.imdecode(dataIn, cv2.IMREAD_ANYCOLOR)
    #
    image = cv2.imdecode(_image, 1)
    image.reshape(width, height)
    print(image)
    cv2.imshow("image",image)
    
    #print(image)
    #print(60/_total)
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        s.close()
        #break

if __name__ == "__main__":
    main()

    