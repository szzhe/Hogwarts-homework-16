from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                             ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                  'scrollable(true).instance(0)).'
                                                  'scrollIntoView(new UiSelector().'
                                                  f'text("{text}").instance(0));')
    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def wait_for(self, by, locator):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((by, locator)))


