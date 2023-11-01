import time

from appium import webdriver
from pathlib import Path
from appium.options.ios import XCUITestOptions

apk_path = str(Path.cwd() / "app/MVCTodo.app")

capabilities = {
    'deviceName': 'SDET-iPhone12-red',
    'platformName': 'iOS',
    'automationName': 'xcuitest',
    'platformVersion': '17.1',
    'udid': '00008101-000C31160E80001E',
    'app': apk_path
}
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

driver.implicitly_wait(10)

time.sleep(2)

driver.quit()
