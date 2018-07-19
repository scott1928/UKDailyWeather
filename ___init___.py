from twython import Twython
import random
import version0
import os
import image_picker
import time
import config

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

try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


internet = have_internet()


while internet == False:
	print("Internet is offline at " + time.strftime("%H:%M,%S"))
	time.sleep(1200)
	internet = have_internet()

print("Internet online and script ran at: " + time.strftime("%H:%M,%S"))
imgfile = image_picker.img_pick()
message = version0.headline_generator() 
photo = open(config.folder+str(imgfile),'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message,media_ids=[response['media_id']])
print("Tweeted: {}".format(message))