from selenium.webdriver.common.by import By

from selenium_wechat.po.base_page import BasePage


class AddMember(BasePage):
    # chrome - -remote - debugging - port = 9222

    def add_member(self):
        self.find_sendkeys(By.ID, "username", "松")
        self.find_sendkeys(By.ID, "memberAdd_acctid", "szzhe")
        self.find_sendkeys(By.ID, "memberAdd_phone", "13901234567")
        self.find_click(By.CSS_SELECTOR, "[class='qui_btn ww_btn js_btn_save']")
