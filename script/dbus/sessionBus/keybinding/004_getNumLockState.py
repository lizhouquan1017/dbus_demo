# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          004_getNumLockState
# @Test Description:      用于获取当前NumLock的状态.
# @Test Condition:        无
# @Test Step:             1.获取当前NumLock的状态；
# @Test Result:           1.返回Int32类型数据;
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
        self.Step("步骤1：获取当前NumLock的状态，返回Int32类型数据")
        keybinding.getNumLockState()

    def tearDown(self):
        self.Step("收尾:无")
