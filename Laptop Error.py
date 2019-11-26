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
time.sleep(6)
search_button = driver.find_element_by_id('com.walmart.android:id/search_mag_icon')
element_class_edit_text = driver.find_elements_by_class_name("android.widget.EditText")
search_field = driver.find_element_by_id('com.walmart.android:id/search_src_text')

search_field.click()
user_action.wait(3000)
driver.set_value(search_field, "Lenovo Flex 14 16Gb")
driver.execute_script('mobile: performEditorAction', {'action': 'done'})

time.sleep(9)
item_price = driver.find_elements_by_id('com.walmart.android:id/shop_item_price')
item_price_1 = item_price[0].text
item_price_2 = item_price[1].text
item_price_3 = item_price[2].text
print(item_price_1, item_price_2)
time.sleep(6)
user_action.press(x=439, y=895).release().perform()
user_action.wait(5000)
TouchAction(driver).tap(x=439, y=895)
time.sleep(6)
compare_price = driver.find_element_by_id('com.walmart.android:id/price_view')
price_2 = compare_price.text

if compare_price == item_price_1:
    print("Test Pass 1")
else:
    print("Test Fail 0")


