from tkinter import *
from PIL import ImageTk, Image
import os
import cv2
import functions as fn
imgSize = 300



class Application:
    def __init__(self, master=None):
        self.frame = Frame(master)
        self.frame.pack()

        #img = ImageTk.PhotoImage(Image.open("testeArea.jpeg"))
        img = cv2.imread('testeArea.jpeg')
        dim = (int(imgSize * img.shape[1]/max(img.shape)),int(imgSize * img.shape[0]/max(img.shape)))
        self.img = cv2.resize(img,dim)
        self.iArray = Image.fromarray(self.img)
        self.tkImage = ImageTk.PhotoImage(self.iArray)
        self.a = cv2.imread("testeArea.jpeg")
        self.a = fn.resizeImg(self.a,imgSize)
        self.atk = fn.ImgTk(self.a)
        self.panel = Label(self.frame, image = self.atk)
        self.panel.image = self.atk
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

        self.txt = Label(self.frame,text="oiiiiiiiii")
        self.txt.pack()

root = Tk()
root.geometry("500x500")
Application(root)
root.mainloop()

