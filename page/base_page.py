"""
@Author: lester
@Create: 2019/10/23
@Purpose:页面的基类，实现各种页面的操作
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Page(object):

    def __init__(self, driver=None, time_out=5):
        self.driver = driver
        self.time_out = time_out
        self.action = ActionChains(driver)

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def open(self):
        self.driver.get(url=self.url)

    def find_element(self, loc):
        try:
            return WebDriverWait(self.driver, timeout=self.time_out).until(ec.visibility_of_element_located(loc))
        except TimeoutException as e:
            print(e)

    def find_elements(self, loc):
        try:
            return WebDriverWait(self.driver, timeout=self.time_out).until(ec.visibility_of_any_elements_located(loc))
        except TimeoutException as e:
            print(e)

    def click(self, loc=None, message='', element=None):
        if element is None:
            element = self.find_element(loc)
        for i in range(3):
            try:
                element.click()
                break
            except Exception as e:
                sleep(2)
                print("click:", e)

    def input_text(self, loc, text, message='', refresh=False):
        element = self.find_element(loc)
        if element is None or element==False:
            print('input_text:无可见元素')
            element = self.driver.find_element(*loc)
        try:
            element.send_keys(text)
            # if element.get_attribute('value') != text:
            #     element.click()
            #     element.send_keys()
        except Exception:
            if refresh is True:
                self.driver.refresh()
                self.input_text(self, loc, text)

    def get_current_window_handle(self):
        return self.driver.current_window_handle()

    def switch_window(self, handle):
        self.driver.switch_to.window(handle)

    def close_tab(self):
        self.driver.close()

    def excute_js(self, js, *args):
        self.driver.execute_script(js, *args)

    def move_to_element(self, loc):
        self.action.move_to_element(self.find_element(loc)).perform()

    def scroll_into_view(self, loc):
        element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    def open_page(self, url):
        self.driver.get(url)










