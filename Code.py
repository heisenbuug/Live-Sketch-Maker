import cv2
import numpy as np


def sketch(image):
   
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    imgGrayBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    
    canny_edges = cv2.Canny(imgGrayBlur, 10, 70) 
    
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV) 
    return mask
    
capture = cv2.VideoCapture(0)

while True:
    ret, frames = capture.read()
    cv2.imshow('Live Sketcher Maker', sketch(frames))
    if cv2.waitKey(1) == 13: 
        break

capture.release()   
cv2.destroyAllWindows()
