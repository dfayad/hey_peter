This is a Raspberry Pi Project aimed to be my personal Alexa-like smart device.

It uses OpenCV and SpeechRecognition Python libaries and it uses .wav recordings of Peter Romero's voice (college housemate) to respond to commands and execute programs. It originally used PocketSphinx due to the fact that it works without internet for speech recognition but now it uses Google's speech recognition system so it requires network connectivity. This also allows for increased new abilities like displaying weather data and sending texts.

Here's the first demo video showing some of the features: https://www.youtube.com/watch?v=FKI37sYgyzY

Here's a demo of the "send text" functionality https://www.youtube.com/watch?v=iQ0sRBOzROM

A better quality version of the send text video: https://www.youtube.com/watch?v=BTft0iFqqok

The current script with the features shown on the video is on: complete_peter_start.py

Here are the specific libraries you need:

For Speech Recognition: SpeechRecognition https://pypi.org/project/SpeechRecognition/ Make sure to download all the dependencies specified there before the installation.

For Computer Vision: OpenCV Installing OpenCV on the Raspberry Pi can take a really long time but my College Professor showed me this command that installs a funcitonal version very easily: $sudo apt-get install libopencv-dev python-opencv

To get weather information PyOWM (Python Wrapper for OpenWeatherMap API) https://github.com/csparpa/pyowm

To send texts (Python Wrapper for Google Voice API) https://github.com/pettazz/pygooglevoice

To receive texts: Install Beautiful Soup and depending if you are using python2 (i am), you might need to install the xml parser ony my raspberry pi i used these commands: "pip install beautifulsoup4" "sudo apt-get install python-lxml"

So far here is what it can do:

Respond to you when you say "Hey Peter"

Run a motion detection program (using OpenCV) if you stay the command "start motion detection" which is based on this project: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

If you say the command "weather" it returns the current temperature (in celsius) and the weather general status (sunny, rainy, cloudy) in the location specified in the weather.py file.

The command "send text" sends "Hello! from Hey Peter!" to any phone number that you want (i think it has to be a US number), you just gotta get a Google Voice account first, and then write your credentials (email, password and target phone number) in the send_text() function of the complete_peter_start.py file.

You can also start a timer by saying "timer 10" where the second parameter is the number of seconds you want the timet to go for.

Groceries: So I always forget to bring a list of groceries whenever i go to the supermarket, so I decided communicating with peter would be the best way to fix that. If you run read_and_resp_sms.py it will act as a server and if you send an sms "groceries" to hey_peter's google phone number, it will respond with a list of groceries it generated from the file 'data.json'. You can also add groceries to the 'data.json' file using hey peter by saying "groceries [item]" in the main program.
Here's the demo for this: https://www.youtube.com/watch?v=0Vh6wX_27kI

What I plan to implement next:

Implement some kind of alarm system so that in case the Pi detects movement in the house it will trigger a countdown and then emit a loud sound unless a keyword is said to the microphone.

Display a funny picture of Peter once the program starts just for funzies hehe

Add music playing functionality. Ex. "Hey Peter, play Despacito." I'm gonna try to use Spotify's API for this.

Keep track of a grocery list that I can access remotely (maybe using Google Voice or Dropbox?)

Hardware

For the complete setup here you can find the links to the amazon stuff I use to develop the project:

Monitor: https://www.amazon.com/gp/product/B00S8W8QMG

Keyboard: https://www.amazon.com/gp/product/B005EOWBHC

HDMI: https://www.amazon.com/gp/product/B014I8SSD0

Mouse: https://www.amazon.com/gp/product/B005EJH6RW

RPi Camera Module https://www.amazon.com/gp/product/B01ER2SKFS

Raspberry Pi: https://www.amazon.com/gp/product/B01CD5VC92

USB Microphone: https://www.amazon.com/gp/product/B00UZY2YQE

SD Card: https://www.amazon.com/Sandisk-Ultra-Micro-UHS-I-Adapter/dp/B073JWXGNT