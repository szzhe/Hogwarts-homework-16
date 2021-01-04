from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.base_page import BasePage

class AddMember(BasePage):
    _location_member_name = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", "aaaaa")
    _location_member_sex = (MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
    _location_member_sex_change = (MobileBy.XPATH, "//*[@text='女']")
    _location_member_phone = (MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", "11114444999")
    _location_member_save = (MobileBy.XPATH, "//*[@text='保存']")

    def add_member_ok(self):
        self.find_and_send(*self._location_member_name)
        self.find_click(*self._location_member_sex)
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_click(*self._location_member_sex_change)
        self.find_and_send(*self._location_member_phone)
        self.find_click(*self._location_member_save)

        return True
