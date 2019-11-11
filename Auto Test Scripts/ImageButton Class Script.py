from appium import webdriver

desired_Capabilities = {
    "deviceName": "emulator5554",
    "platformName": "Android",
    "app": "C:\\Users\\Abraham\\Downloads\\Walmart_v19.32.1_apkpure.com.apk",
    "appPackage": "com.walmart.android",
    "appWaitActivity": "com.walmart.android.app.main.HomeActivity",
    "platformVersion": "8.0"
}

# Create test driver object
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Capabilities)
driver.implicitly_wait(30)

# Clicking on NAV tab
driver.find_element_by_accessibility_id('Open navigation drawer').click()

# Clicking on first option under Nav tab; set your store
set_your_store = driver.find_element_by_id('com.walmart.android:id/app_nav_header_store_location'
                                           )
set_your_store.click()
driver.back()

driver.find_element_by_accessibility_id('Open navigation drawer').click()
driver.find_element_by_id('com.walmart.android:id/home_pov_image').is_displayed()



# Get all element by varying classes
#elements = driver.find_element_by_('android.widget.ImageView')
#driver.set_value(elements, "Home")

#search_button = driver.find_element_by_id('com.walmart.android:id/search_mag_icon')
