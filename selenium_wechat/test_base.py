import os

import pytest
import yaml
from selenium import webdriver


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookies = driver.get_cookies()
    print(cookies)
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookies, f)
    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    print("登录成功")
    driver.quit()


if __name__ == '__main__':
    pytest.main(["test_base.py", "--alluredir", "../allure-results/"])
    # os.system(r"allure serve allure-results")
    os.system(r"allure generate --clean ../allure-results -o ../allure-report")
    os.system(r"allure open ../allure-report")
