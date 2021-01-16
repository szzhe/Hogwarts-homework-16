from appium.webdriver.common.mobileby import MobileBy
from test_frame.page.pre_page import PrePage


class Search(PrePage):
    def search(self):
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("xx")

        self.driver.yaml_load("../page/search.yaml")

        return True