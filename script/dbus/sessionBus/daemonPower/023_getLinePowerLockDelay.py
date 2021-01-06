# -*- coding: utf-8 -*-

# ****************************************************
# @Test Case ID:          023_getLinePowerLockDelay
# @Test Description:      接通电源时，不做任何操作，到自动锁屏的时间,单位秒。
# @Test Condition:
# @Test Step:             1.读取LinePowerLockDelay属性值；
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
        self.Step("步骤1:读取LinePowerLockDelay属性值，检查读取成功")
        daemonPower.getLinePowerLockDelay()

    def tearDown(self):
        self.Step("收尾:无")
