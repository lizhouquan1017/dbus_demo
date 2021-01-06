# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          008_shortcutSwitchLayout
# @Test Description:      用于切换键盘布局快捷键的flag.
# @Test Condition:        无
# @Test Step:             1.切换键盘布局快捷键的flag；
# @Test Result:           1.返回UInt32类型数据;
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
        self.Step("步骤1：切换键盘布局快捷键的flag，返回UInt32类型数据")
        keybinding.shortcutSwitchLayout()

    def tearDown(self):
        self.Step("收尾:无")
