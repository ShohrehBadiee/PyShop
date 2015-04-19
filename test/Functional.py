__author__ = 'mahdi'
from selenium import webdriver

testing_browser = webdriver.Firefox()

testing_browser.get('http://localhost:8000/product/home')

assert 'this is home page' in testing_browser.page_source

#testing_browser.close()




