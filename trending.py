from twython import Twython
import random
import os
import time
import config
import tweepy

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


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_trends():
    me = api.trends_closest(50.8225,0.1372)
    results = api.trends_place(44418)
    trends = set([trend['name'] for trend in results[0]['trends']])
    trending_string = ""
    for item in trends:
        trending_string = trending_string + str(item) + " "
    return trending_string

