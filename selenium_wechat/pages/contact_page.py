from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_wechat.pages.base_page import BasePage
from selenium_wechat.pages.add_member_page import AddMember

class ContactPage(BasePage):
    def goto_add_member(self):
        _location_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        '''
        添加成员操作
        :return:
        '''
        # 解决循环导入的问题
        self.wait_click(*_location_add_member)
        self.find_click(*_location_add_member)
        return AddMember(self.driver)

    def get_member(self):
        _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        '''
        获取成员列表，用来做断言信息
        :return:
        '''
        self.wait_click(*_location_member_list)
        member_list = self.finds(*_location_member_list)
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def goto_add_branch(self):
        _location_add_branch = (By.CSS_SELECTOR, ".js_create_dropdown")
        _location_create_braach = (By.CSS_SELECTOR, ".js_create_party")
        _location_branch_name_wait = (By.CSS_SELECTOR, ".inputDlg_item .ww_inputText")
        _location_branch_name = (By.CSS_SELECTOR, ".inputDlg_item .ww_inputText", "szzhe")
        _location_branch_parent = (By.CSS_SELECTOR, ".js_parent_party_name")
        _location_branch_parent_anchor = (
        By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[3]/div/div", Keys.ENTER)
        _location_branch_submit = (By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]")
        _location_tips = (By.CSS_SELECTOR, "#js_tips")

        self.wait_click(*_location_add_branch)
        self.find_click(*_location_add_branch)
        self.find_click(*_location_create_braach)

        self.wait_locate(*_location_branch_name_wait)
        self.find_sendkeys(*_location_branch_name)
        self.find_click(*_location_branch_parent)
        self.find_sendkeys(*_location_branch_parent_anchor)
        self.find_click(*_location_branch_submit)

        tips = self.find(_location_tips).text
        assert "新建部门成功" in tips
