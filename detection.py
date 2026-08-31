import cv2 as cv 
from capture import open_webcam
from capture import read_frame

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
def detect_faces(frame):

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return faces
if __name__ == "__main__":
    video_flow=open_webcam()
    while True :
        webcam_working,frames=read_frame(video_flow)
        if webcam_working ==False:
             break
        else:
            detect_faces(frames)
            cv.imshow("face detection",frames)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    video_flow.release()
    cv.destroyAllWindows()