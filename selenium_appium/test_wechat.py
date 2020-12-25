from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


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
        '''
        resource-id会经常发生变化，建议组合Xpath使用
        :return:
        '''

        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/a41" and @text="微信登录"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gg5"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cey"]').click()
        WebDriverWait(self.driver, 10).until(lambda x: "工作台" in self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/elq" and @text="工作台"]').click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        # 提示自动打卡已完成，执行更新操作
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iow"]').click()

        # 更新下班卡 - 定位中，不在打卡范围内(腾讯地图)，你已在打卡范围内
        # print(self.driver.page_source)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aws"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aws"]').click()

        # 获取最新记录的打卡内容
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awv"]')))
        result_dk = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awv"]').text
        # print(result_dk)
        assert '今日打卡已完成，好好休息' in result_dk

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["test_wechat.py", "-s", "-v"])
