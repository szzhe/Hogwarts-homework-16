import pytest
from selenium.webdriver.common.by import By
from selenium_wechat.pages.base_page import BasePage

class AddMember(BasePage):
    _location_username = (By.ID, "username", "松")
    _location_acctid = (By.ID, "memberAdd_acctid", "szzhe")
    _location_Add_phone = (By.ID, "memberAdd_phone", "13901234567")
    _location_save = (By.CSS_SELECTOR, "[class='qui_btn ww_btn js_btn_save']")

    def add_member(self):
        self.find_sendkeys(*self._location_username)
        self.find_sendkeys(*self._location_acctid)
        self.find_sendkeys(*self._location_Add_phone)
        self.find_click(*self._location_save)

        # 解决循环导入的问题
        from selenium_wechat.pages.contact_page import ContactPage

        return ContactPage(self.driver)

    @pytest.mark.skip
    def add_member_fail(self, acctid, phone):
        self.find_sendkeys(By.ID, "username", "松")
        self.find_sendkeys(By.ID, "memberAdd_acctid", "szzhe")
        self.find_sendkeys(By.ID, "memberAdd_phone", "13901234567")
        self.find_click(By.CSS_SELECTOR, "[class='qui_btn ww_btn js_btn_save']")

        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list
