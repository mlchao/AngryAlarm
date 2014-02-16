#Angry_Alarm script
from nexmomessage import NexmoMessage
import urllib2

class Task:

    def __init__(self, n, t, no, iscomp):
        self.name = n
        self.time = t
        self.notes = no
        self.isCompleted = iscomp
        
    def complete(self):
        self.isCompleted = True
        
class User:
    
    def __init__(self, n, pho, tsks):
        self.name = n
        self.phone = pho
        self.tasks = tsks
        
    def send_text(self):
        
        msg = {
            'reqtype': 'json',
            'api_key':  '47bcdeb1',
            'api_secret': 'd6be33eb',
            'from': '19705500043',
            'to': '13477597022',
            'text':'WHY ARE YOU SUCH A SLACKER?!?!?!'
            }
        sms = NexmoMessage(msg)
        sms.set_text_info(msg['text'])
        response = sms.send_request()

        if response:
             # do something with response data
            print('worked')
        else:
            # handle the error
            print('nope')

    def call(self):
        url_request='https://rest.nexmo.com/tts/json?api_key=47bcdeb1&api_secret=d6be33eb&from=19705500043&to=13477597022&text=DO+YOUR+WORK+NOW' 
        f=urllib2.urlopen(url_request)
        print(f.read())
        print (f.getcode())

 #test script
if __name__ =='__main__':

    mytask=Task('do homework', '2/17', '', False)
    me=User('michelle','8327557056', mytask)
    
    if me.tasks.isCompleted==False:
        print('in loop')
       # me.send_text()

    me.call()