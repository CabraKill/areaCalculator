import cv2
from imageData import ImageData


def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayBilatel = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(grayBilatel, 30, 200)

    contours, hie = cv2.findContours(
        edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contoursList = []
    for c in contours:
        #cnt = contours[0]
        M = cv2.moments(c)
        if M['m00'] >= 50 and M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #contoursList.append([c, [cx, cy]])
            contoursList.append([c,cx,cy])
    result = ImageData(img,edged, contoursList,[gray,grayBilatel])#contours)
    return result
