# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          009_getOnBattery
# @Test Description:      Boolean read 是否使用电池 接通电源时为 false 使用电池时为 true
# @Test Condition:
# @Test Step:             1.读取OnBattery属性值；
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
        self.Step("步骤1:读取OnBattery属性值，检查读取成功")
        daemonPower.getOnBattery()

    def tearDown(self):
        self.Step("收尾:无")