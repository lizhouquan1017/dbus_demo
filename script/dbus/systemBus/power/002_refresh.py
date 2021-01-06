# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          001_getBatteries
# @Test Description:      刷新电池，电源适配器（AC Adapter）的状态(充电或未充电，充满电池时间等)
# @Test Condition:
# @Test Step:             1.刷新电池，电源适配器（AC Adapter）的状态(充电或未充电，充满电池时间等)；
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
        self.Step("步骤1:刷新电池，电源适配器状态并检查刷新成功")
        power.refresh()

    def tearDown(self):
        pass
