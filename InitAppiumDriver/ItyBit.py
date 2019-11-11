from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import WebDriverException

from InitAppiumDriver import desired_Cap
import unittest
import time

desired_cap = desired_Cap()


# Create Driver
class TestAndroid(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(30)

    def test_elements(self):
        user_action = TouchAction(self.driver)
        click_elements = self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().scrollable(true)')
        self.assertIsInstance(click_elements, list)

        if len(click_elements) >= 2:
            print(f"Test Pass")
        else:
            print("Fail")


if __name__ == '__main__':
    unittest.main()
'''imoport LookupError
linReg(weight = balance)'''