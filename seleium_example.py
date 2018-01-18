#!/usr/bin/env python3.6

#import required libraries
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox, FirefoxProfile




url = "https://data.gov.in/catalog/company-master-data"
driver = webdriver.Firefox()

# Selenium driver inititalization 
driver.wait = WebDriverWait(driver, 5) #
driver.get(url)
#list_=[]
def looping_pages():
	for i in range(2,7):
		driver.get(url)
		button = driver.find_element_by_link_text(str(i)).click()
		#link = driver.find_element_by_link_text("Bihar")
		#data = link.text
		#list_.append(data)
		time.sleep(5)
looping_pages()

