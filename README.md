This is a Raspberry Pi Project aimed to be my personal Alexa-like smart device.

It uses OpenCV and SpeechRecognition Python libaries and it uses .wav recordings of Peter Romero's voice (college housemate) to respond to commands and execute programs. It originally used PocketSphinx for speech recognition but now it uses Google's speech recognition system so it requires network connectivity.

Here are the specific libraries you need:

For Speech Recognition: SpeechRecognition
https://pypi.org/project/SpeechRecognition/
Make sure to download all the dependencies specified there before the installation.

For Computer Vision: OpenCV
Installing OpenCV on the Raspberry Pi can take a really long time but my College Professor showed me this command that installs a funcitonal version very easily:
$sudo apt-get install libopencv-dev python-opencv

To get weather information PyOWM 
(Python Wrapper for OpenWeatherMap API)
https://github.com/csparpa/pyowm

So far here is what it can do:
1) Respond to you when you say "Hey Peter"

2) Run a motion detection program (using OpenCV) if you stay the command "start motion detection" which is based on this project: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

3) If you say the command "weather" it returns the current temperature (in celsius) and the weather general status (sunny, rainy, cloudy) in the location specified in the weather.py file.

What I plan to implement next:

1) Implement some kind of alarm system so that in case the Pi detects movement in the house it will trigger a countdown and then emit a loud sound unless a keyword is said to the microphone.

2) Integrate all functionalities into a single system. So far every funciton works on a different script and needs to be organized better.

3) Display a funny picture of Peter once the program starts just for funzies hehe

