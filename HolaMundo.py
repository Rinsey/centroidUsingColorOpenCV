import cv2
import numpy as np

lower = np.array([15,125,20])
upper = np.array([35,255,255])

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour)>1200:
                x, y, w, h = cv2.boundingRect(contour) 
                M = cv2.moments(mask)
                cX = int (M["m10"]/M["m00"])
                cY = int (M["m01"]/M["m00"])
                cv2.circle(img,(cX,cY),5, (0,0,255),-1)

    cv2.imshow("mask", mask)
    cv2.imshow("webcam", img)

    cv2.waitKey(1)





