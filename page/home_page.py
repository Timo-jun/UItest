from page.base_page import Page
from page.home_page_header import Header
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(Header):

    def qq(self):
        print('11')


if __name__ == '__main__':
    from page.login_page import LoginPage
    from operation.login_page_op import LoginPageOp
    driver = webdriver.Chrome()
    driver.get('http://login.test.seeshion.com/accountCenter/login')
    driver.maximize_window()
    sleep(5)
    hp = HomePage(driver)
    lp = LoginPageOp(LoginPage(driver))
    lp.login_op('13129344458', '123456')
    sleep(5)
    hp.hover_home_list()
    hp.click_control()

    # hp.click_material_resource()


