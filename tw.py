import tweepy
from random import choice
from time import sleep

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
since_id = 1

twt = api.search_users(q="introoderalrt")

twt = api.user_timeline(screen_name = "introoderalrt", since_id = since_id, count=1)
for t in twt:
    print("Found!")
    print(t)
    print(t.text)
    print(t.status_id)
    since_id = t.status_id
    
