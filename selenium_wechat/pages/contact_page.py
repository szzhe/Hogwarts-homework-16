from selenium.webdriver.common.by import By
from selenium_wechat.pages.base_page import BasePage
from selenium_wechat.pages.add_member_page import AddMember

class ContactPage(BasePage):
    def goto_add_member(self):
        '''
        添加成员操作
        :return:
        '''
        # 解决循环导入的问题
        self.wait_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.find_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        return AddMember(self.driver)

    def get_member(self):
        '''
        获取成员列表，用来做断言信息
        :return:
        '''
        member_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # member_list_res = [i.text for i in member_list]
        member_list_res = []
        for i in member_list:
            member_list_res.append(i)
        print(member_list_res)
        return member_list_res
