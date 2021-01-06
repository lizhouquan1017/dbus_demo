# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          012_getBatteryState
# @Test Description:      Dict of {String,UInt32}
#                         电池状态
#                         例如：
#                         {'BAT0': 1L}
#                         表示 电池 BAT0 的状态为 1
#                         状态数字代表的意义：
#                         0 Unknown 未知
#                         1 Charging 充电中
#                         2 Discharging 不充电
#                         3 Empty 空
#                         4 FullyCharged 充满
#                         5 PendingCharge
#                         6 PendingDischarge
# @Test Condition:
# @Test Step:             1.读取BatteryState属性值；
# @Test Result:           1.检查读取成功;
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
        self.Step("步骤1:读取BatteryState属性值，检查读取成功")
        daemonPower.getBatteryState()

    def tearDown(self):
        self.Step("收尾:无")
