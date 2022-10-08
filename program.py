import cv2
import numpy as np 

path = "haarcascade_eye.xml"
eyeCascade = cv2.CascadeClassifier(path)

img = cv2.imread('pic.jpg')
height, width = img.shape[:2]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
frame = img

eyes = eyeCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (70, 70))
for (x, y, w, h) in eyes:
    frame[y+10:y+h-10, x:x+w, 0]=np.random.normal(size=(h-20,w))
    frame[y+10:y+h-10, x:x+w, 1]=np.random.normal(size=(h-20,w))
    frame[y+10:y+h-10, x:x+w, 2]=np.random.normal(size=(h-20,w))
        
cv2.imwrite("result.jpg", frame)

res = cv2.resize(frame, (int(width / 4), int(height / 4)))
cv2.imshow('result', res)
cv2.waitKey(0)
