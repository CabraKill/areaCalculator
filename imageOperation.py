import cv2
import numpy as np
"""Functions to work visualy on the image."""


def drawQuota(image, value, point2, point1=None, orientation=0):
    """Draws a quota on the image. 0 for horizontal and 1 for vertial """
    point1 = [0, 0] if point1 == None else point1
    offSet = 20
    quota = 20
    color = [255, 0, 0]
    thickness = 2
    value = '%.5f' % (value)

    if(not orientation):
        middlex = (point1[0] - point2[0])/2
        middlex = middlex if middlex >= 0 else -middlex
        middlex = int(middlex + point1[0])
        middley = point2[1] + offSet + quota + 10
        # horizontal line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet + int(quota/2)), (point2[0]-offSet*0, point2[1]+offSet+int(quota/2)), color, thickness)
        # left line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet), (point1[0]+offSet*0, point2[1]+offSet+quota), color, thickness)
        # right line
        cv2.line(image, (point2[0]-offSet*0, point2[1] +
                         offSet), (point2[0]-offSet*0, point2[1]+offSet+quota), color, thickness)
        # Text
        cv2.putText(img=image, fontScale=0.5, color=color,
                    text=str(value),
                    thickness=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(middlex, middley))
    else:
        middlex = point2[0] + offSet + quota + 10
        middley = int((point1[1] - point2[1])/2)
        middley = middley + point2[1]

        # horizontal top line
        cv2.line(image, (point2[0]+offSet, point2[1] +
                         offSet*0), (point2[0]+offSet+quota, point2[1]+offSet*0), color, thickness)
        # vertical line
        cv2.line(image, (point2[0]+offSet + int(quota/2), point1[1] +
                         offSet*0), (point2[0]+offSet + int(quota/2), point2[1]+offSet*0), color, thickness)
        # horizontal bottom line
        cv2.line(image, (point2[0]+offSet, point1[1] +
                         offSet*0), (point2[0]+offSet+quota, point1[1]+offSet*0), color, thickness)
        # Text
        cv2.putText(img=image, fontScale=0.5, color=color,
                    text=str(value),
                    thickness=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(middlex, middley))


def blur(img, blur=(5, 5)):
    """Receives an image and an array with blur.\n"""
    """Returns an image with blur"""
    kernel = np.ones(blur, np.float32)/(blur[0]*blur[1])
    dst = cv2.filter2D(img, -1, kernel)
    return dst
