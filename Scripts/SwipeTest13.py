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

##ID: 02200’x.y = 31 (tap on List)
##Class: android.widget.ImageView 

el1 = driver.find_element_by_accessibility_id("Open navigation drawer")
el1.click()
time.sleep(8)

TouchAction(driver).press(x=454, y=1178).move_to(x=486, y=687).release().perform()
time.sleep(8)
user_action.tap(x=304, y=1365).perform()

