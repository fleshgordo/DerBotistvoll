# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.google.com")

# save current window focus
main_window = driver.current_window_handle

# open new tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

# Load a page in second tab 
driver.get('http://www.duckduckgo.com')

time.sleep(2)

for i in range(100):
	# switch tabs
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB) 
	# put focus back onto main window
	driver.switch_to_window(main_window)
	time.sleep(1)

# close the tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 

time.sleep(2)
driver.quit()