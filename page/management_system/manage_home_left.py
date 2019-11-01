from page.base_page import Page
from selenium.webdriver.common.by import By


class ManageHomeLeft(Page):
    goods_center = (By.XPATH, "//li//div//span[text()='商品中心']")
    goods_audit = (By.XPATH, "//li//div//span[text()='商品审核']")
    ga_material_resource = (By.XPATH, "(//li//div[span[text()='商品审核']]//following-sibling::ul//li)[1]")
    ga_design_center = (By.XPATH, "(//li//div[span[text()='商品审核']]//following-sibling::ul//li)[2]")
    ga_clothing_company = (By.XPATH, "(//li//div[span[text()='商品审核']]//following-sibling::ul//li)[3]")
    ga_design_tool = (By.XPATH, "(//li//div[span[text()='商品审核']]//following-sibling::ul//li)[4]")
    ga_witkey_center = (By.XPATH, "(//li//div[span[text()='商品审核']]//following-sibling::ul//li)[5]")
    goods_manage = (By.XPATH, "//li//div//span[text()='商品管理']")
    goods_content_set = (By.XPATH, "//li//div//span[text()='商品内容设置']")
    member_right_control = (By.XPATH, "//li//div//span[text()='会员权益管理']")

    def click_ga_clothing_company(self):
        self.click(self.ga_clothing_company)

    def click_ga_design_center(self):
        self.click(self.ga_design_center)

    def click_ga_design_tool(self):
        self.click(self.ga_design_tool)

    def click_ga_material_resource(self):
        self.click(self.ga_material_resource)

    def click_ga_witkey_center(self):
        self.click(self.ga_witkey_center)

    def click_goods_audit(self):
        self.click(self.goods_audit)

    def click_goods_center(self):
        self.click(self.goods_center)

    def click_goods_content_set(self):
        self.click(self.goods_content_set)

    def click_goods_manage(self):
        self.click(self.goods_manage)

    def click_member_right_control(self):
        self.click(self.member_right_control)
