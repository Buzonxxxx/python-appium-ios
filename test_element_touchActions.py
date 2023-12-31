import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

apk_path = str(Path.cwd() / "app/MVCTodo.app")

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

driver.background_app(-1)

action = TouchAction(driver)

i = 0
while not driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Settings').is_displayed():
    action.press(x=24, y=172).wait(2000).move_to(x=285, y=172).perform()
    i += 1
    print(f'Swipe count: {i}')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Settings').click()

time.sleep(2)

driver.quit()
