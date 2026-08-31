import cv2 as cv
import time

webcam =cv.VideoCapture(0,cv.CAP_AVFOUNDATION)
if not webcam.isOpened():
    print("error : cant acces the webcam")
    exit()
time.sleep(1.0)
for _ in range(20):
    webcam.read()
while True:
    webcam_working , frame = webcam.read()
    if not webcam_working:
        break
    cv.imshow("live webcam",frame)
    if cv.waitKey(1) &0xFF==ord("q"):
        break
cap.release()
cv.destroyAllWindows()