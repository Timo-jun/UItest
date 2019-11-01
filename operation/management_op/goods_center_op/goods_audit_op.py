from page.management_system.goods_center.ga_design_center import DesignCenter


class GoodsAudit(DesignCenter):

    def design_center_audit(self, goods_name, store_name=None, design_style=None):
        """
        usage: 设计中心，审核流程
        goods_name: 商品名称
        store_name: 店铺名称
        design_style: 设计类型对应的选项名称
        """
        self.click_goods_center()
        self.click_goods_audit()
        self.click_ga_design_center()
        self.type_goods_name_search(goods_name)
        if store_name is not None:
            self.type_store_name_search(store_name)
        if design_style is not None:
            self.click_design_style()
            self.click_design_style_option(design_style)
        self.click_search_button()
        self.click_audit_button()
        self.click_audit_pass()
        self.click_result_submit()
        self.click_result_confirm()