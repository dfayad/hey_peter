from googlevoice import Voice
import sys
from bs4 import BeautifulSoup
import time
import cv2
from six.moves import input

def extractsms(htmlsms) :
    #	Extract all conversations by searching for a DIV with an ID at top level.
    tree = BeautifulSoup(htmlsms, 'lxml')			# parse HTML into tree    class="gc-message-sms-text"
    texts = tree.find_all("span",attrs={'class' : 'gc-message-sms-text'})
    #print(type(tree))
    #print(texts)
    msgs = []
    for text in texts:
        content = text.text.strip()
        msgs.append(content)
    #print(msgs)
    return msgs

voice = Voice()
email = 'hey.peter.rpi@gmail.com'
pw = input('hey peter password: ')
voice.login(email,pw)

def thimg():
    voice.sms()
    print("sup")

    messages = extractsms(voice.sms.html)
    print("")
    print("")
    if 'groceries' in messages:
        print("extract groceries")
        phoneNumber = 6073798229
        text = 'heres a list of the groceries: [bread, milk]'
        voice.send_sms(phoneNumber, text)
    else:
        print("do nothing..")

    for message in voice.sms().messages:
        message.delete()
    print("deleted all messages too btw <3")

start=time.time()
while True:
    
    #time.sleep(5)

    diff = time.time() - start
    if diff > 5:
        print('5 seconds have passed')
        #define new start
        start=time.time()
        #run new 
        thimg()

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

print("bye")
