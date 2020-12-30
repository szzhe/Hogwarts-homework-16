from appium.webdriver.common.mobileby import MobileBy
from selenium_appium.po.base_page import BasePage

class WeWorkPage(BasePage):

    _location_clock_awm = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awm"]')
    _location_clock_iow = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iow"]')
    _location_clock_aws = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aws"]')
    _location_clock_awv = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awv"]')

    def push_the_clock(self):
        self.scroll_find_click("打卡")

        # 上下班是否首次打卡
        first_clock = self.find(*self._location_clock_awm)
        if first_clock is not None:
            first_clock.click()
        else:
            # 已打过卡，执行更新操作
            self.find_click(*self._location_clock_iow)

        # 更新下班卡 - 定位中，不在打卡范围内(腾讯地图)，你已在打卡范围内
        # print(self.driver.page_source)
        self.wait_located(*self._location_clock_aws)
        self.find_click(*self._location_clock_aws)

        # 获取最新记录的打卡内容
        self.wait_located(*self._location_clock_awv)
        result_dk = self.find(*self._location_clock_awv).text
        assert '今日打卡已完成，好好休息' in result_dk

