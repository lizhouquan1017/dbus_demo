# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_getBatteryPercentage
# @Test Description:      Dict of {String,Double} 电池电量百分比 例如： {'BAT0': 50} 表示 电池 BAT0 的电量百分比是 50%
# @Test Condition:
# @Test Step:             1.读取BatteryPercentage属性值；
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
        self.Step("步骤1:读取BatteryPercentage属性值，检查读取成功")
        daemonPower.getBatteryPercentage()

    def tearDown(self):
        self.Step("收尾:无")
