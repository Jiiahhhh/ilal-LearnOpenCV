import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

cv.waitKey(0) #agar imshow tidak langsung tertutup, 0=tak terbatas

#Reading videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

#Video dijalankan dengan memutar frame 1 per 1

while True:
    #Video dalam 'capture' memuat 2 value: boolean & array
    #boolean = mengindikasikan apakah frame dapat dibaca/tidak {disimpan dalam isTrue}
    #array = isi dari framenya (gambar adalah kumpulan data numerik) {disimpan dalam frame}
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()