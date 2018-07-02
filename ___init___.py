from twython import Twython
import random
import version0
import os
import image_picker
import time

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
print("Internet online")

while internet == False:
	print("internet offline at " + time.strftime("%H:%M,%S"))
	time.sleep(1200)
	internet = have_internet()

imgfile = image_picker.img_pick()
message = version0.headline_generator() 
photo = open('/Users/scottkirwan/Documents/api/pics/'+str(imgfile),'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message,media_ids=[response['media_id']])
print("Tweeted: {}".format(message))