# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          007_getLayoutDesc
# @Test Description:      GetLayoutDesc(string layout) -> (string description),获取键盘布局的说明
#                         参数 layout : 键盘布局
#                         返回值 description : 说明
# @Test Condition:        1.无
# @Test Step:             1.通过 LayoutList 方法获取当前可用布局，添加布局
#                         2.调用 GetLayoutDesc 方法，获取键盘布局的说明
# @Test Result:           2.正确返回数据，无报错
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:通过 LayoutList 方法获取当前可用布局，添加布局")
        self.layouts_list = inputDeviceKeyboard.get_layout_list()
        self.Step("步骤2:调用 GetLayoutDesc 方法，获取键盘布局的说明")
        for option in self.layouts_list:
            inputDeviceKeyboard.getLayoutDesc(option)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
