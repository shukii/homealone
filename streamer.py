from twython import TwythonStreamer

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            
            
    def on_error(self, status_code, data):
        print("error:", status_code, data)
        #self.disconnect()

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='#')