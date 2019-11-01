import os
import sys

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from selenium import webdriver
from page.official_website.login_page import LoginPage
from common.AutoLog import AutomationLog
from operation.login_page_op import LoginPageOp
import time
import pytest


@pytest.fixture(scope='class')
def get_driver():
    """测试场景初始化配置(整个class仅执行一遍)"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options._arguments = ['disable-infobars']
    driver = webdriver.Chrome(options=chrome_options)
    AutomationLog.LogMsg("YssPlusMaterialShow 测试场景执行开始!")
    yield driver
    AutomationLog.LogMsg("YssPlusMaterialShow 测试场景执行完成!")
    driver.quit()


class TestYssPlusMaterialShow:

    def test_login(self, get_driver):
        get_driver.get('http://login.test.seeshion.com/accountCenter/login')
        get_driver.maximize_window()
        op = LoginPageOp(LoginPage(get_driver))
        op.login_op('13129344487', '123456')
        time.sleep(20)


