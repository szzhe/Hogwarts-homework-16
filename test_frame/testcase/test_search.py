import pytest
from test_frame.app import App

class TestSearch:
    '''
    pytest test_search.py --alluredir ./allure_result
    allure serve ./allure_result
    '''
    def setup(self):
        self.app = App()
        self.app.start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()

    def teardown(self):
        self.app.quit()

if __name__ == '__main__':
    pytest.main(["test_search.py", '-s', '-v'])