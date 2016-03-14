# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox('')
driver.get("https://en.wikipedia.org/wiki/Special:Random")

print "waiting ..."
time.sleep(10)
print "closing"
driver.close()
