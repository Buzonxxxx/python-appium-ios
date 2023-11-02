from appium.webdriver.common.appiumby import AppiumBy


def test_contacts(appium_driver):
    driver = appium_driver
    driver.implicitly_wait(10)
    driver.find_element(by=AppiumBy.ID, value='Attributes').click()
    wheel = driver.find_elements(by=AppiumBy.CLASS_NAME, value='XCUIElementTypePickerWheel')[0]

