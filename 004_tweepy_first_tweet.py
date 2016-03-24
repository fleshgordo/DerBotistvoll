import tweepy, sys
from config import config

#tweettext = "d'isch no imma uhuru in"
#tweettext = sys.argv[1]

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

print api.search("jesuisbot")
# sende einen tweet
#api.update_status(tweettext)
