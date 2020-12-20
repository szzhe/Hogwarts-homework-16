import yaml
from selenium.webdriver.common.by import By
from selenium_wechat.pages.basePage import BasePage

class add_memter_Page(BasePage):

    wechat_contact = (By.ID, "menu_contacts")

    add_member_name = (By.ID, "username")
    add_member_acctid = (By.ID, "memberAdd_acctid")
    add_member_iphone = (By.ID, "memberAdd_phone")
    add_member_save = (By.CSS_SELECTOR, "qui_btn ww_btn js_btn_save'")[0]

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_loginpage_wx(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.maximize_window()

    def get_cookie(self):
        with open("../data.yaml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)

    def goto_index(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_contact(self):
        self.click(*self.wechat_contact)

    def start_add_mement(self):
        self.driver.find_elements_by_css_selector("[class='qui_btn ww_btn js_add_member']")[1].click()

    def input_member_name(self):
        self.input_text("宋", *self.add_member_name)

    def input_member_acctid(self):
        self.input_text("szzhe", *self.add_member_acctid)

    def input_member_iphone(self):
        self.input_text("13901234567", *self.add_member_iphone)

    def save_member(self):
        self.driver.find_elements_by_css_selector("[class='qui_btn ww_btn js_btn_save']")[0].click()

