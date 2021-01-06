# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          017_clearShortcutKeystrokes
# @Test Description:      清除一个快捷键的所以按键组合.
# @Test Condition:        无
# @Test Step:             1.清除一个快捷键的所以按键组合；
# @Test Result:           1.检查接口执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.shortcuts_id = "screenshot"
        self.shortcuts_type = 0

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：清除一个快捷键的所以按键组合")
        keybinding.clearShortcutKeystrokes(self.shortcuts_id, self.shortcuts_type)

    def tearDown(self):
        self.Step("收尾:无")
