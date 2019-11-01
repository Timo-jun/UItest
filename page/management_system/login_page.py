from page.base_page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    username = (By.XPATH, "//input[@placeholder='账号名称']")
    password = (By.XPATH, "//input[@placeholder='密码']")
    login_button = (By.XPATH, "//button//span[text()='登录']")

    def type_username(self, text):
        self.input_text(self.username, text)

    def type_password(self, text):
        self.input_text(self.password, text)

    def click_login_button(self):
        self.click(self.login_button)


