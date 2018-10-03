from bs4 import BeautifulSoup
from six.moves import input
from update_json import get_list

#send sms
def send_text(voice):
    

    #phoneNumber = input('Number to send message to: ')
    #text = input('Message text: ')
    phoneNumber = 6073798229 #write number you wanna get
    text = 'Hello from Hey Peter!'

    voice.send_sms(phoneNumber, text)


#read sms
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

#check for incoming groceries text
def read_and_resp(voice):
    voice.sms()
    print("sup")

    messages = extractsms(voice.sms.html)
    print("")
    print("")
    if 'groceries' in messages:
        print("extract groceries")
        phoneNumber = 6073798229
        text = str(get_list('data.json'))
        #text = 'heres a list of the groceries: [bread, milk]'
        voice.send_sms(phoneNumber, text)
    else:
        print("do nothing..")

    for message in voice.sms().messages:
        message.delete()
    print("deleted all messages too btw <3")
