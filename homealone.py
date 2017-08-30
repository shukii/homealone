from picamera import PiCamera
from gpiozero import Button
from gpiozero import MotionSensor 
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

camera = PiCamera()
button = Button(27)
sense = MotionSensor(21)
count = 0

print("System armed!")

def captureAndTweet():
    message = "Intruder alert!! Do you recognise this mug?"
    camera.capture("/home/pi/button.jpg")
    with open("/home/pi/button.jpg", 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)
    print("Tweeted: %s" % message)
    global count 
    count += 1

while True and count < 3:
    button.when_pressed = captureAndTweet
    sense.when_motion = captureAndTweet