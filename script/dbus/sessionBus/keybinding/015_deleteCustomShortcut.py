# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          015_deleteCustomShortcut
# @Test Description:      删除一个自定义快捷键.
# @Test Condition:        无
# @Test Step:             1.删除一个自定义快捷键；
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
        self.name = "打开浏览器"
        self.action = "bash /usr/bin/google-chrome"
        self.keystroke = "<Alt>F1"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：添加一个自定义快捷键，获取id")
        shortcut_id = keybinding.getCustomShortcutId(self.name, self.action, self.keystroke)

        self.Step("步骤2：删除一个自定义快捷键")
        keybinding.deleteCustomShortcut(shortcut_id)

    def tearDown(self):
        self.Step("收尾:无")
