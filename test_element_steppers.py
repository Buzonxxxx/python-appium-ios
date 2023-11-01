import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

apk_path = str(Path.cwd() / "app/UIKitCatalog.app")

capabilities = {
    'deviceName': 'iPhone 15',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '17.0.1',
    'udid': '219F6608-97BB-4A7A-8362-8733D9EE0C8C',
    'app': apk_path
}
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

driver.implicitly_wait(10)

# increase to 5
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Steppers').click()
count = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="0"][1]')
stepper = driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeButton[@name="Increment"])[1]')

while count.get_attribute('value') != '5':
    stepper.click()

time.sleep(2)

driver.quit()
