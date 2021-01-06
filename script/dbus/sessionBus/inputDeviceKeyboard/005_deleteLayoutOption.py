# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          005_deleteLayoutOption
# @Test Description:      DeleteLayoutOption(string option) -> (),删除一个键盘布局选项,参数 option: 键盘布局选项
# @Test Condition:        1.通过 LayoutList 方法获取当前可用布局，添加布局
# @Test Step:             1.调用 DeleteLayoutOption 方法，删除LayoutList键盘布局选项，并检查是否添加成功
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
            inputDeviceKeyboard.addLayoutOption(option)
            time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用 DeleteLayoutOption 方法，删除LayoutList键盘布局选项，并检查是否添加成功")
        for option in self.layouts_list:
            inputDeviceKeyboard.deleteLayoutOption(option)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
