import tweepy, time
from config import config
import pprint

pp = pprint.PrettyPrinter(indent=4)
# authenticating twitter consumer key
auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])

api = tweepy.API(auth)

query = "working on my novel"

while True:
	results = api.search(query,lang="en")
	for result in results:
		if str(result.id) in open('retweets.txt').read():
			print "already tweeted: " + str(result.id)
		else:
			print "retweet: " + str(result.id)
			f=open('retweets.txt','a')
			f.write(str(result.id) + "\n")
			f.close()
			try:
				api.retweet(result.id)
				r=open('retweets.md','a')
				r.write(r'\huge ')
				r.write(result.text.encode('utf-8') + '\n')
				r.write(r'\newline\newline ')
				r.write(r'\large ')
				r.write("@" + result.user.screen_name.encode('utf-8') + " at " + result.created_at.strftime('%m/%d/%Y'))
				r.write('\n')
				r.write(r'\newpage')
				r.write('\n')
				#r.write(r'\n')
				r.close()
			except:
				f=open('retweets.txt','a')
				f.write(str(result.id) + "\n")
				f.close()
				continue
		print "------"
		time.sleep(2)
	#print "waiting for news ..."
	time.sleep(120)