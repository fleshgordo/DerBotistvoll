# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

driver = webdriver.Firefox()
driver.get("https://www.google.ch/maps/place/View+Rd,+London+N6+4DJ,+Vereinigtes+K%C3%B6nigreich/@51.5779648,-0.1529593,3a,75y,306.58h,90t/data=!3m7!1e1!3m5!1s7zSuwLCG_H9VDTHefa8cBg!2e0!6s%2F%2Fgeo3.ggpht.com%2Fcbk%3Fpanoid%3D7zSuwLCG_H9VDTHefa8cBg%26output%3Dthumbnail%26cb_client%3Dmaps_sv.tactile.gps%26thumb%3D2%26w%3D203%26h%3D100%26yaw%3D320.06158%26pitch%3D0!7i13312!8i6656!4m2!3m1!1s0x48761a4799e86c71:0x54305e42988401c2")
time.sleep(2)
driver.find_element_by_css_selector("canvas.widget-scene-canvas").click()

mapBackground = driver.find_element_by_css_selector("canvas.widget-scene-canvas")

for i in range(200):
	print "step: " + str(i) 
	#driver.find_element_by_css_selector("canvas.widget-scene-canvas").click()
	driver.drag_and_drop("canvas.widget-scene-canvas", "canvas.widget-scene-canvas")
	
	
print "waiting ..."
print "closing"
driver.close()