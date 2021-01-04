from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium_appium.po.base_page import BasePage
from selenium_appium.po.main_page import MainPage

class App(BasePage):
    def start(self, driver: WebDriver = None):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            # desired_caps["platformVersion"] = "7.1.2"
            # desired_caps["deviceName"] = "127.0.0.1:62001"
            desired_caps["platformVersion"] = "10.0.0.180"
            desired_caps["deviceName"] = "D5F7N18611005773"
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
            desired_caps["noReset"] = True
            desired_caps["unicodeKeyBoard"] = True
            desired_caps["resetKeyBoard"] = True
            desired_caps["skipServerInstallation"] = True
            # desired_caps["dontStopAppOnReset"] = True
            desired_caps["skipDeviceInitialization"] = True
            desired_caps["ensureWebviewsHavePages"] = True
            desired_caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            # 启动app
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)