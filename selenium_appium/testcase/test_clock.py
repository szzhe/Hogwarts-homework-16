import pytest
from selenium_appium.po.app import App

class TestClock():
    def setup(self):
        self.main = App()
        self.main.start()

    @pytest.mark.skip
    def test_push_clock(self):
        self.main.goto_main().goto_wework().push_the_clock()

    def test_add_member(self):
        self.main.goto_main().goto_contains().goto_add_member().add_member_ok()

    def teardown(self):
        self.main.quit()

if __name__ == '__main__':
    pytest.main(["test_clock.py", "-v", "-s"])
