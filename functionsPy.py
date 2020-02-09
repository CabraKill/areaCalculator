import cv2
from PIL import ImageTk, Image
import numpy as np
import tkinter


def resizeImg(img, imgSize):
    dim = (int(imgSize * img.shape[1]/max(img.shape)),
           int(imgSize * img.shape[0]/max(img.shape)))
    return cv2.resize(img, dim)

# Receives an image
# Returns the Widget ready to pack


def ImgTk(frame, img):
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
