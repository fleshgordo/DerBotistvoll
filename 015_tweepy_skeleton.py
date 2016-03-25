import tweepy
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

# create twitter object
api = tweepy.API(auth)