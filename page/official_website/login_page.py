"""
@Author: lester
@Create: 2019/10/23
@Purpose:登录页
"""
from selenium.webdriver.common.by import By

from page.base_page import Page


class LoginPage(Page):
    login_dialog = (By.XPATH, "//li[text()='登录']")
    register_dialog = (By.XPATH, "//li[normalize-space(text())='注册']")
    login_phone = (By.XPATH, "//input[@placeholder='手机号/ID']")
    all_password = (By.XPATH, "//input[@placeholder='密码']")
    login_button = (By.XPATH, "//button[text()='登录']")
    register_person = (By.XPATH, "//span[text()='个人注册']")
    register_company = (By.XPATH, "//span[text()='企业注册']")
    register_phone = (By.XPATH, "//input[@placeholder='手机号']")
    register_name = (By.XPATH, "//input[@placeholder='昵称']")
    register_code = (By.XPATH, "//input[@placeholder='验证码']")
    register_get_code = (By.XPATH, "//span[text()='获取验证码']")
    register_protocol = (By.XPATH, "//span[@class='el-checkbox__inner']")
    register_button = (By.XPATH, "//button[text()='注册']")

    def type_all_password(self, password):
        self.input_text(self.all_password, password)

    def click_login_button(self):
        self.click(self.login_button)

    def click_login_dialog(self):
        self.click(self.login_dialog)

    def type_login_phone(self, phone):
        self.input_text(self.login_phone, phone)

    def click_register_button(self):
        self.click(self.register_button)

    def type_register_code(self, code):
        self.input_text(self.register_code, code)

    def click_register_company(self):
        self.click(self.register_company)

    def click_register_dialog(self):
        self.click(self.register_dialog)

    def click_register_get_code(self):
        self.click(self.register_get_code)

    def type_register_name(self, name):
        self.input_text(self.register_name, name)

    def click_register_person(self):
        self.click(self.register_person)

    def type_register_phone(self, phone):
        self.input_text(self.register_phone, phone)

    def click_register_protocol(self):
        self.click(self.register_protocol)
