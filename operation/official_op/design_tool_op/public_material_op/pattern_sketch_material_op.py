from page.official_website.design_tool.public_material.pattern_sketch_material import PatternSketchMaterial
from time import sleep


class PatternSketchMaterialOp(PatternSketchMaterial):

    def buy_psm(self):
        self.click_public_material()
        self.click(self.pattern_sketch_material)
        self.input_text(self.search_input, 'UI测试')
        self.click(self.search_button)
        self.click(self.commodity)
