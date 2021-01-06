# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          002_addUserLayout_01
# @Test Description:      AddUserLayout(string layout) -> (),增加用户键盘布局
#                         参数 layout: 键盘布局
# @Test Condition:        1.清除所有layout
# @Test Step:             1.通过 LayoutList 方法获取当前可用布局
#                         2.调用 AddUserLayout 方法，添加可用layout，并检查是否添加成功
# @Test Result:           2.每一个布局都可添加成功
# @Test Remark:
# @Author:  ut001627
# ***************************************************

import time

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import inputDeviceKeyboard


class TestCase(OSBase):
    def setUp(self):
        self.Step("预制条件1:清除所有layout")
        inputDeviceKeyboard.clear_user_layouts()
        time.sleep(2)

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:通过 LayoutList 方法获取当前可用布局")
        layouts_list = inputDeviceKeyboard.get_layout_list()
        self.Step("步骤2:调用 AddUserLayout 方法，添加可用layout，并检查是否添加成功")
        for layout in layouts_list:
            inputDeviceKeyboard.addUserLayout(layout)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
