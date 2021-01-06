# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          013_getBatteryStatus
# @Test Description:      表示电源状态
#                         1. "Charging"
#                         2. "Discharging"
#                         3. "Not charging"
#                         4. "Full"
#                         其他状态为Unknow
# @Test Condition:
# @Test Step:             1.读取电源状态值
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
        self.Step("步骤1:读取电源状态值并检查读取成功")
        power.getBatteryStatus()

    def tearDown(self):
        self.Step("收尾:无")
