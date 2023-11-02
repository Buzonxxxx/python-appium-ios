import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By

capabilities = {
    'deviceName': 'SDET-iPhone12-red',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '17.1',
    'udid': '00008101-000C31160E80001E',
    'browserName': 'Safari'
}
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

driver.implicitly_wait(10)

driver.get('http://google.com')
driver.find_element(By.XPATH, "//*[@id='XSqSsc']").send_keys("Hello Appium!!!")

time.sleep(2)

driver.quit()
