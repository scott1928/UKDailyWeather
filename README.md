# UKDailyWeather

a basic script for reading the weather from dark sky's API. Comparing multiple city's weather to find one colder than the hottest place in the uk, creating a hyperbolic headline and posting it to twitter.

You need to create a folder to store the photos you want in the tweets as well as a auth.py file with your twitter api details

sample auth file:

consumer_key        = 'xxxxxxx'
consumer_secret     = 'xxxxxx'
access_token        = 'xxxxxx'
access_token_secret = 'xxxxxx'

and a config file with your folder name and dark sky api details, sample config.py:

key = 'xxxxxxx'
folder = '/home/pi/UKDailyWeather/pics'