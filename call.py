from nexmomessage import NexmoMessage

msg = {
    'reqtype': 'json',
    'api_key':  '47bcdeb1',
    'api_secret': 'd6be33eb',
    'from': '19705500043',
    'to': '+15803998205',
    'text': 'Hello world! Michelle says hi'
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