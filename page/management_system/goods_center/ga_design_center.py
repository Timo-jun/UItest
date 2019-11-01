from selenium.webdriver.common.by import By
from page.management_system.manage_home_left import ManageHomeLeft


class DesignCenter(ManageHomeLeft):
    # 列表页
    goods_name_search = (By.XPATH, "//label[text()='商品名称']//following-sibling::div//input")
    store_name_search = (By.XPATH, "//label[text()='店铺名称']//following-sibling::div//input")
    register_time_search = (By.XPATH, "//label[text()='上架时间']//following-sibling::div//input")
    design_style = (By.XPATH, "//label[text()='设计类型']//following-sibling::div//span")
    design_style_options = (By.XPATH, "//ul[contains(@class,'ivu-select-dropdown-list')]//li[contains(.,'replace')]")
    search_button = (By.XPATH, "//button//span[text()='查询']")
    reset_button = (By.XPATH, "//button//span[text()='重置']")
    # 匹配所有审核按钮，所以需要先进行精确查询操作
    audit_button = (By.XPATH, "//button//span[text()='审核']")

    # 详情页
    audit_pass = (By.XPATH, "//span[text()='审核通过']")
    result_reason = (By.XPATH, "//textarea")
    result_submit = (By.XPATH, "//button//span[text()='提交']")
    result_confirm = (By.XPATH, "//div[@class='ivu-modal-confirm-footer']//span[text()='确定']")
    result_cancel = (By.XPATH, "//div[@class='ivu-modal-confirm-footer']//span[text()='取消']")

    def click_design_style(self):
        self.click(self.design_style)

    def click_design_style_option(self, option):
        loc = (self.design_style_options[0], self.design_style_options[1].replace('replace', option))
        self.click(loc)

    def click_audit_button(self):
        self.click(self.audit_button)

    def click_audit_pass(self):
        self.click(self.audit_pass)

    def type_goods_name_search(self, search):
        self.input_text(self.goods_name_search, search)

    def type_register_time_search(self, search):
        self.input_text(self.register_time_search, search)

    def click_reset_button(self):
        self.click(self.reset_button)

    def click_result_cancel(self):
        self.click(self.result_cancel)

    def click_result_confirm(self):
        self.click(self.result_confirm)

    def type_result_reason(self, reason):
        self.input_text(self.result_reason, reason)

    def click_result_submit(self):
        self.click(self.result_submit)

    def click_search_button(self):
        self.click(self.search_button)

    def type_store_name_search(self, search):
        self.input_text(self.store_name_search, search)
