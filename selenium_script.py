import time
from selenium import webdriver
 
driver = webdriver.Chrome('D:\Git_WS\chromedriver')
driver.get('http://www.google.com/');
time.sleep(20)
#driver.quit()