# python-appium-ios

## Installation
1. Install Node.js v16: `nvm install 16`(use NVM)
2. Install JDK: b`rew install openjdk@11`
3. Install Appium Server: `npm i -g appium`
4. Install xcuitest driver: `appium driver install xcuitest`
5. Install the Command Line Tools: `xcode-select--install`
6. Install Appium-Doctor: `npm install -g appium-doctor`
7. Run Appium-Doctor to check dependencies: `appium-doctor`

## Precondition
### Real Device Test Setup
1. Open Xcode and log in Apple ID
2. Clone WebDriverAgent: `git clone https://github.com/appium/WebDriverAgent.git`
3. Build WebDriverAgent App on your real device
    - Open `WebDriverAgent.xcodeproj` from the download folder
    - Build `WebDriverAgentRunner` target on your device
    - Select `WebDriverAgent` file and select `WebDriverAgentRunner` target
    - Select your team and modify Bundle identifier(just add some strings should be OK)
    - Select `IntergrationApp` target, select your team and modify Bundle identifier(just add some strings should be OK)
    - Build `IntergrationApp` on your device
4. Disable auto-lock on your device: Settings > Display & Brightness > Auto-Lock > Never
5. Trust the developer: Settings > General > VPN&Device Management

### Note1: Manual Update webdriveragent
1. In case of any OS upgrade(iOS), the framework gets disturbed as the other apps(Appium version/xcode/mac os) become unsupported.
2. We might get errors like `Unable to launch WebDriverAgent because of xcodebuild failure: xcodebuild failed with code 65` or `A valid provisioning profile for this executable was not found.`
3. Check the signing and capabilities for webdriveragentrunner and webdriveragentlib, it should be signed in using a proper developer account
4. Try running the tests again and check if the error isn’t coming anymore. In case the same errors still comes we need to do the next steps mentioned below
5. In such cases we can download the latest webdriver agent from `https://github.com/appium/WebDriverAgent/releases`
6. Then delete all files except Build folder from `.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent`
7. From the downloaded folder we can copy all files and paste inside the `.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent` folder
8. It should work

### Note2: Use ios-webkit-debug-proxy
1. If the test still unable to connect to the device try using **ios-webkit-debug-proxy**
2. Install `brew install ios-webkit-debug-proxy`
3. Run `ios_webkit_debug_proxy -c [Devic udid]:27753`
4. Run your test

## Safari Test
- Enable Web Inspector: Go to Settings > Safari > Advanced > Web Inspector
- Check Safari elements:
  1. Open Safari app on your phone and connect it with Mac machine
  2. Open desktop Safari and enable developer mode: Settings > Advanced > Check "Show features for web developers"
  3. Go to desktop Safari's developer menu, find your device and open the web in Safari
  4. Check the web elements

## Parallel Execution
1. Run `appium -p 4724 --driver-xcuitest-webdriveragent-port=8201`
2. Run `appium -p 4725 --driver-xcuitest-webdriveragent-port=8200`
3. Install `pytest-xdist`
4. Add `addopts = -n2` in `pytest.ini`
5. Update `conftest.py`
    ```pycon
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
    ```
6. Run the test
    ```pycon
    def test_contacts(appium_driver):
        driver = appium_driver
        driver.implicitly_wait(10)
        driver.find_element(by=AppiumBy.ID, value='Attributes').click()
    ```
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