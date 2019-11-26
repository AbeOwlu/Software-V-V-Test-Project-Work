from InitAppiumDriver import desired_Cap
from appium import webdriver


def search_box(input_Text):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap())
    driver.implicitly_wait(3)
    search_function = driver.find_element_by_accessibility_id('Search')
    search_function.click()
    driver.implicitly_wait(3)
    driver.set_value(search_function, input_Text)
    driver.execute_script('mobile: performEditorAction', {'action': 'done'})
    driver.implicitly_wait(3)
    driver.find_element_by_accessibility_id('Nearest store tab').click()
    driver.implicitly_wait(3)
    driver.find_element_by_accessibility_id('clear and exit search')

