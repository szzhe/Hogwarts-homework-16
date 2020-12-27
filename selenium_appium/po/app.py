from appium import webdriver

from selenium_appium.po.base_page import BasePage
from selenium_appium.po.main_page import MainPage

class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "7.1.2"
            desired_caps["deviceName"] = "127.0.0.1:62001"
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
            # desired_caps["appActivity"] = ".launch.WwMainActivity",
            # desired_caps["appActivity"] = ".login.controller.LoginWxAuthActivity",
            desired_caps["noReset"] = "true"
            desired_caps["unicodeKeyBoard"] = "true"
            desired_caps["resetKeyBoard"] = "true"
            # desired_caps["skipServerInstallation"] = "true",
            # desired_caps["dontStopAppOnReset"] = "true",
            # desired_caps["skipDeviceInitialization"] = "true",
            desired_caps["ensureWebviewsHavePages"] = True
            desired_caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            # 启动app
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)