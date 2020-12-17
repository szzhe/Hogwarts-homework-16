from time import sleep
from pom.pages.basePage import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    search_input = (By.ID, 'kw')
    search_btn = (By.ID, 'su')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_baidu(self, driver):
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()

    def input_kw(self):
        self.clear(*self.search_input)
        self.input_text("霍格沃兹测试学院", *self.search_input)

    def click_search_btn(self):
        self.click(*self.search_btn)
        sleep(2)
