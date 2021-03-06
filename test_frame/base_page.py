import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_frame.blank_handle import blank_warpper

class BasePage:
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    FIND_AND_SEND = "find_and_send"
    CONTENT = "content"

    def __init__(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        # desired_caps["platformVersion"] = "10.0.0.180"
        # desired_caps["deviceName"] = "D5F7N18611005773"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = True
        desired_caps["unicodeKeyBoard"] = True
        desired_caps["resetKeyBoard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

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
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH, xpath_expr)
            elif action == self.FIND_AND_SEND:
                content = step.get(self.CONTENT)
                self.find_and_send(MobileBy.XPATH, xpath_expr, content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)
