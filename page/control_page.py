from page.base_page import Page
from selenium.webdriver.common.by import By


class ControlPage(Page):
    # enter_protocol = (By.XPATH, "(//span[text()='确 定'])[2]")
    # autonym_protocol = (By.XPATH, "(//span[text()='确 定'])[1]")
    rt_username = (By.XPATH, "//span[@class='span']")
    go_autonym = (By.XPATH, "//span[normalize-space(text())='去实名认证']")
    real_name = (By.XPATH, "//li[contains(.,'实名认证')]")
