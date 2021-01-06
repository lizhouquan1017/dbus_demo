# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          001_addLayoutOption
# @Test Description:      AddLayoutOption(string option) -> (),增加键盘布局选项
#                         参数 option : 键盘布局选项
# @Test Condition:        1.清除所有option
# @Test Step:             1.通过 LayoutList 方法获取当前可用布局
#                         2.自定义一个布局名称，如：'ltest;'
#                         3.调用 AddLayoutOption 方法，添加可用layout和自定义布局名称，并检查是否添加成功
# @Test Result:           3.每一个布局都可添加成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:清除所有option")
        inputDeviceKeyboard.clear_layout_options()
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:通过 LayoutList 方法获取当前可用布局")
        layouts_list = inputDeviceKeyboard.get_layout_list()

        self.Step("步骤2:自定义一个布局名称'ltest;'")
        new_layout = 'ltest;'
        layouts_list.append(new_layout)

        self.Step("步骤3:调用 AddLayoutOption 方法，添加可用layout和自定义布局名称，并检查是否添加成功")
        for option in layouts_list:
            inputDeviceKeyboard.addLayoutOption(option)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:清除所有option")
        inputDeviceKeyboard.clear_layout_options()
        time.sleep(2)
