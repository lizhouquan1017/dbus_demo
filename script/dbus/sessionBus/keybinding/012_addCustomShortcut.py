# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          012_addCustomShortcut
# @Test Description:      添加一个自定义快捷键.
# @Test Condition:        无
# @Test Step:             1.添加一个自定义快捷键；
# @Test Result:           1.返回Int32类型数据;
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
        self.Step("步骤1：添加一个自定义快捷键，返回Int32类型数据")
        keybinding.addCustomShortcut(self.name, self.action, self.keystroke)

    def tearDown(self):
        self.Step("收尾:无")
