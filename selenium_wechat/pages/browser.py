import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wechat.pages.base_page import BasePage
from selenium_wechat.pages.main_page import MainPage

class Browser(BasePage):
    def start(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.opt = webdriver.ChromeOptions()
            self.opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=self.opt)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def __cookie_login(self):
        with open("../datas/data.yml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            if yaml_data is None:
                self.__cookie_get()
            else:
                for cookie in yaml_data:
                    if "expiry" in cookie:
                        cookie.pop("expiry")
                    self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def __cookie_get(self):
        cookies = self.driver.get_cookies()
        if "exopiry" in cookies:
            cookies.pop("expiry")
        with open("../datas/data.yml", "w", encoding="utf-8") as f:
            yaml.dump(cookies, f)

    def goto_main(self):
        return MainPage(self.driver)
