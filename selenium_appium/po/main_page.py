from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.base_page import BasePage
from selenium_appium.po.contains_page import Contains
from selenium_appium.po.wework_page import WeWorkPage

class MainPage(BasePage):
    _location_enter_contains = (MobileBy.XPATH, '//*[contains(@text,"通讯录")]')
    _location_enter_wework = (MobileBy.XPATH, '//*[contains(@text,"工作台")]')

    def goto_contains(self):
        self.find_click(*self._location_enter_contains)
        return Contains(self.driver)

    def goto_wework(self):
        self.find_click(*self._location_enter_wework)
        return WeWorkPage(self.driver)

