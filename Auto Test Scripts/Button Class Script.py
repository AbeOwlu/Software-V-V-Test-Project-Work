import traceback

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


developer_list = []
found_list = []

# Getting elements of class widget.Button in a list
# Swiping 6 times
i = 0
while i < 6:
    element_class_button = driver.find_elements_by_class_name("android.widget.Button")

    for element_name in element_class_button:
        el_name = element_name.get_attribute('text')
        found_list.append(el_name)
        while element_class_button[2].is_displayed():
            # swipe laterally-sideway on the button tab
            user_action.press(x=1041, y=608).move_to(x=555, y=603).release().perform()
            # press(x=964, y=606).move_to(x=615, y=611).release().perform()
            i = i + 1

print(found_list)

# Test for developer to check found element with expected elements in activity
assert developer_list == found_list, "TestError: Found List Doesn't Match Application List"


# Testing elements in the buttons class list
for elements_counting in found_list:
    i = 1
    found_list[i].click()

    try:
        check_shelf_result = driver.find_element_by_id('com.walmart.android:id/shelf_result_count')
        check_shelf_result.is_enabled()
        # call search function.. EditText Class.

        # Check Sort and Filter
        user_action.wait(6000)
        user_action.press(x=475, y=1062).move_to(x=475, y=491).release().perform()
        time.sleep(3)

        user_action.wait(3000)
        user_action.press(x=475, y=491).move_to(x=475, y=862).release().perform()
        time.sleep(6)
        driver.find_element_by_id('com.walmart.android:id/shelf_results_sort_filter').click()

        # Test a submenu function
        user_action.wait(3000)
        user_action.tap(x=1348, y=1052).perform()
        time.sleep(3)
        user_action.wait(3000)
        user_action.tap(x=558, y=1408).perform()
        time.sleep(3)
        # Done, then exit
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat').click()

        # Check Cart function
        time.sleep(2)
        test_cart = driver.find_element_by_id('com.walmart.android:id/cart_view')
        test_cart.click()
        time.sleep(3)
        driver.find_element_by_accessibility_id('Navigate up')
        time.sleep(3)
        driver.back()
    except:
        traceback.print_exc()
    i = +1
    '''

'''
    # Scroll tab for next three ta
    if i == 3:
        while element_class_button[2].is_displayed():
            # swipe laterally continuously
            TouchAction(driver).press(x=964, y=606).move_to(x=615, y=611).release().perform()
    else:
        driver.refresh()

