from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import time
from operation.login_page_op import LoginPageOp
from page.login_page import LoginPage
import os


def a():

    chrome_options = webdriver.ChromeOptions()
    chrome_options._arguments = ['disable-infobars']  # 去除自动软件控制提示信息
    driver = webdriver.Chrome(chrome_options=chrome_options)  # 启动浏览器驱动
    driver.get('http://login.test.seeshion.com/accountCenter/login')
    driver.maximize_window()
    lp = LoginPage(driver)
    lpo = LoginPageOp(lp)
    lpo.login_op('13129344487','123456')
    time.sleep(5)
    url2 = 'http://dashboard.test.seeshion.com/#/design/patternGoods?type=add'
    driver.get(url=url2)
    time.sleep(10)
    driver.find_element_by_xpath("//label[contains(.,'作品类型')]//following-sibling::div//input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//span[text()='四方循环图']").click()
    aa = driver.find_element_by_xpath("//input[@name='img']")
    print(aa)
    print(aa.get_attribute('type'))
    print(aa.tag_name)
    aa.send_keys(r'D:\testpo\common\te.png')
    time.sleep(10)
    driver.quit()
# D:\testpo\common\te.png
# (//div[@class='vicp-drop-area']//input[@style='display: none;'])[1]
if __name__ == '__main__':
    a()






