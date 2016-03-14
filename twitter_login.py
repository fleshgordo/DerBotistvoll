# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

driver = webdriver.Firefox('')
driver.get("https://en.wikipedia.org/wiki/Special:Random")
driver.find_element_by_id("signin-email").clear()
driver.find_element_by_id("signin-email").send_keys("ritzdank")
driver.find_element_by_id("signin-email").clear()
driver.find_element_by_id("signin-email").send_keys("gordo@yugo.at")
driver.find_element_by_id("signin-password").clear()
time.sleep(1)
driver.find_element_by_id("signin-password").send_keys("")
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
print "waiting ..."
time.sleep(10)
print "closing"
driver.close()
