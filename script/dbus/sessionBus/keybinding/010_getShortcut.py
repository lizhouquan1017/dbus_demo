# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          010_getShortcut
# @Test Description:      获取一个快捷键.
# @Test Condition:        无
# @Test Step:             1.获取一个快捷键；
# @Test Result:           1.返回String类型数据;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.shortcut_id = "capslock"
        self.shortcut_type = 2

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：获取一个快捷键，返回String类型数据")
        keybinding.getShortcut(self.shortcut_id, self.shortcut_type)

    def tearDown(self):
        self.Step("收尾:无")
