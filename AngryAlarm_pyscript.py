#Angry_Alarm script
from nexmomessage import NexmoMessage

class Task:

    def __init__(self, n, t, no, iscomp):
        self.name = n
        self.time = t
        self.notes = no
        self.isCompleted = iscomp
        
    def complete():
        isCompleted = true
        
class User:
    
    def __init__(self, n, pho, tsks):
        self.name = n
        self.phone = pho
        self.tasks = tsks
        
def send_text(task):
    if(!task.isCompleted) 
        msg = {
        'reqtype': 'json',
        'api_key': 'e09b4f8d',
        'api_secret': 'e4744669',
        'from': '15013036357',
        'to': '+15803998205',
        'text': 'WHY ARE YOU SUCH A SLACKER?!?!?!'
        }
        sms = NexmoMessage(msg)
        sms.set_text_info(msg['text'])
    
        
    
        
    
        