from appium.webdriver.common.mobileby import MobileBy
from pom_xueqiu.base_page import BasePage
from pom_xueqiu.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_serch_page(self):
        self.find(MobileBy.XPATH, "com.xueqiu.android:id/tv_search").click()
        return SearchPage(self.driver)

    def goto_stocks(self):
        pass

    def goto_trade(self):
        pass

    def goto_message(self):
        pass
