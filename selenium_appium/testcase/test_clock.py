import pytest
from selenium_appium.po.app import App

class TestClock():
    def setup(self):
        self.main = App()
        self.main.start()

    def test_push_clock(self):
        self.main.goto_main().goto_wework().push_the_clock()

    def teardown(self):
        self.main.quit()

if __name__ == '__main__':
    pytest.main(["test_clock.py", "-v", "-s"])
