import tweepy, time
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

# create twitter object
api = tweepy.API(auth)

# get WOEID for zurich
zurich = api.trends_closest(47.3,8.5)
zID = zurich[0]['woeid']

# get current trend hashtags
trendsZ = api.trends_place(zID)

for trendsInZueri in trendsZ[0]['trends']:
	print "searching for " + trendsInZueri['name']
	hashTag = trendsInZueri['name'].replace('#','')
	retweet = api.search(trendsInZueri['name'])[0]
	retweetID = retweet.id
	try:
		api.retweet(retweetID)
		print "retweeted: " + retweet.text
	except:
		continue
	print "------"
	time.sleep(2)