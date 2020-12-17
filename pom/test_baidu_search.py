from time import sleep
import pytest
from selenium import webdriver

class Testbaidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_baidu(self):
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(3)

        print(self.driver.execute_script("return window.document.title"))
        print(self.driver.execute_script("return JSON.stringify(performance.timing)"))

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["test_baidu_search.py"])
