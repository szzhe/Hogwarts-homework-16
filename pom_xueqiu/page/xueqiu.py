from appium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class Xueqiu:
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self, driver: WebElement = None):
        if driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "7.1.2"
            desired_caps["deviceName"] = "127.0.0.1:62001"
            desired_caps["appPackage"] = self._package
            desired_caps["appActivity"] = self._activity
            desired_caps["noReset"] = True
            desired_caps["unicodeKeyBoard"] = True
            desired_caps["resetKeyBoard"] = True
            # desired_caps["dontStopAppOnReset"] = True
            desired_caps["skipDeviceInitialization"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            print(self.driver)
            self.driver.start_activity(self._package, self._activity)
            # self.driver.launch_app()
        return self

    def teardown(self):
        self.driver.quit()