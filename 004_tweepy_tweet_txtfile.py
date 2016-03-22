import tweepy, time
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)
 
filename=open("twitter_text.txt",'r')
f=filename.readlines()
filename.close()
 
for line in f:
	print "next tweet: " + line
	api.update_status(line)
	time.sleep(10)#Tweet every 15 minutes