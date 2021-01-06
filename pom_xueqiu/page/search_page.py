from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy


class SearchPage:

    def __init__(self, driver: WebElement):
        self.driver = driver

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        currect_price = self.driver.find_element(MobileBy.XPATH,
                                                 "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(currect_price)
        assert float(currect_price) > 225
