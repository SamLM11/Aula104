import cv2

img = cv2.imread('butterfly.jpg')

cv2.imshow('BorboletaImg', img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('BorboletaImg', gray)

cv2.waitKey(0)