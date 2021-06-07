import cv2
import numpy as np
import imutils
camera_id = 0
video = cv2.VideoCapture(camera_id)
while True:
    ret, frame = video.read()
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binImg = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Contours number found:" + str(len(contours)))
    print(contours[0])

    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    cv2.imshow('video',frame)
    cv2.waitKey()
video.release()
cv2.destroyAllWindows()