import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
mask = frame.copy()
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    frameMask = cv2.bitwise_and(mask,frame)
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("VideoGray", imgray)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cnt = contours[4]
    #print(len(cnt))
    cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
