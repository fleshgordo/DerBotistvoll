# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib

query = "test"

driver = webdriver.Firefox()
driver.get("https://images.google.com/")
time.sleep(2)
driver.find_element_by_id("lst-ib").clear()
driver.find_element_by_id("lst-ib").send_keys(query)
driver.find_element_by_name("btnG").click()
time.sleep(2)

source = driver.page_source
soup = BeautifulSoup(source)
i = 0

for tag in soup.findAll("img", { "class" : "rg_i" }):
	filename = "./tmp_img/" + query + str(i) + ".jpg"
	print "downloading file: " + filename
	try:
		urllib.urlretrieve (tag.attrs['src'], filename)
	except:
		continue
	i+=1
	
time.sleep(10)
driver.close()