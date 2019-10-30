from page.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    home_page = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[1]")
    material_resource = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[2]")
    design_center = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[3]")
    clothing_company = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[4]")
    customer_center = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[5]")
    design_tool = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[6]")
    solution_project = (By.XPATH, "(//ul[@class='yz-navmenu'])//li[7]")
    home_list = (By.XPATH, "//div[@class='login-info']//div[@class='avatar']")
    control_button = (By.XPATH, "//a[text()='管理控制台']")
    cancel_button = (By.XPATH, "//a[text()='退出登录']")

    def click_material_resource(self):
        self.click(self.material_resource)

    def hover_home_list(self):
        self.move_to_element(self.home_list)

    def click_control(self):
        self.click(self.control_button)