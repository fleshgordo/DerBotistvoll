# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time

searchWords = ['hallo','how to kill','my teacher is','what is switzerland']

driver = webdriver.Firefox()
driver.get("https://www.google.ch")

for word in searchWords:
	print "searching for: "  + word
	driver.find_element_by_id("lst-ib").clear()
	driver.find_element_by_id("lst-ib").send_keys(word)
	time.sleep(3)
	source = driver.page_source
	soup = BeautifulSoup(source)
	#for tag in soup.findAll("div", { "class" : "sbqs_c" }):
	for tag in soup.findAll("div", { "class" : "sbqs_c" }):
		print tag.text
	time.sleep(5)


print 'closing browser'
time.sleep(5)
driver.close()