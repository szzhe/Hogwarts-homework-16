from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.blank_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    # def find(self, by, locator=None):
    #     if locator is None:
    #         return self.driver.find_element(*by)
    #     else:
    #         return self.driver.find_element(by=by, value=locator)

    def find(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        # 捕获元素没找到异常
        except Exception as e:
            for blank in self.blank_list:
                eles = self.finds(blank)
                if len(eles) > 0:
                    # 对黑名单元素进行点击
                    eles[0].click()
                    return self.find(by, locator)
            return e

    def finds(self, by, locator):
            return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator=None):
        if locator is None:
            self.find(*by).click()
        else:
            self.find(by=by, locator=locator).click()

    def find_and_send(self, by, locator, text):
        if locator is None:
            self.find(*by).send_keys(text)
        else:
            self.find(by=by, locator=locator).send_keys(text)

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
