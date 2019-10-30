from ..company_page_header import ComPageHeader
from selenium.webdriver.common.by import By


class DevConHeader(ComPageHeader):
    task_situation = (By.XPATH, "//span[text()='返回任务概况']")
    increase_control = (By.XPATH, "//span[contains(.,'新增管控')]")
    produce_framework = (By.XPATH, "//div[@class='btn-group']//span[contains(.,'产品架构表')]")
    control_list = (By.XPATH, "//div[@class='btn-group']//span[contains(.,'管控列表')]")
    control_task = (By.XPATH, "//div[@class='btn-group']//span[contains(.,'管理任务表单')]")
    my_duty = (By.XPATH, "//li[contains(.,'我负责的')]")
    audit = (By.XPATH, "//li[contains(.,'审核/审批')]")
