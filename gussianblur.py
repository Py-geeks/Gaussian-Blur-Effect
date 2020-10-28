import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png")

#GUSSIAN BLUR EFFECT
gauss = cv2.GaussianBlur(img,ksize=(15,15),sigmaX=0,sigmaY=0)
print('Gaussian Blur Applied.')

#comparing original vs gauusian blur
cv2.imshow('original',img)
cv2.imshow('gauss',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
