# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          018_getLowPowerAutoSleepThreshold
# @Test Description:      触发自动开始睡眠的电池电量，默认值为5
# @Test Condition:
# @Test Step:             1.读取LowPowerAutoSleepThreshold属性值；
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
        self.Step("步骤1:读取LowPowerAutoSleepThreshold属性值，检查读取成功")
        daemonPower.getLowPowerAutoSleepThreshold()

    def tearDown(self):
        self.Step("收尾:无")
