# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_lookupConflictingShortcut
# @Test Description:      查找冲突的快捷键.
# @Test Condition:        无
# @Test Step:             1.查找冲突的快捷键；
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
        self.keystroke = "<Alt>F8"

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：查找冲突的快捷键，返回String类型数据")
        keybinding.lookupConflictingShortcut(self.keystroke)

    def tearDown(self):
        self.Step("收尾:无")
