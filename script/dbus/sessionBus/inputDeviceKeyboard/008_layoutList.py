# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          008_layoutList
# @Test Description:      LayoutList() -> (map[string]string layout_list),获取键盘布局列表,返回值 layout_list : 键盘布局列表
# @Test Condition:        1.无
# @Test Step:             1.调用 LayoutList 方法获取键盘布局列表
# @Test Result:           1.正常调用无报错
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
        self.Step("步骤1:调用 LayoutList 方法获取键盘布局列表")
        inputDeviceKeyboard.layoutList()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(2)
