from selenium.webdriver.common.by import By
from selenium_wechat.po.base_page import BasePage
from selenium_wechat.po.contact_page import ContactPage
from selenium_wechat.po.add_member_page import AddMember


class MainPage(BasePage):

    def goto_add_member(self):
        self.find_click(By.CSS_SELECTOR, ".ww_indexImg_AddMember")
        return AddMember(self.driver)

    def goto_contact(self):
        return ContactPage(self.driver)
