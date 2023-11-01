# python-appium-ios

## Installation
1. Install Node.js v16: `nvm install 16`(use NVM)
2. Install JDK: b`rew install openjdk@11`
3. Install Appium Server: `npm i -g appium`
4. Install xcuitest driver: `appium driver install xcuitest`
5. Install the Command Line Tools: `xcode-select--install`
6. Install Appium-Doctor: `npm install -g appium-doctor`
7. Run Appium-Doctor to check dependencies: `appium-doctor`

## Snippets
- Swipe left to find Settings App
```pycon
action = TouchAction(driver)

i = 0
while not driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Settings').is_displayed():
    action.press(x=24, y=172).wait(2000).move_to(x=285, y=172).perform()
    i += 1
    print(f'Swipe count: {i}')
```
- Toggle Switch
```pycon
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Switches').click()

toggle = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeSwitch[`value == "1"`][1]')
if toggle.get_attribute('value') == '1':
    toggle.click()
```
- Handle steppers
```pycon
# increase to 5
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Steppers').click()
count = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="0"][1]')
stepper = driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeButton[@name="Increment"])[1]')

while count.get_attribute('value') != '5':
    stepper.click()
```
- Adjust slider
```pycon
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Sliders').click()

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[1]/XCUIElementTypeSlider').send_keys('0.6')
print(driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeCell[1]/XCUIElementTypeSlider').get_attribute('value'))
```