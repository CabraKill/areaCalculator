import PIL
import cv2
import imageOperation as iop
import functionsPy as fn


class ImageData:
    """Class to store characteristics of the image pos processing."""

    def __init__(self, imageSource, imageMask, contours, othersFrames=None, imageScale=[1, 1]):
        """Sets the mask image and contours of the current segmentation."""
        self.imageSource = imageSource.copy()
        self.imageMask = imageMask
        self.contours = contours
        self.currentIndex = 0
        self.imageScale = imageScale

    def updateCurrentIndex(self, index):
        if(index == None):
            self.currentIndex = self.currentIndex + \
                1 if self.currentIndex < len(self.contours)-1 else 0
        else:
            print(index)
            self.currentIndex = index

    def updateImage(self, image, w,imageToUpdate=None):
        """Receives an image and widget label to update."""
        iArray = PIL.Image.fromarray(image)
        tkImage = PIL.ImageTk.PhotoImage(iArray)
        w.configure(image=tkImage)
        w.image = tkImage
        imageToUpdate = image

    def drawIndexedContour(self, image, i, drawValues=True):
        """Receives an image and index of contours to draw the contour.\n
        Returns the image drawed."""
        imageCopy = image.copy()
        print("index: {}".format(self.currentIndex))
        print("length: {}".format(len(self.contours)))
        if(len(self.contours) > 0):
            print("contours length: {}".format(len(self.contours[i])))
            print("contour: {}".format([self.contours[i][0][0]]))
            cv2.drawContours(
                imageCopy, [self.contours[i][0]], -1, (0, 255, 0), 3)

            if(drawValues):
                text = "Area: [{}] cm^2".format(self.getArea(index=i))
                print(text)
                #cv2.putText(img=imageCopy, fontScale=0.6, color=(0, 255, 0),text="+",thickness=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(self.contours[i][1], self.contours[i][2]))
                cv2.circle(img=imageCopy, center=(
                    self.contours[i][1], self.contours[i][2]), radius=5, color=(255, 0, 0), thickness=2)
                cv2.putText(img=imageCopy, fontScale=0.8, color=(0, 0, 255),
                            text=text,
                            thickness=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(0, 20))
                #self.drawQuota(imageCopy, point2=(self.contours[i][1], self.contours[i][2]))
                leftmost = tuple(
                    self.contours[i][0][self.contours[i][0][:, :, 0].argmin()][0])
                rightmost = tuple(
                    self.contours[i][0][self.contours[i][0][:, :, 0].argmax()][0])
                topmost = tuple(
                    self.contours[i][0][self.contours[i][0][:, :, 1].argmin()][0])
                bottommost = tuple(
                    self.contours[i][0][self.contours[i][0][:, :, 1].argmax()][0])
                # draw horizontal quota
                iop.drawQuota(image=imageCopy, value=fn.pointDistance(point1=leftmost, point2=(self.contours[i][1], self.contours[i][2]), scale=self.imageScale[1])[1],
                              point2=(self.contours[i][1], self.contours[i][2]), point1=leftmost)
                # draw vertical quota
                iop.drawQuota(image=imageCopy, value=fn.pointDistance(point1=topmost, point2=(self.contours[i][1], self.contours[i][2]), scale=self.imageScale[1])[2],
                              point2=(self.contours[i][1], self.contours[i][2]), point1=topmost, orientation=1)
        return imageCopy

    def updateImageWidgetDrawed(self, w, index):
        """Receives an image and widget.\n
        Automatically updates to the next contour."""
        self.updateCurrentIndex(index)
        # fn.resizeImg(self.drawIndexedContour(self.imageSource, 500)
        #self.updateImage(self.drawIndexedContour(self.imageSource, self.currentIndex), w)
        self.updateImage(fn.resizeImg(self.drawIndexedContour(
            self.imageSource, self.currentIndex), 500), w)

    def drawQuota(self, image, point2, point1=None):
        point1 = [0, 0] if point1 == None else point1
        offSet = 20
        quota = 20
        color = [255, 0, 0]
        thickness = 2
        # horizontal line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet + int(quota/2)), (point2[0]-offSet*0, point2[1]+offSet+int(quota/2)), color, thickness)
        # left line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet), (point1[0]+offSet*0, point2[1]+offSet+quota), color, thickness)

        # right line
        cv2.line(image, (point2[0]-offSet*0, point2[1] +
                         offSet), (point2[0]-offSet*0, point2[1]+offSet+quota), color, thickness)

    def getArea(self, index=None):
        index = index if index != None else self.currentIndex
        #M = cv2.moments(self.contours[index][0])
        #area = M['m00']
        area = cv2.contourArea(self.contours[index][0])
        return area*self.imageScale[0]

    def updateScale(self):
        self.imageScale = fn.imageScale(0.95*0.9, self.getArea())
        print("imageScale = {}".format(self.imageScale))
