import cv2
from PIL import ImageTk, Image
import numpy as np
import tkinter

"""General functions to help and server the code."""


def resizeImg(img, imgSize):
    dim = (int(imgSize * img.shape[1]/max(img.shape)),
           int(imgSize * img.shape[0]/max(img.shape)))
    return cv2.resize(img, dim)


def ImgTk(frame, img):
    """Receives an image;\n"""
    """Returns the Widget ready to pack."""
    img = resizeImg(img, 500)
    iArray = Image.fromarray(img)
    tkImage = ImageTk.PhotoImage(iArray)
    widget = tkinter.Label(frame, image=tkImage)
    widget.image = tkImage
    return widget


def joinImg(iArray):
    img = np.hstack(iArray[0], iArray[1])
    if len(iArray) > 2:
        for i in range(2, len(iArray)-1):
            img = np.hstack(img, iArray[i])
    return img


def packFrameLabelImage(frameMaster, label, image):
    frameimage = tkinter.Frame(frameMaster)
    frameimage.pack()
    labelImage = tkinter.Label(frameimage, text=label)
    labelImage.pack()
    imageWidget = ImgTk(frameMaster, image)
    imageWidget.pack()
    return frameimage


def imageScale(realArea, area):
    "Returns an array with the areaScale and the lengthScale"
    print("realarea: {} | area: {}".format(realArea, area))
    areaScale = realArea/area
    lengthScale = areaScale**0.5
    return [areaScale, lengthScale]


def pointDistance(point1, point2, scale=1):
    """Returns the linear, horizontal and vertical distance , scaled if set, in an array"""
    import math
    linear = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    horizontal = point1[0] - point2[0]
    horizontal = horizontal if horizontal >= 0 else -horizontal
    vertical = point1[1] - point2[1]
    vertical = vertical if vertical >= 0 else -vertical
    return[linear*scale, horizontal*scale, vertical*scale]
