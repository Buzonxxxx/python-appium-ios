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

# increase to 5
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Steppers').click()
count = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="0"][1]')
stepper = driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeButton[@name="Increment"])[1]')

while count.get_attribute('value') != '5':
    stepper.click()

time.sleep(2)

driver.quit()
