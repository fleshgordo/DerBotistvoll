from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.google.ch')
# schlafe 4sekunden lang
time.sleep(4)
driver.quit()