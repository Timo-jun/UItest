"""
@Author: lester
@Create: 2019/10/23
@Purpose:页面的基类，实现各种页面的操作
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Page(object):

    def __init__(self, driver, url='', time_out=5):
        self.driver = driver
        self.url = url
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

    def click(self, loc, message='', refresh=False):
        element = self.find_element(loc)
        try:
            element.click()
        except Exception:
            if refresh is True:
                self.driver.refresh()
                self.click(self, loc)

    def input_text(self, loc, text, message='', refresh=False):
        element = self.find_element(loc)
        try:
            element.send_keys(text)
            if element.get_attribute('value') != text:
                element.click()
                element.send_keys()
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
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", self.driver.find_element(loc))
        except Exception as e:
            print(e)









