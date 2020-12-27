from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.base_page import BasePage
from selenium_appium.po.wework_page import WeWorkPage

class MainPage(BasePage):
    def goto_contains(self):
        pass

    def goto_wework(self):
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/elq" and @text="工作台"]')
        return WeWorkPage(self.driver)

