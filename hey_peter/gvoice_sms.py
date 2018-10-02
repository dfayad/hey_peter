#send sms
def send_text(voice):
    

    #phoneNumber = input('Number to send message to: ')
    #text = input('Message text: ')
    phoneNumber = 6073798229 #write number you wanna get
    text = 'Hello from Hey Peter!'

    voice.send_sms(phoneNumber, text)