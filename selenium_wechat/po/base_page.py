from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(f"{text}")
