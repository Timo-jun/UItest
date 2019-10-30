"""
@Author: lester
@Create: 2019/10/24
@Purpose:登录页操作流程
"""
from page.login_page import LoginPage
import requests
from bs4 import BeautifulSoup


class LoginPageOp:

    def __init__(self, page):
        self.lp = page
        # self.lp = LoginPage(1)

    # 登录流程
    def login_op(self, phone, password):
        self.lp.click_login_dialog()
        self.lp.type_login_phone(phone)
        self.lp.type_all_password(password)
        self.lp.click_login_button()

    def register_op(self, phone, password, name, register_type=2):
        if register_type == 1:
            self.lp.click_register_person()
        else:
            self.lp.click_register_company()
        self.lp.type_register_phone(phone)
        self.lp.click_register_get_code()
        self.lp.type_register_name(name)
        self.lp.type_all_password(password)
        self.lp.type_register_code(self.get_code_op(phone))
        self.lp.click_register_protocol()
        self.lp.register_button()

    @staticmethod
    def get_code_op(phone):
        """
        获取手机验证码
        :param phone: 手机号码
        :return: 验证码
        """
        url = 'http://10.10.5.51:8079/ViewCode'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'mobile': phone}
        r = requests.post(url=url, headers=header, data=data)
        soup = BeautifulSoup(r.text, 'html.parser')
        if soup.find('title').text == '错误':
            print('111')
        return soup.find('input', attrs={'name': 'code'})['value']


if __name__ == '__main__':
    pass








