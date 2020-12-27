import pytest
from selenium_appium.po.app import App

class TestClock():
    def test_push_clock(self):
        app = App()
        app.start()
        app.goto_main().goto_wework().push_the_clock()

if __name__ == '__main__':
    pytest.main(["test_clock.py", "-v", "-s"])
