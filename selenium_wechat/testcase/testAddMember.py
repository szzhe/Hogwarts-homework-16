import pytest
from selenium_wechat.pages.browser import Browser

class TestAddMember:

    def setup(self):
        self.add_member = Browser()
        self.add_member.start()

    @pytest.mark.skip
    def test_add_member(self):
        self.add_member.goto_main().goto_add_member().add_member()

    def test_add_member_by_contact(self):
        self.add_member.goto_main().goto_contact().goto_add_member().add_member().get_member()

if __name__ == '__main__':
    pytest.main(["testAddMember.py", "-v", "-s"])
