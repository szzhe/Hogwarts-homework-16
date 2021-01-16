import pytest
from test_frame.base_page import BasePage
from test_frame.page.main import Main

class TestSearch:
    '''
    1.testcase目录下创建screenshot目录，存放黑名单blank截图.
    2.testcase目录下存放allure_result报表，
    pytest test_search.py --alluredir ./allure_result
    allure serve ./allure_result
    3.CMD命令行，执行scrcpy --record file.mp4开始录制，ctrl+c中断录制
    '''
    def setup(self):
        basepage = BasePage()
        self.app = Main(basepage)

    def test_search(self):
        self.app.goto_market().goto_search().search()

    def teardown(self):
        self.app.driver.quit()

if __name__ == '__main__':
    pytest.main(["test_search.py"])