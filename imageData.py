import PIL
import cv2
import imageOperation as iop


class ImageData:
    def __init__(self, imageSource, imageMask, contours, othersFrames=None):
        """Sets the mask image and contours of the current segmentation."""
        self.imageSource = imageSource.copy()
        self.imageMask = imageMask
        self.contours = contours
        self.currentIndex = 0

    def updateCurrentIndex(self, index):
        if(index == None):
            self.currentIndex = self.currentIndex + \
                1 if self.currentIndex < len(self.contours)-1 else 0
        else:
            print(index)
            self.currentIndex = index

    def updateImage(self, image, w):
        """Receives an image and widget label to update."""
        iArray = PIL.Image.fromarray(image)
        tkImage = PIL.ImageTk.PhotoImage(iArray)
        w.configure(image=tkImage)
        w.image = tkImage

    def drawIndexedContour(self, image, i, drawValues=True):
        """Receives an image and index of contours to draw the contour.\n
        Returns the image drawed."""
        imageCopy = image.copy()
        print("index: {}".format(self.currentIndex))
        print("contour: {}".format([self.contours[i][0][0]]))
        print("length: {}".format(len(self.contours[i])))
        cv2.drawContours(imageCopy, [self.contours[i][0]], -1, (0, 255, 0), 3)

        if(drawValues):
            M = cv2.moments(self.contours[i][0])
            text = "prediction: [{}]%".format(M['m00'])
            print(text)
            """cv2.putText(img=imageCopy, fontScale=0.6, color=(0, 255, 0),
                        text="+",
                        thickness=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(self.contours[i][1], self.contours[i][2]))"""
            cv2.circle(img=imageCopy, center=(
                self.contours[i][1], self.contours[i][2]), radius=5, color=(255, 0, 0), thickness=2)
            cv2.putText(img=imageCopy, fontScale=0.8, color=(0, 0, 255),
                        text=text,
                        thickness=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(0, 20))
            #self.drawQuota(imageCopy, point2=(self.contours[i][1], self.contours[i][2]))
            iop.drawQuota(image=imageCopy, point2=(
                self.contours[i][1], self.contours[i][2]))
            iop.drawQuota(image=imageCopy, point2=(
                self.contours[i][1], self.contours[i][2]),orientation=1)
        return imageCopy

    def updateImageWidgetDrawed(self, w, index):
        """Receives an image and widget.\n
        Automatically updates to the next contour."""
        self.updateCurrentIndex(index)
        self.updateImage(self.drawIndexedContour(
            self.imageSource, self.currentIndex), w)

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
