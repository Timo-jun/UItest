from .public_material_top import PublicMaterialTop
from ..design_tool_left_top import DesignToolLeftAndHeader
from selenium.webdriver.common.by import By


class PatternSketchMaterial(PublicMaterialTop, DesignToolLeftAndHeader):
    search_input = (By.XPATH, "//input[@placeholder='请输入内容']")
    search_button = (By.XPATH, "//button//span[text()='搜索']")
    select_goods = (By.XPATH, "//span[contains(.,'replace')]//ancestor::div[@class='imgBox']")
    commodity = (By.XPATH, "//div[@class='select-main']//div[@class='imgBox']")
    buy_now = (By.XPATH, "//button//span[text()='立即购买']")

    def type_search_input(self, text):
        self.input_text(self.search_input, text)

    def click_search_button(self):
        self.click(self.search_button)

    def scroll_input(self):
        self.scroll_into_view(self.search_input)

    def click_select_goods(self, text):
        text = (self.select_goods[0], self.select_goods[1].replace('replace', text))
        self.click(text)