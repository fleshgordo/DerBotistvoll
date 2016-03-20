# -*- coding: utf-8 -*-
from selenium import webdriver
import time, random
from bs4 import BeautifulSoup

specialPages = ["/wiki/Main_Page","/wiki/Help:Category","/wiki/Wikipedia:File_Upload_Wizard", "/wiki/Portal:Current_events","/wiki/Wikipedia:Community_portal","/wiki/Help:Contents","/wiki/Wikipedia:About","/wiki/Special:RecentChanges","/wiki/Special:RecentChangesLinked/","/wiki/Wikipedia:About","/wiki/Wikipedia:General_disclaimer"]
driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Special:Random")

while True:
	time.sleep(2)
	source = driver.page_source
	soup = BeautifulSoup(source)
	#print soup.findAll('a')
	linkList = []
	for link in soup.findAll('a', href=True):
		if link['href'].find('/wiki/') == 0 and link['href'] not in specialPages:
			linkList.append(link['href'])

	# cleanup links
	linkList = filter(lambda x: not x.startswith('/wiki/Talk:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Template:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Category'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Special:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Template_talk:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Portal:Featured_content'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Portal:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/File:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Special:RecentChangesLinked'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Help:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Wikipedia_talk:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/User_talk:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/User:'), linkList)
	linkList = filter(lambda x: not x.startswith('/wiki/Wikipedia:'), linkList)
	


	random.shuffle(linkList)
	newLink = "https://wikipedia.org" + linkList[0]
	print "going to " + newLink
	driver.get(newLink)
	time.sleep(5)
print "waiting ..."
time.sleep(10)
print "closing"
driver.close()
