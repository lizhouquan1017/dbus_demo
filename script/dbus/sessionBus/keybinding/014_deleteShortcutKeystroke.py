# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          014_deleteShortcutKeystroke
# @Test Description:      删除快捷键的一个按键组合.
# @Test Condition:        无
# @Test Step:             1.删除快捷键的一个按键组合；
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
        self.shortcuts_id = "show-desktop"
        self.shortcuts_type = 3
        self.keystroke = "<Super>D"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：删除快捷键的一个按键组合")
        keybinding.deleteShortcutKeystroke(self.shortcuts_id, self.shortcuts_type, self.keystroke)

    def tearDown(self):
        self.Step("收尾:无")
