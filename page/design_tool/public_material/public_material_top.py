from ..design_tool_left_top import DesignToolLeftAndHeader
from selenium.webdriver.common.by import By


class PublicMaterialTop(DesignToolLeftAndHeader):
    cloth_style_material=(By.XPATH,"//div[contains(@class,'box')]//span[text()='服装款式素材']")
    pattern_sketch_material=(By.XPATH, "//div[contains(@class,'box')]//span[text()='图案画稿素材']")
    public_img=(By.XPATH, "//div[contains(@class,'box')]//span[text()='公共图片库']")
    plus_lining_material=(By.XPATH, "//div[contains(@class,'box')]//span[text()='面里料素材']")
    accessory_material=(By.XPATH, "//div[contains(@class,'box')]//span[text()='辅料素材']")
    hot_division=(By.XPATH, "//div[contains(@class,'box')]//span[text()='爆款专区']")
