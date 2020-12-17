import pytest
from selenium import webdriver
from pom.pages.searchPage import SearchPage


class TestSearchPage(object):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.search = SearchPage(self.driver)

    def test_search(self):
        self.search.goto_baidu(self.driver)
        self.search.input_kw()
        self.search.click_search_btn()

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["testSearchPage.py"])
