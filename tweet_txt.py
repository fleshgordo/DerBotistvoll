# -*- coding: utf-8 -*-
 
import tweepy, time, sys

#argfile = str(sys.argv[1])

consumer_key = "aH2uQg4ta49gqM2cTwQReT2Uo"
consumer_secret = "Ror7TTREsKH7qzBGCaM0v2KTqvlTWfR1TUnWzghFkeaAyYMkmW"
access_token = "709360177884086272-uEaqXZ5eEHBrfOdV7uYiI1Eyj7q7pT0"
access_token_secret = "rZ3MJ0mvzZh1ZwOlUp4RBL6YX7dDfCbk4NdkqJ8lpLqiS"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
filename=open("./txt/twitter_text.txt",'r')
f=filename.readlines()
filename.close()
 
for line in f:
	print "next tweet: " + line
	try:
		api.update_status(line)
		time.sleep(10)#Tweet every 15 minutes
	except:
		continue