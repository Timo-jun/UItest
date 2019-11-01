from time import sleep
from selenium import webdriver
from operation.login_page_op import LoginPageOp
from page.official_website.login_page import LoginPage
# from page.management_system.login_page import LoginPage
from page.management_system.goods_center.ga_design_center import DesignCenter
from operation.official_op.manage_control_op.designer_studio_op.pattern_design_op import PatternDesignOp
from selenium.webdriver.support import expected_conditions as ec


def a():
    login_url = 'http://login.test.seeshion.com/accountCenter/login'
    chrome_options = webdriver.ChromeOptions()
    chrome_options._arguments = ['disable-infobars']  # 去除自动软件控制提示信息
    driver = webdriver.Chrome(chrome_options=chrome_options)  # 启动浏览器驱动
    driver.get(login_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lop = LoginPageOp(lp)
    lop.login_op('13129344487', '123456')
    sleep(2)
    driver.get('http://dashboard.test.seeshion.com/#/design/patternGoods?type=add')
    sleep(4)
    pdo = PatternDesignOp(driver)
    pdo.pattern_design_upload()
    # mr.click_search_button()
    # mr.click_audit_button()
    # mr.click_audit_pass()
    # mr.click_result_submit()
    # mr.click_result_confirm()





if __name__ == '__main__':
    a()






