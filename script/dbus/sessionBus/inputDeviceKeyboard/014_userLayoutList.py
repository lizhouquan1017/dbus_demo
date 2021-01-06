# -*- coding: utf-8 -*-

# ***************************************************
# @Test Case ID:          014_userLayoutList
# @Test Description:      as UserLayoutList (read),当前用户键盘布局列表
# @Test Condition:        1.无
# @Test Step:             1.调用接口读取 UserLayoutList 属性值
# @Test Result:           1.返回 Array[string,...] 数据类型数据
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
        self.Step("步骤1:调用接口读取 UserLayoutList 属性值")
        inputDeviceKeyboard.userLayoutList()

    def tearDown(self):
        self.Step("收尾:无")
        time.sleep(2)
