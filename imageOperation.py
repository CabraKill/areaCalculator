import cv2
"""Functions to work visualy on the image."""

def drawQuota(image, value, point2, point1=None, orientation=0):
    """Draws a quota on the image. 0 for horizontal and 1 for vertial """
    point1 = [0, 0] if point1 == None else point1
    offSet = 20
    quota = 20
    color = [255, 0, 0]
    thickness = 2
    middlex = (point1[0] - point2[0])/2
    middlex = middlex if middlex >= 0 else -middlex
    middlex = int(middlex + point1[0])
    middley = point2[1] + offSet + int(quota/2) + 5
    if(not orientation):
        # horizontal line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet + int(quota/2)), (point2[0]-offSet*0, point2[1]+offSet+int(quota/2)), color, thickness)
        # left line
        cv2.line(image, (point1[0]+offSet*0, point2[1] +
                         offSet), (point1[0]+offSet*0, point2[1]+offSet+quota), color, thickness)

        # right line
        cv2.line(image, (point2[0]-offSet*0, point2[1] +
                         offSet), (point2[0]-offSet*0, point2[1]+offSet+quota), color, thickness)
        cv2.putText(img=image, fontScale=0.5, color=color,
                    text=str(value),
                    thickness=1, fontFace=cv2.FONT_HERSHEY_SIMPLEX, org=(middlex, middley))
    else:
        # horizontal end line
        cv2.line(image, (point2[0]+offSet, point2[1] +
                         offSet*0), (point2[0]+offSet+quota, point2[1]+offSet*0), color, thickness)

        # vertical line
        cv2.line(image, (point2[0]+offSet + int(quota/2), point1[1] +
                         offSet*0), (point2[0]+offSet + int(quota/2), point2[1]+offSet*0), color, thickness)

        # horizontal start line
        cv2.line(image, (point2[0]+offSet, point1[1] +
                         offSet*0), (point2[0]+offSet+quota, point1[1]+offSet*0), color, thickness)
