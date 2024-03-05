import cv2 as cv

#Menggunkana cv.resize untuk meresize ukuran citra

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    print(dimensions)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_CUBIC)

dogsVideo = '../Resources/Videos/dog.mp4'
capture = cv.VideoCapture(dogsVideo)
capture.set(3, 1280)
capture.set(4, 720)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.5)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()