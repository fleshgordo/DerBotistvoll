# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.google.ch")
driver.find_element_by_id("lst-ib").clear()
driver.find_element_by_id("lst-ib").send_keys("hallo")
#driver.find_element_by_name("btnG").click()
time.sleep(10)
driver.close()