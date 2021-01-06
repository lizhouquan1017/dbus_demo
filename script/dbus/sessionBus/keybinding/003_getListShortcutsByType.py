# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_getListShortcutsByType
# @Test Description:      用于获取指定类型的快捷键列表，并返回String格式列表.
# @Test Condition:        无
# @Test Step:             1.调用ListShortcutsByType函数，获取指定类型的快捷键列表；
# @Test Result:           1.返回string[] list类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.shortcut_type = 2

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：调用ListShortcutsByType函数，获取指定类型的快捷键列表")
        keybinding.getListShortcutsByType(self.shortcut_type)

    def tearDown(self):
        self.Step("收尾:无")
