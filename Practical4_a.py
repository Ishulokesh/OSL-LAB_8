import numpy as np
import cv2

img = cv2.imread('./Images/cat.jpg')     # Loading Image
print(img)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)  #Gaussian Blur with size 7*7

median = cv2.medianBlur(img, 5)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

newfilter_5 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

cv2.imshow('Input_Image', img)
cv2.imshow('Gaussian_blur', gaussian)
cv2.imshow('Median_blur', median)
cv2.imshow('Bilateral_blur', bilateral)
cv2.imshow('gray_filter', gray_image)
cv2.imshow('newfilter_5', newfilter_5)


cv2.waitKey(0)

