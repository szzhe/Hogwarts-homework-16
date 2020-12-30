from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                             ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                  'scrollable(true).instance(0)).'
                                                  'scrollIntoView(new UiSelector().'
                                                  f'text("{text}").instance(0));')
    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def wait_located(self, by, locator=None):
        if locator is None:
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(*by))
        else:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((by, locator)))

    def quit(self):
        self.driver.quit()


