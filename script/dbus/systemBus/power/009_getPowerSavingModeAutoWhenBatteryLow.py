# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_getPowerSavingModeAutoWhenBatteryLow
# @Test Description:      表示电池电量低时（百分比低于20%）是否自动开启节能模式
# @Test Condition:
# @Test Step:             1.读取电池电量低时（百分比低于20%）是否自动开启节能模式值
# @Test Result:           1.检查读取成功;
# @Test Remark:
# @Author:  ut000511
# *****************************************************

import pytest

from frame.base import OSBase
from aw.dbus.systemBus import power


class TestCase(OSBase):

    def setUp(self):
        self.Step("预制条件1:无")

    @pytest.mark.public
    def test_step(self):
        self.Step("步骤1:读取电池电量低时（百分比低于20%）是否自动开启节能模式值并检查读取成功")
        power.getPowerSavingModeAutoWhenBatteryLow()

    def tearDown(self):
        pass
