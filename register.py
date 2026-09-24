from capture import open_webcam
from capture import read_frame
import time 
import cv2 as cv

instructions=["Look straight ahead.", 
              "Turn your head to the left.",
              "Turn your head to the right.", 
              "Lift your head slightly.", 
              "Lower your head slightly."]
instruction_number=0
starting_time=time.time()
elapsed_time=time.time()-starting_time
if __name__ == "__main__":
    video_flow=open_webcam()
    while True :
        webcam_working,frames=read_frame(video_flow)
        if webcam_working ==False:
             break
        else:
            cv.putText(
                    frames,
                    instructions[instruction_number],
                    (800,500),
                    cv.FONT_HERSHEY_SIMPLEX,
                    2,
                    (0,255,0),
                    2
                    )
            if elapsed_time>=6:
                instruction_number+=1

            cv.imshow("face detection",frames)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    video_flow.release()
    cv.destroyAllWindows()