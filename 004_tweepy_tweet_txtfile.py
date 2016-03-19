# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import serversettings
#argfile = str(sys.argv[1])
 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
filename=open("twitter_text.txt",'r')
f=filename.readlines()
filename.close()
 
for line in f:
	print "next tweet: " + line
	try:
		api.update_status(line)
		time.sleep(10)#Tweet every 15 minutes
	except:
		continue