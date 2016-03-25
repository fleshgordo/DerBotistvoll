import tweepy
import pprint
import wikiquote
import random, time
from config import config

pp = pprint.PrettyPrinter(indent=4)

# secret keys 
"""consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = "" """

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
	hashTag = trendsInZueri['name'].replace('#','')
	try: 
		searchQuote = wikiquote.search(hashTag)[0]
		randomComment = random.choice(wikiquote.quotes(searchQuote))
		randomComment = randomComment + ' #' + hashTag
		print "sending out tweet: " + randomComment
		api.update_status(randomComment)
		time.sleep(30)
	except:
		print "tweeting failed ... next try for hashtag" + hashTag
		continue

	print randomComment
	print "-----"