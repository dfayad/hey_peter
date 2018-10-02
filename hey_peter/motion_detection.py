from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os
import subprocess

import datetime

def motion_detection():
    #inintalize camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    rawCapture = PiRGBArray(camera, size=(640, 480))

    #allow camera to warmup
    print("warming up...")
    time.sleep(2.5)

    #initalize first frame in the video
    firstFrame = None

    #capture frames from the camera
    for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        
        #grab frame
        frame = f.array
        #set default as unoccupied
        text = "Unoccupied"

        #TURN THE FRAME INTO GRAYSCALE BECAUSE ONLY WAY WE CAN THRESHOLD
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21,21), 0) #not sure why we blur it

        #if first frame is none then initialize it
        if firstFrame is None:
            firstFrame = gray
            rawCapture.truncate(0)
            continue
            

        #compute the absolute difference between the current frame and the first frame
        frameDelta = cv2.absdiff(firstFrame, gray)

        #SET THE THRESHOLD AT 25, ANY VALUE OVER 25 IS SET TO 255
        #FIRST OUTPUT [0] IS RETVAL
        #SECOND OUTPUT IS THE THRESHOLDED IMAGE
        thresh  = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        #dilate the thresholded image to fill in the holes, then find contours
        # on the thresholded image
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        #loop over the contours
        for c in cnts:
            if cv2.contourArea(c) < 800 or cv2.contourArea(c) > 100000:
                print("nothing to see here")
                continue

            print("hello intruder")

            #compute the bounding box for the contour, draw it on the frame and update text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            text = "Occupied"

        #draw the text and timestamp on the frame
        cv2.putText(frame, "Room Status: {}".format(text), (10,20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %I %M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,255), 1)

        #SHOW THE FRAME AND RECORD IF THE USER PRESSES A KEY
        cv2.imshow("Security Feed", frame)
        cv2.imshow("Thresh", thresh)
        cv2.imshow("Frame Delta", frameDelta)
        key = cv2.waitKey(1) & 0xFF

        #if the q key is pressed break from the loop
        if key==ord("q"):
            break

        rawCapture.truncate(0)

    #cleanup th ecamera and close any open windows
    camera.close()
    cv2.destroyAllWindows()
