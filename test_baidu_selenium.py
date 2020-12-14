import os
import allure
import pytest
import yaml
from selenium import webdriver
import time

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', yaml.safe_load(open("data/datas.yml"))["browser"])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./allure-results/b.png")
        allure.attach.file("./allure-results/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()

if __name__ == '__main__':
    pytest.main(["./test_baidu_selenium.py", "--alluredir", "./allure-results/"])
    # os.system(r"allure serve allure-results")
    os.system(r"allure generate --clean allure-results -o allure-report")
    os.system(r"allure open allure-report")
