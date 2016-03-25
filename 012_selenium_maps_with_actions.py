# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest, time, re

driver = webdriver.Firefox()
driver.get("https://www.google.ch/maps?source=tldso")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
actions.send_keys(Keys.ARROW_UP).perform()
time.sleep(2)
actions.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(2)
actions.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(2)
print "waiting ..."
time.sleep(10)
print "closing"
driver.close()
