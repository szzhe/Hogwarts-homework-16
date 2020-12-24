from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestMainPage(object):
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
            "skipDeviceInitialization": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        sleep(3)

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["test_xueqiu.py", "-s", "-v"])
