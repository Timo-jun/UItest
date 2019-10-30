from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options._arguments = ['disable-infobars']  # 去除自动软件控制提示信息
driver = webdriver.Chrome(chrome_options=chrome_options)  # 启动浏览器驱动
driver.get('http://login.test.seeshion.com/accountCenter/login')
driver.maximize_window()
a = driver.find_element_by_xpath("//input[@placeholder='手机号/ID']")
a.send_keys('1234'+Keys.ENTER)
time.sleep(2)
