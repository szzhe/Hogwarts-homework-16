import pytest
from test_frame.app import App

class TestSearch:
    def setup(self):
        self.app = App()
        self.app.start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()

if __name__ == '__main__':
    pytest.main(["test_search.py", '-s', '-v'])