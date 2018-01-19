import re
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import csv
import os


driver = webdriver.Firefox()
url = "https://www.amazon.in/"
driver.get(url)
result = []
def search():
	search_bar = driver.find_element_by_id("twotabsearchtextbox")
	WebDriverWait(driver,5)
	search_input = input("What item would you like to search?")
	search_bar.send_keys(search_input)
	search_bar.send_keys(Keys.RETURN)
	time.sleep(5)

def scrape():
    results_title = driver.find_elements_by_tag_name('h2')
    results_titles = []
    for i in results_title:
    	results_titles.append(i.text)
    print(results_titles)
    #price_titles = []
    #price_title = driver.find_elements_by_xpath('.//span[@class = "currencyINR"]')
    #for i in price_title:
   # price_titles.append(i.text)
    #print(price_titles)

def scrape_all():
	x_path = '//*[@id="result_%d"]/div/div[3]'
	for i in range(1,30):
			x_path_true = x_path % i
			results = driver.find_element_by_xpath(x_path_true)
			result.append(results.text)
	for i in result:
		# look for a string starting with A-Z and match as much as possible until the linebreak
		title = re.search('^[A-Z]+.*',i)
		print(title)


search()
scrape()


