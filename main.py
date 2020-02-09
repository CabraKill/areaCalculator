import cv2
from tkinter import *
from PIL import ImageTk, Image
import functionsPy as fn
import imageSegmentation as imgSeg
from imageData import ImageData
from const import version

img = fn.resizeImg(cv2.imread("testeAreaB3.jpg"), 500)
#img = fn.resizeImg(cv2.imread("carregador1.jpg"), 500)
#img = fn.resizeImg(cv2.imread("chaveiroCabuto.jpg"), 500)


class Application:
    def __init__(self, master=None):
        self.title = Label(text="Tipos de segmentação")
        self.title.pack()

        self.imageSourceFrame = Frame(master)
        self.imageSourceFrame.pack()
        self.imageSourceLabel = Label(self.imageSourceFrame, text="source")
        self.imageSourceLabel.pack()
        self.imageSource = fn.ImgTk(self.imageSourceFrame, img)
        self.imageSource.pack()

        # Frame of images
        self.imageArea = Frame(master)
        self.imageArea.pack()

        # Frame of CannyImages
        self.imageCannyData = imgSeg.canny(img)
        self.imageCannyFrame = Frame(self.imageArea)
        self.imageCannyFrame.pack(side="left")

        # Frame for Draw
        self.imageCannyDrawFrame = Frame(self.imageCannyFrame)
        self.imageCannyDrawFrame.pack(side="left")
        self.imageCannyDrawLabel = Label(
            self.imageCannyDrawFrame, text="Canny Draw")
        self.imageCannyDrawLabel.pack()
        self.imageCannyDraw = fn.ImgTk(
            self.imageCannyDrawFrame, self.imageCannyData.imageMask)
        self.imageCannyDraw.pack()
        self.imageCannyDraw.bind(
            "<Button-1>", lambda e: self.click(self.imageCannyData, self.imageCannyDraw,self.imageCannyDrawSlider))
        self.imageCannyDrawSlider = Scale(self.imageCannyDrawFrame, from_=0, to=len(
            self.imageCannyData.contours)-1, orient=HORIZONTAL, command=lambda x: self.imageCannyData.updateImageWidgetDrawed(self.imageCannyDraw, int(x)))
        self.imageCannyDrawSlider.pack()
        #self.imageCannyDrawSlider.bind(command= lambda x:self.imageCannyData.updateImageWidgetDrawed(self.imageCannyDraw,x))

        self.imageCannyMaskPack = fn.packFrameLabelImage(
            self.imageCannyFrame, "Mask", self.imageCannyData.imageMask)
        # self.imageCannyMaskPack.pack()
        
        self.versionLabel = Label(master,text= str(version),bg="cyan")
        self.versionLabel.pack(side="bottom")

    # @staticmethod
    @classmethod
    def click(self, iData, w,slider):
        """ Receives an variable and clicks! """
        """iArray = Image.fromarray(image)
        tkImage = ImageTk.PhotoImage(iArray)
        w.configure(image=tkImage)
        w.image = tkImage"""
        #iData.updateImage(image, w)
        iData.updateImageWidgetDrawed(w,None)
        slider.set(iData.currentIndex)


root = Tk()
Application(root)
root.mainloop()
