from googlevoice import Voice
import time
from six.moves import input

from gvoice_sms import read_and_resp

from update_json import get_list

voice = Voice()
email = 'hey.peter.rpi@gmail.com' #write email here
pw = input('hey peter pw: ') #write pw here
voice.login(email, pw)

start=time.time()
while True:
    
    #time.sleep(5)

    diff = time.time() - start
    if diff > 5:
        print('5 seconds have passed')
        #define new start
        start=time.time()
        #run new 
        read_and_resp(voice)

print("bye")
