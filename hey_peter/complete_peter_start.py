#coding: utf-8
import pyowm
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
#import spotipy

#for weather
from weather import get_weather

#for groceries
from groceries import add_grocery

#for timer
from timer import timer

#for texts
from gvoice_sms import send_text
from gvoice_sms import read_texts


#---------for sms------------
from six.moves import input
from googlevoice import Voice
from bs4 import BeautifulSoup #to parse sms
voice = Voice()
email = 'hey.peter.rpi@gmail.com' #write email here
pw = input('hey peter pw: ') #write pw here
voice.login(email, pw)

#------------speech part------------------
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()
print("A moment of silence please..")
with m as source: r.adjust_for_ambient_noise(source)

#motion detection function
from motion_detection import motion_detection



start= time.time()
while True:
    #polling loop every 5 seconds
    diff = time.time() - start
    if diff > 5:
        print('5 seconds have passed')
        #define new start
        start=time.time()
        #run new 
        #read_texts(voice)
    
    #loop over speech here
    print("okay im listening")
    with m as source:audio = r.listen(source)
    print("okay im thinking")
    try: 
        value = r.recognize_google(audio)

        if str is bytes:
            print(u"you said {}".format(value).encode("utf-8"))
            
            #DETECTED A HELLO
            if "hey Peter" in value:
                print("oh hey!")
                os.system('aplay docs/wassup.wav')

            elif "weather" in value:
                print("weather? sure!")
                os.system('aplay docs/Sure.wav')
                print(get_weather())
                        
            elif "thank" in value:
                print("no problem buddy")
                os.system('aplay docs/Sure.wav')

            elif "start motion detection" in value:
                print("weather? sure!")
                os.system('aplay docs/Sure.wav')
                print(motion_detection())

            elif "send text" in value:
                print("sending text...")
                os.system('aplay docs/Sure.wav')
                send_text(voice)

            elif "timer" in value:
            	print("starting timer...")
            	os.system('aplay docs/Sure.wav')
            	string_value = str(value)
            	l = string_value.split(" ")
            	secs = int(l[1])
            	timer(secs)

            elif "grocer" in value:
                #so it catches grocery or groceries
                print("adding to grocery list...")
                os.system('aplay docs/Sure.wav')
                string_value = str(value)
                arr = string_value.split(" ")
                grocery_item = arr[1:]
                s=""
                for word in grocery_item:
                    s=s+str(word)
                add_grocery(s)

            elif ("exit" in value) or ("bye" in value):
                print("oh ok gbye i'll miss you")
                os.system('aplay docs/Sure.wav')
                break
    
    except sr.UnknownValueError:
        print("oops didnt catch that")
            
    #exit
