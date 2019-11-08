import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture(scope='class')
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options._arguments = ['disable-infobars']  # 去除自动软件控制提示信息
    driver = webdriver.Chrome(chrome_options=chrome_options)  # 启动浏览器驱动
    yield driver
    print('22222222')



@pytest.fixture(scope='class')
def kpp():
    print('start')
    yield '11111'
    print('end')

