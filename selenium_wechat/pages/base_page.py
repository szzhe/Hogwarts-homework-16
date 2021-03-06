from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        self.driver = base_driver

    def find(self, by, locator: str = None):
        if isinstance(locator, tuple):
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)

    def find_click(self, by, locator: str = None):
        if isinstance(locator, tuple):
            self.find(*by).click()
        else:
            self.find(by=by, locator=locator).click()

    def finds(self, by, locator: str = None):
        if isinstance(locator, tuple):  # <class 'str'>
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=locator)

    def find_sendkeys(self, by, locator, text: str):
        self.find(by, locator).send_keys(f"{text}")

    def wait_locate(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((by, locator)))

    def wait_click(self, by, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))