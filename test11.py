from page.official_website.login_page import LoginPage as a
from page.management_system.login_page import LoginPage as b
from selenium import webdriver


class A:
    def __init__(self,driver):
        self.driver = driver

    def a(self):
        print(self.driver)

class B(A):
    qq = '123'
    def b(self):
        print(self.qq)

class C(A):
    qq = '1234'
    def c(self):
        print(self.qq)

class D(C,B):
    ee = '12345'

if __name__ == '__main__':
    d = D('321')
    d.a()
    d.b()
    d.c()







