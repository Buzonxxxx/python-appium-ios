import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By

apk_path = str(Path.cwd() / "app/MVCTodo.app")

capabilities = {
    'deviceName': 'iPhone 15',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '17.0.1',
    'udid': '219F6608-97BB-4A7A-8362-8733D9EE0C8C',
    'browserName': 'Safari'
}
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

driver.implicitly_wait(10)

driver.get('http://google.com')
driver.find_element(By.XPATH, "//*[@id='XSqSsc']").send_keys("Hello Appium!!!")

time.sleep(2)

driver.quit()
