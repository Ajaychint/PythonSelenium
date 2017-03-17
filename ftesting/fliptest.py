'''
Created on 17/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
from lib2to3.tests.support import driver
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://seller.flipkart.com/?utm_source=flipkart&utm_medium=website&utm_campaign=sellbutton")
    
    driver.find_element_by_id("useremail").send_keys("halingerachappa@gmail.com")
    driver.find_element_by_id("userphone").send_keys("7353249488")
    driver.find_element_by_id("edit-submit--2").click()
    driver.find_element_by_link_text("/slp/services").click()
    
