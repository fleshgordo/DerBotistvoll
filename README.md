# Der Bot ist voll

Several web bot projects for course "Der Bot ist voll" using various python libraries (bs4, tweepy, selenium webdriver, wikiquote). Workshop held at Zhdk in March 2016. Follow us on [@zhdkbot](https://www.twitter.com/zhdkbot). Scripts have been tested on osX and GNU/Linux systems.

## Installation Mac
	sudo easy_install pip
	sudo pip install selenium
	sudo pip install tweepy
	sudo pip install bs4

## Installation Linux
	sudo apt-get install python-pip
	sudo pip install selenium
	sudo pip install tweepy
	sudo pip install bs4

## Optionally for NLTK (natural language toolkit)
	sudo pip install textblob
	sudo python -m textblob.download_corpora
	sudo pip install feedparser

## Optionally for wikiquote
	git clone https://github.com/federicotdn/python-wikiquotes.git
	cd python-wikiquotes
	sudo python setup.py install

## Optionally upgrade pip
	sudo pip install --upgrade pip
	sudo pip install requests[security]