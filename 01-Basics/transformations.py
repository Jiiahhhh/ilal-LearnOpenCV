import cv2
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2) #rotPoint = titik tengah rotasi gambar
        # // = floor division, pembagian yang outputnya akan langsung dibulatkan.
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
    #warpAffine() merupakan fungsi untuk mengimplementasikan transformasi ke citra


# Translation
def translate(img, x, y):
    (height, width) = img.shape[:2] #citra berbentuk array (tinggi, lebar, channels)
    dimensions = (width, height)
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

rotated = rotate(img, -45, )
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

#Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) #INTER_CUBIC mengurangi Aliasing
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

#Cropping
cropped = img[200:300, 1:100] #200:400 = baris, 300:400 = kolom
cv.imshow('Cropped', cropped)

cv.waitKey(0)
