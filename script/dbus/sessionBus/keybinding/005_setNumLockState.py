# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          005_setNumLockState
# @Test Description:      用于设置当前NumLock的状态.
# @Test Condition:        无
# @Test Step:             1.设置当前NumLock的状态；
# @Test Result:           1.检查执行成功;
# @Test Remark:
# @Author:  ut001919
# *****************************************************

import time

import pytest

from aw.dbus.sessionBus import keybinding
from frame.base import OSBase


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:获取参数")
        self.states = [0, 1]

    @pytest.mark.public
    def test_step(self):
        for state in self.states:
            self.Step(f"步骤1：设置当前NumLock的状态为{state}")
            keybinding.setNumLockState(state)
            time.sleep(2)

            self.CheckPoint(f"检查点1：检查设置当前NumLock设置{state}是否成功")
            keybinding.checksetNumLockState(state)
            time.sleep(2)

    def tearDown(self):
        self.Step("收尾:无")
