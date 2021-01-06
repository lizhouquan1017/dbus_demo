# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          003_refreshBatteries
# @Test Description:      刷新所有电池设备的状态
# @Test Condition:
# @Test Step:             1.刷新所有电池设备的状态
# @Test Result:           1.检查刷新成功;
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
        self.Step("步骤1:刷新所有电池设备的状态并检查刷新成功")
        power.refreshBatteries()

    def tearDown(self):
        pass
