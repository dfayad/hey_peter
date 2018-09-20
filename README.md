This is a Raspberry Pi Project aimed to be my personal Alexa-like smart device.

It uses OpenCV and SpeechRecognition Python libaries and it uses .wav recordings of Peter Romero's voice (college housemate) to respond to commands and execute programs. It originally used PocketSphinx for speech recognition but now it uses Google's speech recognition system so it requires network connectivity.

So far here is what it can do:
1) Respond to you when you say "Hey Peter"
2) Run a motion detection program (using OpenCV) if you stay the command "start motion detection" which is based on this project: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

What I plan to implement next:
1) "Peter, How's the weather?"
    Will try to extract the weather of the current location by calling some weather API

2) Implement some kind of alarm system so that in case the Pi detects movement in the house it will trigger a countdown and then emit a loud sound unless a keyword is said to the microphone.

