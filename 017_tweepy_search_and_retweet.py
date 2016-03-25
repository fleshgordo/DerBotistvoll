import tweepy, time
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

query = "der bot ist voll"

results = api.search(query)

for result in results:
	print result.text
	print result.id
	api.retweet(result.id)
	print "------"
	time.sleep(2)