import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

apk_path = str(Path.cwd() / "app/UIKitCatalog.app")

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

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Sliders').click()

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[1]/XCUIElementTypeSlider').send_keys('0.6')
print(driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[1]/XCUIElementTypeSlider').get_attribute('value'))

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[2]/XCUIElementTypeSlider').send_keys('0.8')
print(driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[2]/XCUIElementTypeSlider').get_attribute('value'))

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[3]/XCUIElementTypeSlider').send_keys('0.2')
print(driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[3]/XCUIElementTypeSlider').get_attribute('value'))

time.sleep(2)

driver.quit()
