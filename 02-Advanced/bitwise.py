import cv2 as cv
import numpy as np
#biasanya dipakai untuk proses segmentasi objek/masking

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) #buat kotak
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1) #buat lingkaran

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND --> interscting regions (pixel yang saling bertemu saja yang akan muncul)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#bitwise OR --> non-intersecting and intersecting regions (semua pixel yang ada akan muncul)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR -> non-intersecting regions (semua pixel yang tidak bertemu saja yang akan muncul)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise Not', bitwise_not)

cv.waitKey(0)