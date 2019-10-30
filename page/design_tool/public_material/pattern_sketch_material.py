from .public_material_top import PublicMaterialTop
from selenium.webdriver.common.by import By


class PatternSketchMaterial(PublicMaterialTop):
    search_input =(By.XPATH,"//input[@placeholder='请输入内容']")
    search_button = (By.XPATH,"//button//span[text()='搜索']")
    select_goods=(By.XPATH,"//span[contains(.,'replace')]//ancestor::div[@class='imgBox']")