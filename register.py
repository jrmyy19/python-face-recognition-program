from capture import open_webcam
from capture import read_frame
import time 
import cv2 as cv
if __name__ == "__main__":
    video_flow=open_webcam()
    while True :
        webcam_working,frames=read_frame(video_flow)
        if webcam_working ==False:
             break
        else:
            cv.putText(
                frames,
                "regardez tout droit",
                (100,100),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )