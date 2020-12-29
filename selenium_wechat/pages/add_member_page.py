import pytest
from selenium.webdriver.common.by import By
from selenium_wechat.pages.base_page import BasePage

class AddMember(BasePage):
    _location_username = (By.ID, "username", "松")
    _location_acctid = (By.ID, "memberAdd_acctid", "szzhe")
    _location_Add_phone = (By.ID, "memberAdd_phone", "13901234567")
    _location_branch = (By.CSS_SELECTOR, '.js_show_party_selector')
    _location_branch_anchor = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div[4]/div[2]/ul/li/ul/li/a')
    _location_branch_anchor_del = (By.CSS_SELECTOR, '.ww_menuDialog_DualCols_colRight_cnt_item_delete')
    _location_branch_save = (By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Blue.js_submit")

    _location_save = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save")

    def add_member(self):
        self.find_sendkeys(*self._location_username)
        self.find_sendkeys(*self._location_acctid)
        self.find_sendkeys(*self._location_Add_phone)

        self.find_click(*self._location_branch)
        self.find_click(*self._location_branch_anchor)
        self.find_click(*self._location_branch_anchor_del)
        self.find_click(*self._location_branch_save)

        self.find_click(*self._location_save)

        # 解决循环导入的问题
        from selenium_wechat.pages.contact_page import ContactPage

        return ContactPage(self.driver)

    @pytest.mark.skip
    def add_member_fail(self, acctid, phone):
        self.find_sendkeys(*self._location_username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find_click(*self._location_save)

        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in res]
        return error_list
