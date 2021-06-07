import cv2
import numpy as np
import sqlite3
import os
count = 0
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w+10, y+h+10),(233,0,41), 2)
        count += 1
    print(count)
    count = 0
    cv2.imshow('FACE', frame)
    if cv2.waitKey(1) & 0xFF == ord('s') :
        i = 0
        cv2.imwrite(str(i)+ ".png", frame)
        i+= 1
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
cap.release()
cv2.destroyAllWindows()



