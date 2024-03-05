import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging (cocok untuk mengatasi noise homogen)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#Gaussian Blur (paling halus)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur (bagus untuk mengatasi salt & pepper noise)
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)