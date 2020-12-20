from time import sleep
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome --remote-debugging-port=9222
'''CSS常用定位方法
    find_element_by_css_selector（）获取元素对象列表
    #id id选择器根据id属性来定位元素
    .class  class选择器，根据class属性值来定位元素
    [attribute='value'] 根据属性来定位元素
    element>element 根据元素层级来定位 父元素>子元素
'''

def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookie = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookie, f)

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element(By.ID, "menu_contacts").click()
    sleep(2)
    driver.find_elements_by_css_selector("[class='qui_btn ww_btn js_add_member']")[1].click()
    sleep(2)
    driver.find_element(By.ID, "username").send_keys("宋")
    driver.find_element(By.ID, "memberAdd_acctid").send_keys("szzhe")
    driver.find_element(By.ID, "memberAdd_phone").send_keys("13901234567")
    driver.find_elements_by_css_selector("[class='qui_btn ww_btn js_btn_save']")[0].click()

if __name__ == '__main__':
    pytest.main(["test_base.py", "-v", "-s"])
