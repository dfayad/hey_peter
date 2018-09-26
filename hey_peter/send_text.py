from six.moves import input
from googlevoice import Voice


def run():
    voice = Voice()
    email = 'some@email' #write email here
    pw = 'some_pw' #write pw here
    voice.login(email, pw)

    #phoneNumber = input('Number to send message to: ')
    #text = input('Message text: ')
    phoneNumber = 6073798229
    text = 'sup'

    voice.send_sms(phoneNumber, text)

run()
#__name__ == '__main__' and run()
