from page.base_page import Page
from selenium.webdriver.common.by import By
from datetime import datetime


class IncreaseControl(Page):
    control_name = (By.XPATH, "//label[text() = '管控名称']//following - sibling::div //input")
    select_brand = (By.XPATH,"//input[@placeholder='请选择品牌']")
    brand_list = (By.XPATH,"//li//span[text()='replace']")
    select_year = (By.XPATH,"//input[@placeholder='请选择']")
    year_list = (By.XPATH,"//li//span[text()='"+str(datetime.now().year)+"年']")
    select_quarter = (By.XPATH,"//span[text()='冬']//preceding-sibling::span//span")
    increase_task = (By.XPATH, "//button//span[text()='添加任务']")

    def click_brand_list(self, brand):
        loc = self.brand_list[0] + self.brand_list[1].replace('replace', brand)
        self.click(loc)

