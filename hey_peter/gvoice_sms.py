from bs4 import BeautifulSoup
from six.moves import input
from update_json import get_list
from update_json import delete_items

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
    phoneNums = tree.find_all("span", attrs={'class': 'gc-message-sms-from'})
    #print(type(tree))
    #print(texts)
    msgs = []

    for text in texts:
        content = text.text.strip()
        msgs.append(content)
    #print(msg)

    nums = []
    for phoneNum in phoneNums:
        content = phoneNum.text.strip()
        nums.append(content)

    return msgs, nums

#check for incoming groceries text
def read_and_resp(voice):
    voice.sms()
    print("sup")

    messages, nums = extractsms(voice.sms.html)
    print("nums"+str(nums))
    if len(nums)==1:
        phoneNum=nums[0][2:-1]
    else:
        phoneNum=6073798229
    print("")
    print("")
    if 'groceries' in messages:
        print("extract groceries")
        phoneNumber = phoneNum
        text = str(get_list('data.json'))
        #text = 'heres a list of the groceries: [bread, milk]'
        voice.send_sms(phoneNumber, text)

    elif 'delete groceries' in messages:
        delete_items('data.json')
        voice.send_sms(phoneNum, 'deleted grocery list')

    else:
        print("do nothing..")

    for message in voice.sms().messages:
        message.delete()
    print("deleted all messages too btw <3")
