# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

driver = webdriver.Firefox()
driver.get("https://www.google.ch/maps?source=tldso")
time.sleep(5)
driver.find_element_by_css_selector("canvas.widget-scene-canvas").click()

mapBackground = driver.find_element_by_css_selector("canvas.widget-scene-canvas")


mapBackground.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
mapBackground.send_keys(Keys.ARROW_UP)
time.sleep(1)
	
print "waiting ..."
time.sleep(10)
print "closing"
driver.close()