# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import datetime

response = urllib2.urlopen('https://twitter.com/zhdkbot')

html = response.read()
soup = BeautifulSoup(html, "lxml")

tweets = soup.find_all('li', 'js-stream-item')

#print tweets
tweet_text = soup.find_all('p', 'js-tweet-text')
tweet_links = soup.find_all('a', 'js-details')

for i in range(0, len(tweet_text)):
    text = tweet_text[i].get_text().encode('ascii', 'ignore')
    print text

    #link = 'https://twitter.com' + tweet_links[i]['href']