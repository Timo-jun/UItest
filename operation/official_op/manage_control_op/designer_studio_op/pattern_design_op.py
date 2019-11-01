from page.official_website.manage_control.designer_studio.pattern_design_con import PatterDesignControl


class PatternDesignOp(PatterDesignControl):

    def pattern_design_upload(self):
        self.type_works_name('UI测试')
        self.click_works_type()
        self.click_first_option()
        self.click_works_purpose()
        self.click_works_purpose_option()
        self.upload_img(r'D:\testpo\common\te.png')
        self.type_works_price('10')
        self.click_pattern_element()
        self.click_first_option()
        self.click_dominant_tone()
        self.click_first_option()
        self.click_suitable_object()
        self.click_first_option()
        self.type_suitable_scene('123123')
        self.click_works_season()
        self.click_first_option()
        self.type_upload_production(r'D:\testpo\common\te.png')
        self.click_both_radio()
        self.type_production_describe('123123123')
        self.click_all_save()