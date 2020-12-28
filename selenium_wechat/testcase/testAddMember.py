import pytest
from selenium_wechat.po.browser import Browser


class TestAddMember:

    def test_add_member(self):
        add_member = Browser()
        add_member.start()
        add_member.goto_main().goto_add_member().add_member()

if __name__ == '__main__':
    pytest.main(["testAddMember.py", "-v", "--tb=long"])
