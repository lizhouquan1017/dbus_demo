# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_PowerReset
# @Test Description:      重置所有相关设置
# @Test Condition:
# @Test Step:             1.调用Reset () ↦ ()；
# @Test Result:           1.检查函数执行成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import daemonPower


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:调用Reset () ↦ ()函数，检查执行成功")
        daemonPower.reset()

    def tearDown(self):
        self.Step("收尾:无")
