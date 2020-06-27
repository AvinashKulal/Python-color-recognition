import cv2
import numpy as np

#creation of capture object
cap = cv2.VideoCapture(0)
def empty(a):
    pass


cv2.namedWindow("MyTrackbar")
cv2.resizeWindow("MyTrackbar",400,350)
cv2.createTrackbar("HueMin","MyTrackbar",0,255,empty)
cv2.createTrackbar("HueMax","MyTrackbar",255,255,empty)
cv2.createTrackbar("SatMin","MyTrackbar",0,255,empty)
cv2.createTrackbar("SatMax","MyTrackbar",255,255,empty)
cv2.createTrackbar("ValMin","MyTrackbar",0,255,empty)
cv2.createTrackbar("ValMax","MyTrackbar",255,255,empty)

while True:

    success,frame = cap.read()
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HueMin","MyTrackbar")
    h_max = cv2.getTrackbarPos("HueMax","MyTrackbar")
    s_min = cv2.getTrackbarPos("SatMin","MyTrackbar")
    s_max = cv2.getTrackbarPos("SatMax","MyTrackbar")
    v_min = cv2.getTrackbarPos("ValMin","MyTrackbar")
    v_max = cv2.getTrackbarPos("ValMax","MyTrackbar")

    l_bound = np.array([h_min,s_min,v_min])
    h_bound = np.array([h_max,s_max,v_max])

    mask_frame = cv2.inRange(frame_hsv,l_bound,h_bound)
    result_frame = cv2.bitwise_and(frame,frame,mask = mask_frame)

    cv2.imshow("ResultFrame",result_frame)
    cv2.imshow("MaskFrame",mask_frame)
    #cv2.imshow("HsvFrame",frame_hsv)
    cv2.imshow("OriginalFrame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()



