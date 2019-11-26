from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from InitAppiumDriver import desired_Cap, \
    use_search
from selenium.common.exceptions import StaleElementReferenceException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import time

desired_cap = desired_Cap()

# Create Test Driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
user_action = TouchAction(driver)

i = 0
while i <= 2:
    element_class_button = driver.find_elements_by_class_name("android.widget.Button")

    for elements in element_class_button[1 + i:]:

        try:
            elements.click()
            check_shelf_result = driver.find_element_by_id('com.walmart.android:id/shelf_results_sort_filter')
            check_shelf_result.click()

            time.sleep(3)
            user_action.press(x=1348, y=1052).release().perform()
            time.sleep(6)
            user_action.press(x=558, y=1408).release().perform()
            user_action.wait(6000)
            driver.back()
            time.sleep(3)

            test_cart = driver.find_element_by_id('com.walmart.android:id/cart_view')
            test_cart.click()
            time.sleep(6)
            driver.find_element_by_accessibility_id('Navigate up').click()
            time.sleep(6)

            search_field = driver.find_element_by_accessibility_id('Search')

            search_field.click()
            search_text = driver.find_element_by_id('com.walmart.android:id/search_src_text')
            user_action.wait(3000)
            search_text.click()
            time.sleep(6)
            driver.set_value(search_text, "Goodies")
            driver.execute_script('mobile: performEditorAction', {'action': 'done'})

            time.sleep(6)
            driver.back()
            time.sleep(9)
            driver.back()
            driver.back()

        except StaleElementReferenceException:
            time.sleep(3)
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
            your_element = WebDriverWait(driver, 9, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.Button')))
            time.sleep(9)

    i = + 1
    if i == 2:
        user_action.press(x=1041, y=608).move_to(x=555, y=603).release().perform()
        i = 0
        time.sleep(10)
