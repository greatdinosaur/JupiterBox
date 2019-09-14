import cv2
import time
 
# single funct, return a numpy frame object
def snapShot(camera_idx = 0):# camera_idx default = 0 normally usb = 1 /or you can try with 1,2,3
    cap = cv2.VideoCapture(camera_idx)
    # get a frame
    ret, frame = cap.read()
    cap.release()
    return frame
    
 
# continuously write picture, refresh picture itself
def snapShotCt(camera_idx = 0):# camera_idx default = 0 normally usb = 1 /or you can try with 1,2,3
    cap = cv2.VideoCapture(camera_idx)
    # get a frame
    ret, frame = cap.read()
 
    while ret: 
        cv2.imwrite("./capture.jpg", frame) # write picture 
        time.sleep(5) # delay 1s, delete if possible
        ret, frame = cap.read() # next frame
        break # for test, delete in real use
    cap.release()

while 1:
  snapShotCt()

