from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def find_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(f"{text}")

    def wait_click(self, by, locator):
        # element_to_be_clickable 判断元素是否可点击
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable((by, locator)))
