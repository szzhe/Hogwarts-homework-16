import pytest
from selenium_wechat.pages.browser import Browser

class TestAddMember:

    # chrome --remote-debugging-port=9222

    def setup(self):
        self.add_member = Browser()
        self.add_member.start()

    def test_add_member(self):
        # 1.跳转添加成员页面  2. 添加成员 3. 自动跳转到通讯录页面
        res = self.add_member.goto_main().goto_add_member().add_member().get_member()
        assert '松' in res

    @pytest.mark.skip
    def test_add_member_by_contact(self):
        # 1.跳转到通讯录  2.跳转添加成员页面  3. 添加成员 4.自动跳转到通讯录页面
        res = self.add_member.goto_main().goto_contact().goto_add_member().add_member().get_member()
        assert '松' in res

    @pytest.mark.skip
    @pytest.mark.parametrize("accid, phone, expect_res",
                             [("YinXiaoShiDa", "13199998888", "该帐号已被“宋小哲”占有"),
                              ("xx2", "15810795067", "该手机号已被“宋振哲”占有")])
    def test_add_member_fail(self, accid, phone, expect_res):
        res = self.add_member.goto_main().goto_add_member().add_member_fail(accid, phone)
        assert expect_res in res

    @pytest.mark.skip
    def test_add_branch(self):
        self.add_member.goto_main().goto_contact().goto_add_branch()

    def quit(self):
        self.quit()

if __name__ == '__main__':
    pytest.main(["testAddMember.py", "-v", "-s"])
