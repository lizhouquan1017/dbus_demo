# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          006_deleteUserLayout
# @Test Description:      DeleteUserLayout(string layout) -> (),删除一个用户键盘布局,参数  layout : 键盘布局
# @Test Condition:        1.通过 LayoutList 方法获取当前可用布局，添加布局
# @Test Step:             1.调用 DeleteUserLayout 方法，删除LayoutList键盘布局选项，并检查是否添加成功
# @Test Result:           1.删除成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:通过 LayoutList 方法获取当前可用布局，添加布局")
        self.layouts_list = inputDeviceKeyboard.get_layout_list()
        for option in self.layouts_list:
            inputDeviceKeyboard.addUserLayout(option)
            time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 DeleteUserLayout 方法，删除LayoutList键盘布局选项，并检查是否添加成功")
        for layout in self.layouts_list:
            inputDeviceKeyboard.deleteUserLayout(layout)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:添加cn;")
        inputDeviceKeyboard.addUserLayout('cn;')
        time.sleep(2)
