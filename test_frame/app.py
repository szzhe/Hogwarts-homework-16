from appium import webdriver
from selenium_appium.po.base_page import BasePage
from test_frame.page.main import Main

class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "6.0.1"
            desired_caps["deviceName"] = "127.0.0.1:7555"
            # desired_caps["platformVersion"] = "10.0.0.180"
            # desired_caps["deviceName"] = "D5F7N18611005773"
            desired_caps["appPackage"] = "com.xueqiu.android"
            desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
            desired_caps["noReset"] = True
            desired_caps["unicodeKeyBoard"] = True
            desired_caps["resetKeyBoard"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            # 启动app
            self.driver.launch_app()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def goto_main(self):
        return Main(self.driver)