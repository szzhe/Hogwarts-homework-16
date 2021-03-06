from selenium.webdriver.common.by import By
from selenium_wechat.pages.base_page import BasePage
from selenium_wechat.pages.contact_page import ContactPage
from selenium_wechat.pages.add_member_page import AddMember

class MainPage(BasePage):

    def goto_add_member(self):
        self.find_click(By.CSS_SELECTOR, ".ww_indexImg_AddMember")
        return AddMember(self.driver)

    def goto_contact(self):
        self.find_click(By.ID, "menu_contacts")
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID, "menu_index").click()

    def quit(self):
        self.driver.quit()
