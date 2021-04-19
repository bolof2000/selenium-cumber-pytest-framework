from selenium import webdriver
import time
import pdb

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="C:\Users\hersh\Documents\Automation and Code\UI-automation\ui-automation\drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demostore.supersqa.com/")
driver.implicitly_wait(5)

test1 = driver.find_element_by_link_text('My account')
text = driver.find_element_by_link_text('My account').text
result1 = test1.get_attribute('href')
result2 = driver.find_element_by_link_text('My account').get_property('href')
result3 = driver.find_element_by_link_text('My account').size

driver.quit()

pdb.set_trace()
