# -*- coding: utf-8 -*-
from selenium import webdriver
import time, os

profile = webdriver.FirefoxProfile(os.path.expanduser("~/Library/Application Support/Firefox/Profiles/k9ex01ng.default/"))
driver = webdriver.Firefox(firefox_profile=profile) 

driver.get("https://www.twitter.com")
try:
	driver.find_element_by_id("signin-email").clear()
	driver.find_element_by_id("signin-email").send_keys("milfbar@gmail.com")
	driver.find_element_by_id("signin-password").clear()
	time.sleep(1)
	driver.find_element_by_id("signin-password").send_keys("")
	time.sleep(1)
	driver.find_element_by_xpath("//button[@type='submit']").click()
except:
	pass

time.sleep(2)
driver.find_element_by_id("tweet-box-home-timeline").click()
time.sleep(2)
driver.find_element_by_id("tweet-box-home-timeline").send_keys("in the beginning there was the word")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("(//button[@type='button'])[19]").click()

print "waiting ..."
time.sleep(10)
print "closing"
driver.quit()
