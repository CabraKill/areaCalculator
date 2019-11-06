import cv2

#cap = cv2.VideoCapture("172.20.10.11")
frame = cv2.imread("testeArea.jpeg")
while True:
    #cv2.imshow("Video", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    cv2.imshow("Video Edged", edged)

    contours, hie = cv2.findContours(edged,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    for c in contours:
        #cnt = contours[0]
        M = cv2.moments(c)
        if M['m00'] >= 50 and M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
            cv2.putText(img=frame, fontScale=0.5, color=(255, 0, 0),
                    text="predict: [{}]%".format(M['m00']),
                    thickness=3, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(cx, cy))
            cv2.drawContours(frame, c, -1, (0,255,0), 3)
    cv2.imshow("Video", frame)
    
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
