from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.add_member_page import AddMember
from selenium_appium.po.base_page import BasePage

class Contains(BasePage):
    _location_member_csn = (MobileBy.XPATH, '//*[contains(@text,"手动输入添加")]')

    def goto_add_member(self):
        self.scroll_find_click("添加成员")

        self.find_click(*self._location_member_csn)
        return AddMember(self.driver)