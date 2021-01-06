# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          011_getBatteryCapacity
# @Test Description:      表示电池充满时的电量和设计的充满时电量之比
# @Test Condition:
# @Test Step:             1.读取电量之比值
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
        self.Step("步骤1:读取电量之比值并检查读取成功")
        power.getBatteryCapacity()

    def tearDown(self):
        self.Step("收尾:无")
