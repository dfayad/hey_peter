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

#------------speech part------------------
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

print("A moment of silence please..")
with m as source: r.adjust_for_ambient_noise(source)
print("set min energy threshold to {}".format(r.energy_threshold))
while True:
    print("waiting for you to call out my name")
    with m as source:audio = r.listen(source)
    print("okay im listening")
    try: 
        value = r.recognize_google(audio)

        if str is bytes:
            print(u"you said {}".format(value).encode("utf-8"))
            if "hey Peter" in value:
                print("oh hey!")
                os.system('aplay docs/wassup.wav')
                break
        print("that's not my name!")
    
    except sr.UnknownValueError:
        print("oops didnt catch that")

while True:
    print("say something")
    with m as source:audio = r.listen(source)
    print("got it now time to investigate sounds")
    try:
        value = r.recognize_google(audio)

        if str is bytes:
            print(u"you said {}".format(value).encode("utf-8"))
            print(type(value))
            if "weather" in value:
                print("gathering weather info...")
                os.system('aplay docs/Sure.wav')
                break
            
    except sr.UnknownValueError:
        print("oops didnt catch that")

owm = pyowm.OWM('95a141370f399bb06abaa704d3c26a29')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
location = 'Poughkeepsie,US'
observation = owm.weather_at_place(location)
w = observation.get_weather()
status = w.get_status()
currTemp = int(w.get_temperature('celsius')['temp'])
print('Heres the weather:')
print("The current temperature in " + str(location) + " is " + str(currTemp) + "ºC and the status is " + str(status))
observation_list = owm.weather_around_coords(-22.57, -43.12)
#print(observation_list)
