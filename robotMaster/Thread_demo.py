import cv2
import numpy as np
import threading
import time
def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        c = cv2.waitKey(1)
        if c == ord('q'):
            break
def fun1():
    start_time = time.time()
    count = 0
    while True:
        #print("1111111111")
        print(count)
        count = count + 1
        end_time = time.time()
        #print(start_time - end_time)
        if end_time - start_time > 10:
            break

if __name__ == "__main__":
    t = threading.Thread(target=open_camera,name="Open Camera")
    t.start()

    t2 = threading.Thread(target=fun1,name="fun1")
    t2.start()

    

