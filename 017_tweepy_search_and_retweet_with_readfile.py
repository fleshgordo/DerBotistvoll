import tweepy, time
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

query = "Trump is drumpf"

while True:
	results = api.search(query)
	for result in results:
		print result.text
		#print result.id
		if str(result.id) in open('retweets.txt').read():
			print "already tweeted: " + str(result.id)
		else:
			print "retweet: " + str(result.id)
			f=open('retweets.txt','a')
			f.write(str(result.id) + "\n")
			f.close()
			try:
				api.retweet(result.id)
			except:
				f=open('retweets.txt','a')
				f.write(str(result.id) + "\n")
				f.close()
				continue
		print "------"
		time.sleep(2)
	print "waiting for news ..."
	time.sleep(120)