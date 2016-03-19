from textblob import TextBlob
import tweepy, time, re
from config import config

# Authenticate with Twitter
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

# Load text file
filename=open("./txt/marx2.txt",'r')
text=filename.readlines()
text = ' '.join(text)
filename.close()

blob = TextBlob(text.decode('utf-8'))
tags = blob.tags

for blobs in blob.tags:
	if blobs[1] == 'NNP':
		wordchange = '#'+blobs[0]
		blob = blob.replace(blobs[0],wordchange)
		print "changing: " + wordchange

for sentence in blob.sentences:
	sentence = re.sub('\#+', '#', str(sentence))
	print sentence
	print "--"
	
	try:
		print "next tweet: " + str(sentence)
		api.update_status(sentence)
		time.sleep(120)#Tweet every 15 minutes
	except:
		continue
#blob.translate(to="es")  # 'La amenaza titular de The Blob...'