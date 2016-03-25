from selenium import webdriver
import time, os

profile = webdriver.FirefoxProfile(os.path.expanduser("~/Library/Application Support/Firefox/Profiles/rp4ltkdp.default/"))
driver = webdriver.Firefox(firefox_profile=profile) 

driver.get('http://www.google.ch')
# schlafe 4sekunden lang
time.sleep(4)
driver.quit()