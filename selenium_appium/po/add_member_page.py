from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.base_page import BasePage

class AddMember(BasePage):

    def add_member_ok(self):
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '姓名')]/..//*[@text='必填']", "aaaaa")
        self.find_click(MobileBy.XPATH,
                            "//*[contains(@text, '性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text, '手机')]/..//*[@text='手机号']",
                           "11114444999")
        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        return True
