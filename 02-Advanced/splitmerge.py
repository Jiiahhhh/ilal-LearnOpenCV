import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8') #untuk mengisi channel warna yang diganti ke 0 (hitam)

b,g,r = cv.split(img) #untuk memisah channel warna dari gambar

blue = cv.merge([b, blank, blank]) #channel warna biru
green = cv.merge([blank, g, blank]) #channel warna hijau
red = cv.merge([blank, blank, r]) #channel warna merah

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r]) #menyatukan semua channel warna
cv.imshow('Merged Image', merged)

cv.waitKey(0)