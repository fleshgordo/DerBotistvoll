# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.google.ch/maps?source=tldso")
time.sleep(10)
driver.close()