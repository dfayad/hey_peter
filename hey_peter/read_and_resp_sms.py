from googlevoice import Voice
import sys
from bs4 import BeautifulSoup
import time
#import cv2

def extractsms(htmlsms) :
    #	Extract all conversations by searching for a DIV with an ID at top level.
    tree = BeautifulSoup(htmlsms, 'lxml')			# parse HTML into tree    class="gc-message-sms-text"
    texts = tree.find_all("span",attrs={'class' : 'gc-message-sms-text'})
    phoneNums = tree.find_all("span",attrs={'class' : 'gc-message-sms-from'})
    
    #print(type(tree))
    #print(texts)
    msgs = []
    for text in texts:
        content = text.text.strip()
        msgs.append(content)
    #print(msgs)

    nums = []
    for phoneNum in phoneNums:
        content = phoneNum.text.strip()
        nums.append(content)

    print(nums)

    return msgs, nums

voice = Voice()
email = 'hey.peter.rpi@gmail.com'
pw = input('hey peter password: ')
voice.login(email,pw)

def thimg():
    voice.sms()
    print("sup")

    messages, phoneNums = extractsms(voice.sms.html)

    if len(phoneNums) == 1:
        phoneNumber = phoneNums[0][2:-1]
        print('only one phone num sent messages')
        print(phoneNumber)
    else:
        phoneNumber = 6073798229

    print("")
    print("")
    if 'groceries' in messages:
        print("extract groceries")
        
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

    #key = cv2.waitKey(1) & 0xFF
    #if key == ord("q"):
    #    break

print("bye")
