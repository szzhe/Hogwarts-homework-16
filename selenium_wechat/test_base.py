from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome --remote-debugging-port=9222
# driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_add_member")[2].click()
# https://work.weixin.qq.com/wework_admin/frame#contacts
# https://work.weixin.qq.com/wework_admin/loginpage_wx
# https://work.weixin.qq.com/wework_admin/frame

def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = driver.get_cookies()
    print(cookie)
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookie, f)

def test_login():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            print(cookie)
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    sleep(10)
    driver.find_element(By.ID, "menu_contacts").click()
    print("登录成功")

if __name__ == '__main__':
    pytest.main(["test_base.py", "--alluredir", "../allure-results/"])
    # os.system(r"allure serve allure-results")
    # os.system(r"allure generate --clean ../allure-results -o ../allure-report")
    # os.system(r"allure open ../allure-report")
