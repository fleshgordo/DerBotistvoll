# -*- coding: utf-8 -*-
import random, time
import tweepy
from config import config

# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

# create twitter object
api = tweepy.API(auth)

for line in open('./txt/adjektive.txt','r'):
	adjectives = line.split(', ')
	random.shuffle(adjectives)
	for adjective in adjectives:
		f = open('./txt/adjektive_used.txt','a')
		f.write(adjective + ', ')
		f.close()
		tweet = "der #bot ist voll " + adjective
		print tweet
		try:
			api.update_status(tweet)
		except:
			continue
		randomdelay = random.randint(30,60)
		time.sleep(randomdelay)