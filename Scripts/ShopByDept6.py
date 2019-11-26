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

##ID: 02200’x.y = 32(shopBydept_Baby) 
##Class: android.widget.ImageView 

el1 = driver.find_element_by_accessibility_id("Open navigation drawer")
el1.click()
time.sleep(8)
user_action.tap(x=304, y=879).perform()

time.sleep(8)
user_action.tap(x=131, y=977).perform()