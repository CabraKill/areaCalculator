import cv2
from tkinter import *
from PIL import ImageTk, Image
import functionsPy as fn
import imageSegmentation as imgSeg

img = fn.resizeImg(cv2.imread("testeArea.jpeg"),500)
class Application:
    def __init__(self, master=None):
        self.title = Label(text="Tipos de segmentação")
        self.title.pack()

        self.imageSourceFrame = Frame(master)
        self.imageSourceFrame.pack()
        self.imageSourceLabel = Label(self.imageSourceFrame,text="source")
        self.imageSourceLabel.pack()
        self.imageSource = fn.ImgTk(self.imageSourceFrame,img)
        self.imageSource.pack()

        self.imageArea = Frame(master)
        self.imageArea.pack()
        
        self.imageCannyFrame = Frame(self.imageArea)
        self.imageCannyFrame.pack(side="left")
        self.imageCannyLabel = Label(self.imageCannyFrame,text="Canny")
        self.imageCannyLabel.pack()
        self.imageCanny = fn.ImgTk(self.imageCannyFrame,imgSeg.canny(img))
        self.imageCanny.pack()
        
        """iArray = Image.fromarray(fn.resizeImg(cv2.imread("testeArea.jpeg"),300))
        tkImage = ImageTk.PhotoImage(iArray)
        widget = Label(self.imageArea,image = tkImage)
        widget.image = tkImage
        self.image = widget"""
        
        
root = Tk()
Application(root)
root.mainloop()
