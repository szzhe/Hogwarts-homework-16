from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium_appium.po.base_page import BasePage
from selenium_appium.po.wework_page import WeWorkPage


class MainPage(BasePage):
    def goto_contains(self):
        pass

    def goto_wework(self):
        # WebDriverWait(self.driver, 10).until(lambda x: "工作台" in self.driver.page_source)
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/elq" and @text="工作台"]')
        return WeWorkPage(self.driver)

