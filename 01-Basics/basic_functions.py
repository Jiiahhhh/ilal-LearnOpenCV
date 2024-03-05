import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Images', img)

# Periksa urutan kanal warna
channel_order = 'BGR' if img[0,0,0] == img[0,0,2] else 'RGB'
print("Urutan kanal warna: ", channel_order)

# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# cv.imshow('Gray2', gray2)

# #Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_REFLECT)
# cv.imshow('Blur', blur)

# #Edge Cascade (deteksi tepi)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image (penebalan garis putih hasil edge)
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)