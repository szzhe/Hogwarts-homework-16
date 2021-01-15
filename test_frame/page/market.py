from appium.webdriver.common.mobileby import MobileBy
from test_frame.page.pre_page import PrePage
from test_frame.page.search import Search

class Market(PrePage):
    def goto_search(self):
        # self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')

        self.basepage.yaml_load("../page/market.yaml")

        return Search(self.basepage)