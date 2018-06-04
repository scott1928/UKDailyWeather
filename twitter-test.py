from twython import Twython
import random
import version0
import os

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


imgdir = '/Users/scottkirwan/Documents/api/pics/'
print(imgdir)
imgfile = random.choice(os.listdir(imgdir))
print(imgfile)
message = version0.headline_generator() 
photo = open('/Users/scottkirwan/Documents/api/pics/'+str(imgfile),'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=message,media_ids=[response['media_id']])
print("Tweeted: {}".format(message))