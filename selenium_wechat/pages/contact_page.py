from selenium.webdriver.common.by import By

from selenium_wechat.pages.add_member_page import AddMember
from selenium_wechat.pages.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        '''
        添加成员操作
        :return:
        '''
        self.wait_click(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        self.find_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        return AddMember(self.driver)

    def get_member(self):
        pass
