import driver as driver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from InitAppiumDriver import desired_Cap
import unittest
import time

desired_cap = desired_Cap()
# Create Test Driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
user_action = TouchAction(driver)

#ID: 01200  

##Class: android.widget.ImageButton 
el1 = driver.find_element_by_accessibility_id("Open navigation drawer")
el1.click()