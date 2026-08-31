import cv2 as cv
import time
def open_webcam():
    webcam =cv.VideoCapture(0,cv.CAP_AVFOUNDATION)
    if not webcam.isOpened():
        print("error : cant acces the webcam")
        exit()
    time.sleep(1.0)
    for _ in range(20):
        webcam.read()
    return webcam
def read_frame(webcam):
        webcam_working , frame = webcam.read()
        return webcam_working,frame

if __name__ == "__main__":
    video_flow=open_webcam()
    while True :
        webcam_working,frames=read_frame(video_flow)
        if webcam_working ==False:
            break
        else:
            cv.imshow("webcam",frames)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    video_flow.release()
    cv.destroyAllWindows()