import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_frame.blank_handle import blank_warpper


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.blank_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    @blank_warpper
    def find(self, by, locator=None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator=None):
        if locator is None:
            self.find(*by).click()
        else:
            self.find(by=by, locator=locator).click()

    def find_and_send(self, by, locator, content):
        if locator is None:
            self.find(*by).send_keys(content)
        else:
            self.find(by=by, locator=locator).send_keys(content)
        # self.find(by=by, locator=locator).send_keys(content)

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'getChildByText(new UiSelector().'
                                                             'className("android.widget.TextView"), "'+f"{text}"+'")')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def wait_located(self, by, locator=None):
        if locator is None:
            return WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(*by))
        else:
            return WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((by, locator)))

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def quit(self):
        self.driver.quit()

    def yaml_load(self, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for step in data:
            xpath_expr = step.get("find")
            action = step.get("action")
            if action == "find_and_click":
                self.find_and_click(MobileBy.XPATH, xpath_expr)
            elif action == "find_and_send":
                content = step.get("content")
                self.find_and_send(MobileBy.XPATH, xpath_expr, content)
