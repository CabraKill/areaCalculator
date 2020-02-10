import cv2
from tkinter import *
from PIL import ImageTk, Image
import functionsPy as fn
import imageSegmentation as imgSeg
from imageData import ImageData
from const import version

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

img = fn.resizeImg(cv2.imread("testeArea.jpeg"), 500)
# img = fn.resizeImg(cv2.imread("carregador1.jpg"), 500)
# img = fn.resizeImg(cv2.imread("chaveiroCabuto.jpg"), 500)


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
            "<Button-1>", lambda e: self.click(self.imageCannyData, self.imageCannyDraw, self.imageCannyDrawSlider))
        self.imageCannyDrawSlider = Scale(self.imageCannyDrawFrame, from_=0, to=len(
            self.imageCannyData.contours)-1, orient=HORIZONTAL, command=lambda x: self.imageCannyData.updateImageWidgetDrawed(self.imageCannyDraw, int(x)))
        self.imageCannyDrawSlider.pack()
        # self.imageCannyDrawSlider.bind(command= lambda x:self.imageCannyData.updateImageWidgetDrawed(self.imageCannyDraw,x))

        self.imageCannyMaskPack = fn.packFrameLabelImage(
            self.imageCannyFrame, "Mask", self.imageCannyData.imageMask)
        # self.imageCannyMaskPack.pack()

        self.versionLabel = Label(
            master, text="Dígito " + str(version), bg="cyan")
        self.versionLabel.pack(side="bottom")

    # @staticmethod
    @classmethod
    def click(self, iData, w, slider):
        """ Receives an variable and clicks! """
        """iArray = Image.fromarray(image)
        tkImage = ImageTk.PhotoImage(iArray)
        w.configure(image=tkImage)
        w.image = tkImage"""
        # iData.updateImage(image, w)
        iData.updateImageWidgetDrawed(w, None)
        slider.set(iData.currentIndex)
        self.plotSurface(iData)

    @classmethod
    def plotSurface(self, iDataCurrent):
        mpl.rcParams['legend.fontsize'] = 10

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = []
        y = []
        # print("current x: {}".format(i[0][0][0]))
        for i in iDataCurrent.contours[iDataCurrent.currentIndex][0]:
            x.append(i[0][0])
            y.append(i[0][1])
        #x, y = np.meshgrid(x, y)
        z = np.multiply(x, 0)
        z = np.subtract(z, -1)

        #x,y,z = self.createSurface(x,y,z,square=False)
        #x, y, z = self.createMap(x, y, z)
        #x, y, z = self.createPlane()
        #x, y, z = self.createMap(x, y, z)
        #surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0,antialiased=False, label='3d Visualization')
        x, y, z = self.plot_surface(np.array(x), np.array(y), np.array(z))
        surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0,
                               antialiased=False, label='3d Visualization')

        #x, y, z = self.createMap(x, y, z)
        #surf = ax.contour3D(x, y, z, 50, cmap='binary')
        #x, y, z = self.createMap(x, y, z)
        #surf = ax.plot_wireframe(x, y, z, rstride=5, cstride=5, label='3d Visualization')
        #x, y, z = self.createMap(x, y, z,square=False)
        #surf = ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
        #ax.legend()

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        #ax.set_xlabel('x')
        #ax.set_ylabel('y')
        #ax.set_zlabel('z')
        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #ax.set_title('Surface plot')
        plt.show()

    @classmethod
    def plotArea(self, iDataCurrent):
        mpl.rcParams['legend.fontsize'] = 10

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        z = [0]
        x = []
        y = []
        # print("current x: {}".format(i[0][0][0]))
        for i in iDataCurrent.contours[iDataCurrent.currentIndex][0]:
            x.append(i[0][0])
            y.append(i[0][1])
        print(x)
        print("##")
        print(y)
        # x = [ 10, 20, 30]
        # y = [ 10, 20, 30]

        ax.plot(x, y, z, label='3d Visualization')
        ax.legend()

        plt.show()

    @classmethod
    def drawEverything(self, points):
        for i in points:
            print("current size: {}".format(len(i[0])))
            # print("current array: {}".format(i[0]))
            print("current x: {}".format(i[0][0][0]))
            for j in i[0]:
                x.append(j[0][0])
                y.append(j[0][1])

    @classmethod
    def createSurface(self, areaX, areaY, areaZ, size=300, square=TRUE):
        if(square):
            surfaceX = np.zeros([size, size])
            surfaceY = np.zeros([size, size])
            surfaceZ = np.zeros([size, size])

            for i in range(len(areaX)):
                #print("aqui oooooooo: {}".format(areaX))
                for j in range(len(areaX[i])):
                    surfaceX[69+i][69+j] = areaX[i][j]
            for i in range(len(areaY)):
                for j in range(len(areaY[i])):
                    surfaceY[69+i][69+j] = areaY[i][j]
            for i in range(len(areaZ)):
                for j in range(len(areaZ[i])):
                    surfaceZ[69+i][69+j] = areaZ[i][j]
        else:
            surfaceX = np.ones([size])
            surfaceY = np.ones([size])
            surfaceZ = np.ones([size])

            for i in range(len(areaX)):
                surfaceX[69+i] = areaX[i]
            for i in range(len(areaY)):
                surfaceY[69+i] = areaY[i]
            for i in range(len(areaZ)):
                surfaceZ[69+i] = areaZ[i]
        return [surfaceX, surfaceY, surfaceZ]

    @classmethod
    def plot_surface(self, areaX, areaY, areaZ, size=300):
        """surfaceX = []
        surfaceY = []
        surfaceZ = []
        for i in range(len(areaX)):
            surfaceX.append(areaX)
        for i in range(len(areaY)):
            surfaceY.append(areaZ)
        for i in range(len(areaZ)):
            surfaceZ.append(areaZ)"""
        #surfaceZ = np.zeros([len(areaX),len(areaY)])

        """X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)
        surfaceX = X
        surfaceY = Y
        surfaceZ = Z"""
        areaXX = areaX.copy()
        for i in range(len(areaX)):
            areaXX.append(areaX[i])
        areaYY = areaY.copy()
        np.concatenate(areaYY,areaYY)
        surfaceX, surfaceY = np.meshgrid(areaXX,areaXX)
        #surfaceZ = np.zeros([len(areaX),len(areaY)])
        lineZ = areaZ.copy()
        np.concatenate(lineZ,lineZ)
        surfaceZ = []
        for i in range(len(lineZ)):
            surfaceZ.append(lineZ)
        print("surfacez size:"+str(len(surfaceZ)))
        return [surfaceX, surfaceY, np.array(surfaceZ)]

    @classmethod
    def createMap(self, areaX, areaY, areaZ, size=300, square=True):
        if(not square):
            surfaceX = np.arange(start=0, stop=size)
            surfaceY = np.arange(start=0, stop=size)
            surfaceZ = np.zeros([size])

            for i in range(len(areaX)):
                surfaceX[69+i] = areaX[i]
            for i in range(len(areaY)):
                surfaceY[69+i] = areaY[i]
            for i in range(len(areaZ)):
                surfaceZ[69+i] = areaZ[i]
        else:
            surfaceX = np.arange(start=0, stop=size)
            surfaceY = np.arange(start=0, stop=size)
            surfaceX, surfaceY = np.meshgrid(surfaceX, surfaceY)
            surfaceZ = np.zeros([size, size])

            #surfaceX, surfaceY = np.meshgrid(areaX, areaY)
            #surfaceZ = np.zeros([len(areaX),len(areaY)])

            print("area shape size = x: {} | y: {} | z: {}".format(
                len(areaX), len(areaY), len(areaZ)))
            print("surface shape size = x: {} | y: {} | z: {}".format(
                len(surfaceX), len(surfaceY), len(surfaceZ)))

            for i in range(len(areaX)):
                #print("x: {} | y: {}".format(areaX[i],areaY[i]))
                x = areaX[i]
                y = areaY[i]
                z = areaZ[i]
                #print("zzzzzz " + str(z))
                surfaceZ[x][y] = z

            # for i in range(len(areaX))
        return [surfaceX, surfaceY, surfaceZ]

    @classmethod
    def createPlane(self, size=300):
        surfaceX = np.arange(start=0, stop=size)
        surfaceY = np.arange(start=0, stop=size)
        surfaceX, surfaceY = np.meshgrid(surfaceX, surfaceY)
        print(surfaceX)
        surfaceZ = np.zeros([size, size])
        for i in range(50):
            for j in range(50):
                surfaceZ[139+i][139+j] = 1
        return [surfaceX, surfaceY, surfaceZ]


root = Tk()
Application(root)
root.mainloop()
