import cv2 as cv 
img=cv.imread("senegal-flag.jpg")
# converting to greyscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("greyscaled",gray)
cv.waitKey(0)


import cv2 as cv
img= cv.imread("senegal-flag.jpg")
def rescaleImage(frame,scale=0.75):
    # image photo and live video
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0]*scale)
    dimensions= (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def changeResolution(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)
 

rescaledPhoto=rescaleImage(img)
cv.imshow("senegal",rescaledPhoto)

capture= cv.VideoCapture("video.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleImage(frame,scale=0.1)

    cv.imshow("video", frame)
    cv.imshow("video resized",frame_resized)
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows 
