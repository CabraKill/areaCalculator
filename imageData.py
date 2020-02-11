import PIL
import cv2


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
            cv2.putText(img=imageCopy, fontScale=0.5, color=(0, 255, 0),
                        text=text,
                        thickness=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(self.contours[i][1], self.contours[i][2]))
        return imageCopy

    def updateImageWidgetDrawed(self, w, index):
        """Receives an image and widget.\n
        Automatically updates to the next contour."""
        self.updateCurrentIndex(index)
        self.updateImage(self.drawIndexedContour(
            self.imageSource, self.currentIndex), w)
