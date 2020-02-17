import cv2
from tkinter import *
from PIL import ImageTk, Image
import functionsPy as fn
import imageSegmentation as imgSeg
from imageData import ImageData
from const import version
import pathlib
import imageOperation as iop

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#img = fn.resizeImg(cv2.imread("testeArea.jpeg"), 500)
# img = fn.resizeImg(cv2.imread("carregador1.jpg"), 500)
#img = fn.resizeImg(cv2.imread("chaveiroCabuto.jpg"), 500)
#img = fn.resizeImg(cv2.imread("perfilIsopor4.jpg"), 500)
#img = fn.resizeImg(cv2.imread("photosTest\\pratinho1.jpg"), 500)
img = cv2.imread("photosTest\\pratinho2Q.jpg") #scale: imageScale=[0.41,0.17]
#img = fn.resizeImg(cv2.imread("photosTest\\calda1.jpg"), 500)
# print(str(pathlib.Path(__file__).parent.absolute())+"\\photosTest\\papelão1.jpg")
#img = fn.resizeImg(cv2.imread("photosTest\\papelao1.jpg"), 500)

img = fn.resizeImg(img, 500)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


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
        #self.imageCannyDrawSliderBlur = Scale(self.imageCannyDrawFrame, from_=0, to=10, orient=VERTICAL)
        # self.imageCannyDrawSliderBlur.pack(side="left")
        self.imageCannyDraw = fn.ImgTk(
            self.imageCannyDrawFrame, self.imageCannyData.imageSource)
        self.imageCannyDraw.pack()
        self.imageCannyDraw.bind(
            "<Button-1>", lambda e: self.click(self.imageCannyData, self.imageCannyDraw, self.imageCannyDrawSlider))
        self.imageCannyDraw.bind(
            "<Button-3>", lambda e: self.plotSurface(self.imageCannyData))
        self.imageCannyData.updateImageWidgetDrawed(self.imageCannyDraw, None)

        self.imageCannyDrawScaleButton = Button(self.imageCannyDrawFrame, text="º", command=self.imageCannyData.updateScale)
        self.imageCannyDrawScaleButton.pack(side="right")

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

    @classmethod
    def plotSurface(self, iDataCurrent):
        mpl.rcParams['legend.fontsize'] = 10

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = []
        y = []
        # print("current x: {}".format(i[0][0][0]))
        # print everything
        """for contourIndex in range(len(iDataCurrent.contours)):
            for i in iDataCurrent.contours[contourIndex][0]:
                x.append(i[0][1])
                y.append(i[0][0])"""
        width = iDataCurrent.imageSource.shape[1]
        height = iDataCurrent.imageSource.shape[0]
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_zlim(0, 10)
        print("w: {} heigth: {}".format(width, height))
        for i in iDataCurrent.contours[iDataCurrent.currentIndex][0]:

            pointX = width - 1 - i[0][0]
            pointX = 0 if pointX < 0 else pointX
            pointY = height - 1 - i[0][1]
            pointY = 0 if pointY < 0 else pointY

            x.append(i[0][0])
            y.append(pointY)
        print("oioioioi: {}".format(
            iDataCurrent.contours[iDataCurrent.currentIndex][0][0]))
        #x, y = np.meshgrid(x, y)
        z = np.multiply(x, 0)
        z = np.subtract(z, -1)

        #x,y,z = self.createSurface(x,y,z,square=False)
        #x, y, z = self.createMap(x, y, z)
        #x, y, z = self.createPlane()
        #x, y, z = self.createMap(x, y, z)
        #surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0,antialiased=False, label='3d Visualization')
        #x, y, z = self.plot_surface(np.array(x), np.array(y), np.array(z))
        #surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0,antialiased=False, label='3d Visualization')

        #x, y, z = self.createMap(x, y, z)
        #surf = ax.contour3D(x, y, z, 50, cmap='binary')
        #x, y, z = self.createMap(x, y, z)
        #surf = ax.plot_wireframe(x, y, z, rstride=5, cstride=5, label='3d Visualization')
        #x, y, z = self.createMap(x, y, z,square=False)
        #surf = ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
        x, y, z = self.mapToDivison3D(x, y, z, heigth=1, divisions=50)
        surf = ax.plot(x, y, z, label='Repartições')
        #x, y, z = self.mapToDivison3D(x, y, z, heigth=5, divisions=1)
        #surf = ax.scatter(x, y, z)
        # ax.legend()

        #plt.xlim(0, width)

        # Customize the z axis.
        #ax.set_zlim(-1.01, 1.01)
        # ax.zaxis.set_major_locator(LinearLocator(10))
        # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # ax.set_xlabel('x')
        # ax.set_ylabel('y')
        # ax.set_zlabel('z')
        # Add a color bar which maps values to colors.
        #fig.colorbar(surf, shrink=0.5, aspect=5)
        #ax.set_title('Surface plot')
        plt.show()

    @classmethod
    def mapToDivison3D(self, areaX, areaY, areaZ, heigth, start=0, divisions=100):
        zLine = np.arange(start, heigth, (heigth - start)/divisions)
        surfaceX = areaX.copy()
        surfaceY = areaY.copy()
        surfaceZ = areaX.copy()
        for i in range(divisions):
            surfaceX = np.concatenate((surfaceX, areaX))
            surfaceY = np.concatenate((surfaceY, areaY))
            lineZ = np.full([len(areaX)], zLine[i])
            surfaceZ = np.concatenate((surfaceZ, lineZ))
        print("len = x: {} | y: {} | z: {}".format(
            len(surfaceX), len(surfaceY), len(surfaceZ)))
        print("First point= x:{} | y:{} | z:{}".format(
            areaX[0], areaY[0], zLine[0]))
        print("last point= x:{} | y:{} | z:{}".format(
            areaX[-1], areaY[-1], zLine[-1]))
        return [surfaceX, surfaceY, surfaceZ]

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
            x = []
            y = []
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
        """X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)"""

        doubleAreaX = np.concatenate((areaX, areaX))
        doubleAreaY = np.concatenate((areaY, areaY))
        line0Z = np.zeros([len(areaZ)])
        doubleAreaZ = np.concatenate((areaZ, line0Z))
        print("doubleAreaZ size: {}".format(len(doubleAreaX)))
        surfaceX, surfaceY = np.meshgrid(doubleAreaX, doubleAreaY)
        surfaceZ = []
        for i in range(len(doubleAreaZ)):
            surfaceZ.append(doubleAreaZ)
        # return [X, Y, Z]
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
