from page.base_page import Page
from selenium.webdriver.common.by import By


class ComPageHeader(Page):
    com_pro = (By.XPATH, "//li[contains(.,'企业作品库')]")
    com_plus_material = (By.XPATH, "//li[contains(.,'企业面料库')]")
    com_accessory_material = (By.XPATH, "//li[contains(.,'企业辅料库')]")
    com_img = (By.XPATH, "//li[contains(.,'企业图库')]")
    com_pro_layout = (By.XPATH, "//li[contains(.,'企业商品企划库')]")
    dev_plan_control = (By.XPATH, "//li[contains(.,'开发计划管控')]")

