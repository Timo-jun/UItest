from page.base_page import Page
from selenium.webdriver.common.by import By


class ControlLeftTop(Page):
    company_control = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'企业管理')]")
    account_control = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'账户管理')]")
    purchase_control = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'采购管理')]")
    designer_studio = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'设计师工作室')]")
    style_material_control = (By.XPATH, "// li[ @ role = 'menuitem'] // span[contains(., '款式图素材管理')]")
    pattern_design_control = (By.XPATH, " // li[ @ role = 'menuitem'] // span[contains(., '图案设计管理')]")
    cloth_company = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'服装企业')]")
    material_control = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'材料管理')]")
    dev_control = (By.XPATH, "//li[@role='menuitem']//span[contains(.,'开发管控')]")
    whole_path = (By.XPATH,"//div[@role='navigation' and @aria-label='Breadcrumb']")

    def click_designer_studio(self):
        self.click(self.designer_studio)

    def click_pattern_design_control(self):
        self.click(self.pattern_design_control)
    
