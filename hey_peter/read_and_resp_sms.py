from googlevoice import Voice
import sys
from bs4 import BeautifulSoup

def extractsms(htmlsms) :
    #	Extract all conversations by searching for a DIV with an ID at top level.
    tree = BeautifulSoup(htmlsms, "lxml")			# parse HTML into tree    class="gc-message-sms-text"
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