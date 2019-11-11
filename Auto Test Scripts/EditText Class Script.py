from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_Capabilities = {
    "deviceName": "emulator5554",
    "platformName": "Android",
    "app": "C:\\Users\\Abraham\\Downloads\\Walmart_v19.32.1_apkpure.com.apk",
    "appPackage": "com.walmart.android",
    "appWaitActivity": "com.walmart.android.app.main.HomeActivity",
    "platformVersion": "8.0"

}

# Create Driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Capabilities)
driver.implicitly_wait(30)

# Get elements of EditTex in a list
user_action = TouchAction(driver)
search_button = driver.find_element_by_id('com.walmart.android:id/search_mag_icon')
element_class_edit_text = driver.find_elements_by_class_name("android.widget.EditText")

# Selecting and testing elements of EditText
for elements_counting in element_class_edit_text:
    elements_counting.click()
    sub_menu = driver.find_elements_by_css_selector()
    driver.set_value(element_class_edit_text[0], "Goodies")
    driver.execute_script('mobile: performEditorAction', {'action': 'done'})

    driver.back()

driver.background_app(seconds=-3)
driver.activate_app(app_id= "com.walmart.android")
user_action.press(x=475, y=862)   .move_to(x=514, y=491)   .release()   .perform()





###element_class = driver.find_elements_by_class_name("android.widget.TextView")

###no_of_elements = len(element_class)

###for test_number in no_of_elemets:
###for names in element_name_list:
###found_element = driver.set_value(test_number, names)
