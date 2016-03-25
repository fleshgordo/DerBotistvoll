# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.nzz.ch")

time.sleep(3)

# scrollTo(x,y)  position in pixels
driver.execute_script("window.scrollTo(0, 1000);")

time.sleep(10)
driver.close()