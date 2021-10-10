import numpy as np
import cv2
carsCascade = cv2.CascadeClassifier("resources/cars.xml")
bodyCascade = cv2.CascadeClassifier("resources/haarcascade_fullbody.xml")
img = cv2.imread("resources/car-image.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pedestrians = bodyCascade.detectMultiScale(imgGray,1.1,4)
cars = carsCascade.detectMultiScale(imgGray,1.1,4)


for (x,y,w,h) in pedestrians:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





