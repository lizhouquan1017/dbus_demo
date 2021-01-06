# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          002_getListAllShortcuts
# @Test Description:      用于获取快捷键列表，并返回String格式列表.
# @Test Condition:        无
# @Test Step:             1.调用ListAllShortcuts函数，获取快捷键列表；
# @Test Result:           1.返回string[] list类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用ListAllShortcuts函数，获取快捷键列表")
        keybinding.getListAllShortcuts()

    def tearDown(self):
        self.Step("收尾:无")
