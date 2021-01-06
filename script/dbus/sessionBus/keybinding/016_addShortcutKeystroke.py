# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          016_addShortcutKeystroke
# @Test Description:      向一个快捷键中添加一个按键组合.
# @Test Condition:        无
# @Test Step:             1.向一个快捷键中添加一个按键组合；
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
        self.keystroke = "<Alt>F11"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：向一个快捷键中添加一个按键组合")
        keybinding.addShortcutKeystroke(self.shortcuts_id, self.shortcuts_type, self.keystroke)

    def tearDown(self):
        self.Step("收尾:无")
