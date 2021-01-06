# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_setCapsLockState
# @Test Description:      用于设置CapsLock的状态.
# @Test Condition:        无
# @Test Step:             1.设置CapsLock的状态；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.state = 0

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1：设置当前NumLock的状态")
        keybinding.setCapsLockState(self.state)

    def tearDown(self):
        self.Step("收尾:无")
