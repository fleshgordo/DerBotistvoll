from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://www.google.ch')

# go fullscreen
ActionChains(driver).send_keys(Keys.F11).perform()

time.sleep(4)
driver.quit()