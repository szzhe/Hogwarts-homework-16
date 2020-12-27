from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium_appium.po.base_page import BasePage


class WeWorkPage(BasePage):
    def push_the_clock(self):
        self.scroll_find_click("打卡")

        # 上下班首次打卡
        first_clock = self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awm"]')
        if first_clock is not None:
            first_clock.click()
        else:
            # 提示自动打卡已完成，执行更新操作
            self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iow"]')

        # 更新下班卡 - 定位中，不在打卡范围内(腾讯地图)，你已在打卡范围内
        # print(self.driver.page_source)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aws"]')))
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aws"]')

        # 获取最新记录的打卡内容
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awv"]')))
        result_dk = self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awv"]').text
        # print(result_dk)
        assert '今日打卡已完成，好好休息' in result_dk