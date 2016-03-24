# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.nzz.ch")

time.sleep(1)

scrollEndPos = 5000
steps = 10

print driver.get_window_size()
for y in range(scrollEndPos):
	if y % steps == 0:
		print "scroll to: " + str(y)
		position = "window.scrollTo(0, " + str(y) + ");"
		driver.execute_script(position)

time.sleep(10)
driver.close()
