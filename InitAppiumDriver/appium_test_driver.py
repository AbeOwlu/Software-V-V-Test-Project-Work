from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import traceback
import time


def desired_Cap():
    desired_Capabilities = {
        "deviceName": "emulator5554",
        "platformName": "Android",
        "platformVersion": "8.0",
        "automationName": 'uiautomator2',
        "app": "C:\\Users\\Abraham\\Downloads\\Walmart_v19.32.1_apkpure.com.apk",
        "appPackage": "com.walmart.android",
        "appWaitActivity": "com.walmart.android.app.main.HomeActivity",

    }
    return desired_Capabilities
