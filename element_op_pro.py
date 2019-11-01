"""
@Author: lester
@Create: 2019/10/24
@Purpose:页面元素操作代码pro
"""
from page.management_system.manage_home_left import ManageHomeLeft
a = dir(ManageHomeLeft)
for i in a:
    end = i[-1]
    start = i[:-1]
    if '1' == end:
        print('def click_{0}(self):\n\tself.click(self.{0})' .format(start))

    if '2' == end:
        print('def type_{0}(self, {1}):\n\tself.input_text(self.{0},{1})'. format(start, i.split('_')[-1][:-1]))

