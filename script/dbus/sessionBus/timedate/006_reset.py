# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          006_reset
# @Test Description:      重置系统时间和网络时间同步
# @Test Condition:
# @Test Step:             1.重置系统时间和网络时间同步；
# @Test Result:           1.检查重置成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.sessionBus import timedate


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:设置不使用NTP")
        timedate.setNTP(False)

        self.Step("预制检查点1:检查NTP状态为False")
        timedate.checkNTPStatus('disable')

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:重置系统时间和网络时间同步，")
        timedate.reset()

        self.Step("检查点1:检查NTP状态重置为True")
        timedate.checkNTPStatus('enable')

    def tearDown(self):
        self.Step("收尾:无")