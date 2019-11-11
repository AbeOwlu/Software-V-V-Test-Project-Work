from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from InitAppiumDriver import desired_Cap
from InitAppiumDriver import ItyBit
import time

desired_cap = desired_Cap()

# Create Test Driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
user_action = TouchAction(driver)


test_ele = ItyBit.TestAndroid.test_elements(TestAndroid)
print(test_ele)





