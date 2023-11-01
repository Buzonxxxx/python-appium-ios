import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

apk_path = str(Path.cwd() / "app/MVCTodo.app")

capabilities = {
    'deviceName': 'iPhone 12',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '14.5',
    'udid': '85AB259A-A605-4B18-BA95-BB3A3808EDAE',
    'app': apk_path
}
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').click()
driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeOther[2]').send_keys('abc')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create').click()

time.sleep(2)

driver.quit()
