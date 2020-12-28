import yaml
from selenium import webdriver
from selenium_wechat.po.base_page import BasePage
from selenium_wechat.po.main_page import MainPage


class Browser(BasePage):
    def start(self):
        if self.driver is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            cookies = self.driver.get_cookies()
            with open("../datas/data.yaml", "w", encoding="utf-8") as f:
                yaml.dump(cookies, f)
            with open("../datas/data.yaml", encoding="utf-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)
