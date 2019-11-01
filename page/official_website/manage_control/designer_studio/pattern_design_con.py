from ..control_left_top import ControlLeftTop
from selenium.webdriver.common.by import By
import os
from time import sleep


class PatterDesignControl(ControlLeftTop):
    # //div[text()='最新测试套件']//parent::td//following-sibling::td//span[text()='下架']
    search_input = (By.XPATH, "//input[@placeholder='搜索作品名称']")
    search_button = (By.XPATH, "//button[span[text()='搜索']]")
    upload_works = (By.XPATH, "//button[span[text()='上传作品']]")
    # 需要先走搜索流程
    works_select = (By.XPATH, "//button[span[text()='查看']]")
    # 删除
    works_delete = (By.XPATH, "(//tr//td[last()]//button//span)[1]")
    # 编辑
    works_update = (By.XPATH, "(//tr//td[last()]//button//span)[2]")
    # 上架/下架/送审
    works_status = (By.XPATH, "(//tr//td[last()]//button//span)[3]")
    works_name = (By.XPATH, "//label[contains(.,'作品名称')]//following-sibling::div//input")
    works_type = (By.XPATH, "//label[contains(.,'作品类型')]//following-sibling::div//input")
    works_purpose = (By.XPATH, "//label[contains(.,'作品用途')]//following-sibling::div//input")
    works_purpose_option = (By.XPATH, "//li//span[text()='设计图售卖']")
    works_price = (By.XPATH, "//label[contains(.,'价格')]//following-sibling::div//input")
    pattern_element = (By.XPATH, "//label[contains(.,'图案元素')]//following-sibling::div//input")
    dominant_tone = (By.XPATH, "//label[contains(.,'主色调')]//following-sibling::div//input")
    suitable_object = (By.XPATH, "//label[contains(.,'适用对象')]//following-sibling::div//input")
    suitable_scene = (By.XPATH, "//label[contains(.,'适用场景')]//following-sibling::div//input")
    works_season = (By.XPATH, "//label[contains(.,'适用季节')]//following-sibling::div//input")
    upload_production = (By.XPATH, "//label[contains(.,'作品上传')]//following-sibling::div//input")
    # 通用下拉列表第一选项定位，通过是否存在display属性值判断哪个下拉列表
    first_option = (By.XPATH, "//div[not(contains(@style,'display'))]//div[@class='el-scrollbar']//li//span")
    both_radio = (By.XPATH, "//span[text()='两者都有' and @class='el-radio__label']")
    design_center_radio = (By.XPATH, "//span[text()='设计中心' and @class='el-radio__label']")
    design_tool_radio = (By.XPATH, "//span[text()='设计工具-素材库' and @class='el-radio__label']")
    production_describe = (By.XPATH, "//div[@data-placeholder='书写你的内容']")
    all_save = (By.XPATH, "//button[contains(@class,'saveBtn')]//span[text()='保存']")
    production_img = (By.XPATH, "(//div[@class='vicp-drop-area']//input[@type='file'])[1]")
    upload_icon = (By.XPATH, "//i[@class='el-icon-plus']")
    upload_save = (By.XPATH, "//button[not(contains(@class,'saveBtn'))]//span[text()='保存']")

    def upload_img(self, path):
        """   
        Path:路径，可以是相对路径和绝对路径。使用\的需要防止转义
        """
        self.click(self.upload_icon)
        self.input_text(self.production_img, os.path.abspath(path))
        self.click(self.upload_save)

    def click_first_option(self):
        """
        Usage：点击下拉列表第一选项
        """
        sleep(1)
        a = self.find_elements(self.first_option)[0]
        try:
            print('options:', a.text)
        except Exception:
            pass
        self.click(element=a)

    def click_works_purpose_option(self):
        self.click(self.works_purpose_option)

    def click_all_save(self):
        self.click(self.all_save)

    def click_both_radio(self):
        self.click(self.both_radio)

    def click_design_center_radio(self):
        self.click(self.design_center_radio)

    def click_design_tool_radio(self):
        self.click(self.design_tool_radio)

    def click_dominant_tone(self):
        self.click(self.dominant_tone)

    def click_pattern_element(self):
        self.click(self.pattern_element)

    def type_production_describe(self, describe):
        self.input_text(self.production_describe, describe)

    def click_search_button(self):
        self.click(self.search_button)

    def type_search_input(self, text):
        self.input_text(self.search_input, text)

    def click_suitable_object(self):
        self.click(self.suitable_object)

    def type_suitable_scene(self, scene):
        self.input_text(self.suitable_scene, scene)

    def type_upload_production(self, production):
        self.input_text(self.upload_production, production)

    def click_upload_works(self):
        self.click(self.upload_works)

    def click_works_delete(self):
        self.click(self.works_delete)

    def type_works_name(self, name):
        self.input_text(self.works_name, name)

    def type_works_price(self, price):
        self.input_text(self.works_price, price)

    def click_works_purpose(self):
        self.click(self.works_purpose)

    def click_works_season(self):
        self.click(self.works_season)

    def click_works_select(self):
        self.click(self.works_select)

    def click_works_status(self):
        self.click(self.works_status)

    def click_works_type(self):
        self.click(self.works_type)

    def click_works_update(self):
        self.click(self.works_update)
