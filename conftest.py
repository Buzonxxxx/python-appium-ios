import time

from appium import webdriver
import pytest
from appium.options.ios import XCUITestOptions


# for parallel test
@pytest.fixture(params=["device1", "device2"], scope="function")
def appium_driver(request):
    if request.param == "device1":
        capabilities = {
            'deviceName': 'SDET-iPhone12-red',
            'platformName': 'iOS',
            'automationName': 'xcuitest',
            'platformVersion': '17.1',
            'udid': '00008101-000C31160E80001E',
            'bundleId': 'com.louis.IntegrationApp'
        }
        driver = webdriver.Remote('http://localhost:4724', options=XCUITestOptions().load_capabilities(capabilities))
    if request.param == "device2":
        capabilities = {
            'deviceName': 'iPhone 15',
            'platformName': 'iOS',
            'automationName': 'xcuitest',
            'platformVersion': '17.0.1',
            'udid': '219F6608-97BB-4A7A-8362-8733D9EE0C8C',
            'bundleId': 'com.louis.IntegrationApp'
        }
        driver = webdriver.Remote('http://localhost:4725', options=XCUITestOptions().load_capabilities(capabilities))
    yield driver
    time.sleep(2)
    driver.quit()
