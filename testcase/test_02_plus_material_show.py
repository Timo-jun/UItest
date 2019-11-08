from poium import PageWait as pw,Page, PageElement as pe
import pytest
import allure
from selenium import webdriver
from time import sleep
import os



class BaiDuPage(Page):
    search_input = pe(css='#kw')
    search_button = pe(css='#su')


class TestAa:
    @allure.title('THIS IS A TITLE')
    @allure.description('THIS IS A DESCRIPTION')
    def test_search(self, get_driver):
        driver = get_driver
        # self.driver.search_input.send_keys('poium')
        page = BaiDuPage(driver)
        page.get('https://www.baidu.com')
        page.search_input = 'poium'
        page.search_button.click()
        sleep(3)
        b = page.screenshots(path=os.getcwd(), filename='test.png')
        allure.attach.file(b, attachment_type=allure.attachment_type.PNG)
        sleep(3)

if __name__ == '__main__':
    print(os.getcwd())





