from time import sleep

import pytest
from selenium import webdriver
from selenium_wechat.addMember import add_memter_Page

class TestAddMember():
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)

        self.driver = webdriver.Chrome()
        self.add = add_memter_Page(self.driver)
        self.driver.implicitly_wait(5)

    def test_add_member(self):

        self.add.goto_loginpage_wx()
        self.add.get_cookie()
        self.add.goto_index()

        self.add.goto_contact()
        sleep(2)
        self.add.start_add_mement()
        self.add.input_member_name()
        self.add.input_member_acctid()
        self.add.input_member_iphone()
        self.add.save_member()

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["testAddMember.py", "-v", "-s"])