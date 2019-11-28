import cv2
from PIL import ImageTk, Image
import numpy as np

def resizeImg(img, imgSize):
    dim = (int(imgSize * img.shape[1]/max(img.shape)),int(imgSize * img.shape[0]/max(img.shape)))
    return cv2.resize(img,dim)

def ImgTk(img):
    iArray = Image.fromarray(img)
    tkImage = ImageTk.PhotoImage(iArray)
    return tkImage

def joinImg(iArray):
    img = np.hstack(iArray[0],iArray[1])
    if len(iArray) > 2:
        for i in range(2,len(iArray)-1):
            img = np.hstack(img,iArray[i])
    return img