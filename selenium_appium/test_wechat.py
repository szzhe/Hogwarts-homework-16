
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestMainPage():
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # "appActivity": ".login.controller.LoginWxAuthActivity",
            "noReset": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "skipServerInstallation": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "settings[waitForIdleTimeout]": 0
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(6)

    def test_search(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/a41" and @text="微信登录"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gg5"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cey"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/egd" and @text="工作台"]').click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ig6"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/auq"]').click()
        result_dk = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/av0"]').text
        assert '今日打卡已完成，好好休息' in result_dk

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["test_wechat.py", "-s", "-v"])
