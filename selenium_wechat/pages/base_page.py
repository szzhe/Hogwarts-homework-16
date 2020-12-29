from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver

    def find(self, by, locator=None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)

    def find_click(self, by, locator=None):
        if locator is None:
            self.find(*by).click()
        else:
            self.find(by=by, locator=locator).click()

    def finds(self, by, locator=None):
        print(">>>", by, locator)
        if locator is None:  # <class 'str'>
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=locator)

    def find_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(f"{text}")

    def wait_click(self, by, locator):
        # element_to_be_clickable 判断元素是否可点击
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable((by, locator)))

    def quit(self):
        self.driver.quit()
