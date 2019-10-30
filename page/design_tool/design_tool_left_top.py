from page.base_page import Page
from selenium.webdriver.common.by import By


class DesignToolLeftAndHeader(Page):
    public_material = (By.XPATH, "(//li[@role='menuitem']//span)[1]")
    person_buy = (By.XPATH, "(//li[@role='menuitem']//span)[2]")
    design_space = (By.XPATH, "(//li[@role='menuitem']//span)[3]")
    company_space = (By.XPATH, "(//li[@role='menuitem']//span)[4]")
    home_page = (By.XPATH, "//span[@class='navto'and text()='云丝尚首页']")

    def click_company_space(self):
        self.click(self.company_space)

    def click_design_space(self):
        self.click(self.design_space)

    def click_home_page(self):
        self.click(self.home_page)

    def click_person_buy(self):
        self.click(self.person_buy)

    def click_public_material(self):
        self.click(self.public_material)



